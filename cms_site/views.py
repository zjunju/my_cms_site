import os
from django.http import FileResponse
from django.utils.http import urlquote
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

upload_dir = settings.UPLOAD_DIR  #D:\1毕业设计\cms_site\media\upload
public_dir = settings.PUBLIC_DIR  #D:\1毕业设计\cms_site\media\public

#下载文件
def download_file(request):
    user = request.user
    if user.is_authenticated:
        file_path = request.GET.get('file', None)
        if file_path:
            file_name = os.path.basename(file_path)
            file = open(file_path, 'rb')  #打开要下载的文件，然后进行下载
            response = FileResponse(file)
            response['Content-Type']='application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"'%urlquote(file_name)
            return response
        else:
            messages.error(request, '找不到文件')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')

#删除文件
def delete_file(request):
    user = request.user
    if user.is_authenticated:
        file_path = request.GET.get('file_path', None)
        if file_path:
            try:
                os.remove(file_path)
                messages.success(request, '删除成功!')
            except FileNotFoundError:
                messages.error(request, '找不到该文件!')
        else:
            messages.error(request, '没有选择文件！')
        return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/')

#上传文件
def upload_file(request):
    user = request.user
    if user.is_authenticated:
        if user.person == 'student':
            student = user.student
            if student.teacher:
                upload_path = os.path.join(upload_dir, student.teacher.name + student.teacher.number, \
                                            student.name + student.number)
            else:
                messages.error(request, '暂未选择老师，请先选择老师')
                return redirect(request.META.get('HTTP_REFERER','/'))
        else:
            teacher = user.teacher
            upload_path = os.path.join(upload_dir, teacher.name + teacher.number)

        if request.method == 'POST':
            file_max_size = 50 * 1024 * 1024    #单位为B
            myFile = request.FILES.get("myfile", None)   #所有提交的文件都保存在request.FILES
            if myFile and myFile.size < file_max_size:
                with open(os.path.join(upload_path, myFile.name), 'wb+') as fo:
                    for chunk in myFile.chunks():
                        fo.write(chunk)
                messages.success(request, '上传成功')
            
        return redirect(request.META.get('HTTP_REFERER','/'))
    else: 
        return redirect('/')
