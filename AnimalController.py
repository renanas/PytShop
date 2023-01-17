from flask import Blueprint, make_response, jsonify, request

from AnimalResponse import animalFind

animal_ct = Blueprint('Animal', __name__)

# ROUTES
@animal_ct.route('', methods=['GET'])
def getAllAnimal():
    return make_response(jsonify(animalFind))

@animal_ct.route('/<int:id>', methods=['GET'])
def getOneAnimal(id):
    animalid = id

    for indice, animal in enumerate(animalFind):
        if animal.get('ID') == animalid:
            findAnimal = animal

    return make_response(jsonify(findAnimal))

@animal_ct.route('', methods=['POST'])
def postAnimal():
    animal = request.json
    animalFind.append(animal)
    return make_response(jsonify(animal))

@animal_ct.route('', methods=['PUT'])
def putAnimal():
    animalRequest = request.json
    for indice, animal in enumerate(animalFind):
        if animal.get('ID') == animalRequest.get('ID'):
            animalFind[indice] = animalRequest

    return make_response(jsonify(animalFind))

@animal_ct.route('/<int:id>', methods=['DELETE'])
def deleteAnimal(id):
    animalid = id
    for indice, animal in enumerate(animalFind):
        if animal.get('ID') == animalid:
            del animalFind[indice]

    return make_response(jsonify(animalFind))