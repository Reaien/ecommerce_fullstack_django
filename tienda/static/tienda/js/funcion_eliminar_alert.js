function eliminarProducto(id) {
   Swal.fire({
    "title": "Confirmación",
    "text": "Esta acción no se puede deshacer",
    "icon": "question",
    "showCancelButton": true,
    "cancelButtonText": "Cancelar",
    "confirmButtonText": "Confirmar",
    "reverseButtons": true,
    "confirmButtonColor": "#dc3545"
   })
   .then(function(result){
        if(result.isConfirmed){
            window.location.href = "eliminar-producto/"+id
        }
   })
}