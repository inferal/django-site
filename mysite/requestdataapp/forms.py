from django import forms

class UserBioForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(label="You age")
    bio = forms.CharField(label="Biography", widget=forms.Textarea)