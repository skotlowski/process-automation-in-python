# # deklarowanie list
# lista = []
# lista1 = [2, 3, 4, 5, 6, 7, 8]
# lista2 = ["kwiatek", "woda", "doniczka", "ziemia"]
#
# # konstruktor
# zakres = range(2,5)
# print(zakres)
# lista3 = list(zakres)
# print(lista3)
#
# # w listach moga byc rozne elementy
# lista4 = ["zero", 1, 2.0, range(5)]
# print(lista4)
#
# # str to list
# imie = "walenty"
# lista_imie = list(imie)
# print(lista_imie)
#
# print(len(lista4))
#
# # syntactic sugar
# sweet_list = [element for element in lista_imie]
# print(sweet_list)
#
# # kwadraty = [x**2 for x in range(101)]
# #print(kwadraty)
#
# # listy mozna indeksowac
# print(sweet_list[1])
# print(lista3[2])
#
# # mozna slicowac ciac
# print(sweet_list[1:5])
# print(sweet_list[1:6:2])
#
# # funkcje wbudowane
# sweet_list.append("nowy")
# print(sweet_list)
#
# sweet_list.extend(lista1)
# print(sweet_list)
#
# # lista do str
# s = ["s", "a", "b", "4"]
#
# wyraz = "".join(s)
# print(wyraz)
#
#
#
#
#
#
#


cukierasy = ["kasztanki", "malaga", "michałki"]
sweet_list = [f"Lubię {element.upper()}" for element in cukierasy]
print(sweet_list)

sweets_i_like = []
for sweet in cukierasy:
    # transformed = f"Lubię {sweet.upper()}"
    sweets_i_like.append(f"Lubię {sweet.upper()}")
print(sweets_i_like)



na_literę = "m"
sweet_list = [f"Lubię {element.upper()}" for element in cukierasy if element.startswith(na_literę)]
print(sweet_list)


sweets_i_like = []
for sweet in cukierasy:
    if sweet.startswith(na_literę):
        sweets_i_like.append(f"Lubię {sweet.upper()}")
print(sweets_i_like)


sweet_list = [f"{'Lubię' if element.startswith(na_literę) else 'Nie lubię'} {element.upper()}"
              for element
              in cukierasy]
print(sweet_list)

cukierasy = ["kasztanki", "malaga", "michałki"]
napoje = ["cola", "fanta", "sprite"]
desery = [f"na deser jest {cuks} i {napój}" for cuks in cukierasy for napój in napoje]

for deser in desery:
    print(deser)

desery = []
for cuks in cukierasy:
    for napój in napoje:
        desery.append(f"na deser jest {cuks} i {napój}")

for deser in desery:
    print(deser)
