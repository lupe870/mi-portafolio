// Menú de navegación dinámico
document.getElementById('mobile-menu').addEventListener('click', function() {
    const navList = document.getElementById('nav-list');
    navList.classList.toggle('active');
});

// Carrusel de imágenes
let currentSlide = 0;

function showSlide(index) {
    const slides = document.getElementsByClassName('slide');
    if (index >= slides.length) currentSlide = 0;
    else if (index < 0) currentSlide = slides.length - 1;
    else currentSlide = index;

    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove('active');
    }
    slides[currentSlide].classList.add('active');
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

// Cargar contenido dinámico desde un archivo JSON
fetch('projects.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const projectsSection = document.getElementById('projects');
        const carousel = projectsSection.querySelector('.carousel');

        data.projects.forEach(project => {
            const div = document.createElement('div');
            div.className = 'slide';
            div.innerHTML = `
                <img src="${project.image}" alt="${project.title}">
                <h3>${project.title}</h3>
                <p>${project.description}</p>
            `;
            carousel.appendChild(div);
        });

        showSlide(0); // Mostrar la primera imagen del carrusel
    })
    .catch(error => console.error('Error al cargar los proyectos:', error));

// Desplazamiento automático de las imágenes
setInterval(() => {
    changeSlide(1); // Cambiar a la siguiente imagen
}, 5000); // Cambiar cada 5 segundos

// Validación del formulario de contacto
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name === '' || email === '' || message === '') {
        alert('Todos los campos son obligatorios');
        return;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        alert('Por favor ingresa un correo electrónico válido');
        return;
    }

    alert('Formulario enviado correctamente');
    this.reset();
});
