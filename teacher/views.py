#django里的
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.utils import IntegrityError  #键值重复错误
from django.contrib import messages

#自己写的模型、方法
from announcement.utils import getAnnouncement
from users.models import User
from student.models import Student

from message.models import Message
from thesis.models import Thesis, Tag
from thesis.forms import PublishThesisForm, UpdateThesisForm
from cms_site.utils import get_page_list, get_public_file, \
                           get_teacher_file, get_student_file, sendMessage  
from .forms import UpdateInfoForm
from .models import Teacher

num = 3
no_r_mesg_count = 0

def teacher_home(request):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        context = {}
        students_dict = {}

        teacher = Teacher.objects.get(number = user.username)
        students = teacher.student_set.all()
        for student in students:
            student_file_dict = get_student_file(student)
            students_dict[student] = student_file_dict
        #获取公共文件文件夹下的所有文件
        public_files_dict = get_public_file(user.person)
        teacher_files_dict = get_teacher_file(teacher)

        no_r_mesg_count = Message.objects.filter(receiver=user, is_read=False).count()
        announcements = getAnnouncement(user)
        ann_count = len(announcements)
        if user.no_r_ann_count != ann_count or user.no_r_message_count != no_r_mesg_count:
            user.no_r_ann_count = ann_count
            user.no_r_message_count = no_r_mesg_count
            user.save()

        context['students_dict'] = students_dict
        context['public_files_dict'] = public_files_dict
        context['teacher_files_dict'] = teacher_files_dict
        context['teacher'] = teacher
        context['students'] = students
        return render(request, 'teacher/teacher_home.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def update_info(request):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        teacher = Teacher.objects.get(number = user.username)
        #判断用户是提交修改数据还是进入修改数据页面
        if request.method == 'POST':
            update_info_form = UpdateInfoForm(request.POST)
            if update_info_form.is_valid():
                max_number = update_info_form.cleaned_data['max_number']
                teacher.college = update_info_form.cleaned_data['college']
                teacher.job_title = update_info_form.cleaned_data['job_title']
                teacher.introduction = update_info_form.cleaned_data['introduction']
                teacher.max_number = max_number
                teacher.phonenumber = update_info_form.cleaned_data['phone_number']
                teacher.rest_number = max_number - teacher.student_set.all().count()
                teacher.save()
                messages.success(request, '修改成功！')
                return redirect(reverse('teacher_home'))

        else:
            #将用户原来的数据提取出来放到初始化UpdateInfoForm表单的数据上
            initial_data={'college':teacher.college,'max_number':teacher.max_number,\
                        'job_title':teacher.job_title,'introduction':teacher.introduction,\
                        'phone_number':teacher.phonenumber}
            update_info_form = UpdateInfoForm(initial = initial_data)
        context = {}
        context['update_info_form'] = update_info_form
        return render(request, 'teacher/update_info.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def teacher_thesis(request):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        all_theses = Thesis.objects.filter(publisher = user)
        need_verify_theses = Thesis.objects.filter(publisher__person = 'student', \
                                publisher__student__teacher = user.teacher,need_verify=True)

        context = {}
        context['theses'] = all_theses
        context['is_choiced_theses'] = all_theses.filter(is_choiced=True)
        context['no_choiced_theses'] = all_theses.filter(is_choiced=False)
        context['need_verify_theses'] = need_verify_theses
        return render(request, 'teacher/teacher_thesis.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

def publish_thesis(request):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        if request.method == 'POST':
            publish_thesis_form = PublishThesisForm(request.POST)
            if publish_thesis_form.is_valid():
                title = publish_thesis_form.cleaned_data['title']
                content = publish_thesis_form.cleaned_data['content']
                tags = publish_thesis_form.cleaned_data['tag'].split()
                try:
                    thesis = Thesis.objects.create(title = title, content = content, publisher =user)
                    for tag in tags:
                        tag_obj, is_create = Tag.objects.get_or_create(name = tag)
                        thesis.tags.add(tag_obj)
                    messages.success(request, '发布选题成功！')
                    return redirect(request.GET.get('from', '/'))    #发布成功，跳转到原来的页面
                except IntegrityError:
                    publish_thesis_form.add_error(None, '不能重复创建同一论文题目')
        else:
            publish_thesis_form = PublishThesisForm()

        context = {}
        context['thesis_form'] = publish_thesis_form
        context['panel_head'] = '发布论文题目'
        context['submit_value'] = '发布'
        return render(request, 'teacher/publish_thesis.html', context)
    else:
        redirect('/')

#修改论文题目信息
def update_thesis(request, thesis_pk):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        thesis = Thesis.objects.get(pk = thesis_pk)
        initial = {'title':thesis.title, 'content':thesis.content}
        if request.method == 'POST':
            update_thesis_form = UpdateThesisForm(request.POST, initial=initial)
            if update_thesis_form.is_valid():
                if update_thesis_form.has_changed():
                    title = update_thesis_form.cleaned_data['title']
                    content = update_thesis_form.cleaned_data['content']
                    try:
                        thesis.title = title
                        thesis.content = content
                        thesis.save()
                        messages.success(request, '修改成功')
                        return redirect(request.GET.get('from', '/'))
                    except IntegrityError:
                        update_thesis_form.add_error(None, '不能重复创建同一论文题目')
                else:
                    return redirect(request.GET.get('from', '/'))
        else:
            update_thesis_form = UpdateThesisForm(initial=initial)
        context = {}
        context['thesis_form'] = update_thesis_form
        context['panel_head'] = '修改论文题目信息'
        context['submit_value'] = '修改'
        return render(request, 'teacher/publish_thesis.html', context)
    else:
        return redirect('/')

def delete_thesis(request):
    user = request.user
    if user.is_authenticated and user.person=='teacher':
        try:
            thesis_title = request.GET.get('thesis_title', None)
            if thesis_title:
                thesis = Thesis.objects.get(title = thesis_title, publisher=user)
                if not thesis.is_choiced:
                    thesis.delete()
                    messages.success(request,'删除成功！')
                else:
                    messages.error(request,'该选题已有人选择')
            return redirect(reverse('teacher_thesis'))
        except ObjectDoesNotExist:
            messages.error(request, '未找到该选题！')
        return redirect(request.META.get('HTTP_REFERER', reverse('teacher_thesis')))
    else:
        return redirect('/')

def student_info(request):
    user = request.user
    if user.is_authenticated and user.person == 'teacher':
        context = {}
        student_name = request.GET.get('student_name')
        try:
            student = Student.objects.get(name = student_name, teacher=user.teacher)
            thesis = student.thesis
            if not thesis:
                student_pub_thesis = Thesis.objects.filter(publisher=student.user, is_choiced=True)
                if student_pub_thesis:
                    context['student_pub_thesis'] = student_pub_thesis[0]
            else:
                context['thesis'] = thesis
            context['student'] = student
            return render(request, 'teacher/student_info.html', context)

        except ObjectDoesNotExist:
            return redirect(request.META.get('HTTP_REFERER', reverse('teacher_home')))
    else:
        return redirect('/')

def aggre_thesis(request):
    user = request.user
    if user.is_authenticated and user.person == 'teacher':
        thesis_pk = request.GET.get('thesis_pk', None)
        if thesis_pk:
            try:
                thesis = Thesis.objects.get(pk = thesis_pk)
                student = thesis.publisher.student
                student.thesis = thesis
                student.is_choiced_thesis = True
                thesis.need_verify = False
                student.save()
                thesis.save()
                messages.success(request,'已同意')
                return redirect(reverse('teacher_home'))
            except ObjectDoesNotExist:
                messages.error(request, '找不到该选题')
        return redirect(reverse('teacher_home')) 
    else:
        return redirect('/')

#不同意学生的选题
def disaggre_thesis(request):
    user = request.user
    if user.is_authenticated and user.person == 'teacher':
        print(request.POST.get('student_user_pk', None))
        receiver_pk = int(request.POST.get('student_user_pk', None))
        if receiver_pk:
            try:
                receiver = User.objects.get(pk=receiver_pk)
                thesis = receiver.thesis_set.first()
                content = request.POST.get('disggre_text', None)
                if content.strip():
                    Message.objects.create(receiver = receiver, sender=user,content=content)
                    thesis.need_verify = False
                    thesis.save()
                    messages.success(request, '发送成功！')
                else:
                    messages.error(request, '理由不能为空！')

            except ObjectDoesNotExist:
                pass
            return redirect(request.META.get('HTTP_REFERER', reverse('teacher_home')))
        
    else:
        messages.error(request, '请先登录')
        return redirect('/') 

#查看与某位学生的消息记录
def message_with_student(request):
    user = request.user
    if user.is_authenticated and user.person == 'teacher':
        teacher = user.teacher
        student_pk = request.GET.get('student_pk', None)
        if student_pk:
            student = Student.objects.get(pk = student_pk)
            teacher_messages = Message.objects.filter(sender=student.user, \
                                                    receiver=teacher.user)
            student_messages = Message.objects.filter(sender=teacher.user, \
                                                    receiver=student.user)

            both_messages = sorted(list(teacher_messages) + list(student_messages), \
                                    key=lambda message:message.send_time)
            no_r_m = Message.objects.filter(receiver=user, sender=student.user, is_read=False)
            no_r_m.update(is_read=True)
            user.no_r_message_count = 0
        else:
            return redirect(reverse(latest_message))
        context = {}
        context['both_messages'] = both_messages
        context['teacher'] = teacher
        context['student'] = student
        return render(request, 'teacher/send_message.html', context)
    else:
        messages.error(request, '请先登录')
        return redirect('/')

#发送消息函数
def send_message(request):
    user = request.user
    if user.is_authenticated and user.person =='teacher':
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

#查看所有发送消息的用户列表界面
def latest_message(request):
    user = request.user
    if user.is_authenticated and user.person =='teacher':
        teacher = user.teacher
        latest_message_dict = {}
        students = Student.objects.filter(teacher = teacher)
        for student in students:
            teacher_message = Message.objects.filter(sender=student.user, \
                                                    receiver=teacher.user).first()
            student_message = Message.objects.filter(sender=teacher.user, \
                                                    receiver=student.user).first()

            if teacher_message and student_message:
                if teacher_message.send_time > student_message.send_time:
                    latest_message_dict[student] = teacher_message
                else:
                    latest_message_dict[student] = student_message
            else:
                if teacher_message:
                    latest_message_dict[student] = teacher_message
                elif student_message:
                    latest_message_dict[student] = student_message
                else:
                    latest_message_dict[student] = ''
        
        context = {}
        context['latest_message_dict'] = latest_message_dict
        return render(request, 'teacher/message.html', context)
    else:
        return redirect('/')

