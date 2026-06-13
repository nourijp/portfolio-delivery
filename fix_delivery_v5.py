import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Remove Cheryl's testimonial
cheryl_html = """               <li>
                  <p>Hamed’s communications were critical in allowing for that success.</p> 
                  <div class="testimonial-author">
                    	<img src="images/testimonials/testimonial-cheryl-veldman.png" alt="Cheryl Veldman">
                    	<div class="author-info">
                    		Cheryl Veldman
                    		<span class="position">Professional Colleague</span>
                    	</div>
                  </div>                 
             	</li>\n"""
html = html.replace(cheryl_html, '')


# 2. Fix Delivery Toolkit section
# Remove the h4 heading completely
html = html.replace('<h4 style="text-align: center; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; font-size: 1.2rem;">Delivery Toolkit</h4>\n', '')

# Remove animate-this from ANYWHERE inside #clients and #contact
def remove_animate_this(section_id, html):
    start = html.find(f'<section id="{section_id}"')
    if start == -1: return html
    end = html.find('</section>', start) + len('</section>')
    chunk = html[start:end]
    chunk = chunk.replace(' animate-this', '')
    return html[:start] + chunk + html[end:]

html = remove_animate_this('clients', html)
html = remove_animate_this('contact', html)

# 3. Ensure Resume PDF works perfectly.
# It should already be correct in previous steps, but let's double check.
html = html.replace('<a class="button stroke" href="assets/files/Hamed-Nouri-Delivery-Manager-2026.pdf" target="_blank" style="margin-left: 15px;">\n				  					View Resume\n				  				</a>', '<a class="button stroke" href="assets/files/Hamed-Nouri-Delivery-Manager-2026.pdf" target="_blank" style="margin-left: 15px;">\n				  					View Resume\n				  				</a>')
# wait I didn't change it, I'm just making sure.

with open("index.html", "w") as f:
    f.write(html)

print("HTML script executed.")
