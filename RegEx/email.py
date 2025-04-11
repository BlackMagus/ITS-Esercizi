import re

def extract_email(text):
    pattern = r'\S+@\S+'
    emails = re.findall(pattern,text)

    return emails


testo = "questa è la mia email alessiobasile@gmail.com, però puoi cottatarmi anche su support@gmail.com"
print(extract_email(testo))
