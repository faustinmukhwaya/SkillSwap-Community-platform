# SkillSwap Community Platform

## Project Overview
The SkillSwap Community Platform is a Python-based CLI application that allows users to exchange skills interactively. Users can manage their profiles, skills, and exchanges through a user-friendly command-line interface.

## Features
- Interactive menus for managing Users, Skills, and Exchanges.
- Create, delete, and display objects for Users, Skills, and Exchanges.
- View related objects (e.g., skills for a user, users for an exchange).
- Find objects by attributes (e.g., user by name/email, skill by name/user_id).
- Validate user input and operations with clear error messages.

## Setup Instructions
1. Install `pipenv` if not already installed:
   ```bash
   pip install pipenv
   ```
2. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd SkillSwap-Community-platform
   ```
3. Install dependencies:
   ```bash
   pipenv install
   ```
4. Run the application:
   ```bash
   pipenv run python -m skillswap.cli
   ```

## Usage Guide
- Follow the interactive menus to manage Users, Skills, and Exchanges.
- Input validation ensures smooth operation and prevents invalid entries.

## Project Structure
```
SkillSwap-Community-platform/
├── skillswap/
│   ├── __init__.py
│   ├── models.py
│   ├── utils.py
│   └── cli.py
├── Pipfile
└── README.md
```

## Dependencies
- `prompt_toolkit`: For enhanced CLI input handling.

## Code Quality
- Follows OOP best practices.
- Modular design with clear method names and single responsibility principles.

## Testing
- Robust input validation ensures the CLI handles bad inputs gracefully.