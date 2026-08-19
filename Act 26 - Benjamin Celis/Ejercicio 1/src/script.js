/*
Ejercicio 01: Modificación del DOM con Métodos de Selección
Enunciado: Crear un programa que, al hacer clic en un botón, cambie el contenido de
un párrafo en la página utilizando los métodos para acceder al DOM. Los pasos
específicos son:
1. Al cargar la página, se debe mostrar un párrafo con el texto: Texto inicial".
2. Al hacer clic en un botón, se debe cambiar ese texto por: "El texto ha sido
modificado con JavaScript".
3. Usar getElementById() para seleccionar el párrafo y modificar su contenido con
textContent
*/
function cambiarTexto() {
    let parrafo = document.getElementById("parrafo");
    parrafo.textContent = "El texto ha sido modificado con JavaScript";
}