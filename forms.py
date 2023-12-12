from django import forms
from . import models

class PatientsForm(forms.ModelForm):
    class Meta:
        model = models.patientmodel
        fields = "__all__"