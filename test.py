import pprint

datos = {'nombre': 'Juan', 'edad': 30, 'hobbies': ['ciclismo', 'lectura', 'viajar'], 'amigos': {'Carlos': {'edad': 25, 'ciudad': 'Madrid'}, 'Ana': {'edad': 28, 'ciudad': 'Barcelona'}}}

# Uso de print
print("Usando print:")
print(datos)

# Uso de pprint
print("\nUsando pprint:")
pprint.pprint(datos)
