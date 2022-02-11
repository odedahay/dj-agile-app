from django.shortcuts import render, redirect
from .models import Contact, Applicant

def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        messages = request.POST.get('message')

         # Save to DB
        contact = Contact(name=name, email=email, phone=phone, message=messages)
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
            cv_file = False

        # Save to DB
        applicant = Applicant(first_name=first_name, last_name=last_name, email=email, contact_num=contact_num, position=position, cv_file=cv_file, message=message, job_id=job_id, job_category=job_category)
        applicant.save()
    
        return redirect('/contact-us/thank-you')

    #return render('contact-us/applicant')
