from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError   #键值重复错误

from cms_site.utils import get_page_list, get_tag_list

from thesis.forms import UpdateThesisForm
from thesis.models import Thesis
from teacher.models import Teacher

from .models import Student

num = 3     #定义每页的数据数量

#学生点击我的选题进入学生已选选题的界面
def student_thesis(request):        
    user = request.user
    if user.is_authenticated and user.person == 'student':

        context = {}
        student = user.student
        thesis = student.thesis
        if not thesis:
            student_pub_thesis = Thesis.objects.filter(publisher = user)
            if student_pub_thesis:     
                context['student_pub_thesis'] = student_pub_thesis[0]

        context['thesis'] = thesis
        context ['student'] = student
        return render(request, 'student/student_thesis.html', context)
    else:
        return redirect('/')

#所有导师列表
def teacher_list(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        page = request.GET.get('page', 1)
        teacher_name = request.GET.get('teacher_name', '')
        if teacher_name:        #判断学生是否搜索
            teachers = Teacher.objects.filter(name__contains = teacher_name, \
                                              college =user.student.college)
            if teachers.count() == 0:
                messages.error(request, '搜索不到这位老师，已为你显示所有教师')
                teachers = Teacher.objects.filter(college= user.student.college)
            else:
                messages.success(request, '为你找到如下结果')
        else:   #学生未进行搜索教师，显示所有教师
            teachers = cache.get('teachers', None)
            if not teachers:
                teachers = list(Teacher.objects.filter(college= user.student.college))
                cache.set('teachers', teachers, 600)

        context = get_page_list(teachers, page, num, 'teachers_with_page')

        context['teachers'] = teachers
        return render(request, 'student/teacher_list.html', context)
    else:
        return redirect('/')

#选择教师
def apply_teacher(request, teacher_pk):
    user = request.user
    if user.is_authenticated and user.person =='student':
        student = user.student
        if student.teacher:
            messages.error(request, '你已有导师')
        else:
            teacher = Teacher.objects.get(pk=teacher_pk)
            student.teacher = teacher
            student.save()
            messages.success(request, '选择成功')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')

#查看教师信息
def teacher_info(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student_teacher = user.student.teacher
        teacher_name = request.GET.get('teacher_name', '')   #获取老师的pk
        if teacher_name:
            page = request.GET.get('page', 1)
            try:
                teacher = Teacher.objects.get(name = teacher_name)
                theses = teacher.user.thesis_set.filter(is_choiced = False)
                context = {}
                context['theses'] = theses
                context['teacher'] = teacher
                if student_teacher == teacher:  #判断教师是否为学生导师，如果是，则导航栏高亮
                    context['active'] = 'active'
                return render(request, 'student/teacher_info.html', context)
            except ObjectDoesNotExist:
                pass

        if student_teacher:  #判断学生是否选择导师
            messages.error(request,'请选择查看哪位教师')
        else:
            messages.error(request, '暂未选择教师')
        return redirect(request.META.get('HTTP_REFERER', reverse('teacher_list')))
    else:
        return redirect('/')

#学生点击马上选题，进入选题列表界面，进行选题
def thesis_list(request):
    user = request.user
    if user.is_authenticated and user.person =='student':
        college = user.student.college
        page = request.GET.get('page', 1)
        if request.method == 'POST':
            thesis_name = request.POST.get('thesis_name')
            if thesis_name.strip():
                theses = Thesis.objects.filter(is_choiced=False, title__contains=thesis_name,\
                                                publisher__teacher__college = college)
                if theses.count():
                    messages.success(request, '为你找到如下结果')
                else:
                    messages.error(request, '未找到结果，为你显示所有论文选题')
                    return redirect(reverse('thesis_list'))
            else:
                messages.error(request, '论文题目不能为空')
                return redirect(reverse('thesis_list'))
        else:
            theses = cache.get('theses', None)
            if not theses:
                theses = Thesis.objects.filter(is_choiced = False, \
                                            publisher__teacher__college = college)
                cache.set('theses', theses, 120)

        tag_list = cache.get('thesis')
        if not tag_list:
            tag_list = get_tag_list(user.student.college)
            cache.set('tag_lsit', tag_list, 600)

        context = get_page_list(theses, page, num, 'theses_with_page')
        context['theses'] = theses
        context['content_header'] = '所有论文题目'
        context['tags'] = tag_list
        return render(request, 'student/thesis_list.html', context)
    else:
        return redirect('/')

def thesis_list_with_tag(request, tag_name):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        context = {}
        page = request.GET.get('page', 1)
        theses = cache.get('theses', None)
        if theses:
            theses = theses.filter(tags__name = tag_name, is_choiced=False)
        else:
            theses = Thesis.objects.filter(is_choiced = False, tags__name = tag_name)
        if theses:
            context = get_page_list(theses, page, num, 'theses_with_page')

        tag_list = cache.get('tag_list')
        if not tag_list:
            tag_list = get_tag_list(user.student.college)
            cache.set('tag_lsit', tag_list, 600)

        context['theses'] = theses
        context['tags'] = tag_list
        context['content_header'] = tag_name
        return render(request, 'student/thesis_list.html', context)
    else:
        return redirect('/')

def apply_thesis(request, thesis_pk):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student = Student.objects.filter(number = user.username)
        try:
            thesis = Thesis.objects.get(pk = thesis_pk)
            #判断老师还剩下几个学生位
            teacher = thesis.publisher.teacher
            if student[0].is_choiced_thesis or user.thesis_set.count() > 0:
                messages.error(request, '你已经选择论文题目。')
                return redirect(request.META.get('HTTP_REFERER'))
            elif teacher.rest_number <= 0:
                messages.error(request,'该老师已经满人')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                try:
                    student.update(thesis = thesis, teacher=teacher, is_choiced_thesis=True)
                    teacher.rest_number -= 1
                    thesis.is_choiced = True
                    thesis.save()
                    teacher.save()
                    messages.success(request, '选择成功')
                except IntegrityError:
                    messages.error(request, '该题已被选择！')
                    return redirect(reverse('thesis_list'))
                return redirect(reverse('student_thesis'))
        except ObjectDoesNotExist:
            messages.error(request, '该题已被教师删除！')
            return redirect(reverse('thesis_list'))
    else:
        return redirect('/')

#只取消选择论文题目， 不取消选择教师
def cancel_thesis(request, thesis_pk):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student = Student.objects.get(number = user.username)
        teacher = student.teacher
        thesis = Thesis.objects.get(pk = thesis_pk)
        student.thesis = None
        student.is_choiced_thesis = False
        thesis.is_choiced = False
        teacher.rest_number += 1
        student.save()
        thesis.save()
        teacher.save()
        messages.success(request, '取消选题成功')
        return redirect(reverse('student_thesis'))
    else:
        return redirect('/')

#取消选择教师，论文选题和教师同时取消选择
def cancel_teacher(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student = user.student 
        thesis = student.thesis
        teacher = student.teacher
        teacher.rest_number += 1
        student.teacher = None
        if thesis:
            thesis.is_choiced = False
            student.thesis = None
            student.is_choiced_thesis = False
        if user.thesis_set.all():
            user.thesis_set.all().delete()
        student.save()
        teacher.save()
        messages.error(request, '取消成功！')
        return redirect(reverse('student_thesis'))

    else:
        return redirect('/')

#学生自己添加选题
def add_thesis(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        student = user.student
        #判断学生是否已经发布过论文选题
        if user.thesis_set.count() > 0:
            messages.error(request, '你已经发布过论文选题！')
        elif student.thesis:
            messages.error(request, '你已经有论文选题！')
        else:
            if request.method == 'POST':
                thesis_form = UpdateThesisForm(request.POST)
                if thesis_form.is_valid():
                    title = thesis_form.cleaned_data['title']
                    content = thesis_form.cleaned_data['content']
                    teacher = student.teacher
                    if teacher:
                        thesis = Thesis.objects.create(title=title, content=content,\
                                        is_choiced=True,need_verify=True,publisher=user)

                        messages.success(request, '已添加自己的选题成功，等待教师审核！')
                    else:
                        messages.error(request, '还未选择指导老师！')
                    return redirect(reverse('student_thesis'))
            else:
                thesis_form = UpdateThesisForm()

            context = {}
            context['thesis_form'] = thesis_form
            return render(request, 'student/add_thesis.html', context)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')

def delete_thesis(request, thesis_pk):
    user = request.user
    if user.is_authenticated and user.person=='student':
        thesis = Thesis.objects.get(pk = thesis_pk)
        student = user.student
        student.thesis = None
        student.is_choiced_thesis = False
        student.save()
        thesis.delete()
        messages.success(request,'删除成功！')

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))
