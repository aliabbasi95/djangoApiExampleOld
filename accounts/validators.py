import re
from django.core.exceptions import ValidationError


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z.",
                code="password_no_upper",
            )

    def get_help_text(self):
        return "Your password must contain at least 1 uppercase letter, A-Z."


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[a-z]", password):
            raise ValidationError(
                "The password must contain at least 1 lowercase letter, a-z.",
                code="password_no_lower",
            )

    def get_help_text(self):
        return "Your password must contain at least 1 lowercase letter, a-z."


class SymbolValidator(object):  # new
    def validate(self, password, user=None):  # new
        if not re.findall("[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
            raise ValidationError(  # new
                (
                    "The password must contain at least 1 symbol"
                ),
                code="password_no_symbol",  # new
            )

    def get_help_text(self):  # new
        return "Your password must contain at least 1 symbol"


class HasNumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall("\d", password):
            raise ValidationError(
                (
                    "The password must contain at least 1 number"
                ),
                code="password_no_symbol",
            )

    def get_help_text(self):
        return "Your password must contain at least 1 number: " + "1234567890"
