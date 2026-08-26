/*
Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.
*/
function Verificar(){
    let c1 = document.getElementById("clave").value;
    let c2 = document.getElementById("clave1").value;
    if (c1==c2){
        alert("Sus contraseñas son iguales")
    }
    else{
        alert("Sus contraseñas no son iguales")
    }
}
