# Create your views here.
from django.shortcuts import render, redirect
from .forms import DataScienceConsultingForm, RoboticProcessAutomationForm, ProcessOptimizationForm
from .models import DataScienceConsultingRequest



def data_science_consulting(request):
    if request.method == 'POST':
        form = DataScienceConsultingForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the DataScienceConsultingRequest model
            data_science_request = DataScienceConsultingRequest(
                **form.cleaned_data)
            data_science_request.save()

            # Redirect to the success page (replace 'success_page' with the actual success page name)
            return redirect('success_page')
    else:
        form = DataScienceConsultingForm()

    return render(request, 'services/data_science_consulting.html', {'form': form})


def robotic_process_automation(request):
    form = RoboticProcessAutomationForm()
    return render(request, 'services/robotic_process_automation.html', {'form': form})


def process_optimization(request):
    form = ProcessOptimizationForm()
    return render(request, 'services/process_optimization.html', {'form': form})
