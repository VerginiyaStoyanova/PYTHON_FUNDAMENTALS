import re

line_string = input()

pattern_title = r"<title>(.*?)</title>"
title = ''.join(re.findall(pattern_title, line_string))

pattern_content = r"<body>.+</body>"
matches = re.findall(pattern_content, line_string)
erase_content = re.findall(r'>([^><]*)', ''.join(matches))

content = ''

for match in erase_content:
    content += match

content = content.replace('\\n', '')
print(f"Title: {title}")
print(f"Content: {content}")