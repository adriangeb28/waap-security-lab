"""RASP reutilizable para funciones sensibles del laboratorio."""
import functools
import logging
import re

SQL_PATTERN = re.compile(r"(?:UNION|OR\s+1\s*=\s*1|--|;\s*DROP)", re.I)
PATH_PATTERN = re.compile(r"(?:\.\./|%2e%2e)", re.I)
logger = logging.getLogger("rasp")


def protect(operation_builder):
    @functools.wraps(operation_builder)
    def wrapped(*args, **kwargs):
        operation = operation_builder(*args, **kwargs)
        if SQL_PATTERN.search(operation) or PATH_PATTERN.search(operation):
            logger.warning("RASP blocked: %s", operation)
            raise PermissionError("RASP blocked runtime operation")
        return operation
    return wrapped
