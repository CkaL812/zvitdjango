let visibleCount = 4;

function moveRight() {
    const container = document.getElementById("sliderContainer");
    const slides = container.children;

    if (slides.length > visibleCount) {
        const first = slides[0];
        first.style.transition = "opacity 0.6s ease";
        first.style.opacity = "0";
        setTimeout(() => {
            container.appendChild(first);
            first.style.transition = "none";
            first.style.opacity = "0";
            void first.offsetWidth; // перезапуск анімації
            first.style.transition = "opacity 0.6s ease";
            first.style.opacity = "1";
        }, 600);
    }
}

function moveLeft() {
    const container = document.getElementById("sliderContainer");
    const slides = container.children;

    if (slides.length > visibleCount) {
        const last = slides[slides.length - 1];
        last.style.transition = "opacity 0.6s ease";
        last.style.opacity = "0";
        setTimeout(() => {
            container.insertBefore(last, slides[0]);
            last.style.transition = "none";
            last.style.opacity = "0";
            void last.offsetWidth;
            last.style.transition = "opacity 0.6s ease";
            last.style.opacity = "1";
        }, 600);
    }
}
