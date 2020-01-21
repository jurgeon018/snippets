from .models import CustomUser
import logging
from django.contrib.auth.backends import ModelBackend 
from allauth.account.auth_backends import AuthenticationBackend


class CustomBackend(AuthenticationBackend): # (AuthenticationBackend|object|ModelBackend)
    def authenticate(self, email, password):    
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, id):
        try:
            user = CustomUser.objects.get(id=id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(id)d not found")
            return None
