from django import forms
from .models import Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Vertel hier iets leuks'}),
        max_length=4000,
        help_text='Maximale lengte mag niet meer zijn dan 4000 karacters.'
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]