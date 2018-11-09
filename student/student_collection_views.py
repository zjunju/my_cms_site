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

def cancel_collect(request):
    user = request.user
    if user.is_authenticated and user.person =='student':
        ct = request.GET.get('content_type')
        content_type = ContentType.objects.get(model=ct)
        object_id = request.GET.get('object_id')
        student = user.student
        collect = Collection.objects.get(content_type=content_type, object_id=object_id, student=student)
        collect.delete()
        messages.success(request, '取消收藏成功')
        return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/')

def student_collection(request):
    user = request.user
    if user.is_authenticated and user.person =='student':
        student = user.student
        thesis_ct = ContentType.objects.get_for_model(Thesis)
        teacher_ct = ContentType.objects.get_for_model(Teacher)
        thesis_collections = Collection.objects.filter(student=student, content_type=thesis_ct)
        teacher_collectons = Collection.objects.filter(student=student, content_type=teacher_ct)

        context = {}
        no_r_mesg_count = Message.objects.filter(receiver=user, is_read=False).count()
        context['thesis_collections'] = thesis_collections
        context['teacher_collectons'] = teacher_collectons
        context['no_r_mesg_count'] = no_r_mesg_count
        return render(request, 'student/student_collection.html', context)
    else:
        return redirect('/')
        