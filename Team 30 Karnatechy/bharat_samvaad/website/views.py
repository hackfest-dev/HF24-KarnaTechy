from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def complaint(request):
    return render(request, 'complaints.html')

def feedback(request):
    return render(request, 'feedback.html')

def login(request):
    # Handle user login logic here
    return render(request, 'login.html')