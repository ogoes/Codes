import Codes
<<<<<<< HEAD
objeto = Codes.coleta("codes.json")
=======
obj = Codes.coleta("codes.json")
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc


cod = open("codificado.txt", "w")
decod = open("decodificado.txt", "r")

decod_string = decod.read().lower()
decod_list = list(decod_string)

<<<<<<< HEAD
for carac in decod_list:
    for chave in objeto:
        if carac == chave:
            cod.write(objeto[chave])
=======
for elem in decod_list:
    for o in obj:
        if elem == o:
            cod.write(obj[o])
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc
            cod.write(' ')

cod.close()
decod.close()