from __future__ import annotations

import argparse
import sys

from src.password_generator import generate_password


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gerador de senhas seguras para uso em terminal."
    )
    parser.add_argument(
        "--length",
        type=int,
        default=16,
        help="Tamanho da senha gerada. Padrão: 16",
    )
    parser.add_argument(
        "--no-letters",
        action="store_true",
        help="Exclui letras ASCII da senha.",
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Exclui números da senha.",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclui símbolos da senha.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        password = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols,
        )
    except ValueError as exc:
        parser.error(str(exc))
        return 2

    print(f"Senha gerada: {password}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

