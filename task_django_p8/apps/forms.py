# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserModel
# from django.core.exceptions import ValidationError
# from django.forms import Form, CharField, PasswordInput, TextInput
# from django.utils.text import capfirst
# from django.utils.translation import gettext_lazy as _
# # .login .form-row #id_username, .login .form-row #id_password {
# #     padding: 8px;
# #     width: 100%;
# #     box-sizing: border-box;
# # }
#
# class CustomAuthForm(Form):
#     phone = CharField(max_length=255, strip=False, widget=TextInput(attrs={"autofocus": True,  'style': 'padding: 8px;width: 100%;box-sizing: border-box'}))
#     password = CharField(
#         strip=False,
#         widget=PasswordInput(attrs={"autocomplete": "current-password"}),
#     )
#
#     error_messages = {
#         "invalid_login": _(
#             "Please enter a correct %(phone)s and password. Note that both "
#             "fields may be case-sensitive."
#         ),
#         "inactive": _("This account is inactive."),
#     }
#
#     def __init__(self, request=None, *args, **kwargs):
#         """
#         The 'request' parameter is set for custom auth use by subclasses.
#         The form data comes in via the standard 'data' kwarg.
#         """
#         self.request = request
#         self.user_cache = None
#         super().__init__(*args, **kwargs)
#
#     def clean(self):
#         phone = self.cleaned_data.get("phone")
#         password = self.cleaned_data.get("password")
#
#         if phone is not None and password:
#             self.user_cache = authenticate(
#                 self.request, phone=phone, password=password
#             )
#             if self.user_cache is None:
#                 raise self.get_invalid_login_error()
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#
#         return self.cleaned_data
#
#     def confirm_login_allowed(self, user):
#         """
#         Controls whether the given User may log in. This is a policy setting,
#         independent of end-user authentication. This default behavior is to
#         allow login by active users, and reject login by inactive users.
#
#         If the given user cannot log in, this method should raise a
#         ``ValidationError``.
#
#         If the given user may log in, this method should return None.
#         """
#         if not user.is_active:
#             raise ValidationError(
#                 self.error_messages["inactive"],
#                 code="inactive",
#             )
#
#     def get_user(self):
#         return self.user_cache
#
#     def get_invalid_login_error(self):
#         return ValidationError(
#             self.error_messages["invalid_login"],
#             code="invalid_login",
#             params={"phone": self.phone_field.verbose_name},
#         )
