from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        """
        fields = ("field1", "field2")
        exclude = ("field3", "field4")
        """
