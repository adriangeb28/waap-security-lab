import re
from functools import wraps

SQLI_PATTERNS = [
    re.compile(r"\bor\b\s+\d+\s*=\s*\d+", re.I),
    re.compile(r"union\s+select", re.I),
    re.compile(r"--\s*$", re.I),
]

def protect_query(func):
    """Demostración académica de una defensa RASP alrededor de una operación sensible."""
    @wraps(func)
    def wrapper(query, *args, **kwargs):
        if any(p.search(query) for p in SQLI_PATTERNS):
            raise PermissionError("RASP bloqueó una entrada con patrón SQLi")
        return func(query, *args, **kwargs)
    return wrapper
