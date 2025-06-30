# Midterm Calculator Project
 
A full-featured, extensible CLI calculator with advanced operations, undo/redo, history persistence, logging, configuration via `.env`, and continuous integration.
 

---
 
## 📋 Table of Contents
 
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [.env Configuration](#env-configuration)
* [Usage](#usage)
    * [Running the REPL](#running-the-repl)
    * [Available Commands](#available-commands)
* [Testing](#testing)
* [CI/CD](#cicd)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
 
---
 
## 🎯 Features
 
* **Basic & Advanced Operations**
    `add`, `subtract`, `multiply`, `divide`, `power`, `root`, `modulus`, `int_divide`, `percent`, `abs_diff`.
 
* **Undo/Redo & History**
    Memento-pattern based undo/redo.
    History persisted automatically or on demand to CSV via pandas.
 
* **Logging & Auto-Save**
    Observer-pattern logging of every calculation to a log file.
    Auto-save of history to CSV whenever a new calculation runs.
 
* **Configuration Management**
    All settings in a `.env` file and loaded with python-dotenv:
    * Log directory & file
    * History directory & file
    * Max history size
    * Auto-save toggle
    * Calculation precision & input limits
    * File encoding
 
* **Input Validation & Error Handling**
    Custom exceptions (`ValidationError`, `OperationError`) for invalid inputs and illegal operations.
 
* **Color-Coded Output**
    User prompts and errors are colorized via Colorama for readability.
 
* **Comprehensive Test Suite**
    Pytest tests covering operations, history, validators, persistence, and REPL behavior.
    ≥ 90% coverage enforced in CI.
 
---
 
## 🚀 Getting Started
 
### Prerequisites
 
* Python 3.8+
* Git
 
### Installation
 
# Clone the repo
git clone git@github.com:your-username/midterm-calculator-project.git
cd midterm-calculator-project
 
# Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate
 
# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
 
### .env Configuration
 
Create a `.env` file in the project root with these example values:
 
 
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=data
CALCULATOR_LOG_FILE=calculator.log
CALCULATOR_HISTORY_FILE=history.csv
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=4
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
 
## 💻 Usage
 
### Running the REPL
 
To start the calculator, run:
 
python -m app.calculator
 
You'll then see the calculator prompt:
 
Calculator REPL. Type 'help' for commands.
>>
 
### Available Commands
 
| Command          | Description                                  |
| :--------------- | :------------------------------------------- |
| `add a b`        | Adds `a + b`                                 |
| `subtract a b`   | Subtracts `b` from `a`                       |
| `multiply a b`   | Multiplies `a × b`                           |
| `divide a b`     | Divides `a ÷ b`                              |
| `power a b`      | Calculates `a` raised to the power of `b` (`a^b`) |
| `root a b`       | Calculates the `b`-th root of `a`            |
| `modulus a b`    | Returns the remainder of `a` divided by `b` (`a mod b`) |
| `int_divide a b` | Performs integer division of `a` by `b`      |
| `percent a b`    | Calculates `(a / b) * 100`                   |
| `abs_diff a b`   | Returns the absolute difference `|a - b|`    |
| `history`        | Shows all past calculations                  |
| `clear`          | Clears the in-memory history                 |
| `undo`           | Undoes the last calculation                  |
| `redo`           | Redoes the last undone calculation           |
| `save`           | Manually saves history to CSV                |
| `load`           | Loads history from CSV                       |
| `help`           | Lists all available commands                 |
| `exit`           | Quits the application                        |
 
---
 
## 🧪 Testing
 
Run the full test suite with coverage:
 
pytest --cov=app --cov-fail-under=90
 
All tests must pass, and code coverage must be at least **90%**.
 
---
 
## ⚙️ CI/CD
 
This project uses **GitHub Actions** for continuous integration and deployment.
 
* **Workflow**: `.github/workflows/python-app.yml`
* **Triggers**: `push` and `pull_request` events to the `main` branch
* **Steps**:
    * Checkout code
    * Set up Python
    * Install dependencies
    * Run tests with a coverage threshold
 
---
 
## 📁 Project Structure
 
project_root/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_input_validators.py
│   ├── test_history.py
│   ├── test_calculator.py
│   ├── test_operations_extras.py
│   └── test_calculator_extra.py
├── .env
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── python-app.yml
 
---
 
## 🤝 Contributing
 
We welcome contributions! Please follow these steps:
 
1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix:
 
    git checkout -b feature/your-feature-name
 
3.  **Commit your changes** with a clear message:
 
    git commit -m "Add feature: your feature description"
 
4.  **Push** your branch to your forked repository:
 
    git push origin feature/your-feature-name
 
5.  **Open a Pull Request** to the `main` branch of the original repository.
 
---
 
## 📄 License
 
This project is licensed under the **MIT License**.
