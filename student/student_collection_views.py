from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError

from thesis.models import Thesis
from teacher.models import Teacher
from message.models import Message

from .models import Collection

def collect(request, object_id):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        try:
            ct = request.GET.get('content_type')
            model = ContentType.objects.get(model=ct).model_class()
            content_object = model.objects.get(pk=object_id)
            Collection.objects.create(content_object=content_object, student = user.student)
            messages.success(request, '收藏成功！')
        except IntegrityError:
            if ct == 'thesis':
                messages.error(request, '你已经收藏过此题！')
            else:
                messages.error(request,'你已经收藏过此教师')
        return redirect(request.META.get('HTTP_REFERER','/')) 
    else:
        return redirect('/')

def cancel_collect(request, ct, object_id):
    user = request.user
    if user.is_authenticated and user.person =='student':
        content_type = ContentType.objects.get(model=ct)
        student = user.student
        collect = Collection.objects.get(content_type=content_type, object_id=object_id,\
                                          student=student)
        collect.delete()
        messages.success(request, '取消收藏成功')
        return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/')

def student_collection(request):
    user = request.user
    if user.is_authenticated and user.person =='student':
        student = user.student
        thesis_collections = Thesis.objects.filter(collection__student=student,\
                                                    is_choiced=False)
        teacher_collections = Teacher.objects.filter(collection__student=student, \
                                                    rest_number__gt=0)
        invalid_theses = Thesis.objects.filter(collection__student=student,\
                                                    is_choiced=True)
        invalid_teachers = Teacher.objects.filter(collection__student=student, \
                                                    rest_number=0)
        context = {}
        context['thesis_collections'] = thesis_collections
        context['teacher_collections'] = teacher_collections
        context['invalid_theses'] = invalid_theses
        context['invalid_teachers'] = invalid_teachers
        return render(request, 'student/student_collection.html', context)
    else:
        return redirect('/')
        