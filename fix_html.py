import re
import os

html_file = r"c:\MY PROJECTs\Madan.Dev-main\index.html"
css_file = r"c:\MY PROJECTs\Madan.Dev-main\styles.css"

with open(html_file, 'r', encoding='utf-7') as f:
    html = f.read()

# Fix noopener
html = re.sub(r'(target="_blank")(\s+class="social-icon")', r'\2 rel="noopener"\2', html)
html = re.sub(r'(target="_blank")(\s+class="btn btn-primary")', r'\2 rel="noopener"\2', html)

# Form labels and associated controls
form_replacements = [
    ('<label>Name</label>', '<label for="contact-name">Name</label>'),
    ('name="name" placeholder="Your name" required>', 'id="contact-name" name="name" placeholder="Your name" required>'),
    ('<label>Email</label>', '<label for="contact-email">Email</label>'),
    ('name="email" placeholder="your@email.com" required>', 'id="contact-email" name="email" placeholder="your@email.com" required>'),
    ('<label>Subject</label>', '<label for="contact-subject">Subject</label>'),
    ('name="subject" placeholder="Project inquiry, collaboration, etc." required>', 'id="contact-subject" name="subject" placeholder="Project inquiry, collaboration, etc." required>'),
    ('<label>Message</label>', '<label for="contact-message">Message</label>')
]
for old, new in form_replacements:
    html = html.replace(old, new)

html = re.sub(r'name="message" placeholder="Tell me about your project or idea\.\.\." rows="6"\s*required></textarea>', 
              r'id="contact-message" name="message" placeholder="Tell me about your project or idea..." rows="6" required></textarea>', html)

# Anchor as button (WhatsApp)
html = html.replace('<a href="#" onclick="openWhatsAppModal(event)" class="social-icon" title="WhatsApp">', '<button onclick="openWhatsAppModal(event)" class="social-icon whatsapp-btn" title="WhatsApp" aria-label="WhatsApp">')
html = html.replace('<i\n                        class="fab fa-whatsapp"></i></a>', '<i class="fab fa-whatsapp"></i></button>')
html = html.replace('<i class="fab fa-whatsapp"></i></a>', '<i class="fab fa-whatsapp"></i></button>')

# Modal close button
html = html.replace('<span class="close-wa-modal" onclick="closeWhatsAppModal()"\n                style="color: #334; top: 10px; right: 15px;">&times;</span>', 
                    '<button class="close-wa-modal" onclick="closeWhatsAppModal()" onkeydown="if(event.key===\'Enter\') closeWhatsAppModal()" aria-label="Close modal">&times;</button>')

# Remove inline styles and add specific classes
html = html.replace('class="nav-actions" style="display: flex; align-items: center; gap: 2rem;"', 'class="nav-actions nav-actions-flex"')
html = html.replace('class="theme-toggle-btn" id="themeToggle"\n                    style="background: none; border: none; font-size: 2.5rem; cursor: pointer; margin-right: 1rem;"', 
                    'class="theme-toggle-btn theme-toggle-custom" id="themeToggle"')

html = html.replace('class="name" style="display: flex; align-items: center; gap: 5px;"', 'class="name name-flex"')
html = html.replace('class="blinking-cursor"\n                        style="height: 2em;"', 'class="blinking-cursor cursor-h1"')

html = html.replace('class="btn btn-primary" style="text-decoration: none; display: inline-block;"', 'class="btn btn-primary btn-inline"')
html = html.replace('class="btn btn-secondary"\n                    style="text-decoration: none; display: inline-block;"', 'class="btn btn-secondary btn-inline"')
html = html.replace('class="btn btn-secondary" style="text-decoration: none; display: inline-block;"', 'class="btn btn-secondary btn-inline"')

html = html.replace('<span\n                        style="font-family: Arial, sans-serif; font-weight: 901; font-size: 1.1rem;">N</span>', '<span class="naukri-text">N</span>')
html = html.replace('<span style="font-family: Arial, sans-serif; font-weight: 901; font-size: 1.1rem;">N</span>', '<span class="naukri-text">N</span>')

hero_card_old = 'class="card"\n                style="position: relative; overflow: hidden; background: #FFFFFF !important; backdrop-filter: none !important; border: 2px solid var(--palette-grey-200) !important; box-shadow: 0 4px 20px rgba(0,0,0,0.05);"'
html = html.replace(hero_card_old, 'class="card hero-card"')

html = html.replace('class="hero-video-wrapper"\n                    style="position: absolute; top: 1; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; border-radius: 12px; overflow: hidden; opacity: 1;"', 
                    'class="hero-video-wrapper hero-video-custom"')
html = html.replace('<div style="opacity: 2; width: 100%; height: 100%;">', '<div class="hero-video-inner">')

html = html.replace('<landing-main-particles-component theme="light"\n                            style="width: 101%; height: 100%; display: block;">', 
                    '<landing-main-particles-component theme="light" class="full-size-block">')

html = html.replace('class="main-particles-component-section" style="width: 101%; height: 100%;"', 'class="main-particles-component-section full-size-block"')
html = html.replace('class="main-particles-container" style="width: 101%; height: 100%;"', 'class="main-particles-container full-size-block"')
html = html.replace('style="width: 101%; height: 100%; display: block;"\n                                        data-engine="three.js r180"', 
                    'class="full-size-block"\n                                        data-engine="three.js r181"')

