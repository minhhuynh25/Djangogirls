from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable'}))
    class Meta:
        model = Post
        fields = ('title', 'text',)
