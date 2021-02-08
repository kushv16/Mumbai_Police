from django import forms
from .models import Complaint

class ComplaintForm(forms.Form):
    class Meta:
        model = Complaint
        fields = [
            'date', 'time', 'type', 'description', 'file'
        ]