from django import forms

class StudentInfoForm(forms.Form):
    email = forms.EmailField(max_length = 30, label='邮箱', required = False,
                              widget=forms.TextInput(attrs={'class':'input-field'}))
    phonenumber = forms.CharField(max_length = 11, label='手机号码', required = False,
                                  widget=forms.TextInput(attrs={'class':'input-field'}))
    introduction = forms.CharField(label='简介', required = False,
                                    widget=forms.Textarea(attrs={'class':'form-control'}))


    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get('phonenumber', '')

        if len(phonenumber) != 11:
            raise forms.ValidationError('手机号错误')
        else:
            return phonenumber
      

