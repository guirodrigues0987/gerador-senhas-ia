# Registro de Prompt

## Etapa 1

**Comando do usuário:** "Sugira a estrutura de pastas do projeto (incluindo local para testes e documentação). Explique por que a biblioteca secrets é superior para este caso de uso. Escreve o código da função principal de geração de senha, permitindo customizar tamanho e tipos de caracteres (letras, números, símbolos)."

**Por que essa instrução foi importante:** ela definiu o escopo inicial do MVP, separando arquitetura, justificativa de segurança e implementação da função central. Isso evita misturar decisão técnica com código e ajuda a manter o projeto fácil de testar e evoluir.

## Etapa 2

**Comando do usuário:** "Crie um arquivo main.py na raiz do projeto. Este arquivo deve servir como a interface de linha de comando (CLI). Use a biblioteca argparse para permitir que o usuário escolha o tamanho da senha (ex: --length 20) e quais caracteres incluir (ex: --no-symbols). O main.py deve importar a função generate_password do arquivo src/password_generator.py. Registro de Prompt: Documente esta etapa no arquivo docs/registro_de_prompt.md, explicando por que o argparse é a escolha padrão para criar ferramentas CLI profissionais em Python. Garanta que, ao final, o programa imprima a senha gerada de forma clara no terminal."

**Por que essa instrução foi importante:** ela transformou o gerador em uma ferramenta utilizável no terminal, com parâmetros explícitos e previsíveis. `argparse` é importante aqui porque entrega ajuda automática, validação básica e uma interface padrão que facilita uso, manutenção e evolução da CLI.

## Etapa 3

**Comando do usuário:** "Preciso que você escreva o conteúdo do meu arquivo README.md. Ele deve seguir exatamente a estrutura abaixo, baseada nos requisitos do meu laboratório: Título e Breve Descrição: Gerador de Senhas Seguras - Um MVP focado em desenvolvimento assistido por IA. Configuração de Ambiente: Instruções detalhadas para criar a venv, ativar e instalar o requirements.txt. Exemplos de Uso: Mostrar como rodar o main.py com diferentes flags (comprimento, símbolos, etc). Tecnologias e Modelos de IA: Listar Python 3.11+, bibliotecas nativas e mencionar que utilizei o GPT-5.5 como assistente de código. Limitações e Próximos Passos: Discutir o que não foi feito (ex: interface gráfica, histórico de senhas) e como o projeto pode expandir. Créditos e Licença: Atribuir créditos ao laboratório e usar licença MIT. Gerenciamento de Dependências: Mencionar o uso do requirements.txt. Testes Automatizados: Explicar como rodar o pytest e o que os testes unitários validam. Releases/Tags: Mencionar que a versão estável é a v1.0.0. Registro de Prompt: Documente esta etapa no arquivo docs/registro_de_prompt.md"

**Por que essa instrução foi importante:** ela definiu a documentação de entrada do projeto para uso e avaliação no laboratório, cobrindo instalação, execução, testes, limites e rastreabilidade. O `README.md` vira a referência principal para entender o MVP sem precisar ler o código primeiro.
