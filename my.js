// Particle Animation System
class ParticleSystem {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.particles = [];
        this.particleCount = 120;
        this.mouse = { x: 0, y: 0 };
        this.connectionDistance = 150;
        this.themeColors = { bgRgb: '5, 8, 18' };
        this.cursorDots = [];

        this.updateThemeColors();
        this.resizeCanvas();
        this.initParticles();
        this.setupEventListeners();
        this.animate();
    }

    updateThemeColors() {
        // Use document.body since that's where [data-theme="light"] is applied
        const target = document.body || document.documentElement;
        const computed = getComputedStyle(target);
        this.themeColors.bgRgb = computed.getPropertyValue('--bg-rgb').trim() || '5, 8, 18';
        
        const isLight = document.body?.dataset.theme === 'light';
        this.connectionColor = isLight ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.4)';
        
        if (this.particles) {
            this.particles.forEach(p => {
                p.color = isLight ? '#000000' : '#ffffff';
            });
        }
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    initParticles() {
        this.particles = [];
        const isLight = document.body?.dataset.theme === 'light';
        for (let i = 0; i < this.particleCount; i++) {
            const angle = Math.random() * Math.PI * 2;
            const radius = Math.random() * (Math.max(window.innerWidth, window.innerHeight) / 1.5) + 50;
            this.particles.push({
                angle: angle,
                orbitRadius: radius,
                orbitSpeed: (Math.random() * 0.0015) + 0.0005,
                x: (window.innerWidth / 2) + Math.cos(angle) * radius,
                y: (window.innerHeight / 2) + Math.sin(angle) * radius,
                vx: 0,
                vy: 0,
                radius: Math.random() * 1.5 + 0.5,
                opacity: Math.random() * 0.6 + 0.2,
                color: isLight ? '#000000' : '#ffffff',
                originalOpacity: Math.random() * 0.6 + 0.2
            });
        }
    }

    setupEventListeners() {
        window.addEventListener('resize', () => this.resizeCanvas());
        document.addEventListener('mousemove', (e) => {
            const distance = Math.hypot(e.clientX - this.mouse.x, e.clientY - this.mouse.y);
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;

            // Add futuristic pop-up dots when cursor moves
            if (distance > 1) {
                const dotCount = Math.min(Math.floor(distance / 5) + 1, 3);
                for (let i = 0; i < dotCount; i++) {
                    this.cursorDots.push({
                        x: this.mouse.x + (Math.random() - 0.5) * 15,
                        y: this.mouse.y + (Math.random() - 0.5) * 15,
                        vx: (Math.random() - 0.5) * 1.5,
                        vy: (Math.random() - 0.5) * 1.5,
                        size: Math.random() * 2 + 1.5,
                        life: 1,
                        color: document.body?.dataset.theme === 'light' ? '#000000' : '#ffffff'
                    });
                }
            }
        });
    }

    update() {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;

        this.particles.forEach(particle => {
            // Orbiting math
            particle.angle += particle.orbitSpeed;
            
            // Add a little wobble for the swimming effect
            const wobble = Math.sin(particle.angle * 6) * 5;

            particle.x = centerX + Math.cos(particle.angle) * (particle.orbitRadius + wobble) + particle.vx;
            particle.y = centerY + Math.sin(particle.angle) * (particle.orbitRadius + wobble) + particle.vy;

            // Mouse interaction - repel particles
            const dx = this.mouse.x - particle.x;
            const dy = this.mouse.y - particle.y;
            const distance = Math.hypot(dx, dy);
            const minDistance = 150;

            if (distance < minDistance) {
                const angle = Math.atan2(dy, dx);
                particle.vx -= Math.cos(angle) * 1.5;
                particle.vy -= Math.sin(angle) * 1.5;
                particle.opacity = Math.min(1, particle.opacity + 0.3);
            } else {
                particle.opacity = Math.max(particle.originalOpacity, particle.opacity - 0.015);
            }

            // Damping for mouse repulsion
            particle.vx *= 0.92;
            particle.vy *= 0.92;
        });

        // Update cursor dots
        for (let i = this.cursorDots.length - 1; i >= 0; i--) {
            let dot = this.cursorDots[i];
            dot.x += dot.vx;
            dot.y += dot.vy;
            dot.life -= 0.03; // Fade speed
            dot.size *= 0.92; // Shrink speed

            if (dot.life <= 0 || dot.size <= 0.2) {
                this.cursorDots.splice(i, 1);
            }
        }
    }

    draw() {
        const bgRgb = this.themeColors.bgRgb;

        // Clear canvas with fade effect
        this.ctx.fillStyle = `rgba(${bgRgb}, 0.15)`;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw connections between nearby particles
        this.ctx.globalAlpha = 0.08;
        this.ctx.strokeStyle = this.connectionColor || '#00D9FF';
        this.ctx.lineWidth = 0.8;

        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.hypot(dx, dy);

                if (distance < this.connectionDistance) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
                    this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
                    this.ctx.stroke();
                }
            }
        }

        // Draw particles
        this.particles.forEach(particle => {
            this.ctx.fillStyle = particle.color;
            this.ctx.globalAlpha = particle.opacity;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fill();

            // Glow effect
            this.ctx.strokeStyle = particle.color;
            this.ctx.lineWidth = 0.5;
            this.ctx.globalAlpha = particle.opacity * 0.3;
            this.ctx.stroke();
        });

        // Draw cursor dots
        this.cursorDots.forEach(dot => {
            this.ctx.fillStyle = dot.color;
            this.ctx.globalAlpha = dot.life;
            this.ctx.beginPath();
            this.ctx.arc(dot.x, dot.y, dot.size, 0, Math.PI * 2);

            // Add subtle glow to cursor dots
            this.ctx.shadowBlur = 10;
            this.ctx.shadowColor = dot.color;
            this.ctx.fill();
            this.ctx.shadowBlur = 0; // reset
        });

        this.ctx.globalAlpha = 1;
    }

    animate() {
        this.update();
        this.draw();
        requestAnimationFrame(() => this.animate());
    }
}

