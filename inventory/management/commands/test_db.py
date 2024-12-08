from django.core.management.base import BaseCommand
from inventory.models import Category
from django.db import connection
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Test database connection and operations'

    def handle(self, *args, **options):
        # Test database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                self.stdout.write(self.style.SUCCESS('[OK] Database connection successful'))
        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f'[ERROR] Database connection failed: {str(e)}'))
            return

        # Test model creation
        try:
            category = Category.objects.create(
                name='Test Category',
                description='Test Description'
            )
            self.stdout.write(self.style.SUCCESS(f'[OK] Successfully created category: {category.name}'))
            
            # Test model retrieval
            retrieved = Category.objects.get(name='Test Category')
            self.stdout.write(self.style.SUCCESS('[OK] Successfully retrieved category'))
            
            # Test model deletion
            retrieved.delete()
            self.stdout.write(self.style.SUCCESS('[OK] Successfully deleted category'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'[ERROR] Database operation failed: {str(e)}'))
