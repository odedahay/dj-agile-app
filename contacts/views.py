from sre_constants import SUCCESS
from django.shortcuts import render, redirect, HttpResponse
from .models import Contact, Applicant
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        messages = request.POST.get('message')
        
        # save to object
        contextEmail = {
                'name' :name,
                'email' :email,
                'phone' :phone,
                'message' :messages,
        }
         # Save to DB
        contact = Contact(name=name, email=email, phone=phone, message=messages)

        # Send email to Admin email
        admin_email = 'odedahay@yahoo.com'
        
        # EMAIL_HOST_USER is from setting, using Gmail smtp
        email_provider = settings.EMAIL_HOST_USER

        send_mail(
            'New email inquiry from AGILE Crew website',
            render_to_string('contacts/email.html', contextEmail),
            email_provider,
            [admin_email],
            fail_silently=False,
        )

        contact.save()

        return redirect('/contact-us/thank-you')

    return render(request, 'contacts/contacts.html')

def thank_you(request):
    return render(request, 'contacts/thank-you.html')

def applicant(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact_num = request.POST['contact_num']
        position = request.POST['position']
        message = request.POST['message']
        job_id = request.POST['job_id']
        job_category = request.POST['job_category']

        if 'cv_file' in request.FILES:
            cv_file = request.FILES['cv_file']
        else:
            cv_file = 'None'

         # save to object
        contextEmail = {
                'first_name':first_name,
                'last_name' :last_name,
                'email': email,
                'contact_num':contact_num,
                'position' :position,
                'message':message,
                'job_id': job_id,
                'job_category': job_category
        }

        # Save to DB
        applicant = Applicant(first_name=first_name, last_name=last_name, email=email, contact_num=contact_num, position=position, cv_file=cv_file, message=message, job_id=job_id, job_category=job_category)
              
        applicant.save()

        # Send email to Admin email
        admin_email = 'odedahay@yahoo.com'
        
        # EMAIL_HOST_USER is from setting, using Gmail smtp
        email_provider = settings.EMAIL_HOST_USER

        # Email alert to user
        try:
            mail = EmailMessage(
                'New applicant for '+ position + ', email from AGILE Crew website',
                render_to_string('jobs/email.html', contextEmail),
                email_provider,
                [admin_email],
            )
            mail.content_subtype = 'html'
            
            if 'cv_file' in request.FILES:
                mail.attach(cv_file.name, applicant.cv_file.read(), cv_file.content_type)

            mail.send(fail_silently=False)

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        
        success = 'Applicant '+email+ ' Submitted successfully'
        context = {
            'success':success
        }
        return redirect('/contact-us/applicant/thank-you/', context)

def job_applicant(request):
    context={}
    return render(request, 'jobs/thank-you.html',context)
