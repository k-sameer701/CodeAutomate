from django import forms

class MultiStepForm(forms.Form):
    usage_steps = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usage Step'}), required=False)
    feature_steps = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Feature Step'}), required=False)
    contribution_steps = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contribution Step'}), required=False)
    installation_steps = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Installation Step'}), required=False)
