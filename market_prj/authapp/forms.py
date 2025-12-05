from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordResetForm,
                                       SetPasswordForm)

from authapp.models import TravelUser, TravelUserProfile


# Регистрация
class TravelUserRegisterForm(UserCreationForm):
    class Meta:
        model = TravelUser

        # password1 и password2 берем из UserCreationForm, avatar уже Fileinput по умолчанию

        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2', 'age', 'avatar')

    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return age

# Логин
class TravelUserLoginForm(AuthenticationForm):
    class Meta:
        model = TravelUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# редактирование профиля
class TravelUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = TravelUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# редактирование аккаунта
class TravelUserEditForm(forms.ModelForm):
    class Meta:
        model = TravelUser
        fields = ('username','first_name', 'last_name', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# форма восстановления пароля
class TravelUserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TravelUserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):  # bootstrap
        super().__init__(*args, **kwargs)
        for field, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
