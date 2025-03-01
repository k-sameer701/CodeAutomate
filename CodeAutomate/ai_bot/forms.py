from django import forms

class ChatForm(forms.Form):
    text = forms.CharField(label="Ask Here 👇", max_length=255, widget=forms.TextInput(attrs={'size': 40}))