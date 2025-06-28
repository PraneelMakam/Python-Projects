from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Hardware, Loan, AuditLog

@login_required
def hardware_list(request):
    hardware = Hardware.objects.all()
    return render(request, 'inventory/hardware_list.html', {'hardware': hardware})

@login_required
def checkout(request, pk):
    hardware = get_object_or_404(Hardware, pk=pk)
    if request.method == 'POST':
        Loan.objects.create(hardware=hardware, borrower=request.user)
        AuditLog.objects.create(action='checkout', user=request.user, notes=str(hardware))
        hardware.status = 'checked_out'
        hardware.save()
        return redirect(reverse('hardware_list'))
    return render(request, 'inventory/checkout.html', {'hardware': hardware})

@login_required
def checkin(request, pk):
    hardware = get_object_or_404(Hardware, pk=pk)
    loan = Loan.objects.filter(hardware=hardware, returned_at__isnull=True).last()
    if request.method == 'POST' and loan:
        loan.returned_at = timezone.now()
        loan.save()
        AuditLog.objects.create(action='checkin', user=request.user, notes=str(hardware))
        hardware.status = 'available'
        hardware.save()
        return redirect(reverse('hardware_list'))
    return render(request, 'inventory/checkin.html', {'hardware': hardware})

@login_required
def export_excel(request):
    # placeholder for Excel export
    response = HttpResponse('Excel export placeholder', content_type='text/plain')
    return response

@login_required
def export_pdf(request):
    # placeholder for PDF export
    response = HttpResponse('PDF export placeholder', content_type='text/plain')
    return response
