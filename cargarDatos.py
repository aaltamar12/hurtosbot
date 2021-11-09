import json
from typing import Match

filename = 'contenido.json'

with open(filename, "r") as file:
    contenido = json.load(file)

print(contenido['contenido'])

varTag = None

patrones = []
respuestas = []

def newPatron():
        nextPatron = True
        value = input("Añadir otro patron? Si: 1, No: 0 => ")
        if int(value) == 0 & int(value) != 1:
            nextPatron = False
        return nextPatron

def user():
    global varTag 
    varTag = input("Escribe el nombre del tag: ")

    nextPatron = True
    count = 0
    while nextPatron == True:
        count+=1
        global patrones
        patrones.append(input("Escribe el patron: "))
        nextPatron = newPatron()

    i=0
    while i < count:
        print("\n"+ patrones[i] + "\n")
        respuestas.append(input("Respuesta: "))
        i+=1

user()


print(respuestas)
data = '{"tag" : "%s","patrones":%s,"respuestas":%s}'% (varTag, json.dumps(patrones),json.dumps(respuestas))
print(data)
data = json.loads(data)
contenido["contenido"].append(data)

with open(filename, "w") as file:
    json.dump(contenido, file)

print(contenido)
