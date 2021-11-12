import json
from teachBot import startTraining
from typing import Match

filename = 'contenido.json'

with open(filename, "r") as file:
    contenido = json.load(file)

print(contenido['contenido'])

def newTraining(tag, patrones, respuestas):
    
    print(patrones)
    print(respuestas)
    data = '{"tag" : "%s","patrones":%s,"respuestas":%s}'% (tag, json.dumps(patrones),json.dumps(respuestas))


    print('DATA:')
    print(data)
    data = json.loads(data)
    contenido["contenido"].append(data)

    with open(filename, "w") as file:
        json.dump(contenido, file)

    startTraining()

    print('CONTENIDO GUARDADO:')
    print(contenido)
