

# lambda 

f = lambda x,y:x+y

# map
# Es un apuntador que me toma valores de la lista 
# Dgamos que tengo una lista la cual quiero hacerlo algo

# Quiero elevar cada uno a farenheit

celsius = [39.2,36.5,37.3,37.8]

[i*(9/5)+ 32 for i in celsius]

# Ahora con un map 
# A cada uno de los elementos me tome y calcule la funcion y me los devuelva
farenheit= map(lambda x: x*(9/5) + 32 , celsius)

# Defino la funcion con lambda y cuando entra ese x, el map sera como el list comprehensio 
# me retorna un apuntador de memoria en el compu 
# cada vez que lo corra me genera un apuntador diferente

# con una list me da los valores me trae eso de la memoria del compu donde quedo el calculo
list(map(lambda x: x*(9/5) + 32, celsius))

## Ejercicio 
# Crear una funcion que reciba un argumento y ese argumento
# sera multiplicado por un numero desconocido
# la funcion debe ser creada con lambda

r = lambda x,y: x*y
r(6,8)


def f(n):
	return lambda x: x*n
r=f(2)
x=5
# Si le paso una lista de numeris que quiero multiplicar

l=list(range(1,11))

# Con el map se la aplico a varios numeros

# map(funcion, numeros a los que quiero) en este caso particular
list(map(r,l)) # le digo que todo numero que le pase a f lo multiplica por 2
# Le cojo a los numeros de la lista l y los multiplico por n que ser 2 
# Me queda asi como la tabla del 2

## Ejercicio 2
# Hacer una funcion que dada una lista devuelva un lista con los numeros pares
# Usando un lambda

num=list(range(1,40))

list(filter(lambda i: i%2 ==0,num))

## Ejercicio 3 
# Escribir una funcion que dado un diccionario lo ordene

celulares=[{'Brand':'Nokia', 'Modelo':1100, 'color': 'Silver'},
			{'Brand':'Motorola', 'Modelo':2546, 'color': 'Black'},
			{'Brand':'Apple', 'Modelo':6587, 'color': 'Blue'}]

sorted(celulares, key = lambda x:x['Modelo']) #con el lambda
# Devolver el diccionario ordenado por coloe


## Ejercicio 4 
# Dado una sting quiero saber si empieza por una letra que le digo a la funcion 


## Ejercicio 5
## Crear una lista que me sume los valores de cada una usando la funcion lambda

def sumaLista(x,y):
    res =  list(map(lambda x,y: x+y,x,y))   
    return res
  
sumaLista([1,2,3],[4,5,6])
