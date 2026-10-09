# Prompt Log

## Step 1

**User prompt:** "Suggest the project folder structure (including a place for tests and documentation). Explain why the `secrets` library is better suited to this use case. Write the code for the main password generation function, allowing the length and character types (letters, numbers, symbols) to be customized."

**Why this prompt mattered:** it defined the initial scope of the MVP, separating architecture, security rationale and implementation of the core function. This keeps technical decisions apart from code and makes the project easier to test and evolve.

## Step 2

**User prompt:** "Create a main.py file at the project root. It should be the command-line interface (CLI). Use the argparse library so the user can choose the password length (e.g. --length 20) and which characters to include (e.g. --no-symbols). main.py must import the generate_password function from src/password_generator.py. Prompt log: document this step in docs/prompt_log.md, explaining why argparse is the standard choice for professional Python CLI tools. Make sure the program prints the generated password clearly in the terminal."

**Why this prompt mattered:** it turned the generator into a usable terminal tool with explicit, predictable parameters. `argparse` matters here because it provides automatic help, basic validation and a standard interface that makes the CLI easier to use, maintain and extend.

## Step 3

**User prompt:** "I need you to write the content of my README.md. It must follow exactly the structure below, based on my lab requirements: Title and short description: Secure Password Generator - an MVP focused on AI-assisted development. Environment setup: detailed instructions to create the venv, activate it and install requirements.txt. Usage examples: show how to run main.py with different flags (length, symbols, etc.). Technologies and AI models: list Python 3.11+, standard libraries and mention that I used GPT-5.5 as a code assistant. Limitations and next steps: discuss what was not done (e.g. graphical interface, password history) and how the project could grow. Credits and license: credit the lab and use the MIT license. Dependency management: mention the use of requirements.txt. Automated tests: explain how to run pytest and what the unit tests validate. Releases/tags: mention that the stable version is v1.0.0. Prompt log: document this step in docs/prompt_log.md."

**Why this prompt mattered:** it defined the project's entry documentation for use and evaluation in the lab, covering installation, execution, tests, limits and traceability. The `README.md` becomes the main reference for understanding the MVP without reading the code first.
