from .models import Announcement
from student.models import Student
from django.db.models import Q


def getAnnouncement(obj):
    person = obj.person
    if person == 'teacher':
        announcements = Announcement.objects.filter(Q(receiver = 'all')\
                                                |Q(receiver = 'all_teacher'))

        
        return announcements
    elif person == 'student':
        student = obj.student
        if student.is_choiced_thesis == False:
            announcements = Announcement.objects.filter(Q(receiver='all_student')\
                                        |Q(receiver='all')|Q(receiver='no_thesis_student'))
        elif student.is_choiced_thesis == True:
            announcements = Announcement.objects.filter(Q(receiver='all_student')\
                                        |Q(receiver='all')|Q(receiver='thesis_student'))
        else:
            announcements = Announcement.objects.filter(Q(receiver='all_student')\
                                                            |Q(receiver='all'))
        return announcements
    else:
        return None

'''  read_announcement = student.read_announcement.all()
        announcements = list(filter(lambda announcement:announcement not in read_announcement,\
                                         announcements))'''
