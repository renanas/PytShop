from flask import Blueprint, make_response, jsonify, request

from ClientResponse import clientResponse

client_ct = Blueprint('hello', __name__)

# ROUTES
@client_ct.route('', methods=['GET'])
def getAllClient():
    return make_response(jsonify(clientResponse))

@client_ct.route('/<int:id>', methods=['GET'])
def getOneClient(id):
    clienteid = id

    for indice, cliente in enumerate(clientResponse):
        if cliente.get('id') == clienteid:
            responseCliente = cliente

    return make_response(jsonify(responseCliente))

@client_ct.route('', methods=['POST'])
def postClient():
    client = request.json
    clientResponse.append(client)
    return make_response(jsonify(client))

@client_ct.route('', methods=['PUT'])
def putClient():
    clienteRequest = request.json
    for indice, cliente in enumerate(clientResponse):
        if cliente.get('id') == clienteRequest.get('id'):
            clientResponse[indice] = clienteRequest

    return make_response(jsonify(clientResponse))

@client_ct.route('/<int:id>', methods=['DELETE'])
def deleteClient(id):
    clienteid = id
    for indice, cliente in enumerate(clientResponse):
        if cliente.get('id') == clienteid:
            del clientResponse[indice]

    return make_response(jsonify(clientResponse))
