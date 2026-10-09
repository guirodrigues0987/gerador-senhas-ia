from __future__ import annotations

import secrets
import string


def generate_password(
    length: int = 16,
    use_letters: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generate a password using a cryptographically secure source.

    Args:
        length: Total password length.
        use_letters: Include ASCII letters.
        use_numbers: Include digits.
        use_symbols: Include punctuation symbols.

    Returns:
        A random password using the enabled character sets.

    Raises:
        ValueError: If the length is invalid or no character set is enabled.
    """
    if length <= 0:
        raise ValueError("length must be greater than zero.")

    pools = []
    if use_letters:
        pools.append(string.ascii_letters)
    if use_numbers:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Enable at least one character type.")

    if length < len(pools):
        raise ValueError("length must be at least the number of enabled character types.")

    alphabet = "".join(pools)
    password_chars = [secrets.choice(pool) for pool in pools]
    password_chars.extend(secrets.choice(alphabet) for _ in range(length - len(password_chars)))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
