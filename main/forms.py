from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=50, label='Автор')
    title = forms.CharField(max_length=100, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    image = forms.ImageField(required=False, label='Изображение поста')
