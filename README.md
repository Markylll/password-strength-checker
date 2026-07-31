# password-strength-checker
A simple CLI tool that checks password strength and suggests improvements
# Password Strength Checker

A command-line security tool that evaluates password strength and suggests improvements.

## Features
- Checks 5 password security rules
- Rates passwords: STRONG / MODERATE / WEAK / VERY WEAK
- Lists specific issues found
- Suggests an improved password when weak
- Loops until user quits

## Password Rules Checked
1. Minimum 12 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit (0–9)
5. At least one special character (!@#$%^&*)

## How to Run
```bash
python passwordchecker.py
```

## Example Output
=== PASSWORD STRENGTH CHECKER ===
Enter password (or 'quit' to exit): Hello123

Rules passed: 3 / 5
Strength: WEAK

Issues found:

x Password must be at least 12 characters

x Password must contain at least 1 special character

Suggest improvement: Hello123!abcdefghijkl

## Built With
- Python 3.14.6
- Concepts: functions, dictionaries, string methods, loops, list comprehensions
