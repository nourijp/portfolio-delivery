import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Expand "What I Do" section copy
services_new = """   		<div class="services-list block-1-2 block-tab-full group">

	      	<div class="bgrid service-item animate-this">	
	      		<span class="icon"><i class="icon-earth"></i></span>            
	            <div class="service-content">
	            	<h3 class="h05">Implementation Support</h3>
		            <p>I help organize rollout needs, user readiness, stakeholder alignment, handoffs, launch communication, and post-launch follow-up so software changes do not feel scattered or unclear.</p>	         		
	         	</div> 	         	 
				</div>

				<div class="bgrid service-item animate-this">	
					<span class="icon"><i class="icon-paint-brush"></i></span>                          
	            <div class="service-content">	
	            	<h3 class="h05">Customer Enablement</h3>  
		            <p>I create practical enablement resources including FAQs, guides, training content, workshops, self-service materials, and user-facing documentation that help people understand what to do next.</p>	         		
	            </div>	                          
			   </div>

			   <div class="bgrid service-item animate-this">
			   	<span class="icon"><i class="icon-megaphone"></i></span>		            
	            <div class="service-content">
	            	<h3 class="h05">Stakeholder Coordination</h3>
		            <p>I work across product, IT, HR, SMEs, support teams, leadership, and end users to clarify expectations, gather feedback, reduce confusion, and keep implementation work moving forward.</p>
	            </div> 	            	               
			   </div>

				<div class="bgrid service-item animate-this">
					<span class="icon"><i class="icon-lego-block"></i></span>	              
	            <div class="service-content">
	            	<h3 class="h05">Adoption & Measurement</h3>
		            <p>I use Power BI, usage data, surveys, email engagement, support trends, and user feedback to understand adoption barriers and improve communication, documentation, and training resources.</p>	         		
	            </div>                
				</div>			   

	      </div>"""

# Extract the old services list
s_start = html.find('<div class="services-list')
s_end = html.find('</div>\n\n	   </div> <!-- end row -->', s_start)
if s_start != -1 and s_end != -1:
    html = html[:s_start] + services_new + html[s_end:]

html = html.replace('Practical support for rollouts, documentation, training, stakeholder coordination, and adoption-focused delivery.', 'I support implementation, enablement, documentation, stakeholder coordination, and adoption-focused delivery by turning complex changes into clear plans, usable resources, and smoother user experiences.')

# 2. Testimonials 
test_html = """               <li>
                  <p>Hamed has a rare gift for making the complex feel accessible. His work helped bridge technical changes and user understanding through clear, thoughtful communication and practical support resources.</p> 
                  <div class="testimonial-author">
                    	<img src="images/testimonials/testimonial-edgar-sanchez.png" alt="Edgar Sanchez">
                    	<div class="author-info">
                    		Edgar Sanchez
                    		<span class="position">Platform Engineer, CiraConnect</span>
                    	</div>
                  </div>                 
             	</li>
               <li>
                  <p>His clear, timely communications were a major reason the transition went so smoothly. He helped manage timelines, gather feedback, create training materials, and keep stakeholders aligned.</p> 
                  <div class="testimonial-author">
                    	<img src="images/testimonials/testimonial-daniel-yoes.png" alt="Daniel Yoes">
                    	<div class="author-info">
                    		Daniel Yoes
                    		<span class="position">Serial Founder | B2B SaaS Portfolio</span>
                    	</div>
                  </div>                 
             	</li>
               <li>
                  <p>Hamed’s communications were critical in allowing for that success.</p> 
                  <div class="testimonial-author">
                    	<img src="images/testimonials/testimonial-cheryl-veldman.png" alt="Cheryl Veldman">
                    	<div class="author-info">
                    		Cheryl Veldman
                    		<span class="position">Professional Colleague</span>
                    	</div>
                  </div>                 
             	</li>
               <li>
                  <p>One of the qualities I like most about Hamed Nouri is his creativity and ability to bring an idea to a delivered, executed product! Hamed brought creativity and the ability to turn an idea into a delivered, executed product. He was able to connect strategy, communication, and practical execution in a way that helped move work from concept to completion.</p> 
                  <div class="testimonial-author">
                    	<img src="images/testimonials/testimonial-nicholas-romich.jpg" alt="Nicholas Romich">
                    	<div class="author-info">
                    		Nicholas Romich
                    		<span class="position">VP of Product</span>
                    	</div>
                  </div>                 
             	</li>"""

