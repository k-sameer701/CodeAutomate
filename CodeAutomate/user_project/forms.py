from django import forms

class StepForm(forms.Form):
    step = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a step'}), required=True)