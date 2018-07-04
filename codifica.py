import Codes

objeto = Codes.coleta("codes.json")

cod = open("codificado.txt", "w")
decod = open("decodificado.txt", "r")

decod_string = decod.read().lower()
decod_list = list(decod_string)

for carac in decod_list:
    for chave in objeto:
        if carac == chave:
            cod.write(objeto[chave])
            cod.write(' ')

cod.close()
decod.close()
