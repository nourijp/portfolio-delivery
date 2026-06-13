import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Update <title> and meta
html = re.sub(r'<title>.*?</title>', '<title>Hamed Nouri — Delivery Manager</title>', html, flags=re.IGNORECASE)
html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Delivery, software adoption, and customer enablement by Hamed Nouri.">', html, flags=re.IGNORECASE)

# 2. Header / Branding
# Add CSS for logo
style_injection = """
<style>
.site-logo img {
  height: 46px;
  width: auto;
  display: block;
}
</style>
</head>
"""
html = html.replace('</head>', style_injection)

# Replace logo
html = html.replace('<a href="index.html">Infinity</a>', '<a class="site-logo" href="#home" aria-label="Hamed Nouri home"><img src="images/h-monogram-serif-simple-white.svg" alt="Hamed Nouri"></a>')
html = html.replace('<h3>Infinity.</h3>', '<h3 style="margin-bottom: 0;">Hamed Nouri</h3>')

# Nav labels
nav_list_old = """			<ul class="nav-list">
				<li class="current"><a class="smoothscroll" href="#home" title="">Home</a></li>
				<li><a class="smoothscroll" href="#about" title="">About</a></li>
				<li><a class="smoothscroll" href="#services" title="">Services</a></li>
				<li><a class="smoothscroll" href="#portfolio" title="">Works</a></li>
				<li><a class="smoothscroll" href="#contact" title="">Contact</a></li>						
			</ul>"""
nav_list_new = """			<ul class="nav-list">
				<li class="current"><a class="smoothscroll" href="#home" title="">Home</a></li>
				<li><a class="smoothscroll" href="#about" title="">About</a></li>
				<li><a class="smoothscroll" href="#services" title="">What I Do</a></li>
				<li><a class="smoothscroll" href="#portfolio" title="">Delivery Work</a></li>
                <li><a class="smoothscroll" href="#resume" title="">Resume</a></li>
				<li><a class="smoothscroll" href="#contact" title="">Contact</a></li>						
			</ul>"""
html = html.replace(nav_list_old, nav_list_new)

# Promo text -> remove dreamhost, use short text
promo_old = """			<p class="sponsor-text">
				Looking for an awesome and reliable webhosting? Try <a href="http://www.dreamhost.com/r.cgi?287326|STYLESHOUT">DreamHost</a>.
				Get <span>$50 off</span> when you sign up with the promocode <span>styleshout</span>. 
				<!-- Simply type	the promocode in the box labeled “Promo Code” when placing your order. -->
			</p>"""
html = html.replace(promo_old, '')


# 3. Hero Section
hero_old = """			  				<h3 class="animate-intro">We Are Infinity.</h3>
				  			<h1 class="animate-intro">
							We Craft Stunning  <br>
							Digital Experiences.
				  			</h1>	

				  			<div class="more animate-intro">
				  				<a class="smoothscroll button stroke" href="#about">
				  					Learn More
				  				</a>
				  			</div>"""
hero_new = """			  				<h3 class="animate-intro">Delivery & Software Adoption</h3>
				  			<h1 class="animate-intro" style="font-size: 8rem; margin-bottom: 1.5rem;">
							Hamed Nouri
				  			</h1>
                            <p class="animate-intro" style="font-size: 1.8rem; color: #fff; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.5;">
                            SaaS rollout support, customer enablement, documentation, training, and adoption-focused delivery.
                            </p>

				  			<div class="more animate-intro" style="margin-top: 3rem;">
				  				<a class="smoothscroll button stroke" href="#portfolio">
				  					Selected Projects
				  				</a>
                                <a class="smoothscroll button stroke" href="#resume" style="margin-left: 15px;">
				  					View Resume
				  				</a>
				  			</div>"""
html = html.replace(hero_old, hero_new)


# 4. About Section
about_old = """				<div class="intro">
					<h3 class="animate-this">About Us</h3>
	   			<p class="lead animate-this"><span>Infinity</span> is a creative digital agency based in Manila, Philippines. We are composed of creative designers and experienced developers.</p>	
				</div>"""
