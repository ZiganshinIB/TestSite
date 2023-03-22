from django import forms
from .models import Homework, Curse, GroupC


class HomeworkForm(forms.Form):
     title = forms.CharField(max_length=25, label="Название",
                             widget=forms.TextInput(attrs={"class":"form-control gx-10"}))
     file = forms.FileField(label="Файл",)
     author = forms.CharField(max_length=25, label="Автор",
                              widget=forms.TextInput(attrs={"class": "form-control"}))
     curse = forms.ModelChoiceField(queryset=Curse.objects.all(), label="Курс")


class GroupForm(forms.ModelForm):
    class Meta:
        model = GroupC
        fields = '__all__'


class CurseForm(forms.ModelForm):
    class Meta:
        model = Curse
        fields = '__all__'

