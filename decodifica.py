import Codes
obj = Codes.coleta("codes.json")


cod = open("codificado.txt", "r")
decod = open("decodificado.txt", "w")

cod_string = cod.read()
cod_list = cod_string.split()

for elem in cod_list:
    for o in obj:
        if elem == obj[o]:
            decod.write(o)

decod.close()
cod.close()