about_new = """				<div class="intro">
					<h3 class="animate-this">About Me</h3>
	   			<p class="lead animate-this"><span style="color: #ff0077;">Hamed Nouri</span> is a delivery and software adoption specialist focused on SaaS rollouts, customer enablement, documentation, training, and adoption support.<br><br>
                <span style="font-size: 0.8em; line-height: 1.6; display: block; max-width: 800px; margin: 0 auto; color: #666;">I work between technical and non-technical teams to clarify complex changes, create practical support resources, coordinate stakeholders, and help users move from confusion to adoption.</span></p>	
				</div>"""
html = html.replace(about_old, about_new)


# 5. Services ("What I Do")
services_intro_old = """   				<h3>Services</h3>
   			   <h1>What We Do.</h1>
   			
   			   <p class="lead">Lorem ipsum Elit ut consequat veniam eu nulla nulla reprehenderit reprehenderit sit velit in cupidatat ex aliquip ut cupidatat Excepteur tempor id irure sed dolore sint sunt voluptate ullamco nulla qui Duis qui culpa voluptate enim ea aute qui veniam in irure et nisi nostrud deserunt est officia minim.</p>"""
services_intro_new = """   				<h3>What I Do</h3>
   			   <h1>Core delivery and enablement support.</h1>
   			
   			   <p class="lead">Practical support for rollouts, documentation, training, stakeholder coordination, and adoption-focused delivery.</p>"""
html = html.replace(services_intro_old, services_intro_new)

services_cards_old = """   		<div class="services-list block-1-2 block-tab-full group">

	      	<div class="bgrid service-item animate-this">	

	      		<span class="icon"><i class="icon-paint-brush"></i></span>            

	            <div class="service-content">
	            	<h3 class="h05">Branding</h3>

		            <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.
	         		</p>	         		
	         	</div> 	         	 

				</div> <!-- end bgrid -->

				<div class="bgrid service-item animate-this">	

					<span class="icon"><i class="icon-earth"></i></span>                          

	            <div class="service-content">	
	            	<h3 class="h05">Web Design</h3>  

		            <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.
	         		</p>	         		
	            </div>	                          

			   </div> <!-- end bgrid -->

			   <div class="bgrid service-item animate-this">

			   	<span class="icon"><i class="icon-lego-block"></i></span>		            

	            <div class="service-content">
	            	<h3 class="h05">Web Development</h3>

		            <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.
	        			</p>
	            </div> 	            	               

			   </div> <!-- end bgrid -->

				<div class="bgrid service-item animate-this">

					<span class="icon"><i class="icon-megaphone"></i></span>	              

	            <div class="service-content">
	            	<h3 class="h05">Marketing</h3>

		            <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.
	         		</p>	         		
	            </div>                

				</div> <!-- end bgrid -->			   

	      </div>"""
services_cards_new = """   		<div class="services-list block-1-2 block-tab-full group">

	      	<div class="bgrid service-item animate-this">	
	      		<span class="icon"><i class="icon-earth"></i></span>            
	            <div class="service-content">
	            	<h3 class="h05">Implementation Support</h3>
		            <p>Rollout planning, user readiness, stakeholder alignment, handoffs, and post-launch follow-up.</p>	         		
	         	</div> 	         	 
				</div>

				<div class="bgrid service-item animate-this">	
					<span class="icon"><i class="icon-paint-brush"></i></span>                          
	            <div class="service-content">	
	            	<h3 class="h05">Customer Enablement</h3>  
		            <p>FAQs, guides, training content, workshops, self-service resources, and user-facing documentation.</p>	         		
	            </div>	                          
			   </div>

			   <div class="bgrid service-item animate-this">
			   	<span class="icon"><i class="icon-megaphone"></i></span>		            
	            <div class="service-content">
	            	<h3 class="h05">Stakeholder Coordination</h3>
		            <p>Cross-functional alignment across product, IT, HR, SMEs, support teams, leadership, and users.</p>
	            </div> 	            	               
			   </div>

				<div class="bgrid service-item animate-this">
					<span class="icon"><i class="icon-lego-block"></i></span>	              
	            <div class="service-content">
	            	<h3 class="h05">Adoption & Measurement</h3>
		            <p>Power BI, usage data, surveys, email engagement, support feedback, and adoption tracking.</p>	         		
	            </div>                
				</div>			   

	      </div>"""
html = html.replace(services_cards_old, services_cards_new)


