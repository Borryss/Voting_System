from django import forms
from .models import Poll, PollOption

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']

class PollOptionForm(forms.ModelForm):
    class Meta:
        model = PollOption
        fields = ['description', 'option_text']  # Додаємо поле для опису опції
