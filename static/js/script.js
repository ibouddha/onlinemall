// Smooth scroll for anchor links in the footer
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Animation for Featured Stores Section on Scroll
const featuredSection = document.querySelector('.featured-section');

window.addEventListener('scroll', () => {
    const sectionPos = featuredSection.getBoundingClientRect().top;
    const screenPos = window.innerHeight / 1.3;

    if (sectionPos < screenPos) {
        featuredSection.classList.add('animated');
    }
});
