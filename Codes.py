import json

def coleta(arquivo):
    # Lê o arquivo com os códigos
    codes = open(arquivo, "rb")
    objeto = json.loads(codes.readline())
    codes.close()
    
    return objeto
