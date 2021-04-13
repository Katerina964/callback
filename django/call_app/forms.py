from django import forms
from .models import Crmaccount


class CrmaccountForm(forms.ModelForm):

    class Meta:
        model = Crmaccount
        fields = ('host', 'token',)
