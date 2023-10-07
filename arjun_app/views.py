from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.views import View



# Create your views here.
def index(request):
  return render(request, 'index.html')

# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
        
#         subject = "You have a message"
#         message = message+","+"\nFrom"+" "+name+"\n"+email
#         recipient = 'marjunvinod@gmail.com'
#         # Send the email
#         send_mail(
#             subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
#             # fail_silently=False, use fail_silentlt for this error(gaierror at /contact[Errno 11001] getaddrinfo failed)
        
#         return redirect('/')

class contactview(View):
  def post(self, request):  #Self represents the instance of the class.
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    subject = "You have a message from "+name
    message = message+","+"\nFrom"+" "+name+"\n"+email
    recipient = 'marjunvinod@gmail.com'
    send_mail(
      subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False
    )
    
    return redirect("/")
