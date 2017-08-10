from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['M_Name', 'M_Email', 'M_Message']
        labels = {'M_Name': '', 'M_Email': '', 'M_Message': ''}

