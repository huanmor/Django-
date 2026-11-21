from django import forms
from .models import Activity
from django.core.exceptions import ValidationError
from django.utils import timezone

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'start_time', 'location']
    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if start_time and start_time < timezone.now():
            raise ValidationError("开始时间不能早于当前时间！")
            
        return start_time