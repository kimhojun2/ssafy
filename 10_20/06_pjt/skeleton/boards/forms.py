from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', )
        # # exclude = ('author',)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        # exclude =('author',)