import random
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Thesis

def thesis_detail(request, thesis_pk):
    person = request.user.person
    context = {}
    if person == 'teacher':
        try:
            thesis = Thesis.objects.get(pk = thesis_pk)
            context['thesis'] = thesis
            return render(request, 'teacher/thesis_detail.html', context)
        except ObjectDoesNotExist:
            messages.error(request, '该选题不存在了！')
            return redirect(reverse('teacher_home'))

    elif person == 'student':
        college = request.user.student.college
        try:
            thesis = Thesis.objects.get(pk = thesis_pk)
            theses_list = []
            tags = thesis.tags.all()
            context['thesis'] = thesis
            if tags:
                for tag in tags:
                    theses_list += list(Thesis.objects.filter(tags=tag, is_choiced=False))
                theses_list += Thesis.objects.filter(publisher = thesis.publisher, is_choiced=False)
                theses_set = set(theses_list)
            if thesis in theses_set:
                theses_set.remove(thesis)
            if len(theses_set) > 5:
                context['theses_with_like'] = random.sample(theses_set,5)
            elif len(theses_set) == 0:
                theses = Thesis.objects.filter(publisher__teacher__college=college, is_choiced=False)
                context['theses_with_like'] = random.sample(list(theses),5)
            else:
                context['theses_with_like'] = theses_set
            return render(request, 'student/thesis_detail.html', context)
        except ObjectDoesNotExist:
            theses = Thesis.objects.filter(publisher__teacher__college = college,\
                                            is_choiced=False)
            cache.set('theses', theses, 120)
            messages.error(request, '该选题不存在了！')
            return redirect( reverse('thesis_list'))
        
    else:
        return redirect('/')
        