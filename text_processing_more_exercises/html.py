title_of_an_article = input()
content_of_article = input()
comments = []

while True:
    command = input()

    if command == "end of comments":
        break

    comments.append(command)

print(f"<h1>\n    {title_of_an_article}\n</h1>")
print(f"<article>\n    {content_of_article}\n</article>")

for comment in comments:
    print(f"<div>\n    {comment}\n</div>")