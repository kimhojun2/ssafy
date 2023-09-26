# form 사용자들로부터 데이터를 받기위해 활용하는 방법

from django import forms
from .models import Article

# Form 과 ModelForm의 차이 -> DB
# Form : DB에 저장 X
# ModelForm : DB에 저장 O



# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget = forms.Textarea)


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         # 모델에 있는 모든 필드를 이 폼에서 사용하겠다.
#         fields = '__all__'

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'},
    )

    class Meta:
        model = Article
        fields = '__all__'