# Create your views here.
from django.shortcuts import render, redirect
from .forms import DataScienceConsultingForm, RoboticProcessAutomationForm, ProcessOptimizationForm
from .models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event
from django.core.mail import send_mail
from django.conf import settings


def data_science_consulting(request):
    if request.method == 'POST':
        form = DataScienceConsultingForm(request.POST, request.FILES)
        if form.is_valid():
            data_science_consulting_request = DataScienceConsultingRequest(
                **form.cleaned_data)
            data_science_consulting_request.save()
            # Add this line to send the email
            send_email_notification(form.cleaned_data)

            return redirect('success')
    else:
        form = DataScienceConsultingForm()
    return render(request, 'services/data_science_consulting.html', {'form': form})


def robotic_process_automation(request):
    if request.method == 'POST':
        form = RoboticProcessAutomationForm(request.POST, request.FILES)
        if form.is_valid():
            robotic_process_automation_request = RoboticProcessAutomationRequest(
                **form.cleaned_data)
            robotic_process_automation_request.save()

            return redirect('success')
    else:
        form = RoboticProcessAutomationForm()
    return render(request, 'services/robotic_process_automation.html', {'form': form})


def process_optimization(request):
    form = ProcessOptimizationForm()
    return render(request, 'services/process_optimization.html', {'form': form})

def blog(request):
    return render(request, 'blog/blog.html')

def success_page(request):
    return render(request, 'success.html')


def send_email_notification(form_data):
    subject = 'New Client : Form Submitted on Portfolio'
    message = f"Form data:\n\n{form_data}"
    from_email = settings.EMAIL_HOST_USER
    to_email = [settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_email, to_email, fail_silently=False)

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})