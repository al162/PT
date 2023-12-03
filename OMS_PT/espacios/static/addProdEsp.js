const cont = 0;

function agregar_prod(){
    var fila = document.createElement('tr');
    document.getElementById('body-table').appendChild(fila);

    var td_nombre = document.createElement('td');
    td_nombre.textContent = document.getElementsByName("nombre_prod")
    
}

function alerta(){
    alert('Productos enviados')
}