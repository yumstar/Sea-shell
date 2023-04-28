from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def validate_user_data(data):
    email = data['email'].strip()
    password = data['password'].strip()
    name = data['name'].strip()

    # check for missing data
    if not email:
        raise ValidationError('Please provide a valid email.')
    if not password:
        raise ValidationError('Please provide a password.')
    if not name:
        raise ValidationError('Please provide a name for the user.')

    # validate data
    if UserModel.objects.filter(email=email).exists():
        raise ValidationError('The provided email is in use. Please use a different one.')
    if len(password) < 6:
        raise ValidationError('Please choose a valid password that has a minimum length of 6 characters.')

    return data

def validate_user_email(user_data):
    email = user_data['email'].strip()
    if not email:
        raise ValidationError('Please provide an valid email.')
    return True

def validate_user_password(user_data):
    email = user_data['password'].strip()
    if not email:
        raise ValidationError('Please provide a password.')
    return True
