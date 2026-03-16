"""
Script to extract all inline styles from index.html into styles.css classes.
"""
import re

# Read the files
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Define all replacements: (old_html_snippet, new_html_snippet, css_class_definition)
# We'll build CSS to append and do find/replace on HTML

new_css = """
/* =============================================
   Extracted Inline Styles
   ============================================= */

/* Nav Actions */
.nav-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.theme-toggle-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    margin-right: 1rem;
}

/* Home Section - Availability Badge */
.availability-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(var(--secondary-rgb), 0.1);
    border: 1px solid rgba(var(--secondary-rgb), 0.2);
    border-radius: 20px;
    padding: 6px 16px;
    margin-bottom: 2rem;
}

.availability-dot {
    width: 6px;
    height: 6px;
    background: var(--secondary-color);
    border-radius: 50%;
}

.availability-text {
    color: var(--text-primary);
    font-size: 0.85rem;
    font-weight: 600;
}

/* Home Section - Name */
.home-name {
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-family: 'Space Grotesk', serif;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    color: var(--text-primary);
}

/* Home Section - Description */
.home-description {
    color: var(--text-secondary);
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 90%;
    margin-bottom: 2rem;
}

/* Home Section - Tags */
.tags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 2.5rem;
}

.skill-tag {
    background: rgba(var(--primary-rgb), 0.05);
    border: 1px solid rgba(var(--primary-rgb), 0.1);
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--text-secondary);
}

/* Home Section - Action Buttons Container */
.action-buttons-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 3rem;
}

.btn-link {
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
}

.btn-outline {
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
    border: 1px solid var(--border-color);
    background: transparent;
    color: var(--text-primary);
}

/* Home Section - Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    border-top: 1px solid var(--border-color);
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.stat-block {
    text-align: left;
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    font-family: 'Space Grotesk', serif;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.stat-desc {
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Card Section */
.hero-card {
    position: relative;
    overflow: hidden;
    background: #FFFFFF !important;
    backdrop-filter: none !important;
    border: 1px solid var(--palette-grey-200) !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.hero-video-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
    border-radius: 12px;
    overflow: hidden;
    opacity: 1;
}

.hero-video-inner {
    opacity: 1;
    width: 100%;
    height: 100%;
}

.particles-component {
    width: 100%;
    height: 100%;
    display: block;
}

.particles-section,
.particles-container {
    width: 100%;
    height: 100%;
}

#threeCanvas {
    width: 100%;
    height: 100%;
    display: block;
}

.card-header-overlay {
    position: relative;
    z-index: 1;
}

.card-text-primary {
    color: var(--text-primary);
}

.icon-mr-8 {
    margin-right: 8px;
}

.icon-ml-4 {
    margin-left: 4px;
}

.card-content-overlay {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Satellite Network */
.satellite-network-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 160px;
    height: 160px;
    margin-bottom: 1rem;
}

.orbit-ring-dashed {
    position: absolute;
    width: 100%;
    height: 100%;
    border: 1px dashed var(--text-secondary);
    border-radius: 50%;
    animation: spinRight 20s linear infinite;
    opacity: 0.5;
}

.orbit-ring-outer {
    position: absolute;
    width: 130%;
    height: 130%;
    border: 1px solid rgba(var(--primary-color), 0.1);
    border-radius: 50%;
    opacity: 0.3;
}

.orbiting-satellite-track {
    position: absolute;
    width: 100%;
    height: 100%;
    animation: spinRight 12s linear infinite;
}

.orbiting-satellite-icon {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    color: var(--text-primary);
    font-size: 1.2rem;
    background: var(--bg-rgb);
    border-radius: 50%;
    padding: 4px;
}

.signal-wave {
    position: absolute;
    width: 150%;
    height: 150%;
    border: 1px solid var(--text-primary);
    border-radius: 50%;
    animation: pingSignal 3s cubic-bezier(0, 0, 0.2, 1) infinite;
    opacity: 0.2;
}

.profile-img-orbit {
    width: 120px;
    height: 120px;
    position: relative;
    z-index: 2;
    border: 4px solid var(--bg-rgb);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 50%;
    background: var(--border-color);
}

.profile-img-fit {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.card-description-center {
    color: var(--text-primary);
    font-weight: 600;
    text-align: center;
}

/* About Section */
.about-text-mt {
    margin-top: 1rem;
}

.about-stats-single {
    grid-template-columns: 1fr;
    max-width: 250px;
}

/* Certifications */
.certifications-section {
    margin-top: 3rem;
}

.cert-header-styled {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
}

.cert-icon-color {
    color: var(--primary-color);
}

.cert-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.cert-card {
    padding: 1.5rem;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    background: rgba(var(--nav-rgb), 0.3);
    transition: all 0.3s;
}

.cert-card h4 {
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
}

.cert-card h4 i {
    color: var(--primary-color);
    margin-right: 6px;
}

.cert-card p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.cert-link {
    color: var(--primary-color);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
}

/* Skill bar icon */
.skill-icon-mr {
    margin-right: 8px;
}

/* Projects Grid */
.projects-grid-layout {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
}

.project-card-clickable {
    cursor: pointer;
}

.project-meta-styled {
    margin-top: 1rem;
    border-top: 1px solid var(--border-color);
    padding-top: 1rem;
}

.project-star-info {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

.star-icon-gold {
    color: gold;
}

.project-view-link {
    color: var(--primary-color);
    font-size: 0.9rem;
}

/* Contact Section */
.contact-section-padded {
    padding: 100px 0;
}

.contact-container-grid {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 5%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: start;
}

.contact-label-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1rem;
}

.contact-label-line {
    width: 30px;
    height: 1px;
    background: var(--text-secondary);
}

.contact-label-text {
    color: var(--text-secondary);
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.contact-title {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-family: 'Space Grotesk', serif;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    line-height: 1.1;
}

.contact-intro {
    color: var(--text-secondary);
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 3rem;
}

.contact-info-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.contact-info-card {
    background: rgba(var(--primary-rgb), 0.03);
    border: 1px solid rgba(var(--primary-rgb), 0.1);
    padding: 1.5rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.contact-info-icon-wrap {
    width: 40px;
    height: 40px;
    background: rgba(var(--primary-rgb), 0.1);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.contact-info-icon {
    color: var(--text-secondary);
}

.contact-detail-label {
    color: var(--text-secondary);
    font-size: 0.75rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
}

.contact-detail-value {
    color: var(--text-primary);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    word-break: break-all;
}

/* Contact Form Right */
.contact-form-panel {
    background: var(--text-primary);
    border-radius: 20px;
    padding: 3rem;
    color: var(--dark-bg);
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
}

.contact-form-title {
    font-family: 'Space Grotesk', serif;
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
    color: var(--dark-bg);
}

.contact-form-subtitle {
    color: #64748b;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}

.form-row-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.form-field-group {
    margin-bottom: 1.5rem;
}

.form-field-group-lg {
    margin-bottom: 2rem;
}

.form-label {
    display: block;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 1px;
    color: #475569;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}

.form-input {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    outline: none;
    transition: border-color 0.3s;
    background: transparent;
    color: var(--dark-bg);
}

.form-textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    outline: none;
    transition: border-color 0.3s;
    resize: vertical;
    background: transparent;
    color: var(--dark-bg);
}

.form-submit-btn {
    width: 100%;
    padding: 1rem;
    border: none;
    border-radius: 8px;
    background: #1e293b;
    color: #ffffff;
    font-family: 'Outfit', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.3s;
}

#formStatusMessage {
    margin-top: 15px;
    font-size: 0.9rem;
    display: none;
    text-align: center;
    color: var(--dark-bg);
}

/* WhatsApp Modal Overrides */
.wa-modal-content-light {
    background: white !important;
    border: none;
    max-width: 320px;
    padding: 2rem;
}

.wa-close-dark {
    color: #333;
    top: 10px;
    right: 15px;
}

.wa-qr-center {
    text-align: center;
}

.wa-qr-img {
    width: 100%;
    max-width: 250px;
    margin-bottom: 1.5rem;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.wa-chat-link {
    display: block;
    text-decoration: none;
    width: 100%;
}

/* Responsive additions for contact */
@media (max-width: 1024px) {
    .contact-container-grid {
        grid-template-columns: 1fr;
    }
    .cert-grid {
        grid-template-columns: 1fr;
    }
    .form-row-2col {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .stats-grid {
        grid-template-columns: 1fr;
    }
    .projects-grid-layout {
        grid-template-columns: 1fr;
    }
}
"""

