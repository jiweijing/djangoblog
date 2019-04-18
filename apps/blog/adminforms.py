# from dal import autocomplete
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

