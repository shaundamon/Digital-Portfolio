# Create your views here.
from django.shortcuts import render
from .forms import DataScienceConsultingForm, RoboticProcessAutomationForm, ProcessOptimizationForm


def data_science_consulting(request):
    form = DataScienceConsultingForm()
    return render(request, 'services/data_science_consulting.html', {'form': form})


def robotic_process_automation(request):
    form = RoboticProcessAutomationForm()
    return render(request, 'services/robotic_process_automation.html', {'form': form})


def process_optimization(request):
    form = ProcessOptimizationForm()
    return render(request, 'services/process_optimization.html', {'form': form})
