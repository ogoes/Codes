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


cod = open("codificado.txt", "r")
decod = open("decodificado.txt", "w")

cod_string = cod.read()
cod_list = cod_string.split()

<<<<<<< ours
<<<<<<< HEAD
for codigo in cod_list:
    for carac in objeto:
        if codigo == objeto[carac]:
            decod.write(carac)
=======
=======
>>>>>>> theirs
for elem in cod_list:
    for o in obj:
        if elem == obj[o]:
            decod.write(o)
<<<<<<< ours
>>>>>>> 9f38a656ab9cbe4aa4e4eb1b46b6a1956d8bf0bc
=======
>>>>>>> theirs

decod.close()
cod.close()