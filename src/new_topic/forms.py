from django import forms
from boards.models import Topic
from tinymce.widgets import TinyMCE

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=TinyMCE(attrs={'id':'editor', 'rows': 5, 'placeholder': 'What is on your mind?'}),
        # widget=forms.Textarea(
        #     attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        # ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']