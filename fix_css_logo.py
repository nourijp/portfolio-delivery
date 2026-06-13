with open("css/main.css", "r") as f:
    css = f.read()

# Replace the background rule
css = css.replace('background: url("../images/logo.png") no-repeat center;', '/* background: url("../images/logo.png") no-repeat center; */')

# Let's also restore the img tag in index.html, since using the img tag is much better for arbitrary aspect ratios
with open("index.html", "r") as f:
    html = f.read()

html = html.replace('<a class="site-logo" href="#home" aria-label="Hamed Nouri home">Hamed Nouri</a>', '<a class="site-logo" href="#home" aria-label="Hamed Nouri home"><img src="images/logo.png" alt="Hamed Nouri" style="height: 46px; width: auto; display: block;"></a>')

with open("index.html", "w") as f:
    f.write(html)

with open("css/main.css", "w") as f:
    f.write(css)

print("CSS background disabled and IMG tag restored with correct sizing.")
