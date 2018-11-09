from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

#get_tag_list(college)  get_page_list(obj_list, page, num ,name) 
from cms_site.utils import get_public_file, get_student_file, get_teacher_file, sendMessage
from announcement.utils import getAnnouncement
from message.models import Message
from announcement.models import Announcement

from .forms import StudentInfoForm
from .models import Student

def student_home(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        context = {}
        student = Student.objects.get(number = user.username)

        #获取公告文件
        public_files = get_public_file(user.person)
        context['public_files'] = public_files

        if student.teacher:
            student_files = get_student_file(student) #返回学生文件夹的所有文件
            teacher_files = get_teacher_file(student.teacher)
            context['student_files'] = student_files
            context['teacher_files'] = teacher_files
            
        #获取未读信息数
        no_r_mesg_count = Message.objects.filter(receiver=user, is_read=False).count()
        if no_r_mesg_count != user.no_r_message_count:
            user.no_r_message_count = no_r_mesg_count
            user.save()

        #获取公告
        announcements = getAnnouncement(user)
        no_r_ann_count = len(announcements)
        if user.no_r_ann_count !=no_r_ann_count:
            user.no_r_ann_count = no_r_ann_count
            user.save()

        context['student'] = student
        return render(request, 'student/student_home.html', context)
    else:
        return redirect('/')

#学生修改信息
def student_update_info(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        if request.method == 'POST':
            student_info_form = StudentInfoForm(request.POST)
            student = Student.objects.get(number = user.username)
            if student_info_form.is_valid():
                student.email = student_info_form.cleaned_data['email']
                student.introduction = student_info_form.cleaned_data['introduction']
                student.phonenumber = student_info_form.cleaned_data['phonenumber']
                student.save()
                return redirect(request.GET.get('from', '/'))
        else:
            student = Student.objects.get(number = user.username)
            initial_data = {'email':student.email,'phonenumber':student.phonenumber,\
                            'introduction':student.introduction}
            student_info_form = StudentInfoForm(initial = initial_data)

        context = {}
        context['student_info_form'] = student_info_form
        return render(request, 'student/update_info.html', context)
    else:
        return redirect('/')

#查看与教师的信息记录
def student_message(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        no_r_messges = Message.objects.filter(receiver=user, is_read=False)
        no_r_messges.update(is_read=True)
        user.no_r_message_count = 0
        user.save()
        
        student = user.student
        teacher = student.teacher
        student_messages = Message.objects.filter(Q(sender=student.user) | Q(receiver=student.user))\
                                  .order_by('send_time')
        
        context = {}
        context['student'] = student
        context['teacher'] = teacher
        context['student_messages'] = student_messages
        return render(request, 'student/send_messages.html', context)
    else:
        return redirect('/')

def student_send_message(request):
    user = request.user
    if user.is_authenticated and user.person =='student':
        receiver_pk = request.POST.get('receiver_pk', None)
        content = request.POST.get('message', None)
        if receiver_pk:
            data = sendMessage(receiver_pk, user, content)
            return JsonResponse(data)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def student_no_read_message(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student = user.student
        no_read_messages = Message.objects.filter(receiver=user, is_read = False, \
                                                    sender=student.teacher.user)
        context = {}
        context['content_header'] = '未读消息'
        context['mesg'] = 'mesg'
        context['mesg_active'] = 'active'
        context['ann_or_mesgs'] = no_read_messages
        return render(request, 'student/all_ann_or_mesg.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def all_announcement(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        announcements = getAnnouncement(user)
        
        context = {}
        context['content_header'] = '所有公告'
        context['ann'] = 'ann'
        context['ann_active'] = 'active'
        context['ann_or_mesgs'] = announcements
        return render(request, 'student/all_ann_or_mesg.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def announcement_detail(request, announcement_pk):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        announcement = Announcement.objects.get(pk = announcement_pk)
        
        context = {}
        context['announcement'] = announcement
        return render(request, 'student/announcement_detail.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')
