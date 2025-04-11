import re

def is_integer(s):
    
    s = str(s)
    pattern = r'^-?\d+$' 
    if re.match(pattern, s):
        return True
    else:
        return False
    

print(is_integer(-1.2))
print(is_integer(12))
print(is_integer(-12))
