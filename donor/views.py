# donor/views.py

from django.shortcuts import render, redirect
from .forms import DonorForm
from .models import Donor

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()
    return render(request, 'donor/add_donor.html', {'form': form})



def donor_list(request):
    blood_group = request.GET.get('blood_group')  
    if blood_group:
        donors = Donor.objects.filter(blood_group=blood_group)
    else:
        donors = Donor.objects.all()
    
    return render(request, 'donor/donor_list.html', {'donors': donors})
