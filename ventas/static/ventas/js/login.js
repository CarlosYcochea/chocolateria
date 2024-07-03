document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const email = document.getElementById('typeEmailX').value;
    const password = document.getElementById('typePasswordX').value;

    if (!validateEmail(email)) {
        alert('Por favor, introduce un correo electrónico válido.');
        return;
    }

    if (password.trim() === '') {
        alert('Por favor, introduce tu contraseña.');
        return;
    }

    // If validation passes, you can submit the form or handle the login logic here
    alert('Inicio de sesión exitoso');
    // this.submit(); // Uncomment this line to submit the form
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
