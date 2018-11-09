from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages

from announcement.utils import getAnnouncement #getAnnouncement(user)
from announcement.models import Announcement
from message.models import Message
from .forms import LoginForm, UpdatePsswordForm


def logout(request):
    auth.logout(request)
    
    return redirect(reverse('login'))

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            if user:
                auth.login(request, user)
                if user.person == 'teacher':
                    return redirect(reverse('teacher_home'))
                elif user.person == 'student':
                    student = user.student
                    #判断学生的信息是否完整，如果不完整就发送messages提醒学生
                    if not student.phonenumber or not student.email:
                        messages.warning(request, '请完善个人信息')
                    if not student.teacher:
                        messages.error(request, '请尽快选择教师和选题！')
                    elif not student.is_choiced_thesis:
                        messages.error(request, '请尽快进行选题！')
                    return redirect(reverse('student_home'))
                else:
                    return redirect('/')
    else:
        login_form = LoginForm()

    return render(request, 'users/login.html', {'login_form':login_form})

def update_password(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            update_password_form = UpdatePsswordForm(request.POST)
            if update_password_form.is_valid():
                old_password = update_password_form.cleaned_data['old_password']
                #验证旧密码是否正确
                if auth.authenticate(username=user.username, password=old_password):
                    password = update_password_form.cleaned_data['password']
                    password_again = update_password_form.cleaned_data['password_again']
                    user.set_password(password)
                    user.save()
                    #修改成功后进行登陆
                    user = auth.authenticate(username=user.username, password=password)
                    auth.login(request, user)
                    messages.success(request,'修改成功！')
                    if user.person == 'teacher':
                        return redirect(request.GET.get('from','/teacher'))
                    return redirect(request.GET.get('from', '/student'))
                else:
                    update_password_form.add_error('old_password', '旧密码不正确')
        else:
            update_password_form = UpdatePsswordForm()

        context = {}
        context['update_password_form'] = update_password_form
        if user.person == 'teacher':
            return render(request, 'users/teacher_update_password.html', context)
        else:
            return render(request, 'users/student_update_password.html', context)
    else:
        return redirect('/')
