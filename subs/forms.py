from django import forms
from .models import Thread, Post

class CreateThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = forms.CharField()
        self.fields['post'] = field

    def save(self, commit=True):
        post_content = self.cleaned_data['post']
        self.instance.subrediti_id = self.initial['subrediti'].id
        self.instance.author = self.initial['author']
        self.instance.save()
        Post.objects.create(
            content=post_content,
            author=self.initial['author'],
            thread = self.instance,
        )
        return super().save()


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def save(self, commit=True):
        self.instance.thread = self.initial['thread']
        self.instance.author = self.initial['author']
        self.instance.save()
        return super().save()