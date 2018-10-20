from django.forms import fields, forms
from django.forms.widgets import DateTimeInput, Textarea


class ToDo(forms.Form):
    title = fields.CharField(max_length=2048)
    description = fields.CharField(widget=Textarea)
    todo_time = fields.CharField(widget=DateTimeInput(attrs={'id': 'datetimepickerinput'}))
    status = fields.ChoiceField(choices=(('Pending', 'Pending'), ('In Progress', 'In Progress'),
                                         ('Completed', 'Compeleted')))

    def clean(self):
        cleaned_data = super(ToDo, self).clean()
        return cleaned_data
