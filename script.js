/* ==========================================================================
   ALEXFOLIO INTERACTION & ANIMATION SCRIPT
   Preet Pratap Singh Bhati Portfolio
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Dual Cursor System (Small Orange Dot + Large Blurred Glow + Grow on Hover)
  const cursorDot = document.getElementById('cursorDot');
  const cursorGlow = document.getElementById('cursorGlow');
  
  if (cursorDot && cursorGlow) {
    window.addEventListener('mousemove', (e) => {
      const posX = e.clientX;
      const posY = e.clientY;

      cursorDot.style.transform = `translate3d(${posX}px, ${posY}px, 0)`;
      cursorGlow.style.transform = `translate3d(${posX}px, ${posY}px, 0)`;
    });

    // Detect hover over interactive elements (cards, buttons, links) to grow cursor
    const interactiveElements = document.querySelectorAll('a, button, .glass-panel, input, textarea, .social-icon-btn, .pill');
    interactiveElements.forEach((el) => {
      el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
      el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });
  }

  // 2. Navbar Scroll Glassmorphism State
  const navbar = document.getElementById('navbar');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // ScrollSpy active link highlighting
    let current = '';
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // 3. Scroll Reveal Animation via IntersectionObserver
  const revealElements = document.querySelectorAll('.reveal-on-scroll');

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
    revealObserver.observe(el);
  });

  // 4. Slight Magnetic Attraction Pull + 3D Card Tilt Effect on Hover
  const tiltCards = document.querySelectorAll('.glass-panel:not(.no-hover):not(.no-tilt)');

  tiltCards.forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Calculate 3D tilt angles
      const rotateX = (y - centerY) / 28;
      const rotateY = (centerX - x) / 28;

      // Calculate magnetic pull offsets towards cursor
      const pullX = (x - centerX) / 25;
      const pullY = (y - centerY) / 25;

      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translate3d(${pullX}px, ${pullY - 4}px, 0)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translate3d(0, 0, 0)';
    });
  });

  // 5. Web3Forms Interactive Contact Form Submission Handler
  const contactForm = document.getElementById('contactForm');
  const formStatus = document.getElementById('formStatus');
  const submitBtn = document.getElementById('submitBtn');

  if (contactForm && submitBtn) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const originalBtnContent = submitBtn.innerHTML;

      // Show loading state
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<span>Transmitting Payload...</span> <i class="fa-solid fa-spinner fa-spin"></i>`;

      if (formStatus) {
        formStatus.style.display = 'block';
        formStatus.className = 'form-status-msg status-info';
        formStatus.innerHTML = `<i class="fa-solid fa-satellite-dish"></i> Encrypting and transmitting data stream...`;
      }

      const formData = new FormData(contactForm);
      const object = Object.fromEntries(formData);
      const json = JSON.stringify(object);

      try {
        const response = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: json
        });

        const result = await response.json();

        if (response.status === 200) {
          if (formStatus) {
            formStatus.className = 'form-status-msg status-success';
            formStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> Signal received successfully! I will get back to you shortly.`;
          }
          contactForm.reset();
        } else {
          if (formStatus) {
            formStatus.className = 'form-status-msg status-error';
            formStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Transmission Error: ${result.message || 'Unable to submit'}`;
          }
        }
      } catch (error) {
        if (formStatus) {
          formStatus.className = 'form-status-msg status-error';
          formStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Connection Lost: Unable to send message payload.`;
        }
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnContent;
        if (formStatus) {
          setTimeout(() => {
            formStatus.style.display = 'none';
          }, 6000);
        }
      }
    });
  }

});
