#inicilizar una lista con el 0 y el 1
#inicializar una variable b con 0
#inicializar una variable d con 1
#inicializar una variable c con 0
#un ciclo  True:
#a la variable c sumarle los valores de los indices 0 y 1 ->
#<-de la lista unitlizando las variables b y d para acceder a los indices
#un condicional if para determinar si "c" ->
#<-es mayor a 1000000 si es mayor realizar un break
#agregar al final de la lista "c"
#sumarle 1 a la variable b
#sumarle 1 a la variable d
#mostrar la lista fuara del ciclo while

a = [0, 1]
b = 0
d = 1
c = 0
while True:
    c = a[b]+a[d]
    if c > 1000000:
        break
    a.append(c)
    b = b+1
    d = d+1

print a
print "hola mundo"
print "hola 2"
print "hola 3"