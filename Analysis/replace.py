import re 

def replace(text):

    replace_patterns = [
        (r'\bAnti-Black\b', 'Racially Motivated'),
        (r'\bAnti-Arab\b', 'Racially Motivated'),
        (r'\bAnti-Hispanic\b', 'Racially Motivated'),
        (r'\bAnti-Black or African American;Anti-Gay (Male)\b', 'Racially Motivated')
    ]

    for pattern, replacement in replace_patterns:
        if re.search(pattern, text):
            text = re.sub(pattern, replacement, text)

    return text
