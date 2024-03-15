# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataScienceConsultingForm, RoboticProcessAutomationForm, ProcessOptimizationForm
from .models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event, Education, Experience, Competence, Blog
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from .models import Event 
from datetime import datetime
from django.core.exceptions import ValidationError
import os
from dotenv import load_dotenv
load_dotenv()


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

def blog_list(request):
    blogs = Blog.objects.all()
    print("Blogs: ", blogs)  
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    single_blog = get_object_or_404(blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': single_blog})

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = f'New Client: Form Submitted on Portfolio by {name}'
        project_description = request.POST.get('project_description')
        
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        # Create the HTML email body
        html_email_body = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': project_description
        })

        send_mail(subject, "", from_email, to_email, fail_silently=False, html_message=html_email_body)
        return redirect('success')

    return render(request, 'services/data_science_consulting.html')  

def events(request):
    events_list = Event.objects.all() 

    # Pagination
    paginator = Paginator(events_list, 6)  
    page = request.GET.get('page')
    
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    return render(request, 'events.html', {'events': events})

def experiences_and_education(request):
    education = Education.objects.all()
    experiences = Experience.objects.all()
    context = {
        'education': education,
        'experiences': experiences,
    }
    return render(request, 'experiences_and_education.html', context)

def languages_and_tools(request):
    context = {
        'competences': Competence.objects.all(),
    }
    return render(request, 'languages_and_tools.html', context)

def update_events_from_api():
    access_token = config("ACCESS_TOKEN")
    base_url = "https://api.predicthq.com/v1/events/"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    page = 1  

    while True:  
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            events_data = data['results']

            for event in events_data:
                title = event.get('title', '')
                description = event.get('description', '')
                start = event.get('start')

                if start:
                    dt_object = datetime.fromisoformat(start.replace("Z", "+00:00"))
                    date = dt_object.date()
                    time = dt_object.time()
                else:
                    continue  # Skip event if 'start' is not available

                location_coordinates = event.get('location', [])
                location = ', '.join(map(str, location_coordinates))

                Event.objects.update_or_create(
                    title=title,
                    defaults={
                        'description': description,
                        'date': date,
                        'time': time,
                        'location': location
                    }
                )
            
            # Check if there is a next page
            if 'next' in data and data['next']:
                page += 1 
            else:
                break 
        else:
            print(f"Received unexpected status code {response.status_code}. Stopping.")
            break  