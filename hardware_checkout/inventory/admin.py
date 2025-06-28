from django.contrib import admin
from .models import Hardware, Loan, ServiceRecord, AuditLog

admin.site.register(Hardware)
admin.site.register(Loan)
admin.site.register(ServiceRecord)
admin.site.register(AuditLog)
