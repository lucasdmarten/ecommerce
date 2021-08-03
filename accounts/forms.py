from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import MyUser


class CreateUserForm(forms.ModelForm):

    username = forms.CharField(
                        label='username',
                        max_length=100)
    email = forms.EmailField(
                        label='email',
                        max_length=100)
    password1 = forms.CharField(
                        label='password',
                        max_length=100,
                        widget=forms.PasswordInput())
    password2 = forms.CharField(
                        label='repeat password',
                        max_length=100,
                        widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ('username', 'email', )

    def __init__(self, *args, **kwargs):
        super(
            CreateUserForm, self
            ).__init__(
                *args, **kwargs)  # Call to ModelForm constructor
        self.fields['username'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'
        self.fields['email'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'
        self.fields['password1'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'
        self.fields['password2'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'

    def clean_password2(self):
        password_length = 5
        password1 = self.cleaned_data.get("password1")
        if len(password1) < password_length:
            raise forms.ValidationError(
                "Password must be longer than "
                "{} characters".format(password_length))
        password2 = self.cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    "Passwords do not match")
        email = self.cleaned_data.get('email')
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already register')
        username = self.cleaned_data.get('username')
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already register')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginUserForm(forms.Form):

    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password',
             max_length=100, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(
            LoginUserForm, self).__init__(
                *args, **kwargs)  # Call to ModelForm constructor
        self.fields['email'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'
        self.fields['password'].widget.attrs['style'] = \
            'width: 99% !important; resize: vertical !important;'


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username','email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]