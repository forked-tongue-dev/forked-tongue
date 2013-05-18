from crispy_forms.layout import Submit, Layout
from django.forms import PasswordInput, CharField, BooleanField, Form
from crispy_forms.helper import FormHelper


class LoginForm(Form):
    login = CharField()
    password = CharField(widget=PasswordInput)
    remember_me = BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-loginForm'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(LoginForm, self).__init__(*args, **kwargs)


class SearchForm(Form):
    name = CharField(required=False)
    tags = CharField(required=False)
    groups = CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-searchForm'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = 'search'
        self.helper.help_text_inline = True
        self.helper.layout = Layout()

        self.helper.add_input(Submit('submit', 'Submit'))
        super(SearchForm, self).__init__(*args, **kwargs)