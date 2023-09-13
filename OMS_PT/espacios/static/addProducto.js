function actualizar_total(sumar, valor){
    var precio = document.getElementById("lbl_precio");
    if(sumar){
        precio.value = (parseFloat(precio.value) + parseFloat(valor));
    }else{
        precio.value = (parseFloat(precio.value) - parseFloat(valor));
    }
}

function createDelete(t_campo, id, precio){
    var boton = document.createElement('button');
    boton.setAttribute('class', 'delete fa-solid fa-delete-left');
    boton.onclick = function () {
        const elmnt = document.getElementById('fila_' + id);
        elmnt.remove();

        actualizar_total(false, precio);
    }
    t_campo.appendChild(boton);
}


function agregar_prod(nombre, precio) {
    var fila = document.createElement('tr');
    fila.setAttribute('id', 'fila_'+nombre)
    document.getElementById("body-table").appendChild(fila);

    var td_id = document.createElement('td');
    td_id.textContent = nombre;

    var td_precio = document.createElement('td');
    td_precio.textContent = precio;

    var td_borrar = document.createElement('td');
    createDelete(td_borrar, nombre, precio);

    fila.appendChild(td_id);
    fila.appendChild(td_precio);
    fila.appendChild(td_borrar);

    actualizar_total(true, precio);
};

