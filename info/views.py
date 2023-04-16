# Create your views here.
from django.shortcuts import render, redirect
from .forms import DataScienceConsultingForm, RoboticProcessAutomationForm, ProcessOptimizationForm
from .models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def data_science_consulting(request):
    if request.method == 'POST':
        form = DataScienceConsultingForm(request.POST, request.FILES)
        if form.is_valid():
            data_science_consulting_request = DataScienceConsultingRequest(
                **form.cleaned_data)
            data_science_consulting_request.save()
            # Send email notification
            subject = 'New Client: Form Submitted on Portfolio'
            message = f"Form data:\n\n{data_science_consulting_request}"
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_email, fail_silently=False)


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

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        sender = request.POST['email']

        recipients = ['shaundamon09@gmail.com']

        send_mail(subject, message, sender, recipients)
        return redirect('success_page')  # Redirect to a success page or any other page

    return render(request, 'homePage.html')

def form_submission(request):
    if request.method == 'POST':
        subject = 'New Client: Form Submitted on Portfolio'
        name = request.POST.get('name')
        email = request.POST.get('email')
        project_description = request.POST.get('project_description')
        data_availability = request.POST.get('data_availability')
        
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        # Create the HTML email body
        html_email_body = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': project_description,
            'data available' : data_availability
        })

        # Send the email with the HTML email body
        send_mail(subject, "", from_email, to_email, fail_silently=False, html_message=html_email_body)
        return redirect('success')

    return render(request, 'services/data_science_consulting.html')  # Replace with the name of your template

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})