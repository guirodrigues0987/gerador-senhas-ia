# Gerador de Senhas Seguras - Um MVP focado em desenvolvimento assistido por IA

Gerador de Senhas Seguras é um MVP em Python para gerar senhas com foco em segurança criptográfica, usabilidade em terminal e documentação de processo para laboratório de IA Generativa.

## Configuração de Ambiente

1. Crie a `venv` na raiz do projeto:
```powershell
python -m venv venv
```

2. Ative a `venv` no PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

3. Atualize o `pip`:
```powershell
python -m pip install --upgrade pip
```

4. Instale as dependências listadas em `requirements.txt`:
```powershell
pip install -r requirements.txt
```

## Exemplos de Uso

Gerar uma senha com o tamanho padrão:
```powershell
python main.py
```

Gerar uma senha com 20 caracteres:
```powershell
python main.py --length 20
```

Gerar uma senha sem símbolos:
```powershell
python main.py --no-symbols
```

Gerar uma senha com 24 caracteres, sem números:
```powershell
python main.py --length 24 --no-numbers
```

Gerar uma senha usando apenas letras e números:
```powershell
python main.py --no-symbols
```

## Tecnologias e Modelos de IA

- Python 3.11+
- Bibliotecas nativas do Python: `secrets`, `string`, `argparse`
- Biblioteca de testes: `pytest`
- Assistente de código utilizado no desenvolvimento: GPT-5.5

## Limitações e Próximos Passos

- O projeto ainda não possui interface gráfica.
- Não há histórico de senhas geradas.
- Não existe exportação para arquivo ou integração com cofres de senha.
- Não há política avançada de complexidade, como regras por comprimento mínimo de cada tipo de caractere.
- Não há persistência de configurações do usuário.

Próximos passos possíveis:

- Criar uma interface gráfica simples.
- Adicionar histórico local opcional.
- Incluir validação de força da senha.
- Permitir copiar a senha automaticamente para a área de transferência.
- Salvar perfis de geração com presets.

## Créditos e Licença

Projeto desenvolvido como MVP para um laboratório de IA Generativa.

Licença: MIT.

## Gerenciamento de Dependências

As dependências do projeto são gerenciadas pelo arquivo `requirements.txt`.

Para instalar tudo em um ambiente isolado, use:

```powershell
pip install -r requirements.txt
```

## Testes Automatizados

Os testes automatizados usam `pytest`.

Para executar:

```powershell
pytest
```

Os testes unitários validam:

- Geração de senha com tamanho padrão.
- Geração de senha com tamanho customizado.
- Rejeição de tamanho inválido.
- Rejeição quando nenhum tipo de caractere é habilitado.
- Rejeição quando o tamanho é menor que a quantidade de grupos de caracteres ativados.

## Releases/Tags

A versão estável atual do projeto é `v1.0.0`.

