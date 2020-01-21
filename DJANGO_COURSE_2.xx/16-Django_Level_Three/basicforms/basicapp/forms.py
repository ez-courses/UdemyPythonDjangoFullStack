from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower[0] != 'z':
        raise forms.ValidationError("Name needs to start with z!")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[validators.EmailValidator])
    verify_email = forms.EmailField(label='Email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher =forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    # clean the entire form
    def clean(self):

        # all clean data from the form
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
