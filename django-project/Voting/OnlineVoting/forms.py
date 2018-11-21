from django import forms
from .models import VoteFor

class VoteForm(forms.Form):
	name = forms.CharField(required=False)
	party = forms.CharField(required=False)