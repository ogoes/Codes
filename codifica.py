import Codes
obj = Codes.coleta("codes.json")


cod = open("codificado.txt", "w")
decod = open("decodificado.txt", "r")

decod_string = decod.read().lower()
decod_list = list(decod_string)

for elem in decod_list:
    for o in obj:
        if elem == o:
            cod.write(obj[o])
            cod.write(' ')

cod.close()
decod.close()