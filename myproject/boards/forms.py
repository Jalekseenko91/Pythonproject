from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Vertel hier iets leuks'}),
        max_length=4000,
        help_text='Maximale lengte mag niet meer zijn dan 4000 karacters.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']