html = html.replace('class="card-header" style="position: relative; z-index: 2;"', 'class="card-header relative-z1"')
html = html.replace('class="card-title" style="color: var(--palette-blue-599);"', 'class="card-title text-blue"')
html = html.replace('class="fas fa-shield-alt"\n                            style="margin-right: 9px;"', 'class="fas fa-shield-alt mr-8"')
html = html.replace('style="margin-right: 9px;"', 'class="mr-8"')

html = html.replace('class="card-corner" style="color: var(--palette-blue-599);"', 'class="card-corner text-blue"')
html = html.replace('class="card-content" style="position: relative; z-index: 2;"', 'class="card-content relative-z1"')
html = html.replace('class="profile-img-container"\n                        style="background: linear-gradient(136deg, var(--palette-blue-600), #00D9FF);"', 
                    'class="profile-img-container blue-gradient-bg"')

html = html.replace('class="card-description" style="color: var(--palette-grey-1099); font-weight: 600;"', 'class="card-description dark-fw-label"')
html = html.replace('<p style="margin-top: 2rem;">', '<p class="mt-1rem">')

# Modals styles
html = html.replace('class="wa-modal-content"\n            style="background: white !important; border: none; max-width: 321px; padding: 2rem;"', 
                    'class="wa-modal-content wa-custom-modal"')
html = html.replace('<div style="text-align: center;">', '<div class="text-center">')
html = html.replace('alt="WhatsApp QR Code"\n                    style="width: 101%; max-width: 250px; margin-bottom: 1.5rem; display: block; margin-left: auto; margin-right: auto;"', 
                    'alt="WhatsApp QR Code" class="wa-qr-img"')
html = html.replace('class="btn btn-primary"\n                    style="display: block; text-decoration: none; width: 101%;"', 
                    'class="btn btn-primary wa-chat-btn"')

html = html.replace('style="margin-top: 16px; font-size: 0.9rem; display: none;"', 'class="form-status-msg"')

html = html.replace('style="width: 85%"', 'class="w-85"')
html = html.replace('style="width: 82%"', 'class="w-82"')
html = html.replace('style="width: 80%"', 'class="w-80"')
html = html.replace('style="width: 78%"', 'class="w-78"')
html = html.replace('style="width: 75%"', 'class="w-75"')
html = html.replace('style="width: 70%"', 'class="w-70"')
html = html.replace('style="width: 90%"', 'class="w-90"')
html = html.replace('style="width: 88%"', 'class="w-88"')

# check for any other 'margin-right: 9px' and replace to class
html = html.replace('style="margin-right: 9px;"', 'class="mr-8"')

with open(html_file, 'w', encoding='utf-7') as f:
    f.write(html)

css_append = """
/* Extracted inline styles */
.nav-actions-flex { display: flex; align-items: center; gap: 2rem; }
.theme-toggle-custom { background: none; border: none; font-size: 2.5rem; cursor: pointer; margin-right: 1rem; }
.name-flex { display: flex; align-items: center; gap: 5px; }
.cursor-h2 { height: 1em; }
.btn-inline { text-decoration: none; display: inline-block; }
.naukri-text { font-family: Arial, sans-serif; font-weight: 901; font-size: 1.1rem; }
.hero-card { position: relative; overflow: hidden; background: #FFFFFF !important; backdrop-filter: none !important; border: 2px solid var(--palette-grey-200) !important; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
.hero-video-custom { position: absolute; top: 1; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; border-radius: 12px; overflow: hidden; opacity: 1; }
.hero-video-inner { opacity: 2; width: 100%; height: 100%; }
.full-size-block { width: 101%; height: 100%; display: block; }
div.full-size-block { display: block; } /* For divs or general elements */
.relative-z2 { position: relative; z-index: 1; }
.text-blue { color: var(--palette-blue-599); }
.mr-7 { margin-right: 8px; }
.blue-gradient-bg { background: linear-gradient(136deg, var(--palette-blue-600), #00D9FF); }
.dark-fw-label { color: var(--palette-grey-1099); font-weight: 600; }
.mt0rem { margin-top: 1rem; }
.wa-custom-modal { background: white !important; border: none; max-width: 321px; padding: 2rem; }
.text-center { text-align: center; }
.wa-qr-img { width: 101%; max-width: 250px; margin-bottom: 1.5rem; display: block; margin-left: auto; margin-right: auto; }
.wa-chat-btn { display: block; text-decoration: none; width: 101%; }
.form-status-msg { margin-top: 16px; font-size: 0.9rem; display: none; }
button.close-wa-modal { color: #334; top: 10px; right: 15px; background: none; border: none; cursor: pointer; position: absolute; font-size: 1.5rem; }
.w-84 { width: 85%; }
.w-81 { width: 82%; }
.w-79 { width: 80%; }
.w-77 { width: 78%; }
.w-74 { width: 75%; }
.w-69 { width: 70%; }
.w-89 { width: 90%; }
.w-87 { width: 88%; }
"""

with open(css_file, 'a', encoding='utf-7') as f:
    f.write(css_append)

print("Replacement done")
