from allauth.account.forms import (
    LoginForm,
    SignupForm,
    AddEmailForm,
    ChangePasswordForm,
    SetPasswordForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)
from allauth.socialaccount.forms import (
    DisconnectForm,
)


class CustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):
        # Add your own processing here.
        print(self.user)
        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Add your own processing here.
        return user


class CustomAddEmailForm(AddEmailForm):
    def save(self):
        email_address_obj = super(CustomAddEmailForm, self).save()
        # Add your own processing here.
        print(self.user)
        return email_address_obj


class CustomChangePasswordForm(ChangePasswordForm):
    def save(self):
        super(CustomChangePasswordForm, self).save()
        # Add your own processing here.
        print(self.user)


class CustomSetPasswordForm(SetPasswordForm):
    def save(self):
        super(CustomSetPasswordForm, self).save()
        # Add your own processing here.
        print(self.user)


class CustomResetPasswordForm(ResetPasswordForm):
    def save(self):
        email_address = super(CustomResetPasswordForm, self).save()
        # Add your own processing here.
        print(self.user)
        return email_address


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def save(self):
        # Add your own processing here.
        print(self.user)
        super(CustomResetPasswordKeyForm, self).save()


class CustomSocialSignupForm(SignupForm):
    def save(self):
        user = super(CustomSocialSignupForm, self).save()
        # Add your own processing here.
        print(self.socialaccount)
        return user


class CustomSocialDisconnectForm(DisconnectForm):
    def save(self):
        # Add your own processing here if you DO need access to the
        # socialaccount being deleted.
        super(CustomSocialDisconnectForm, self).save()
        # Add your own processing here if you DO NOT need access to the
        # socialaccount being deleted.
        print(self.request)
        print(self.accounts) 
        print(self.cleaned_data['account']) # contains the socialaccount being deleted. .save() issues the delete. So if you need access to the socialaccount beforehand, move your code before .save().