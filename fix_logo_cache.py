with open("index.html", "r") as f:
    html = f.read()

html = html.replace('images/logo.png', 'images/logo-hn.png')

with open("index.html", "w") as f:
    f.write(html)

print("Logo renamed to logo-hn.png in HTML.")
