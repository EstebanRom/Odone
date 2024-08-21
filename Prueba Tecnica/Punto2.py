# Dependiendo directamente del uso o la aplicacion iria diferente, aunque en el siguiente
# codigo no es necesario la implementacion del TRY EXCEPT, los incorporo ya que en algunos
# casos seria necesario realizarlo de esa manera sin el uso de los IF, o en algunos otros
# casos podria tambien simplemente realizando una validacion en el diccionario como por
# ejemplo usando la funcion de GET o realizando una revicion con FOR

Dic = {'Usuario': 'Juan', 'Contraseña': 'Esteban'}

Usuario = input("Ingresa el nombre de usuario: ")
Contraseña = input("Ingresa la contraseña: ")

try:
    if Usuario == Dic['Usuario']:
        if Contraseña == Dic['Contraseña']:
            print("¡Acceso concedido!")
        else:
            raise ValueError("Contraseña incorrecta")
    else:
        print("Usuario no encontrado.")
        
except ValueError as E:
    print(E)