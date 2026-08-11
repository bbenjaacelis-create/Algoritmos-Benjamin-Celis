def cargar_datos():
    equipos = []
    puntos = []
    diferencia_gol = []
    
    cant = int(input("Ingrese la cantidad de equipos: "))
    for i in range(cant):
        eq = input("Nombre del equipo: ")
        pts = int(input("Puntos: "))
        df = int(input("Diferencia de gol: "))
        
        equipos.append(eq)
        puntos.append(pts)
        diferencia_gol.append(df)
        
    return equipos, puntos, diferencia_gol

def ordenar_tabla(equipos, puntos, diferencia_gol):
    n = len(equipos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if puntos[j] < puntos[j + 1] or (puntos[j] == puntos[j + 1] and diferencia_gol[j] < diferencia_gol[j + 1]):
                aux_eq = equipos[j]
                equipos[j] = equipos[j + 1]
                equipos[j + 1] = aux_eq
                
                aux_pts = puntos[j]
                puntos[j] = puntos[j + 1]
                puntos[j + 1] = aux_pts
                
                aux_df = diferencia_gol[j]
                diferencia_gol[j] = diferencia_gol[j + 1]
                diferencia_gol[j + 1] = aux_df

def mostrar_tabla(equipos, puntos, diferencia_gol):
    resultado = "Salida: "
    for i in range(len(equipos)):
        posicion = f"{i + 1}° {equipos[i]} ({puntos[i]} pts"
        
        empates = 0
        for j in range(len(equipos)):
            if i != j and puntos[i] == puntos[j]:
                empates = empates + 1
                
        if empates > 0:
            posicion = f"{posicion}, DG {diferencia_gol[i]}"
            
        posicion = f"{posicion})"
        
        if i < len(equipos) - 1:
            posicion = f"{posicion}, "
            
        resultado = f"{resultado}{posicion}"
        
    print(f"{resultado}.")


eqs, pts, df_gol = cargar_datos()
ordenar_tabla(eqs, pts, df_gol)
mostrar_tabla(eqs, pts, df_gol)