// Theme initialization
function initTheme(particleSys) {
    const themeToggleBtn = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('theme') || 'light';

    if (savedTheme === 'light') {
        document.body.dataset.theme = 'light';
        if (themeToggleBtn) themeToggleBtn.innerText = '🌙';
        particleSys.updateThemeColors();
    } else {
        delete document.body.dataset.theme;
        if (themeToggleBtn) themeToggleBtn.innerText = '☀️';
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.body.dataset.theme;
            if (currentTheme === 'light') {
                delete document.body.dataset.theme;
                localStorage.setItem('theme', 'dark');
                themeToggleBtn.innerText = '☀️';
            } else {
                document.body.dataset.theme = 'light';
                localStorage.setItem('theme', 'light');
                themeToggleBtn.innerText = '🌙';
            }
            particleSys.updateThemeColors();
        });
    }
}

// Form submission handler — sends email via FormSubmit.co + WhatsApp notification
function initFormSubmission() {
    const contactForm = document.getElementById('secureContactForm');
    const formStatus = document.getElementById('formStatusMessage');
    const submitBtn = document.getElementById('formSubmitBtn');

    if (!contactForm) return;

    // Private contact — not rendered in UI
    const _p = ['91', '9449', '887678'].join('');

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        const nameInput  = contactForm.querySelector('[name="name"]').value.trim();
        const emailInput = contactForm.querySelector('[name="email"]').value.trim();
        const subInput   = contactForm.querySelector('[name="subject"]').value.trim();
        const txtInput   = contactForm.querySelector('[name="message"]').value.trim();

        if (!nameInput || !emailInput || !subInput || !txtInput) {
            showStatus('⚠️ Please fill out all required fields before sending!', '#c0392b');
            return;
        }

        // Dynamically set _replyto so FormSubmit can auto-reply to the sender
        const replyToField = document.getElementById('_replyto_field');
        if (replyToField) replyToField.value = emailInput;

        // Loading state
        const btnText = submitBtn.querySelector('.btn-text');
        const originalHTML = btnText.innerHTML;
        btnText.innerHTML = 'Sending… <i class="fas fa-spinner fa-spin"></i>';
        submitBtn.disabled = true;
        formStatus.style.display = 'none';

        try {
            const formData = new FormData(contactForm);
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            });

            if (response.ok) {
                contactForm.reset();

                // Send WhatsApp notification to private contact
                const waMsg = `📬 New Portfolio Message\n\n👤 Name: ${nameInput}\n📧 Email: ${emailInput}\n📌 Subject: ${subInput}\n\n💬 Message:\n${txtInput}`;
                const waUrl = `https://wa.me/${_p}?text=${encodeURIComponent(waMsg)}`;
                const waWin = window.open(waUrl, '_blank', 'noopener,noreferrer');
                if (waWin) setTimeout(() => waWin.close(), 3000);

                showStatus(
                    '✅ Message delivered! I\'ll respond to <strong>' + emailInput + '</strong> within 24 hours.',
                    '#1a7a4a'
                );
            } else {
                const data = await response.json().catch(() => ({}));
                const msg = data?.errors?.[0]?.message || 'Server error — please try again shortly.';
                showStatus('❌ ' + msg, '#c0392b');
            }
        } catch (err) {
            console.error('Contact form error:', err);
            showStatus('❌ Network error. Check your connection and retry.', '#c0392b');
        }

        btnText.innerHTML = originalHTML;
        submitBtn.disabled = false;
    };

    function showStatus(html, color) {
        formStatus.innerHTML = html;
        formStatus.style.color = color;
        formStatus.style.display = 'block';
        formStatus.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    contactForm.addEventListener('submit', handleFormSubmit);
}

