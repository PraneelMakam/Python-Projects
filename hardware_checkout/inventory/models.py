from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Hardware(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, unique=True)
    serial_number = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, default='available')

    def __str__(self):
        return self.name

class Loan(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.hardware} -> {self.borrower}"

class ServiceRecord(models.Model):
    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    description = models.TextField()
    serviced_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
