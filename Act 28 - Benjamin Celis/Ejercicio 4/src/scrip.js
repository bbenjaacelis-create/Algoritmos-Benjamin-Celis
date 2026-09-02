/*
Modificar el segundo problema resuelto de los ejemplos de la sección “Eventos
onMouseOver y onMouseOut.” Del material 11. (las casillas de la tabla que cambian el
color cuando ingresamos con el mouse) para permitir llamar mediante hipervínculos a
distintos programas que administran web-mail (Gmail, Hotmail y Yahoo!)
*/
function pintar(objeto, col) {
    objeto.style.backgroundColor = col;
}

function link(url) {
    location = url;
}