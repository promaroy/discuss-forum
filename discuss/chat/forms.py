from django.forms import ModelForm, TextInput
from .models import msg

class ConForm(ModelForm):
    class Meta:
        model = msg
        fields = ['name','content']
        widgets = {
            'content': TextInput(attrs={'class' : 'input' , 'placeholder' : 'Enter your message'}),
             'name': TextInput(attrs={'class':'input', 'placeholder': 'enter your name'}),
        }
