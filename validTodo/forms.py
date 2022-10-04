from django import forms

from validTodo.models import TodoModel


class ModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'desc']
