
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Resume
from app_forms.models import PersonalData,Contact,WorkExperience,AcademicFormation




@login_required(login_url='login')
def platform_view(request):
    user = request.user
    success_message = request.session.pop('form_success', None)

    if request.method=='POST':
        title_resume = request.POST.get('title')
        if title_resume:
            request.session['title_resume'] = title_resume
            return redirect('form_wizard')


    user_resume = Resume.objects.filter(user = user)

    context = {
        'user_resume': user_resume,
        'success_message': success_message,
    }
    return render(request, 'cv_platform.html',context)


@login_required(login_url='login')
def delete_resume(request,resume_id):
    resume = get_object_or_404(Resume,id=resume_id,user=request.user)
    resume.delete()
    return redirect('cv_platform')

@login_required(login_url='login')
def preview (request,resume_id):
    preview_resume = Resume.objects.filter(id=resume_id,user=request.user).first()

    personal_data = PersonalData.objects.filter(resume=preview_resume).all()
    contact_data = Contact.objects.filter(resume=preview_resume).all()
    workexperience_data = WorkExperience.objects.filter(resume=preview_resume).all()
    academic_data = AcademicFormation.objects.filter(resume=preview_resume).all()
    context = {''
               'personal_data':personal_data,
               'contact_data':contact_data,
               'workexperience_data':workexperience_data,
               'academic_data':academic_data}
    return render(request,'preview.html',context)








