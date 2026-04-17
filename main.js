// Set current year
const yearSpan = document.getElementById('current-year');
if(yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
}

// Mobile menu toggle
const btn = document.getElementById('mobile-menu-button');
const menu = document.getElementById('mobile-menu');

if(btn && menu) {
    btn.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });

    const mobileLinks = menu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.add('hidden');
        });
    });
}

// Navbar blur
const navbar = document.querySelector('nav');
if(navbar) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('shadow-md', 'bg-white/95');
            navbar.classList.remove('shadow-sm', 'bg-white/90');
        } else {
            navbar.classList.remove('shadow-md', 'bg-white/95');
            navbar.classList.add('shadow-sm', 'bg-white/90');
        }
    });
}

// Before/After Image Slider Logic (RTL optimized inside LTR container)
const compareSlider = document.getElementById('compareSlider');
const afterImage = document.getElementById('afterImage');
const sliderButton = document.getElementById('sliderButton');

if (compareSlider && afterImage && sliderButton) {
    function updateSliderProgress(val) {
        const clipRight = 100 - val;
        afterImage.style.clipPath = `inset(0 ${clipRight}% 0 0)`;
        sliderButton.style.left = `${val}%`;
    }

    // Initialize display
    updateSliderProgress(compareSlider.value);

    // Update on user drag
    compareSlider.addEventListener('input', (e) => {
        updateSliderProgress(e.target.value);
    });
}
