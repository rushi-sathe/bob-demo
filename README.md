# CodeGuard AI - Vulnerable Demo Repository

## WARNING

This repository intentionally contains security vulnerabilities
for testing the CodeGuard AI remediation platform.

DO NOT deploy this application publicly.
DO NOT use real credentials.
DO NOT connect this application to production systems.

## Intentionally Seeded Vulnerabilities

### 1. SQL Injection
File: app.py
Location: search_users()

Issue:
User input is directly inserted into an SQL query.

Expected remediation:
Use parameterized SQL queries.

### 2. Hardcoded Secret
File: config.py

Issue:
Credentials and application secret are hardcoded.

Expected remediation:
Use environment variables for sensitive configuration.

### 3. Vulnerable Dependency
File: requirements.txt

Package:
Pillow==9.4.0

CVE:
CVE-2023-44271

Expected remediation:
Upgrade Pillow to a compatible fixed version.

## Technology Stack

- Python
- Flask
- SQLite
- Pillow

## Run Locally

Create a virtual environment:

python -m venv venv

Activate it and install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Application:
http://127.0.0.1:5000

## Security Testing

Run Semgrep:

semgrep scan --config auto .

Run OWASP Dependency-Check:

dependency-check --project CodeGuard-Demo --scan . --format JSON

Run tests:

pytest

## Expected CodeGuard AI Results

1. Detect SQL Injection.
2. Detect hardcoded credentials.
3. Identify the vulnerable Pillow dependency.
4. Generate remediation patches.
5. Generate regression and exploit-proof tests.
6. Validate patches in an isolated sandbox.
7. Create a GitHub PR only after validation passes.

This repository is intentionally vulnerable and
must only be used in an isolated local testing environment.
