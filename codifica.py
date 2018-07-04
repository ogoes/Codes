import Codes
<<<<<<< ours
<<<<<<< HEAD
objeto = Codes.coleta("codes.json")
=======
obj = Codes.coleta("codes.json")
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc
=======
obj = Codes.coleta("codes.json")
>>>>>>> theirs


cod = open("codificado.txt", "w")
decod = open("decodificado.txt", "r")

decod_string = decod.read().lower()
decod_list = list(decod_string)

<<<<<<< ours
<<<<<<< HEAD
for carac in decod_list:
    for chave in objeto:
        if carac == chave:
            cod.write(objeto[chave])
=======
=======
>>>>>>> theirs
for elem in decod_list:
    for o in obj:
        if elem == o:
            cod.write(obj[o])
<<<<<<< ours
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc
=======
>>>>>>> theirs
            cod.write(' ')

cod.close()
decod.close()