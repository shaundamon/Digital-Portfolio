from django.db import models
import re
from ckeditor.fields import RichTextField
from django.db import models


class MyModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # rest of the fields

class Tag(models.Model):
    TAG_CHOICES = (
        ('Data Science', 'Data Science'),
        ('Robotic Process Automation', 'RPA'),
        ('Data Management', 'Data Management'),
        ('Data Engineering', 'Data Engineering'),
        ('Business Analysis', 'Business Analysis'),
        ('Process Automation', 'Process Automation'),
        ('Machine Learning', 'Machine Learning'),
        ('Software Development', 'Software Development'),
    )

    name = models.CharField(max_length=50, choices=TAG_CHOICES, unique=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Information(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    cv = models.FileField(upload_to='cv', blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class Competence(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.FileField(upload_to='competence/', blank=False, null=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    the_year = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    the_year = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to="projects/", blank=False, null=False)
    tools = models.CharField(max_length=200, blank=False, null=False)
    tags = models.ManyToManyField(Tag)  # Add the tags ManyToMany field
    demo = models.URLField()
    github = models.URLField()
    show_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Project, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub(" ", "_", slug)
        return slug.lower()

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    video = models.FileField(upload_to='project_videos/')
    thumbnail = models.ImageField(upload_to='video_thumbnails/')
    title = models.CharField(max_length=100)
    description = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to="blog/", blank=False, null=False)
    tools = models.CharField(max_length=200, blank=False, null=True)
    demo = models.URLField(blank=True, null=True)  
    github = models.URLField(blank=True, null=True)  
    external_source = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_blog_absolute_url(self):
        return "blog/blog/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Blog, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub(" ", "_", slug)
        return slug.lower()


class DataScienceConsultingRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    objective = models.TextField()
    data_availability = models.CharField(max_length=10, choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unsure', 'Unsure'),
    ])
    budget = models.IntegerField(blank=True, null=True)
    timeline = models.CharField(max_length=10, choices=[
        ('1_week', '1 Week'),
        ('1_month', '1 Month'),
        ('3_months', '3 Months'),
        ('6_months', '6 Months'),
    ])
    additional_information = models.TextField(blank=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name_plural = "Blog"


class RoboticProcessAutomationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100)
    process_name = models.CharField(max_length=200)
    process_description = models.TextField()
    current_challenges = models.TextField()
    estimated_time_savings = models.CharField(
        max_length=100, blank=True, null=True)
    estimated_cost_savings = models.IntegerField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.process_name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='events/')
    # ticket_link = models.URLField()

    def __str__(self):
        return self.title

        
class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
