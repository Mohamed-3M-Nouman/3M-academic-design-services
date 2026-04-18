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

// Image Modal / Lightbox Logic
const imageModal = document.getElementById('imageModal');
const modalImage = document.getElementById('modalImage');
const modalCaption = document.getElementById('modalCaption');
const closeModal = document.getElementById('closeModal');
const galleryItems = document.querySelectorAll('.gallery-item');

if (imageModal && modalImage && closeModal) {
    const openModal = (src, caption) => {
        modalImage.src = src;
        modalCaption.textContent = caption;
        
        // Show modal and fade in
        imageModal.classList.remove('hidden');
        imageModal.classList.add('flex');
        
        // Use a small timeout to allow layout to happen before applying opacity for transition
        setTimeout(() => {
            imageModal.classList.remove('opacity-0', 'pointer-events-none');
            imageModal.classList.add('opacity-100', 'pointer-events-auto');
            modalImage.classList.remove('scale-95');
            modalImage.classList.add('scale-100');
        }, 10);
        
        // Prevent body scroll
        document.body.style.overflow = 'hidden';
    };

    const hideModal = () => {
        // Fade out
        imageModal.classList.remove('opacity-100', 'pointer-events-auto');
        imageModal.classList.add('opacity-0', 'pointer-events-none');
        modalImage.classList.remove('scale-100');
        modalImage.classList.add('scale-95');
        
        // Hide after transition
        setTimeout(() => {
            imageModal.classList.remove('flex');
            imageModal.classList.add('hidden');
            modalImage.src = ''; // Clear source to prevent ghost flashes
            document.body.style.overflow = ''; // Restore scroll
        }, 300);
    };

    // Attach click events to gallery items
    galleryItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault(); // Prevents iOS hover bug
            const src = this.getAttribute('data-img-src');
            const caption = this.getAttribute('data-caption');
            if(src) openModal(src, caption);
        });
    });

    // Close on button click
    closeModal.addEventListener('click', (e) => {
        e.preventDefault();
        hideModal();
    });

    // Close on click outside the image
    imageModal.addEventListener('click', (e) => {
        // If clicking strictly on the background/overlay, not the image
        if (e.target === imageModal || e.target.parentElement === imageModal && e.target !== modalImage) {
            hideModal();
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !imageModal.classList.contains('hidden')) {
            hideModal();
        }
    });
}
