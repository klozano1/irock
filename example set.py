'''
vowels = {'a','e','i','o','u'}
example = set('example')

union= vowels.union(example)
print("union",union)

intersection= vowels.intersection(example)

print("intersection",intersection)


difference= vowels.difference(example)

print("difference",difference)


difference= vowels.difference(example)

print("difference",difference)


tuple_example=('a','b','c','d','e') # tuple no se puede modificar el valor
print(tuple_example)


'''
beers = [{'name': 'Modelo Especial', 'price': 25.00, 'ap': 4.0},
         {'name': 'Indio','price': 20.00, 'ap': 4.2 },
         {'name': 'Tecate Light','price': 30.00, 'ap': 3.5 },
         {'name': 'Minerva', 'price': 35.00, 'ap': 8.0 },
         {'name': 'Budlight', 'price': 18.00, 'ap': 5.0 }]
#output:
#Name Precio
#agregar columna

for dictionary in beers:
    print(dictionary)

beers.append({'name':'Sol', 'price':40.00, 'ap' : 7.0})
print ("llave agregada")
for dictionary in beers:
    print(dictionary)



