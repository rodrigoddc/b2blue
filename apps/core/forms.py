from django import forms


class VoteForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    rating = forms.IntegerField(min_value=0, max_value=10)
