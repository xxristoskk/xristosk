from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from frontpage.forms import ContactForm

# Create your views here.
class ContactView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']

        recipients = ['x.katsaros.ds@gmail.com']

        # send_mail(subject, message, from_email=sender, recipient_list=recipients)
        email = EmailMessage(
            subject,
            message,
            sender,
            recipients,
            reply_to=[sender]
        )
        email.send()

        return redirect('home')

# def home(request):
#     context={}
#     return render(request, 'home.html', context)

def datasets(request):
    return render(request, 'datasets.html', context={})

def projects(request):
    return render(request, 'projects.html', context={})