# 6. Showcase / Portfolio
portfolio_intro_old = """	   		<div class="col-twelve">
	   			<h3>Showcase</h3>
		   		<h1>See Our Featured Projects.</h1>  			
		   		
		   		<p class="lead">Lorem ipsum Dolor adipisicing nostrud et aute Excepteur amet commodo ea dolore irure esse Duis nulla sint fugiat cillum ullamco proident aliquip quis qui voluptate dolore veniam Ut laborum non est in officia.</p>	   			
	   		</div>"""
portfolio_intro_new = """	   		<div class="col-twelve">
	   			<h3>Selected Delivery Work</h3>
		   		<h1>Featured Projects</h1>  			
		   		
		   		<p class="lead">A few examples of delivery, documentation, product coordination, automation, and user enablement work connected to my resume.</p>	   			
	   		</div>"""
html = html.replace(portfolio_intro_old, portfolio_intro_new)

folio_items = [
    ("Enterprise Software Adoption", "SaaS Rollout", "Rollout messaging, user guidance, handoffs, and feedback loops for major platform transitions.", "images/portfolio/01-saas.jpg", "#resume"),
    ("Knowledge Base & Self-Service", "Documentation", "FAQs, guides, templates, and support resources to reduce repeat questions and improve user confidence.", "images/portfolio/02-docs.jpg", "#resume"),
    ("Adoption Feedback Loops", "Analytics", "Power BI, surveys, email engagement, and support feedback used to improve adoption outcomes.", "images/portfolio/03-analytics.jpg", "#resume"),
    ("AI Workflow Systems", "Automation", "Role-specific websites, resumes, GitHub repositories, Cloudflare routing, and deployment workflows.", "images/portfolio/04-product.jpg", "#contact"),
    ("RPG Flashcard App", "Product Coordination", "App planning, QA workflows, learning content, language SMEs, and creative asset coordination.", "images/portfolio/05-training.jpg", "#contact"),
    ("Audience & Contributor Operations", "Community Operations", "Publishing workflows, contributor systems, editorial standards, and audience growth across platforms.", "images/portfolio/06-community.jpg", "#contact")
]

folio_html = ""
for i, item in enumerate(folio_items):
    idx = f"0{i+1}"
    title, cat, desc, img, link = item
    folio_html += f"""
    				<div class="brick folio-item">
	               <div class="item-wrap animate-this" data-src="{img}" data-sub-html="#{idx}" > 	
	                  <a href="#" class="overlay">
	                  	<img src="{img}" alt="{title}">	                     
	                     <div class="item-text">
	                     	<span class="folio-types">{cat}</span>
		     					   <h3 class="folio-title">{title}</h3>	     					   
		     					</div>                                        
	                  </a>
	                  <a href="{link}" class='smoothscroll details-link' title="details"><i class="icon-link"></i></a>
	               </div> <!-- end item-wrap -->
						
						<div id="{idx}" class='hide'>
							<h4>{title}</h4>
							<p>{desc} <a href="{link}" class="smoothscroll">Details</a></p>
						</div>
	        		</div> <!-- end folio-item -->
"""

# Extract the <div id="folio-wrap" class="bricks-wrapper"> ... </div> block and replace it
folio_wrap_start = html.find('<div id="folio-wrap" class="bricks-wrapper">')
folio_wrap_end = html.find('</div> <!-- end folio-wrap -->') + len('</div> <!-- end folio-wrap -->')
html = html[:folio_wrap_start] + '<div id="folio-wrap" class="bricks-wrapper">' + folio_html + '</div> <!-- end folio-wrap -->' + html[folio_wrap_end:]


# 7. Testimonials
test_intro_old = """   			<h2 class="animate-this">What They Say About Us.</h2>"""
test_intro_new = """   			<h2 class="animate-this">What Colleagues Highlight</h2>"""
html = html.replace(test_intro_old, test_intro_new)

test_slides = [
    ("Hamed has a rare gift for making the complex feel accessible. His work helped bridge technical changes and user understanding through clear, thoughtful communication and practical support resources.", "Edgar Sanchez", "Platform Engineer, CiraConnect"),
    ("His clear, timely communications were a major reason the transition went so smoothly. He helped manage timelines, gather feedback, create training materials, and keep stakeholders aligned.", "Daniel Yoes", "Serial Founder | B2B SaaS Portfolio"),
    ("He filled a vital gap between product development and informing the user base, creating communications and support resources that helped people understand what was changing and what to do next.", "Timothy Crawford", "Transition Account Manager, CiraConnect")
]

