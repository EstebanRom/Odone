Diccionario = []
Diccionario.append({"Nombre": "Zapatos XYZ", 
                    "Código de barras": 8569741233658, 
                    "Fabricante": "Deportes XYZ",
                    "Categoría": "Zapatos", 
                    "Género": "Masculino"})
Diccionario.append({"Nombre": "Zapatos ABC", 
                    "Código de barras": 7452136985471, 
                    "Fabricante": "Deportes XYZ",
                    "Categoría": "Zapatos", 
                    "Género": "Femenino"})
Diccionario.append({"Nombre": "Camisa DEF", 
                    "Código de barras": 5236412896324, 
                    "Fabricante": "Deportes XYZ",
                    "Categoría": "Camisas", 
                    "Género": "Masculino"})
Diccionario.append({"Nombre": "Bolso KLM", 
                    "Código de barras": 5863219635478, 
                    "Fabricante": "Carteras Hi-Fashion",
                    "Categoría": "Bolsos", 
                    "Género": "Femenino"})

def Punto1(Diccionario):
    Grupo = {}
    
    for P in Diccionario:
        Fab = P["Fabricante"]
        Cat = P["Categoría"]
        Gen = P["Género"]
        
        if Fab not in Grupo:
            Grupo[Fab] = {}
        
        if Cat not in Grupo[Fab]:
            Grupo[Fab][Cat] = {}
        
        if Gen not in Grupo[Fab][Cat]:
            Grupo[Fab][Cat][Gen] = []
        
        Grupo[Fab][Cat][Gen].append(P)
    
    return Grupo

Respuesta = Punto1(Diccionario)

print(Respuesta, '\n')

for Fabricante, Categorias in Respuesta.items():
    print(f"Fabricante: {Fabricante}")
    for Categoria, Generos in Categorias.items():
        print(f"  Categoría: {Categoria}")
        for Genero, Codigo in Generos.items():
            print(f"    Género: {Genero}")
            for P in Codigo:
                print(f"      P: {P['Nombre']} ({P['Código de barras']})")