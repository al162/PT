function searchMesa(){
    if(document.getElementById('mesa_conf')){
        document.getElementById('mesa_conf').remove();
    }
    id = document.createElement('input');
    lista_mesas = document.getElementById('listaMesas');

    id.setAttribute('id', "mesa_conf");
    id.setAttribute('name', 'mesa_id');
    id.setAttribute('value', lista_mesas.options[lista_mesas.selectedIndex].value);
    id.setAttribute('type', 'hidden');

    form_reserva = document.getElementById('form_reserva');
    form_reserva.appendChild(id);
    
    document.getElementById("crear").removeAttribute('disabled');
}
    