// Initialize on page load
globalThis.addEventListener('DOMContentLoaded', () => {
    // Initialize ParticleSystem first so we can refer to it
    const canvas = document.getElementById('particleCanvas');
    const particleSys = new ParticleSystem(canvas);

    initTheme(particleSys);

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Tab switching for skills
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });

            const tabId = button.dataset.tab;
            const tabContent = document.getElementById(tabId);
            if (tabContent) {
                tabContent.classList.add('active');
            }
        });
    });

    // Animate skill bars on scroll handled by global fade elements below

    initFormSubmission();

    // Skills Sections Expansion Toggle (Mobile Only)
    const viewMoreBtn = document.getElementById('viewMoreSkillsBtn');
    const skillsContent = document.querySelector('.skills-content');
    if (viewMoreBtn && skillsContent) {
        viewMoreBtn.addEventListener('click', () => {
            const isExpanded = skillsContent.classList.toggle('expanded');
            viewMoreBtn.classList.toggle('active');
            
            if (isExpanded) {
                viewMoreBtn.innerHTML = `View Less <i class="fas fa-chevron-up"></i>`;
            } else {
                viewMoreBtn.innerHTML = `View More Skills <i class="fas fa-chevron-down"></i>`;
            }
        });
    }

    // Interactive Hero Tags (Mobile Only)
    document.querySelectorAll('.hero-tag').forEach(tag => {
        tag.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                // Toggle active state for "expand" effect
                this.classList.toggle('active');
                if (navigator.vibrate) navigator.vibrate(20);
            }
        });
    });

    // Add global scroll animations for a premium feel
    const fadeElements = document.querySelectorAll('.card, .stat-card, .expertise-item, .info-block, .project-card, .left-section > *, .certifications, .code-block, .skill-tab-item');
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    
                    // After the transition ends, remove the inline transform so CSS hovers work
                    setTimeout(() => {
                        entry.target.style.transform = '';
                    }, 650);
                }, (index % 5) * 80); // Stagger animations nicely grouped together
                fadeObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    fadeElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s cubic-bezier(0.25, 1, 0.5, 1)';
        fadeObserver.observe(el);
    });

    // Interactive Premium Hover Tilt for Content Cards
    document.querySelectorAll('.project-card, .expertise-item, .stat-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -6; // Up/down tilt
            const rotateY = ((x - centerX) / centerX) * 6;  // Left/right tilt

            // Determine correct slide distance from CSS rules
            const slideDistance = card.classList.contains('project-card') ? -8 : -5;
            
            // Apply 3D rotate with a slight pop-out scale AND the CSS slide-up effect
            card.style.transform = `perspective(1000px) translateY(${slideDistance}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            card.style.zIndex = '10';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transition = 'all 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
            card.style.transform = `perspective(1000px) translateY(0px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            card.style.zIndex = '1';
            
            // Clean up inline transform after animation finishes so normal CSS hovers work if needed
            setTimeout(() => {
                if (!card.matches(':hover')) {
                    card.style.transform = '';
                    card.style.zIndex = '';
                }
            }, 500);
        });

        card.addEventListener('mouseenter', () => {
            card.style.transition = 'none'; // Instant tracking while mouse is moving inside
        });
    });

    // Three.js 3D Particles Effect for CyberSec Card
    const threeCanvas = document.getElementById('threeCanvas');
    if (threeCanvas && typeof THREE !== 'undefined') {
        const container = threeCanvas.parentElement;
        let tWidth = container.offsetWidth;
        let tHeight = container.offsetHeight;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, tWidth / tHeight, 0.1, 1000);

        const renderer = new THREE.WebGLRenderer({ canvas: threeCanvas, alpha: true, antialias: true });
        renderer.setSize(tWidth, tHeight);
        renderer.setPixelRatio(window.devicePixelRatio);

        // Create Particles
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 900;
        const posArray = new Float32Array(particlesCount * 3);

        for (let i = 0; i < particlesCount; i++) {
            // Create a space galaxy spinning disc
            const r = (Math.random() * 2.5) + (Math.random() * 2.5); // Density towards center
            const theta = r * 3 + (Math.random() * Math.PI * 2);
            
            // Add a bit of vertical spread (thicker at center, thinner at edges)
            const ySpread = (1 - (Math.min(r, 2.5) / 2.5)) * (Math.random() - 0.5) * 1.2;

            posArray[i * 3] = (r / 2) * Math.cos(theta);         // x
            posArray[i * 3 + 1] = ySpread;                       // y
            posArray[i * 3 + 2] = (r / 2) * Math.sin(theta);     // z
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        const isLight = document.body?.dataset.theme === 'light';
        const material = new THREE.PointsMaterial({
            size: 0.035,
            color: isLight ? 0x000000 : 0xffffff,
            transparent: true,
            opacity: 0.9,
            sizeAttenuation: true
        });
        globalThis.threeMaterial = material;

        const particlesMesh = new THREE.Points(particlesGeometry, material);
        scene.add(particlesMesh);
        camera.position.z = 2.5;

        // Interactive Mouse Movement Logging
        let mouseX = 0;
        let mouseY = 0;
        const cyberSecCard = document.querySelector('.right-section .card');

        if (cyberSecCard) {
            cyberSecCard.addEventListener('mousemove', (event) => {
                const rect = cyberSecCard.getBoundingClientRect();
                mouseX = ((event.clientX - rect.left) / rect.width - 0.5);
                mouseY = ((event.clientY - rect.top) / rect.height - 0.5);
            });
            cyberSecCard.addEventListener('mouseleave', () => {
                mouseX = 0;
                mouseY = 0;
            });
        }

        const clock = new THREE.Clock();

        // Render Loop
        const animate = () => {
            requestAnimationFrame(animate);
            const elapsedTime = clock.getElapsedTime();

            // Auto rotation + gentle mouse interaction + breathing effect
            particlesMesh.rotation.y = elapsedTime * 0.15 + (mouseX * 1.5);
            particlesMesh.rotation.x = elapsedTime * 0.05 + (mouseY * 1.5);
            particlesMesh.position.y = Math.sin(elapsedTime * 0.5) * 0.15; // Smooth breathing

            renderer.render(scene, camera);
        };

        // Wait momentarily to ensure DOM has painted dimensions accurately
        setTimeout(() => {
            tWidth = container.offsetWidth;
            tHeight = container.offsetHeight;
            camera.aspect = tWidth / tHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(tWidth, tHeight);
            animate();
        }, 100);

        // Adjust 3D canvas accurately on window resize
        window.addEventListener('resize', () => {
            if (!container) return;
            tWidth = container.offsetWidth;
            tHeight = container.offsetHeight;
            camera.aspect = tWidth / tHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(tWidth, tHeight);
        });
    }
});

