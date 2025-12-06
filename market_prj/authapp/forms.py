from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authapp.models import TravelUser, TravelUserProfile


# Регистрация пользователя

class TravelUserRegisterForm(UserCreationForm):
    class Meta:
        model = TravelUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return age


# Редактирование аккаунта

class TravelUserEditForm(forms.ModelForm):
    class Meta:
        model = TravelUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# Логин

class TravelUserLoginForm(AuthenticationForm):
    class Meta:
        model = TravelUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# Редактирование профиля

class TravelUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = TravelUserProfile
        fields = ('tagline', 'aboutMe')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
