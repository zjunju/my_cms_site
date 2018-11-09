from django import forms
from ckeditor.widgets import CKEditorWidget


class PublishThesisForm(forms.Form):
    title = forms.CharField(label='题目', widget=forms.TextInput(attrs={'class':'input-field'}))
    tag = forms.CharField(label='选题标签', widget=forms.TextInput(attrs={'class':'input-field'}))
    content = forms.CharField(label='内容', widget=CKEditorWidget(\
                            config_name ='thesisContent_ckeditor'),\
                            error_messages={'required':'请输入论文题目的内容'} )
    

class UpdateThesisForm(forms.Form):
    title = forms.CharField(label='题目', widget=forms.TextInput(attrs={'class':'input-field'}))
    content = forms.CharField(label='内容', widget=CKEditorWidget(\
                            config_name ='thesisContent_ckeditor') )
