var lista = document.querySelectorAll('.nav li');
function activarLink(){
    lista.forEach((item) =>
        item.classList.remove('active'));
    this.classList.add('active');
}
lista.forEach((item) =>
    item.addEventListener('mouseover', activarLink));

var toggle = document.querySelector('.toggle');
var nav = document.querySelector('.nav');
var container = document.querySelector('.container');

toggle.onclick = function() {
    nav.classList.toggle('active');
    container.classList.toggle('active');
}

$(document).ready(function() {
    $('#formulario-cliente').on('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma tradicional

        // Obtén los valores de los campos del formulario
        var nombre = $('#Nombre').val();
        var rut = $('#Rut').val();
        var email = $('#Email').val();
        var telefono = $('#telefono').val();
        var direccion = $('#direccion').val();

        // Agrega una nueva fila a la tabla con los datos proporcionados por el usuario
        var nuevaFila = `
            <tr>
                <td>${nombre}</td>
                <td>${rut}</td>
                <td>${email}</td>
                <td>${telefono}</td>
                <td>${direccion}</td>
            </tr>
        `;
        $('.tabla-clientes tbody').append(nuevaFila);

        // Limpia los campos del formulario
        $('#formulario-cliente')[0].reset();
    });
});





    