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
    Gera uma senha usando fonte criptograficamente segura.

    Args:
        length: Tamanho total da senha.
        use_letters: Inclui letras ASCII.
        use_numbers: Inclui dígitos.
        use_symbols: Inclui símbolos de pontuação.

    Returns:
        Uma senha aleatória com os conjuntos habilitados.

    Raises:
        ValueError: Se o tamanho for inválido ou nenhum conjunto estiver habilitado.
    """
    if length <= 0:
        raise ValueError("length deve ser maior que zero.")

    pools = []
    if use_letters:
        pools.append(string.ascii_letters)
    if use_numbers:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Ative pelo menos um tipo de caractere.")

    if length < len(pools):
        raise ValueError(
            "length deve ser maior ou igual ao número de tipos de caracteres ativados."
        )

    alphabet = "".join(pools)
    password_chars = [secrets.choice(pool) for pool in pools]
    password_chars.extend(secrets.choice(alphabet) for _ in range(length - len(password_chars)))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)
