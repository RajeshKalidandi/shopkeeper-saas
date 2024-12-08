from django.db import models
from django.conf import settings

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CustomerInteraction(models.Model):
    INTERACTION_TYPES = (
        ('CALL', 'Phone Call'),
        ('EMAIL', 'Email'),
        ('VISIT', 'Store Visit'),
        ('COMPLAINT', 'Complaint'),
        ('FEEDBACK', 'Feedback'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPES)
    interaction_date = models.DateTimeField()
    notes = models.TextField()
    follow_up_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.get_interaction_type_display()}"

class Loyalty(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='loyalty')
    points = models.IntegerField(default=0)
    tier = models.CharField(max_length=20, default='BRONZE')
    last_points_earned = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.points} points"

    class Meta:
        verbose_name_plural = "Loyalties"
