from django import forms
from .models import Todo_list


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        fields = ('title', 'content', 'end_date')
        widgets = {
            'end_date': DateInput()
        }
