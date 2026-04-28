from password import *
import pytest

def test_check_correct():
        check_password("FdedeGHn$") is True

def test_check_password_length():
    with pytest.raises(ValueError):
        check_password("Sjeiw")
    
def test_check_lower():
    with pytest.raises(ValueError):
        check_password("SJFI$")


def test_check_upper():
    with pytest.raises(ValueError):
        check_password("ddjuidwwad")

#new changes
def test_check_special():
    with pytest.raises(ValueError):
        check_password("efjifewEJUD")

