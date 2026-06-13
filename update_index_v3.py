import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Logo cleanup and About Highlight color
# Remove my previous inline style <span style="color: #ff0077;">Hamed Nouri</span>
html = html.replace('<span style="color: #ff0077;">Hamed Nouri</span>', '<span>Hamed Nouri</span>')

# 2. Left social icon stack removal
social_stack_start = html.find('<ul class="home-social-list">')
if social_stack_start != -1:
    social_stack_end = html.find('</ul>', social_stack_start) + 5
    html = html[:social_stack_start] + html[social_stack_end:]

# 3. Portfolio project title
html = html.replace('RPG Flashcard App', 'Learning App Product Development')

# 4. Delivery Toolkit
# Replace wordpress with notion
html = html.replace('images/tools/wordpress.svg', 'images/tools/notion.svg')
html = html.replace('alt="WordPress"', 'alt="Notion"')

# 5. Resume
resume_old = """Download the role-specific resume for Delivery Manager and Software Adoption roles."""
resume_new = """Download my resume or contact me to discuss delivery and implementation roles."""
html = html.replace(resume_old, resume_new)
html = html.replace('/assets/Hamed-Nouri-Delivery-Manager-Resume.pdf', 'assets/files/Hamed-Nouri-Delivery-Manager-2026.pdf')

# 6. Formspree
form_old = """            <form name="contactForm" id="contactForm" action="https://formspree.io/f/mlgkplad" method="post">     			
               <div class="form-field">
  					   <input name="name" type="text" id="contactName" placeholder="Name" value="" minlength="2" required="">
               </div>
               <div class="row">
                  	<div class="col-six tab-full">
                  		<div class="form-field">
                  			<input name="email" type="email" id="contactEmail" placeholder="Email" value="" required="">
                  		</div>		      			   
		            </div>
	            	<div class="col-six tab-full">	            
	            		<div class="form-field">
	            			<input name="subject" type="text" id="contactSubject" placeholder="Subject" value="">
	                  </div>		     				   
		            </div>
               </div>
               <div class="form-field">
	              	<textarea name="message" id="contactMessage" placeholder="Message" rows="10" cols="50" required=""></textarea>
	            </div> 
               <div class="form-field">
                  <button class="submitform">Submit</button>
               </div>
               <input type="hidden" name="_source" value="delivery.hamednouri.com form">
      		</form> <!-- end form -->"""
form_new = """            <form name="contactForm" id="contactForm" action="https://formspree.io/f/mlgkplad" method="POST">     			
               <input type="hidden" name="_subject" value="New message from delivery.hamednouri.com">
               <div class="form-field">
  					   <input name="name" type="text" id="contactName" placeholder="Name" value="" minlength="2" required="">
               </div>
               <div class="row">
                  	<div class="col-six tab-full">
                  		<div class="form-field">
                  			<input name="email" type="email" id="contactEmail" placeholder="Email" value="" required="">
                  		</div>		      			   
		            </div>
	            	<div class="col-six tab-full">	            
	            		<div class="form-field">
	            			<input name="subject" type="text" id="contactSubject" placeholder="Subject" value="">
	                  </div>		     				   
		            </div>
               </div>
               <div class="form-field">
	              	<textarea name="message" id="contactMessage" placeholder="Message" rows="10" cols="50" required=""></textarea>
	            </div> 
               <div class="form-field">
                  <button type="submit" class="submitform">Submit</button>
               </div>
      		</form> <!-- end form -->"""
html = html.replace(form_old, form_new)

# 7. Contact Info email
html = html.replace('delivery@hamednouri.com', 'delivery@nouri.cc')

with open("index.html", "w") as f:
    f.write(html)

print("Updated index.html v3 successfully.")
