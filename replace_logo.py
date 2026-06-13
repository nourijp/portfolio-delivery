with open("index.html", "r") as f:
    html = f.read()

# Replace the logo image
html = html.replace('images/h-monogram-serif-simple-white.svg', 'images/logo.png')

with open("index.html", "w") as f:
    f.write(html)

print("Logo reference updated.")
