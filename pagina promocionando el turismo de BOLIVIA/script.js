// Animación de scroll para las secciones
document.addEventListener("scroll", function() {
    const sections = document.querySelectorAll("section");
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            section.classList.add("visible");
        } else {
            section.classList.remove("visible");
        }
    });
});

// Función para mostrar descripción emergente al hacer clic en una imagen
const images = document.querySelectorAll(".carousel img");
images.forEach(image => {
    image.addEventListener("click", function() {
        const description = document.createElement("div");
        description.classList.add("description-popup");
        description.innerText = `Este es el plato ${image.alt}`;
        document.body.appendChild(description);

        // Posición de la descripción emergente
        description.style.left = `${event.pageX}px`;
        description.style.top = `${event.pageY}px`;

        // Eliminar la descripción emergente después de 3 segundos
        setTimeout(() => {
            description.remove();
        }, 3000);
    });
});

// Carrusel manual con botones de control
const carousels = document.querySelectorAll(".carousel");
carousels.forEach(carousel => {
    let currentIndex = 0;
    const carouselInner = carousel.querySelector(".carousel-inner");
    const images = carouselInner.querySelectorAll("img");

    // Crear botones para controlar el carrusel
    const prevButton = document.createElement("button");
    prevButton.classList.add("carousel-control", "prev");
    prevButton.innerText = "<";
    carousel.appendChild(prevButton);

    const nextButton = document.createElement("button");
    nextButton.classList.add("carousel-control", "next");
    nextButton.innerText = ">";
    carousel.appendChild(nextButton);

    // Función para actualizar la posición del carrusel
    function updateCarousel() {
        carouselInner.style.transform = `translateX(-${currentIndex * 300}px)`;
    }

    // Eventos de clic para los botones
    prevButton.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateCarousel();
    });

    nextButton.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateCarousel();
    });
});
