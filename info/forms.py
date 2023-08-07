"""
This module defines the Message model and related forms.

It provides a ModelForm for submitting messages with a name, email address, and message content.
"""
from django.forms import ModelForm
from .models import Message
from django import forms
from django.core.validators import FileExtensionValidator


class DataScienceConsultingForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g Thembisile Damon'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'E.g shaundamon09@gmail.com'}))
    phone = forms.CharField(label="Your Phone", max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g +27 12 345 6789'}))
    company = forms.CharField(label="Your Company", max_length=100, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g AnalytiKorner Inc.'}))
    project_title = forms.CharField(
        label="Project Title", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g Customer Segmentation, Credit Risk, Churn Propensity'}))
    project_description = forms.CharField(label="Project Description", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'E.g We would like to count the churn propensity of clients with our change of products. /n We would like to investigate the possibility of customers qualifying for credit without the need for credit chec'}))
    objective = forms.CharField(label="Project Objective", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'E.g Our goal is to retain customers with our change of products'}))
    data_availability = forms.ChoiceField(
        label="Data Availability",
        choices=[
            ('yes', 'Yes'),
            ('no', 'No'),
            ('unsure', 'Unsure'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    timeline = forms.ChoiceField(
        label="Project Timeline",
        choices=[
            ('1_week', '1 Week'),
            ('1_month', '1 Month'),
            ('3_months', '3 Months'),
            ('6_months', '6 Months'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    additional_information = forms.CharField(label="Additional Information", required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'E.g On successful delivery of the request/project, we might want to extend the contact for more work'}))
    document = forms.FileField(
        label="Attach Document",
        required=False,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc', 'docx'])],
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )


class RoboticProcessAutomationForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    phone = forms.CharField(label="Your Phone", max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}))
    company = forms.CharField(label="Your Company", max_length=100, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company'}))
    department = forms.CharField(label="Department", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Department'}))
    process_name = forms.CharField(
        label="Process Name", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Process Name'}))
    process_description = forms.CharField(label="Process Description", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Process Description'}))
    current_challenges = forms.CharField(label="Current Challenges", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Current Challenges'}))
    estimated_time_savings = forms.CharField(label="Estimated Time Savings (Hours/Week)",
                                             max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estimated Time Savings'}))
    estimated_cost_savings = forms.IntegerField(
        label="Estimated Cost Savings (USD/Year)", required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estimated Cost Savings'}))
    additional_information = forms.CharField(label="Additional Information", required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Additional Information'}))


class ProcessOptimizationForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Your Phone", max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(label="Your Company", max_length=100, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.CharField(label="Department", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    current_process = forms.CharField(label="Current Process Description", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    desired_process = forms.CharField(label="Desired Process Description", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    process_objectives = forms.CharField(label="Process Objectives", widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    key_performance_indicators = forms.CharField(
        label="Key Performance Indicators", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    estimated_time_savings = forms.CharField(label="Estimated Time Savings (Hours/Week)",
                                             max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estimated_cost_savings = forms.IntegerField(
        label="Estimated Cost Savings (USD/Year)", required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    additional_information = forms.CharField(label="Additional Information", required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))


class MessageForm(ModelForm):
    """
    A form for submitting messages.

    Allows users to submit messages with their name, email address, and a message.
    """
    class Meta:
        """
        Specifies the model and fields to use for the form.
        """
        model = Message
        fields = ['name', 'email', 'message']
