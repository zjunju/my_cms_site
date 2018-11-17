from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='学号', widget=forms.TextInput(
                                                attrs={'placeHolder':'请输入学号',\
                                                        'class':'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                            attrs={'placeHolder':'请输入密码',\
                                                    'class':'form-control'}))
    captcha = CaptchaField(label='验证码')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username = username, password = password)
        if user:
            self.cleaned_data['user'] = user
        else:
            raise forms.ValidationError('学号或者密码错误')
        return self.cleaned_data

class UpdatePsswordForm(forms.Form):
    old_password = forms.CharField(label='旧密码', widget=forms.PasswordInput(\
                                                attrs={'placeHolder':'请输入旧密码','class':'form-control'}))

    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                            attrs={'placeHolder':'请输入密码','class':'form-control'}))

    password_again = forms.CharField(label='再次输入密码', widget=forms.PasswordInput(
                                            attrs={'placeHolder':'再次输入密码','class':'form-control'}))

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次密码输入不一致')
        else:
            return password_again
        


#废弃的注册表单
'''class ReigsterForm(forms.Form):
    username = forms.CharField(label='学号', widget=forms.TextInput(
                                                attrs={'placeHolder':'请输入学号','class':'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                            attrs={'placeHolder':'请输入密码','class':'form-control'}))
    password_again = forms.CharField(label='再次密码', widget=forms.PasswordInput(
                                            attrs={'placeHolder':'再次输入密码','class':'form-control'}))
    person = forms.ChoiceField(label='人物', choices=(('teacher','教师'),('student','学生')),
                                widget='')


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username ).count():
            raise forms.ValidationError('该学号已存在')
        else:
            return username

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次密码输入不一致')
        else:
            return password_again'''