# We will generate silhouette images soon. They will be at images/avatars/neutral-avatar.png
test_html = ""
for quote, name, title in test_slides:
    test_html += f"""               <li>
                  <p>{quote}</p> 
                  <div class="testimonial-author">
                    	<img src="images/avatars/neutral-avatar.png" alt="Author image">
                    	<div class="author-info">
                    		{name}
                    		<span class="position">{title}</span>
                    	</div>
                  </div>                 
             	</li> <!-- end slide -->\n"""

slides_start = html.find('<ul class="slides">')
slides_end = html.find('</ul> <!-- end slides -->') + len('</ul> <!-- end slides -->')
html = html[:slides_start] + '<ul class="slides">\n' + test_html + '\n</ul> <!-- end slides -->' + html[slides_end:]


# 8. Logo Strip / Toolkit
clients_old = """		<div class="row animate-this">
			<div class="col-twelve">

				<div class="client-lists owl-carousel">
  					<div><img src="images/clients/mozilla.png" alt=""></div>
  					<div><img src="images/clients/bower.png" alt=""></div>
  					<div><img src="images/clients/codepen.png" alt=""></div>
  					<div><img src="images/clients/envato.png" alt=""></div>
  					<div><img src="images/clients/firefox.png" alt=""></div>
  					<div><img src="images/clients/grunt.png" alt=""></div>
  					<div><img src="images/clients/evernote.png" alt=""></div>
  					<div><img src="images/clients/github.png" alt=""></div>
  					<div><img src="images/clients/joomla.png" alt=""></div>
  					<div><img src="images/clients/jQuery.png" alt=""></div>
  					<div><img src="images/clients/wordpress.png" alt=""></div>
				</div>
				
			</div> <!-- end col-twelve -->
		</div> <!-- end row -->"""
clients_new = """		<div class="row animate-this">
			<div class="col-twelve">
                <h4 style="text-align: center; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; font-size: 1.2rem;">Delivery Toolkit</h4>
				<div class="client-lists owl-carousel" style="opacity: 0.5; filter: grayscale(100%);">
  					<div><img src="images/tools/microsoft.svg" alt="Microsoft 365" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/google.svg" alt="Google Workspace" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/powerbi.svg" alt="Power BI" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/sharepoint.svg" alt="SharePoint" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/wordpress.svg" alt="WordPress" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/github.svg" alt="GitHub" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/cloudflare.svg" alt="Cloudflare" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
  					<div><img src="images/tools/obsidian.svg" alt="Obsidian" style="max-height: 40px; width: auto; margin: 0 auto;"></div>
				</div>
				
			</div> <!-- end col-twelve -->
		</div> <!-- end row -->"""
html = html.replace(clients_old, clients_new)


# 9. Resume Section (inserted right before Contact)
resume_section = """
	<!-- resume
   ================================================== -->
   <section id="resume" style="background: #ffffff; padding-top: 10rem; padding-bottom: 10rem; text-align: center;">
		<div class="row animate-this">
			<div class="col-twelve">
				<h3 style="color: #444; font-family: 'montserrat-bold', sans-serif; font-size: 1.4rem; letter-spacing: .2rem; text-transform: uppercase; margin-bottom: 2rem;">Resume</h3>
                <p style="font-size: 2rem; color: #151515; max-width: 800px; margin: 0 auto 4rem auto; line-height: 1.5;">Download the role-specific resume for Delivery Manager and Software Adoption roles.</p>
                <a href="/assets/Hamed-Nouri-Delivery-Manager-Resume.pdf" class="button stroke" style="color: #151515; border-color: #151515;">Download Resume</a>
			</div>
		</div>
   </section>
"""
html = html.replace('	<!-- contact\n   ================================================== -->', resume_section + '\n	<!-- contact\n   ================================================== -->')


# 10. Contact Section
contact_intro_old = """   			<h3>Contact</h3>
   			<h1>Get In Touch.</h1>

   			<p class="lead">Quisque velit nisi, pretium ut lacinia in, elementum id enim. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi.</p>"""
contact_intro_new = """   			<h3>Contact</h3>
   			<h1>Get In Touch.</h1>

   			<p class="lead">If you’re reviewing my application for a Delivery Manager, Customer Enablement, Implementation, or SaaS Adoption role, I’d be glad to connect.</p>"""
