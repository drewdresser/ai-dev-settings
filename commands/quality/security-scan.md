---
name: ai-dev:security-scan
description: Scan the codebase for security vulnerabilities and issues.
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
  - Task
---

# Security Scan Command

Scan the codebase for potential security vulnerabilities using parallel specialist scanners.

## Scan Areas

1. **Dependency vulnerabilities** - Known CVEs in packages
2. **Secret detection** - Hardcoded credentials, API keys, tokens
3. **Code pattern analysis** - SQL injection, XSS, command injection, SSRF
4. **Configuration review** - Debug mode, insecure defaults, missing headers

## Process

If Agent Teams is available, create a team for parallel scanning with cross-validation:

```
Create an agent team to perform a comprehensive security scan. Spawn four scanners
using Sonnet:

- dependency-scanner: Audit package dependencies for known CVEs. Run pip audit,
  npm audit, or cargo audit as appropriate.
- secret-scanner: Scan for hardcoded secrets, API keys, passwords, tokens,
  certificates, and .env files committed to git.
- code-pattern-scanner: Analyze code for OWASP Top 10 patterns - SQL injection,
  XSS, command injection, SSRF, insecure deserialization, path traversal.
- config-scanner: Review configs for debug mode, insecure defaults, missing
  security headers, permissive CORS, exposed admin endpoints.

Do NOT scan anything yourself. Only coordinate and produce the final report.

After all scans complete, have the scanners cross-validate findings. For example,
if the dependency scanner finds a vulnerable package, the code-pattern scanner
should check if the vulnerable function is actually called. If the secret scanner
finds an API key, the config scanner should check if .gitignore covers it.
Findings confirmed by multiple scanners get elevated severity.
```

If Agent Teams is not available, run all scans sequentially:

### 1. Dependency Vulnerabilities
```bash
# Python
uv pip audit
# Node
pnpm audit
```

### 2. Secret Detection
```bash
grep -rn "password\s*=" --include="*.py" --include="*.ts" .
grep -rn "api_key\s*=" --include="*.py" --include="*.ts" .
grep -rn "secret\s*=" --include="*.py" --include="*.ts" .
```

### 3. Code Patterns
- SQL injection, command injection, XSS, insecure deserialization, path traversal

### 4. Configuration
- Debug mode, insecure defaults, missing security headers

## Output Format

```markdown
## Security Scan Report

### Summary
| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 1 |
| Medium | 3 |
| Low | 5 |

### Critical Issues
[None found - or list issues]

### High Severity
#### [Issue Title]
- **File**: `src/api/auth.py:42`
- **Type**: Hardcoded secret
- **Description**: API key found in source code
- **Remediation**: Move to environment variable

### Medium Severity
[List medium issues]

### Low Severity
[List low issues]

### Dependency Vulnerabilities
| Package | Version | Vulnerability | Fix Version |
|---------|---------|---------------|-------------|

### Recommendations
1. [Prioritized action items]
```

## Common Patterns to Check

### SQL Injection
```python
# Dangerous
query = f"SELECT * FROM users WHERE id = {user_id}"
# Safe
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### Command Injection
```python
# Dangerous
os.system(f"echo {user_input}")
# Safe
subprocess.run(["echo", user_input], shell=False)
```

### XSS
```javascript
// Dangerous
element.innerHTML = userInput;
// Safe
element.textContent = userInput;
```
