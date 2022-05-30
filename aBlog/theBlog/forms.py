# from tkinter import Widget
from dataclasses import field
# from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Category, Comment


# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainent')]

choices = Category.objects.all().values_list('name', 'name')
# create_choice = forms.TextInput(attrs={'placeholder':'New Category'})


choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titles'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'username', 'value': '', 'id':'author', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here..',
        'rows':'4',
    }))
    
    class Meta:
        model = Comment
        fields = ('content',)