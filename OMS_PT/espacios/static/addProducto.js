function actualizar_precio_lista(sumar, nombre, precio){
    var fila = document.getElementById('fila_'+nombre);

    //obtiene los campos de la fila
    var cantidad = fila.cells[1];
    var td_precio = fila.cells[2];

    if(sumar){
        //aumenta en 1 el campo de cantidad
        cantidad.textContent = parseFloat(cantidad.textContent) + 1.00;
    }else{
        //reduce en 1 el campo de cantidad
        cantidad.textContent = parseFloat(cantidad.textContent) - 1.00;
    }

    td_precio.textContent = precio * cantidad.textContent;
}


function actualizar_total(){
    var precio = document.getElementById("lbl_precio");
    precio.value = '0';

    var tabla = document.getElementById("body-table");

    //Recorre la tabla y suma todos los precios
    for (var i = 0, fila; fila = tabla.rows[i]; i++){
        precio.value = (parseFloat(precio.value) + parseFloat(fila.cells[2].textContent));
    }
}

function createDelete(t_campo, id, precio){
    var boton = document.createElement('button');
    boton.setAttribute('class', 'delete fa-solid fa-delete-left');
    boton.setAttribute('type', 'button');
    boton.onclick = function () {
        const fila = document.getElementById('fila_' + id);
        if(fila.cells[1].textContent > 1){
            actualizar_precio_lista(false, id, precio);
        }else{
            fila.remove();
        }
        
        actualizar_total();
    }
    t_campo.appendChild(boton);
}

function agregar_prod(id, nombre, precio) {
    if(!document.getElementById('fila_'+nombre)){
        //Crea fila y la agrega a la tabla
        var fila = document.createElement('tr');
        fila.setAttribute('id', 'fila_'+nombre);
        document.getElementById("body-table").appendChild(fila);
        //Agrega los datos a la fila
        var td_id = document.createElement('td');
        td_id.textContent = nombre;

        var td_cant = document.createElement('td');
        td_cant.textContent = 1;

        var td_precio = document.createElement('td');
        td_precio.textContent = precio;

        var td_borrar = document.createElement('td');
        createDelete(td_borrar, nombre, precio);

        fila.appendChild(td_id);
        fila.appendChild(td_cant);
        fila.appendChild(td_precio);
        fila.appendChild(td_borrar);

    }else{
        actualizar_precio_lista(true, nombre, precio);
    }

    actualizar_total();
    
    //Crea una lista para enviar en el formulario
    var lista_ul = document.getElementById('listaInput');
    var lista_li = document.createElement('li');
    var lista_input = document.createElement('input');
    lista_input.name = "productos";
    lista_input.setAttribute('value', id);

    lista_ul.appendChild(lista_li);
    lista_li.appendChild(lista_input);
};

