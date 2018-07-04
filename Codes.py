import json

def coleta(arquivo):
    # Lê o arquivo com os códigos
    codes = open(arquivo, "rb")

    objeto = json.loads(codes.read())

    codes.close()
    
    return objeto
