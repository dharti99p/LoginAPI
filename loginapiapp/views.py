from .models import LogIn
from .serializers import LogInSerializer
from rest_framework import viewsets

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        api_url = 'http://localhost:8000/api/login/'

        # api_data = {
        #     'username': username,
        #     'password': password
        # }

        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            # Check if the username and password match any API data
            if any(user['username'] == username and user['password'] == password for user in api_data):
                return redirect(reverse('success_page'))

            # Render login page with an error message
        error_message = 'Invalid credentials. Please try again.'
        return render(request, 'login.html', {'error_message': error_message})

        # Render login page for GET requests
    return render(request, 'login.html')


class LogInViewSet(viewsets.ModelViewSet):
    queryset = LogIn.objects.all()
    serializer_class = LogInSerializer


def success_page(request):
    # Render a success page or perform other actions
    return render(request, 'success.html')
