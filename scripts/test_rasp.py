import sys
sys.path.insert(0,'app')
from rasp_agent import protect

@protect
def make_query(user, password):
    return f"SELECT * FROM users WHERE user='{user}' AND password='{password}'"

ok=make_query('demo','demo123')
print('benign=PASS', ok)
try:
    make_query("' OR 1=1--", 'x')
except PermissionError:
    print('sqli=BLOCKED')
else:
    raise SystemExit('sqli was not blocked')
