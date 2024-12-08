from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'List all tables in the database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cursor.fetchall()
            
            self.stdout.write(self.style.SUCCESS('\nDatabase Tables:'))
            self.stdout.write(self.style.SUCCESS('-' * 50))
            for table in tables:
                self.stdout.write(self.style.SUCCESS(f'[OK] {table[0]}'))