// Developer Console Easter Egg
console.log(
    "%c◇ MK.dev %c| System Initialized",
    "color: #00D9FF; font-size: 24px; font-weight: bold; text-shadow: 0 0 10px #00D9FF;",
    "color: #00FF88; font-size: 16px; font-style: italic;"
);
console.log(
    "%c> Welcome to Madan Kumar S's Portfolio\n> Specialization: Cybersecurity & Embedded Systems\n> Status: Secure connection established.\n> Explore the source, but respect the cyber-defenses. 🛡️",
    "color: #a0a0a0; font-family: monospace; font-size: 14px; line-height: 1.5;"
);

// WhatsApp Modal Controls
globalThis.openWhatsAppModal = function (e) {
    if (e) e.preventDefault();
    const modal = document.getElementById('waModal');
    if (modal) {
        modal.classList.add('active');
    }
};

globalThis.closeWhatsAppModal = function () {
    const modal = document.getElementById('waModal');
    if (modal) {
        modal.classList.remove('active');
    }
};

// Close modal when clicking outside of it
globalThis.addEventListener('click', function (e) {
    const modal = document.getElementById('waModal');
    if (e.target === modal) {
        closeWhatsAppModal();
    }
});

// Premium Mouse Spotlight & Glow Engine
document.addEventListener('DOMContentLoaded', () => {
    const mouseGlow = document.getElementById('mouseGlow');

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    document.addEventListener('mousemove', (e) => {
        // Render Global Spotlight Aura
        if (mouseGlow) {
            mouseGlow.style.left = `${e.clientX}px`;
            mouseGlow.style.top = `${e.clientY}px`;
        }

        // Render localized Hover Border/Glow on Cards
        const glowCards = document.querySelectorAll('.project-card, .expertise-item, .card');
        glowCards.forEach(card => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--x', `${x}px`);
            card.style.setProperty('--y', `${y}px`);
        });
    });
});
