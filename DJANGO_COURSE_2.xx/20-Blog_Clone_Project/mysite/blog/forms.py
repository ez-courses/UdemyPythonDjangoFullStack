from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

        """
        ToDo:
            default author to request.user
        """


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
