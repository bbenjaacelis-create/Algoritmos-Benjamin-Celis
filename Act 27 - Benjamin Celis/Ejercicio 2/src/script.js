/* 
Cargar un nombre y un apellido en dos text. Al presionar un botón,
concatenarlos y mostrarlos en un tercer text (Tener en cuenta que
podemos modificar la propiedad value de un objeto TEXT cuando ocurre
un evento).
*/
function mostrar(){
    let nom = document.getElementById("nombre").value;
    let ape = document.getElementById("apellido").value;
    document.getElementById("text3").textContent = `${nom} ${ape}`;
}
mostrar()