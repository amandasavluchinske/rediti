from django import forms

from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Erro na confirmação de senha."
            )

    def save(self, commit=True):
        raw_password = self.cleaned_data.get('password')
        self.instance.username = self.cleaned_data.get('username')
        self.instance.set_password(raw_password)
        if commit:
            self.instance.save()
        return self.instance