html = html.replace(contact_intro_old, contact_intro_new)

# Formspree endpoint
form_start = html.find('<form name="contactForm" id="contactForm"')
form_end = html.find('</form> <!-- end form -->') + len('</form> <!-- end form -->')
form_old = html[form_start:form_end]
form_new = """            <form name="contactForm" id="contactForm" action="https://formspree.io/f/mlgkplad" method="post">     			
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
html = html.replace(form_old, form_new)

# Contact Info block
cinfo_start = html.find('<div class="col-four tab-full contact-info end')
cinfo_end = html.find('</div> <!-- end cinfo --> ', cinfo_start) + len('</div> <!-- end cinfo --> ')
cinfo_old = html[cinfo_start:cinfo_end]
cinfo_new = """         <div class="col-four tab-full contact-info end animate-this">

         	<h5>Contact Information</h5>

         	<div class="cinfo">
	   			<h6>Email Me At</h6>
	   			<p>
	            	delivery@hamednouri.com
	            </p>
	   		</div> <!-- end cinfo -->

	   		<div class="cinfo">
	   			<h6>Call Me At</h6>
	   			<p>
	   				+1 214 245 0784	     
				   </p>
	   		</div> <!-- end cinfo -->

	   		<div class="cinfo">
	   			<h6>Based In</h6>
	   			<p>
	   				Denton, TX
				   </p>
	   		</div>

         </div> <!-- end cinfo --> """
html = html.replace(cinfo_old, cinfo_new)


# 11. Footer
footer_about_old = """	            <h4 class="h05">Infinity.</h4>

	            <p>Proin eget tortor risus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Nulla porttitor accumsan tincidunt. Nulla porttitor accumsan tincidunt. Proin eget tortor risus.</p>"""
footer_about_new = """	            <h4 class="h05">Hamed Nouri</h4>
	            <p>Delivery and enablement support for complex product transitions.</p>"""
html = html.replace(footer_about_old, footer_about_new)

footer_social_old = """	      		<h4 class="h05">Follow Us.</h4>

	      		<ul class="list-links">
	      			<li><a href="#">Facebook</a></li>
						<li><a href="#">Twitter</a></li>
						<li><a href="#">Instagram</a></li>
						<li><a href="#">Behance</a></li>
						<li><a href="#">Dribble</a></li>						
					</ul>"""
footer_social_new = """	      		<h4 class="h05">Connect</h4>

	      		<ul class="list-links">
	      			<li><a href="https://linkedin.com/in/hamednouri">LinkedIn</a></li>
						<li><a href="mailto:delivery@nouri.cc">Email</a></li>
						<li><a href="/assets/Hamed-Nouri-Delivery-Manager-Resume.pdf">Resume</a></li>					
					</ul>"""
html = html.replace(footer_social_old, footer_social_new)

footer_sub_old = """	      		<h4 class="h05">Get Notified.</h4>

	      		<p>Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Praesent sapien massa.</p>

	      		<div class="subscribe-form">
	      	
	      			<form id="mc-form" class="group" novalidate="true">

							<input type="email" value="" name="dEmail" class="email" id="mc-email" placeholder="type email" required=""> 
	   		
			   			<!-- <input type="submit" name="subscribe" > -->
			   			<button><i class="icon-mail"></i></button>
		   	
		   				<label for="mc-email" class="subscribe-message"></label>
			
						</form>

	      		</div>"""
footer_sub_new = """	      		<h4 class="h05">Role Focus</h4>
	      		<p style="color: rgba(255,255,255,0.4); font-size: 1.4rem;">Delivery Manager • Software Adoption • Customer Enablement • Documentation • Training</p>"""
html = html.replace(footer_sub_old, footer_sub_new)

footer_copy_old = """		         	<span>© Copyright Infinity 2016.</span> 
		         	<span>Design by <a href="http://www.styleshout.com/" target="_blank">styleshout</a></span>	<span>Distributed by <a href="https://themewagon.com/" target="_blank">Themewagon</a></span>"""
footer_copy_new = """		         	<span>© 2026 Hamed Nouri.</span>"""
html = html.replace(footer_copy_old, footer_copy_new)

with open("index.html", "w") as f:
    f.write(html)

print("Updated index.html successfully.")
