
from django.contrib.auth.mixins import UserPassesTestMixin
from account_app.models import User


def send_otp_code(phone_number, code):
    pass


class IdAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin