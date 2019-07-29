from django import forms
from .models import Blog #모델기반의 폼을 마늘겠다

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog #모델은 블로그 기반이다
        fields = ['title', 'description'] #그 안에 필드는 타이틀과 바디를 쓸거다