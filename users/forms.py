# to substitude UserCreationForm in django.contrib.auth.forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class new_db_name(inherited_db_name) is a way to inherit model
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # class Meta define the metadata of the class
    class Meta:
        # The "User" model will be affected by the following configurations.
        # which is field setting
        model = User
        # fields to be shown on our form
        fields = ['username', 'email', 'password1', 'password2']

        # the thing I can not figure out is that why django took apart user as
        # creatform and user these two model.

        # maybe we can take it from this term:
        # auth model has multi object to manage user applications.
        # we are now using two of the objects.