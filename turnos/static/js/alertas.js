document.addEventListener("DOMContentLoaded", function(event) {
});

function alertaTurno(){
    swal({
        title: "Atención",
        text: "Uno o varios invitados no se encuentran registrados, por lo tanto no pueden asistir al turno.",
        icon: "warning",
        button: "Comprendo",
      });
}

function turnoCreado(){
  swal({
    title: "Completado",
    text: "Su turno ha sido registrado con éxito.",
    icon: "success",
    button: "Ok!",
  });
}