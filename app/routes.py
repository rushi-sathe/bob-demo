# CodeGuard AI: SQL injection detected — fix required.
# Replace all raw SQL string formatting with parameterised queries:
#   cursor.execute(sql_string, (param,))
# Description: Raw SQL query constructed from unsanitised user input.

