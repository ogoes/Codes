import Codes
objeto = Codes.coleta("codes.json")

cod = open("codificado.txt", "r")
decod = open("decodificado.txt", "w")

cod_string = cod.read()
cod_list = cod_string.split()

for codigo in cod_list:
    for carac in objeto:
        if codigo == objeto[carac]:
            decod.write(carac)

decod.close()
cod.close()
