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
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    initParticles() {
        this.particles = [];
        for (let i = 0; i < this.particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.3,
                vy: (Math.random() - 0.5) * 0.3,
                radius: Math.random() * 1.2 + 0.5,
                opacity: Math.random() * 0.6 + 0.2,
                color: Math.random() > 0.5 ? '#00D9FF' : '#00FF88',
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
                        color: Math.random() > 0.5 ? '#00D9FF' : '#00FF88'
                    });
                }
            }
        });
    }

    update() {
        this.particles.forEach(particle => {
            // Movement with slight randomness
            particle.x += particle.vx;
            particle.y += particle.vy;

            // Add slight drift
            particle.vx += (Math.random() - 0.5) * 0.02;
            particle.vy += (Math.random() - 0.5) * 0.02;

            // Bounce off walls
            if (particle.x < 0 || particle.x > this.canvas.width) {
                particle.vx *= -1;
                particle.x = Math.max(0, Math.min(this.canvas.width, particle.x));
            }
            if (particle.y < 0 || particle.y > this.canvas.height) {
                particle.vy *= -1;
                particle.y = Math.max(0, Math.min(this.canvas.height, particle.y));
            }

            // Mouse interaction - repel particles
            const dx = this.mouse.x - particle.x;
            const dy = this.mouse.y - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const minDistance = 120;

            if (distance < minDistance) {
                const angle = Math.atan2(dy, dx);
                particle.vx -= Math.cos(angle) * 0.3;
                particle.vy -= Math.sin(angle) * 0.3;
                particle.opacity = Math.min(1, particle.opacity + 0.1);
            } else {
                particle.opacity = Math.max(particle.originalOpacity, particle.opacity - 0.02);
            }

            // Damping
            particle.vx *= 0.98;
            particle.vy *= 0.98;

            // Speed limit
            const speed = Math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy);
            if (speed > 2) {
                particle.vx = (particle.vx / speed) * 2;
                particle.vy = (particle.vy / speed) * 2;
            }
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
        this.ctx.strokeStyle = '#00D9FF';
        this.ctx.lineWidth = 0.8;

        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const dx = this.particles[i].x - this.particles[j].x;
                const dy = this.particles[i].y - this.particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

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

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    // Initialize ParticleSystem first so we can refer to it
    const canvas = document.getElementById('particleCanvas');
    const particleSys = new ParticleSystem(canvas);

    // Theme setup
    const themeToggleBtn = document.getElementById('themeToggle');
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'light') {
        document.body.setAttribute('data-theme', 'light');
        if (themeToggleBtn) themeToggleBtn.innerText = '🌙';
        particleSys.updateThemeColors();
    } else {
        if (themeToggleBtn) themeToggleBtn.innerText = '☀️';
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.body.getAttribute('data-theme');
            if (currentTheme === 'light') {
                document.body.removeAttribute('data-theme');
                localStorage.setItem('theme', 'dark');
                themeToggleBtn.innerText = '☀️';
            } else {
                document.body.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
                themeToggleBtn.innerText = '🌙';
            }
            particleSys.updateThemeColors();
        });
    }

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
            // Remove active class from all buttons
            tabButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            // Hide all tab contents
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });

            // Show selected tab content
            const tabId = button.getAttribute('data-tab');
            const tabContent = document.getElementById(tabId);
            if (tabContent) {
                tabContent.classList.add('active');
            }
        });
    });

    // Animate skill bars on scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillFills = entry.target.querySelectorAll('.skill-fill');
                skillFills.forEach(fill => {
                    const width = fill.style.width;
                    fill.style.width = '0';
                    setTimeout(() => {
                        fill.style.width = width;
                    }, 100);
                });
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.skills-section').forEach(section => {
        observer.observe(section);
    });

    // Form submission
    const contactForm = document.getElementById('secureContactForm');
    const formStatus = document.getElementById('formStatusMessage');
    const submitBtn = document.getElementById('formSubmitBtn');

    if (contactForm) {
        window.sendToWhatsApp = async (e) => {
            e.preventDefault();

            // Extract the user inputted form values explicitly 
            const nameInput = contactForm.querySelector('[name="name"]').value;
            const emailInput = contactForm.querySelector('[name="email"]').value;
            const subInput = contactForm.querySelector('[name="subject"]').value;
            const txtInput = contactForm.querySelector('[name="message"]').value;

            // Simple validation check before running fetch
            if (!nameInput || !emailInput || !subInput || !txtInput) {
                formStatus.textContent = "Please fill out all the fields before sending!";
                formStatus.style.color = "#FF3366";
                formStatus.style.display = 'block';
                return;
            }

            const btnText = submitBtn.querySelector('.btn-text');
            const originalText = btnText.innerHTML;
            btnText.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;
            formStatus.style.display = 'none';

            try {
                // Background email processing using FormSubmit Protocol
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: new FormData(contactForm),
                    headers: { 'Accept': 'application/json' }
                });

                if (response.ok) {
                    // Instantly open the physical WhatsApp native app forwarding the pre-generated text over to the phone
                    const cleanMessage = `Hello Madan!\n\n*Name:* ${nameInput}\n*Email:* ${emailInput}\n*Subject:* ${subInput}\n\n*Message:* ${txtInput}`;
                    window.open(`https://wa.me/919449887678?text=${encodeURIComponent(cleanMessage)}`, '_blank');

                    contactForm.reset();
                    formStatus.innerHTML = `Success! Sent to both your 📧 Email & <i class='fab fa-whatsapp'></i> WhatsApp.`;
                    formStatus.style.color = "#00FF88";
                    formStatus.style.display = 'block';
                } else {
                    formStatus.textContent = "Oops! Temporary Email server connection drop. Try again.";
                    formStatus.style.color = "#FF3366";
                    formStatus.style.display = 'block';
                }
            } catch (error) {
                formStatus.textContent = "Network Error. Please check your signal and retry.";
                formStatus.style.color = "#FF3366";
                formStatus.style.display = 'block';
            }

            btnText.innerHTML = originalText;
            submitBtn.disabled = false;
        };

        // Ensure browser "enter" keys map directly to the function
        contactForm.addEventListener('submit', window.sendToWhatsApp);
    }

    // Add global scroll animations for a premium feel
    const fadeElements = document.querySelectorAll('.card, .stat-card, .expertise-item, .info-block, .project-card, .left-section > *, .certifications, .code-block');
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, (index % 5) * 100); // Stagger animations nicely grouped together
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

        for (let i = 0; i < particlesCount * 3; i++) {
            // Spread particles across a glowing sphere shape
            posArray[i] = (Math.random() - 0.5) * 4;
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        const material = new THREE.PointsMaterial({
            size: 0.025,
            color: 0x3279F9, // Deep blue palette-blue-600 to contrast against white board
            transparent: true,
            opacity: 0.85
        });

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

            // Auto rotation + gentle mouse interaction
            particlesMesh.rotation.y = elapsedTime * 0.15 + (mouseX * 1.5);
            particlesMesh.rotation.x = elapsedTime * 0.05 + (mouseY * 1.5);

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
window.openWhatsAppModal = function (e) {
    if (e) e.preventDefault();
    const modal = document.getElementById('waModal');
    if (modal) {
        modal.classList.add('active');
    }
};

window.closeWhatsAppModal = function () {
    const modal = document.getElementById('waModal');
    if (modal) {
        modal.classList.remove('active');
    }
};

// Close modal when clicking outside of it
window.addEventListener('click', function (e) {
    const modal = document.getElementById('waModal');
    if (e.target === modal) {
        closeWhatsAppModal();
    }
});
