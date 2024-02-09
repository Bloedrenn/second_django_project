from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    image = forms.ImageField(required=False, label='Изображение поста')
