import re
from django.core.exceptions import ValidationError

from core.utils import is_cpf_valid


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):
    if not value or len(value) == 0:
        raise ValidationError("CPF é obrigatório.", "invalid")

    if re.match("([0-9]{11})", value) and not is_cpf_valid(value):
        raise ValidationError("CPF é inválido", "invalid")

    elif not is_cpf_valid(str(value)):
        raise ValidationError("CPF inválido", "invalid")


def validate_phone(value):
    if not re.match("(\(?\d{2}\)?\s)?(\d{4,5}\-?\d{4})", value):
        raise ValidationError("Número de Telefone inválido", "invalid")