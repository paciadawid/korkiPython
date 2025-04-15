# lista, slownik


a_int = 1
a_float = 1.0 # inf numbers after dot
a_string = "jakis tekst"
a_bool = True
a_list = [1, 2, 3, 1, "tekst", [1, 2]] # uporządkowane, mutowalne (edytowalne), nieunikatowe wartosci
print(a_list[-1]) # ujemne wartości w indeksach - iterowanie od końca

a_list.append('nowy teks')
del a_list[2]
a_list[0] = 'nowa wartosc'
print(a_list)

grid = [[1 ,2, 3], [1 ,2, 3], [1 ,2, 3]]
print(grid[1][1])

a_tuple = (1, 2, 3, 1) # uporządkowane, niemutowalne(nieedytowalne), nieunikatowe wartosci
# a_tuple[0] = 'nowy tekst'

a_dict = {    # zbiór klucz-wartość, nieuporządkowane, mutowalne(edytowalne), unikowate klucze
    "marka": "fiat",
    "model": "500",
    "waga": 700,
    "pasażerowie": ["Jan", "Maria"]
}

a_dict2 = {
    "marka": "fiat",
    "model": "500",
    "waga": 700,
    "pasażerowie": ["Jan", "Maria"]
}

print(a_dict["marka"])
a_dict["kolor"] = "czerwony"
a_dict["waga"] = 600

total_mass = a_dict["waga"] + a_dict2["waga"]

print(a_dict)

