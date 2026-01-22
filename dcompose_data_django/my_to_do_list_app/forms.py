from django import forms
from my_to_do_list_app.models import ToDoList

# I have creted ModelForm to act as HTML form fields for perform CRUD operation on frontend side

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('title', 'description', 'completed')
        labels = {
            'completed':'I Agree'
        }
        error_messages = {
            'title':{'required':'You must have to fill title of To Do is compulsory'},
            'description':{'required':'You must have to fill description'},
            'completed':{'required':'Click on Agree click box'}
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title of To Do List'}),

            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter description of To Do List', 'rows':5}),

            'created_at':forms.TextInput(attrs={'class':'form-control', 'readonly':True})
        }