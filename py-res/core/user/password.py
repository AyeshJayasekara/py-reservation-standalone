#  All Rights Reserved
#
#  Author: Ayesh Jayasekara (cim12137@ciom.edu.au)

import re as regex
from typing import Optional

# regex pattern for initial validation
full_regex_pattern = "^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-\+])[A-Za-z\d!@#$%^&*()\-\+]{8,16}$"

# regex pattern for uppercase letters
uppercase_pattern = '[A-Z]'

# regex pattern for digits
digit_pattern = '\d'

# regex pattern for special characters
special_char_pattern = '[!@#$%^&*()\-\+]+'

# regex pattern for alphanumeric characters and given special chars
letter_pattern = '^[A-Za-z\d!@#\$%\^&*\(\)\-\+]*$'

def is_valid(password):
    """Checks password against accepted regex

    :param password: Password entered
    :type password: str

    :returns: if the password entered is valid
    :rtype: bool
    """

    compiled_pattern = regex.compile(full_regex_pattern)
    matched = regex.search(compiled_pattern, password)
    return matched

def has_valid_length(password) -> Optional[str]:
    """Checks password has valid length

    :param password: Password entered
    :type password: str

    """

    if not 8 <= len(password) <= 16:
        return "Password must be between 8 to 16 characters long."

def has_uppercase(password) -> Optional[str]:
    """Check password has an uppercase letter

    :param password: Password entered
    :type password: str

    """

    compiled_pattern = regex.compile(uppercase_pattern)
    if not compiled_pattern.search(password):
        return "Password must contain at least one uppercase letter."

def has_digits(password) -> Optional[str]:
    """Check password has digit

    :param password: Password entered
    :type password: str

    """
    compiled_pattern = regex.compile(digit_pattern)
    if not compiled_pattern.search(password):
        return "Password must contain at least one digit."

def has_special_character(password) -> Optional[str]:
    """Check password has a special character

    :param password: Password entered
    :type password: str

    """
    compiled_pattern = regex.compile(special_char_pattern)
    if not compiled_pattern.search(password):
        return "Password must contain at least one special character."

def has_letters(password) -> Optional[str]:
    """Check password has only accepted letters

    :param password: Password entered
    :type password: str

    """
    compiled_pattern = regex.compile(letter_pattern)
    if not compiled_pattern.match(password):
        return "Password must alphanumeric characters and any of ! @ # $ % ^ & * () - +"

def show_errors(password):
    """Prints all errors associated with entered password

    :param password: Password entered
    :type password: str

    :returns: a list of strings representing the header columns
    :rtype: list
    """

    errors = []

    length = has_valid_length(password)
    uppercase = has_uppercase(password)
    digits = has_digits(password)
    special_char = has_special_character(password)
    letter = has_letters(password)

    if length is not None:
        errors.append(length)
    if uppercase is not None:
        errors.append(uppercase)
    if digits is not None:
        errors.append(digits)
    if special_char is not None:
        errors.append(special_char)
    if letter is not None:
        errors.append(letter)

    return errors



def check_password(password):
    """Initiate the password checking method chain

    :param password: Password entered
    :type password: str

    """
    return True if is_valid(password) else show_errors(password)
