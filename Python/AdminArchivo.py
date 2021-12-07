from os import error
import json

class AdminArchivo:
    @staticmethod
    def cargar(nombreArchivo):
        try:
            with open('./data/{0}'.format(nombreArchivo)) as file:
                data = json.load(file)
                return data
        except error:
            return None