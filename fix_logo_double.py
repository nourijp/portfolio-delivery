with open("index.html", "r") as f:
    html = f.read()

html = html.replace('<a class="site-logo" href="#home" aria-label="Hamed Nouri home"><img src="images/logo.png" alt="Hamed Nouri"></a>', '<a class="site-logo" href="#home" aria-label="Hamed Nouri home">Hamed Nouri</a>')

with open("index.html", "w") as f:
    f.write(html)

print("Double logo fixed.")
