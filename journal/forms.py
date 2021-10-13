from django.forms import ModelForm, Textarea, widgets
from journal.models import Journal

class JournalForm(ModelForm):
    class Meta: #表單元類別
        model = Journal
        fields = ['content']
        widgets = {
            'content':Textarea(attrs={'class':'form-control'}),
        }
        