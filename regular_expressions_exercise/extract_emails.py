import re

sentence = input()
pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_0]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, sentence)

for extracted_email in extracted_emails:
    print(extracted_email[0])