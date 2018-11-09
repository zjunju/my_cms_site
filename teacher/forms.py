from django import forms


class UpdateInfoForm(forms.Form):
    college = forms.CharField(label = '学院', widget=forms.TextInput(attrs={'class':'input-field'}))
    job_title = forms.CharField(label = '职称', widget=forms.TextInput(attrs={'class':'input-field'}))
    phone_number = forms.CharField(label='手机号码', widget=forms.TextInput(attrs={'class':'input-field'}))
    max_number = forms.IntegerField(label='最大指导人数',\
                                    widget=forms.NumberInput(attrs={'class':'input-field'}))
    introduction = forms.CharField(label='简介', required=False,
                                    widget=forms.Textarea(attrs={'class':'form-control'}))
    

    def clean_max_number(self):
        max_number = self.cleaned_data.get('max_number')
        if max_number < 0:
            raise forms.ValidationError('不能小于0')
        else:
            return max_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 11:
            raise form.ValidationError('请输入正确的手机号')
        else:
            return phone_number


