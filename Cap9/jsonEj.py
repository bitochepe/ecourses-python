import json, pathlib

data = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 24,
    "direccion": {
        "calle": "Calle falsa 123",
        "ciudad": "Guatemala",
        "pais": "Guatemala"
    },
    "amigos": [
        "Pedro",
        "Juan",
        "Maria"
    ]
}

# Convertimos el diccionario a una cadena
json_string = json.dumps(data)
print(json_string, type(json_string))

# Guardamos el archivo en formato JSON en un archivo de tipo json

path = pathlib.Path(__file__).parent.resolve() #recuperamos el directorio del archivo actual
with open(str(path)+"\data_file.json", "w") as write_file: #abrimos el archivo en modo escritura
    json.dump(data, write_file) 

path = pathlib.Path(__file__).parent.resolve()
with open(str(path)+"\data_file.json", "w") as write_file: 
    json.dump(data, write_file, indent=4) # indent de 4 espacios

path = pathlib.Path(__file__).parent.resolve()
with open(str(path)+"\data_file.json", "w") as write_file: 
    json.dump(data, write_file, indent=4, sort_keys=True) # indent y ordenado




# Convertimos el diccionario a una cadena
json_string = json.dumps(data)
print(json_string, type(json_string))

# Guardamos el archivo en formato JSON en un archivo de tipo json

#recuperamos el directorio del archivo actual
path = pathlib.Path(__file__).parent.resolve() 
#abrimos el archivo en modo escritura
with open(str(path)+"\data_file.json", "w") as write_file: 
    json.dump(data, write_file) 

path = pathlib.Path(__file__).parent.resolve()
with open(str(path)+"\data_file.json", "w") as write_file: 
    # indent de 4 espacios
    json.dump(data, write_file, indent=4) 

path = pathlib.Path(__file__).parent.resolve()
with open(str(path)+"\data_file.json", "w") as write_file: 
    # indent y ordenado
    json.dump(data, write_file, indent=4, sort_keys=True) 



# json.loads()
# Lee un archivo json y lo convierte en un diccionario
data = '''{
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 24,
    "direccion": {
        "calle": "Calle falsa 123",
        "ciudad": "Guatemala",
        "pais": "Guatemala"
    },
    "amigos": [
        "Pedro",
        "Juan",
        "Maria"
    ]
}'''

json_object = json.loads(data)
print(json_object, type(json_object))

# leer un archivo json y convertirlo en un diccionario
newDic = {}
with open(str(path)+"\data_file.json", "r") as read_file:
    newDic = json.loads(read_file.read())
print(newDic, type(newDic))