# Append new CSS
css += new_css

# Now build the new HTML with classes instead of inline styles
new_html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description"
        content="Madan Kumar S Portfolio - Cybersecurity Analyst &amp; ECE Engineer specializing in embedded systems, VLSI design, and cybersecurity.">
    <meta name="keywords"
        content="Madan Kumar S, Madan Kumar S, Cybersecurity Analyst, ECE Engineer, Portfolio, Embedded Systems, VLSI Design, Karnataka, India">
    <meta name="author" content="Madan Kumar S">
    <meta name="robots" content="index, follow">
    <title>Madan Kumar S | Cybersecurity Analyst &amp; ECE Engineer</title>

    <!-- Browser Profile Icon (Favicon) -->
    <link rel="icon" type="image/png" href="mk_dev_logo.png">
    <link rel="apple-touch-icon" href="mk_dev_logo.png">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Space+Grotesk:wght@400;600&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>

<body data-theme="light">
    <!-- Ambient Global Interactive Spotlight Glow -->
    <div class="mouse-glow" id="mouseGlow"></div>
    <canvas id="particleCanvas"></canvas>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">
                <span>◇</span>
                <span>MK.dev</span>
            </div>
            <ul class="menu">
                <li><a href="#home" class="link"><span class="link-title">Home</span></a></li>
                <li><a href="#about" class="link"><span class="link-title">About</span></a></li>
                <li><a href="#skills" class="link"><span class="link-title">Skills</span></a></li>
                <li><a href="#projects" class="link"><span class="link-title">IC Lobby</span></a></li>
                <li><a href="#contact" class="link"><span class="link-title">Contact</span></a></li>
            </ul>
            <div class="nav-actions">
                <button class="theme-toggle-btn" id="themeToggle"
                    title="Toggle Dark/Light Mode">☀️</button>
            </div>
        </div>
    </nav>

    <!-- Home Section -->
    <section id="home" class="container">
        <div class="left-section">

            <!-- Availability Badge -->
            <div class="availability-badge">
                <span class="availability-dot"></span>
                <span class="availability-text">Available for Internship
                    &amp; Opportunities</span>
            </div>

            <h1 class="name home-name">
                <br>Madan kumar S
            </h1>

            <p class="home-description">
                Second year B.E. student in Electronics &amp; Communication Engineering at Visvesvaraya Technological
                University, Bangalore. Specialising in VLSI design, embedded systems, and intelligent hardware
                solutions.
            </p>

            <div class="tags-container">
                <span class="skill-tag">VLSI Design</span>
                <span class="skill-tag">Embedded Systems</span>
                <span class="skill-tag">VTU Bangalore</span>
                <span class="skill-tag">PCB Design</span>
                <span class="skill-tag">IoT</span>
                <span class="skill-tag">Signal Processing</span>
                <span class="skill-tag">FPGA</span>
            </div>

            <div class="action-buttons action-buttons-row">
                <a href="#contact" class="btn btn-primary btn-link">
                    <i class="fas fa-phone-alt"></i> Get in Touch
                </a>
                <a href="#" download="Madan_Kumar_Resume.pdf" class="btn btn-secondary btn-outline">
                    <i class="fas fa-file-alt"></i> Download Resume
                </a>
                <a href="#about" class="btn btn-secondary btn-outline">
                    <i class="fas fa-eye"></i> View Full CV
                </a>
            </div>

            <div class="stats-grid">
                <div class="stat-block">
                    <div class="stat-number">8.6</div>
                    <div class="stat-desc">Current CGPA</div>
                </div>
                <div class="stat-block">
                    <div class="stat-number">6+</div>
                    <div class="stat-desc">Projects Built</div>
                </div>
                <div class="stat-block">
                    <div class="stat-number">4</div>
                    <div class="stat-desc">Years at VTU</div>
                </div>
            </div>
        </div>

        <div class="right-section">
            <div class="card hero-card">
                <!-- Hero Video Wrapper for 3D Particles -->
                <div class="hero-video-wrapper">
                    <div class="hero-video-inner">
                        <landing-main-particles-component theme="light" class="particles-component">
                            <div class="main-particles-component-section particles-section">
                                <div class="main-particles-container particles-container">
                                    <canvas id="threeCanvas"
                                        data-engine="three.js r180"></canvas>
                                </div>
                            </div>
                        </landing-main-particles-component>
                    </div>
                </div>

                <div class="card-header card-header-overlay">
                    <div class="card-title card-text-primary"><i class="fas fa-shield-alt icon-mr-8"></i> CyberSec</div>
                    <div class="card-corner card-text-primary">⌐</div>
                </div>
                <div class="card-content card-content-overlay">
                    <!-- Satellite Communication Network Orbit Wrapper -->
                    <div class="satellite-network-wrapper">

                        <!-- Orbit Rings -->
                        <div class="orbit-ring-dashed"></div>
                        <div class="orbit-ring-outer"></div>

                        <!-- Orbiting Satellite -->
                        <div class="orbiting-satellite-track">
                            <i class="fas fa-satellite orbiting-satellite-icon"></i>
                        </div>

                        <!-- Signal Waves (Communication Network) -->
                        <div class="signal-wave"></div>

                        <div class="profile-img-container profile-img-orbit">
                            <img src="madan AI.jpeg" alt="Madan kumar S Profile" class="profile-img profile-img-fit">
                        </div>
                    </div>

                    <div class="card-description card-description-center">
                        CyberSecurity &amp; Embedded Systems
                    </div>
                </div>
            </div>

            <div class="floating-dot dot-1"></div>
            <div class="floating-dot dot-2"></div>
            <div class="floating-dot dot-3"></div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about-section">
        <div class="about-container">
            <div class="about-header">
                <span class="section-prefix">// ABOUT_ME</span>
                <h2 class="section-title">Who Am I?</h2>
            </div>

            <div class="about-content">
                <div class="about-text">
                    <p>I'm <strong>Madan Kumar S</strong>, an Electronics &amp; Communication Engineering student at
                        <strong>VTU (Visvesvaraya Technological University)</strong>. My passion lies at the
                        intersection of hardware and security.
                    </p>
                    <p class="about-text-mt">From designing VLSI circuits to analyzing network vulnerabilities, I
                        bring a unique perspective that combines the precision of electronics engineering with the
                        strategic thinking of cybersecurity. I also develop web applications, making me a versatile
                        engineer who can work across the full technology stack.</p>
                </div>

                <div class="about-stats about-stats-single">
                    <div class="stat-card">
                        <div class="stat-value">19+</div>
                        <div class="stat-label">Projects</div>
                    </div>
                </div>

                <div class="expertise-grid">
                    <div class="expertise-item">
                        <div class="expertise-icon"><i class="fas fa-user-shield"></i></div>
                        <div class="expertise-title">Cybersecurity</div>
                        <div class="expertise-desc">Network security, penetration testing, cryptography, and
                            vulnerability assessment.</div>
                    </div>
                    <div class="expertise-item">
                        <div class="expertise-icon"><i class="fas fa-microchip"></i></div>
                        <div class="expertise-title">Electronics &amp; Communication</div>
                        <div class="expertise-desc">Embedded systems, VLSI design, microcontroller programming, and PCB
                            design.</div>
                    </div>
                    <div class="expertise-item">
                        <div class="expertise-icon"><i class="fas fa-laptop-code"></i></div>
                        <div class="expertise-title">Web Development</div>
                        <div class="expertise-desc">Full-stack development with modern frameworks, creating responsive
                            and secure applications.</div>
                    </div>
                </div>
            </div>

            <div class="certifications certifications-section">
                <div class="cert-header cert-header-styled">
                    <i class="fas fa-certificate cert-icon-color icon-mr-8"></i> Licenses
                    &amp; Certifications
                </div>

                <div class="cert-grid">
                    <!-- Certificate 1 -->
                    <div class="cert-card">
                        <h4>
                            <i class="fas fa-shield-alt"></i>
                            Cyber Security + Ethical Hacking</h4>
                        <p>Skill Intern</p>
                        <a href="certificate/skill%20intern.pdf" target="_blank" class="cert-link">Show
                            credential <i class="fas fa-external-link-alt icon-ml-4"></i></a>
                    </div>

                    <!-- Certificate 2 -->
                    <div class="cert-card">
                        <h4>
                            <i class="fas fa-microchip"></i>
                            Embedded Systems Specialization</h4>
                        <p>NIELET</p>
                        <a href="certificate/ebedded%20free%20cirtificte.pdf" target="_blank" class="cert-link">Show
                            credential <i class="fas fa-external-link-alt icon-ml-4"></i></a>
                    </div>

                    <!-- Certificate 3 -->
                    <div class="cert-card">
                        <h4>
                            <i class="fas fa-robot"></i>
                            Generative AI</h4>
                        <p>TCS iON</p>
                        <a href="https://www.linkedin.com/in/madankumar-s-3537b232a/details/certifications/"
                            target="_blank" rel="noopener" class="cert-link">Show
                            credential <i class="fas fa-external-link-alt icon-ml-4"></i></a>
                    </div>

                    <!-- Certificate 4 -->
                    <div class="cert-card">
                        <h4>
                            <i class="fas fa-network-wired"></i>
                            VLSI Design Workshop</h4>
                        <p>VTU</p>
                        <a href="https://www.linkedin.com/in/madankumar-s-3537b232a/details/certifications/"
                            target="_blank" rel="noopener" class="cert-link">Show
                            credential <i class="fas fa-external-link-alt icon-ml-4"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills-section">
        <div class="skills-container">
            <div class="skills-header">
                <span class="section-prefix">// TECHNICAL_ARSENAL</span>
                <h2 class="section-title">Technical Skills;</h2>
            </div>

            <div class="skills-tabs">
                <button class="tab-btn active" data-tab="cybersecurity"><i class="fas fa-shield-alt"></i>
                    Cybersecurity</button>
                <button class="tab-btn" data-tab="electronics"><i class="fas fa-microchip"></i> Electronics</button>
                <button class="tab-btn" data-tab="programming"><i class="fas fa-code"></i> Programming</button>
            </div>

            <div class="skills-content">
                <div class="tab-content active" id="cybersecurity">
                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i>
                                Network Security</span>
                            <span class="skill-percent">85%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="85%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i> Threat
                                Analysis</span>
                            <span class="skill-percent">82%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="82%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i>
                                Vulnerability Assessment</span>
                            <span class="skill-percent">80%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="80%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i>
                                Penetration Testing</span>
                            <span class="skill-percent">78%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="78%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i>
                                Cryptography</span>
                            <span class="skill-percent">75%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="75%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-shield-alt skill-icon-mr"></i>
                                Forensics</span>
                            <span class="skill-percent">70%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="70%"></div>
                        </div>
                    </div>
                </div>

                <div class="tab-content" id="electronics">

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-microchip skill-icon-mr"></i>
                                Embedded Systems</span>
                            <span class="skill-percent">85%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="85%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-microchip skill-icon-mr"></i>
                                Microcontrollers</span>
                            <span class="skill-percent">82%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="82%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-microchip skill-icon-mr"></i> PCB
                                Design</span>
                            <span class="skill-percent">78%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="78%"></div>
                        </div>
                    </div>

                </div>

                <div class="tab-content" id="programming">
                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fab fa-python skill-icon-mr"></i>
                                Python</span>
                            <span class="skill-percent">90%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="90%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-code skill-icon-mr"></i> C/C++</span>
                            <span class="skill-percent">88%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="88%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fas fa-code skill-icon-mr"></i>
                                Verilog/VHDL</span>
                            <span class="skill-percent">82%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="82%"></div>
                        </div>
                    </div>

                    <div class="skill-item">
                        <div class="skill-header">
                            <span class="skill-name"><i class="fab fa-html5 skill-icon-mr"></i> Web
                                Technologies</span>
                            <span class="skill-percent">80%</span>
                        </div>
                        <div class="skill-bar">
                            <div class="skill-fill" data-width="80%"></div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects-section">
        <div class="projects-container">
            <div class="projects-header">
                <span class="section-prefix">// IC_LOBBY</span>
                <h2 class="section-title">My Work( )</h2>
            </div>

            <div class="projects-grid projects-grid-layout">
                <div class="project-card project-card-clickable" onclick="window.open('https://github.com/madans0316-cmd/exammind-', '_blank')">
                    <div class="project-icon"><i class="fas fa-brain"></i></div>
                    <div class="project-title">exammind-</div>
                    <div class="project-category">AI Companion</div>
                    <p class="project-desc">🧠 AI-Powered Study Companion with Gemini 2.0 Flash &amp; Reinforcement
                        Learning.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 0</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>

                <div class="project-card project-card-clickable"
                    onclick="window.open('https://github.com/madans0316-cmd/food-product-scanner', '_blank')">
                    <div class="project-icon"><i class="fas fa-barcode"></i></div>
                    <div class="project-title">food-product-scanner</div>
                    <div class="project-category">Python Scanner</div>
                    <p class="project-desc">A scanner to extract and analyze nutritional properties from food products.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 1</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>

                <div class="project-card project-card-clickable"
                    onclick="window.open('https://github.com/madans0316-cmd/student-to-do-list', '_blank')">
                    <div class="project-icon"><i class="fas fa-tasks"></i></div>
                    <div class="project-title">student-to-do-list</div>
                    <div class="project-category">Web App</div>
                    <p class="project-desc">A responsive standard to-do list specialized for modern students.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 1</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>

                <div class="project-card project-card-clickable"
                    onclick="window.open('https://github.com/madans0316-cmd/decode-every-expression', '_blank')">
                    <div class="project-icon"><i class="fas fa-code"></i></div>
                    <div class="project-title">decode-every-expression</div>
                    <div class="project-category">Web App</div>
                    <p class="project-desc">A decoding utility built to analyze and decode programming expressions.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 1</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>

                <div class="project-card project-card-clickable"
                    onclick="window.open('https://github.com/madans0316-cmd/pulwama-memorial', '_blank')">
                    <div class="project-icon"><i class="fas fa-monument"></i></div>
                    <div class="project-title">pulwama-memorial</div>
                    <div class="project-category">Tribute Site</div>
                    <p class="project-desc">A memorial website offering a tribute to the Pulwama tragedy.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 1</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>

                <div class="project-card project-card-clickable"
                    onclick="window.open('https://github.com/madans0316-cmd/SK.TYLERING', '_blank')">
                    <div class="project-icon"><i class="fas fa-cut"></i></div>
                    <div class="project-title">SK.TYLERING</div>
                    <div class="project-category">Business Site</div>
                    <p class="project-desc">Website to showcase and manage tailoring services efficiently.</p>
                    <div class="project-meta project-meta-styled">
                        <span class="project-star-info"><i class="fas fa-star star-icon-gold"></i> 1</span>
                        <span class="project-view-link">View <i class="fas fa-external-link-alt"></i></span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section contact-section-padded">
        <div class="contact-container contact-container-grid">

            <!-- Left Side -->
            <div class="contact-left">
                <div class="contact-label-row">
                    <span class="contact-label-line"></span>
                    <span class="contact-label-text">Get in Touch</span>
                </div>
                <h2 class="contact-title">Let's Work Together</h2>
                <p class="contact-intro">
                    I am actively seeking internship roles, final year project collaborations, and graduate research
                    opportunities in VLSI, embedded systems, and hardware design. Let's discuss how my skills can add
                    value to your team.
                </p>

                <div class="contact-info-list">
                    <div class="contact-info-card">
                        <div class="contact-info-icon-wrap">
                            <i class="fas fa-envelope contact-info-icon"></i>
                        </div>
                        <div>
                            <div class="contact-detail-label">Email</div>
                            <div class="contact-detail-value">madans0316@gmail.com</div>
                        </div>
                    </div>

                    <div class="contact-info-card">
                        <div class="contact-info-icon-wrap">
                            <i class="fab fa-linkedin-in contact-info-icon"></i>
                        </div>
                        <div>
                            <div class="contact-detail-label">LinkedIn</div>
                            <div class="contact-detail-value">linkedin.com/in/madankumar-s-3537b232a</div>
                        </div>
                    </div>

                    <div class="contact-info-card">
                        <div class="contact-info-icon-wrap">
                            <i class="fab fa-github contact-info-icon"></i>
                        </div>
                        <div>
                            <div class="contact-detail-label">GitHub</div>
                            <div class="contact-detail-value">github.com/madans0316-cmd</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Side (Form) -->
            <div class="contact-right contact-form-panel">
                <h3 class="contact-form-title">Send a Message</h3>
                <p class="contact-form-subtitle">I'll respond within 24 hours.</p>

                <form class="contact-form" id="secureContactForm" action="https://formsubmit.co/madans0316@gmail.com"
                    method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_subject" value="New Portfolio Message!">
                    <input type="hidden" name="_template" value="box">

                    <div class="form-row-2col">
                        <div>
                            <label class="form-label" for="contact-name">Full Name</label>
                            <input type="text" name="name" id="contact-name" placeholder="Your name" required class="form-input">
                        </div>
                        <div>
                            <label class="form-label" for="contact-email">Email Address</label>
                            <input type="email" name="email" id="contact-email" placeholder="your@email.com" required class="form-input">
                        </div>
                    </div>

                    <div class="form-field-group">
                        <label class="form-label" for="contact-org">Organisation</label>
                        <input type="text" name="organisation" id="contact-org" placeholder="Company or University (optional)" class="form-input">
                    </div>

                    <div class="form-field-group">
                        <label class="form-label" for="contact-subject">Subject</label>
                        <input type="text" name="subject" id="contact-subject" placeholder="Internship / Project / Research" required class="form-input">
                    </div>

                    <div class="form-field-group-lg">
                        <label class="form-label" for="contact-message">Message</label>
                        <textarea name="message" id="contact-message" placeholder="Tell me about your opportunity..." rows="4" required class="form-textarea"></textarea>
                    </div>

                    <button type="submit" class="btn form-submit-btn">
                        Send Message
                    </button>
                    <p id="formStatusMessage"></p>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <p><i class="fas fa-code"></i> Designed &amp; Built by Madan Kumar &copy; 2026</p>
    </footer>

    <!-- WhatsApp QR Modal -->
    <div id="waModal" class="wa-modal">
        <div class="wa-modal-content wa-modal-content-light">
            <span class="close-wa-modal wa-close-dark" onclick="closeWhatsAppModal()">&times;</span>
            <div class="wa-qr-center">
                <img src="whatsapp-qr.jpeg" alt="WhatsApp QR Code" class="wa-qr-img">
                <a href="https://wa.me/919449887678" target="_blank" rel="noopener" class="btn btn-primary wa-chat-link"><i class="fab fa-whatsapp"></i> Chat on
                    WhatsApp</a>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="my.js"></script>

</body>

</html>"""

# Write the updated files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✅ Done! All inline styles extracted to styles.css and index.html updated.")
print(f"   - styles.css: {len(css)} bytes")
print(f"   - index.html: {len(new_html)} bytes")
