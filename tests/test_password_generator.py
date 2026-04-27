import pytest

from src.password_generator import generate_password


def test_generate_password_default_length():
    password = generate_password()
    assert len(password) == 16


def test_generate_password_custom_length():
    password = generate_password(length=24)
    assert len(password) == 24


def test_generate_password_rejects_invalid_length():
    with pytest.raises(ValueError):
        generate_password(length=0)


def test_generate_password_rejects_no_character_sets():
    with pytest.raises(ValueError):
        generate_password(use_letters=False, use_numbers=False, use_symbols=False)


def test_generate_password_rejects_short_length_for_selected_sets():
    with pytest.raises(ValueError):
        generate_password(length=2, use_letters=True, use_numbers=True, use_symbols=True)