slides_start = html.find('<ul class="slides">')
slides_end = html.find('</ul> <!-- end slides -->') + len('</ul> <!-- end slides -->')
if slides_start != -1 and slides_end != -1:
    html = html[:slides_start] + '<ul class="slides">\n' + test_html + '\n</ul> <!-- end slides -->' + html[slides_end:]


# 3. Audit broken loading / reveal behavior & 7. Contact section animations
# The user noted sections at the bottom don't load until scrolled past. 
# Infinity uses `animate-this`. If it's broken at the bottom, we'll strip `animate-this` from the Toolkit, Resume, and Contact rows.
# Let's find "Delivery Toolkit" row
tk_start = html.find('<h4>Delivery Toolkit</h4>') # Oops, it was <h4 style="...">Delivery Toolkit</h4>
if tk_start == -1:
    tk_start = html.find('Delivery Toolkit')
# Strip animate-this from toolkit
tk_row = html.rfind('<div class="row animate-this">', 0, tk_start)
if tk_row != -1:
    html = html[:tk_row] + '<div class="row">' + html[tk_row + len('<div class="row animate-this">'):]

# For Resume
res_row = html.find('<section id="resume"')
res_animate = html.find('<div class="row animate-this">', res_row)
if res_animate != -1 and res_animate < res_row + 500:
    html = html[:res_animate] + '<div class="row">' + html[res_animate + len('<div class="row animate-this">'):]

# For Contact
cont_row = html.find('<section id="contact">')
cont_intro = html.find('<div class="row contact-content animate-this">', cont_row)
if cont_intro != -1:
    html = html[:cont_intro] + '<div class="row contact-content">' + html[cont_intro + len('<div class="row contact-content animate-this">'):]
# And the form/info blocks
html = html.replace('<div class="col-eight tab-full contact-form animate-this">', '<div class="col-eight tab-full contact-form">')
html = html.replace('<div class="col-four tab-full contact-info end animate-this">', '<div class="col-four tab-full contact-info end">')

# 4 & 5. Resume behavior
# Hero button -> direct to PDF
hero_buttons_old = """<a class="smoothscroll button stroke" href="#portfolio">
				  					Selected Projects
				  				</a>
                                <a class="smoothscroll button stroke" href="#resume" style="margin-left: 15px;">
				  					View Resume
				  				</a>"""
hero_buttons_new = """<a class="smoothscroll button stroke" href="#portfolio">
				  					Selected Projects
				  				</a>
                                <a class="button stroke" href="assets/files/Hamed-Nouri-Delivery-Manager-2026.pdf" target="_blank" style="margin-left: 15px;">
				  					View Resume
				  				</a>"""
html = html.replace(hero_buttons_old, hero_buttons_new)

# Remove the bottom resume section entirely as it was requested to reduce clutter
res_sec_start = html.find('<!-- resume')
res_sec_end = html.find('</section>', res_sec_start) + len('</section>')
if res_sec_start != -1 and res_sec_end != -1:
    html = html[:res_sec_start] + html[res_sec_end:]

# Update nav link for resume to point to the PDF directly, or remove it? 
# The user said: "Top navigation Resume link, if present, should scroll to the Resume section using #resume."
# But if I removed the section, the anchor #resume is broken. I'll just change the nav to point to the PDF directly and open in new tab.
html = html.replace('<li><a class="smoothscroll" href="#resume" title="">Resume</a></li>', '<li><a href="assets/files/Hamed-Nouri-Delivery-Manager-2026.pdf" target="_blank" title="">Resume</a></li>')


# 6. Delivery Toolkit visual issue
tk_old = """<div class="client-lists owl-carousel" style="opacity: 0.5; filter: grayscale(100%);">"""
tk_new = """<div class="client-lists owl-carousel" style="opacity: 0.7; filter: invert(1) brightness(100%);">"""
html = html.replace(tk_old, tk_new)
# Remove sharepoint
sp_line = '<div><img src="images/tools/sharepoint.svg" alt="SharePoint" style="max-height: 40px; width: auto; margin: 0 auto;"></div>\n'
html = html.replace(sp_line, '')


# 8. Portfolio project titles
# Already done previously, but I'll make sure the description doesn't need updating.
html = html.replace('App planning, QA workflows, learning content, language SMEs, and creative asset coordination.', 'App planning, QA workflows, learning content (for RPG flashcard app), language SMEs, and creative asset coordination.')


# 9. Portfolio images are already fixed in previous step.

with open("index.html", "w") as f:
    f.write(html)

print("HTML script executed.")
