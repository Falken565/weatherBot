from django import forms

from users.models import User


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('tg_id',)
        labels = {
            'tg_id': ('Телеграмм id'),
        }
        help_texts = {
            'tg_id': ('Введите свой телеграмм id'),
        }
