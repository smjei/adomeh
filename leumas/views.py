from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings



# Create your views here.
def index(request):
   return render(request, 'leumas/index.html')

def blog(request):
   return render(request, 'leumas/blog.html')

def blogpost(request):
   return render(request, 'leumas/blogpost.html')

def sam404(request):
   return render(request, 'leumas/sam404.html')


class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        send_mail(
            'Subject - New Contact Me Message From Your Website', 
            'Hello ' + name + ',\n' + message, 
            'samueladomeh@gmail.com', # Admin
            [
                email,
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('index')




