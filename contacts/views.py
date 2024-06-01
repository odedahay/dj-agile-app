from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Contact, Applicant
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from agile.settings import EMAIL_HOST_USER
from django.conf import settings
from django.template.loader import render_to_string
from pages.models import Components
from .forms import ContactForm
import smtplib

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def inquiry(request):
    
    if request.method == 'POST':
        # contact_admin_email = Components.objects.get(slug__exact='inquiry-admin-email')
        try:
            contact_admin_email = Components.objects.get(slug__exact='inquiry-admin-email')
        except Components.DoesNotExist:
            return HttpResponseBadRequest("Admin email component not found.")
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data.get('phone', '')
            message = form.cleaned_data['message']

             # save to object
            contextEmail = {
                    'name' :name,
                    'email' :email,
                    'phone' :phone,
                    'message' :message,
            }
             # Save to DB
            contact = Contact(name=name, email=email, phone=phone, message=message)
            # Send email to Admin email
            admin_email = contact_admin_email.content

            try:
                send_mail(
                    'New email inquiry from AGILE Crew website',
                    render_to_string('contacts/email.html', contextEmail),
                    EMAIL_HOST_USER,
                    [admin_email], 
                    fail_silently=False,
                )
                contact.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            except smtplib.SMTPException as e:
                return HttpResponse(f"SMTP error: {e}")
            except UnicodeEncodeError as e:
                return HttpResponse(f"Unicode encode error: {e}")

            return redirect('/contact-us/thank-you')
    else:
        form = ContactForm()

    return render(request, 'contacts/contacts.html', {'form': form})

def thank_you(request):
    return render(request, 'contacts/thank-you.html')

def applicant(request):
   
    if request.method == 'POST':
    # if is_ajax(request=request):
        applicant_admin_email = Components.objects.get(slug__exact='applicant-admin-email')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact_num = request.POST['contact_num']
        position = request.POST['position']
        message = request.POST['message']
        job_id = request.POST['job_id']
        job_category = request.POST['job_category']

        cv_file = request.FILES['cv_file'] if 'cv_file' in request.FILES else None


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
        applicant = Applicant(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_num=contact_num,
            position=position,
            cv_file=cv_file,
            message=message,
            job_id=job_id,
            job_category=job_category
        )      
        applicant.save()

        # Send email to Admin email
        admin_email = applicant_admin_email.content
       
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
            return HttpResponseBadRequest('Invalid header found')
        
        success = 'Applicant '+email+ ' Submitted successfully'
        context = {
            'success':success
        }
        return redirect('/contact-us/applicant/thank-you/', context)
        # return JsonResponse({
        #             'msg':'Success'
        #         })

def job_applicant(request):
    context={}
    return render(request, 'jobs/thank-you.html',context)
