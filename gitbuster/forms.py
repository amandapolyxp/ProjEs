from django import forms

class tokenProj(forms.Form):
    token = forms.CharField()
    projeto = forms.IntegerField()