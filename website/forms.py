from crispy_forms.layout import Submit
from django.forms import PasswordInput, CharField, BooleanField, Form
from crispy_forms.helper import FormHelper


class LoginForm(Form):
    login = CharField()
    password = CharField(widget=PasswordInput)
    remember_me = BooleanField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(LoginForm, self).__init__(*args, **kwargs)