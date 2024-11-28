


try:
    num1 = int(input("Ingrese un numero entero: "))
    num2 = float(input("Ingrese otro numero entero: "))
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2
    print("La suma es: ", suma)
    print("La resta es: ", resta)
    print("La multiplicacion es: ", multi)
    print("La division es: ", divi)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Error: ""Digite un valor numerico")


print("\n Punto 2")

frutas=[]
n = int(input("Ingrese el numero de frutas que quiere agregar: "))
for i in range(n):
    i = i+1
    fruta = input("Ingrese la fruta: ")
    frutas.append(fruta)

print(frutas)

print("\n Punto 3")

diccionario={

}
diccionario["Titulo"]= input("Ingrese el titulo del libro: ")
diccionario["Autor"]= input("Ingrese el Autor del libro: ")
diccionario["Año De Publicacion"]= int(input("Ingrese el Año de publicaion del libro: "))
diccionario["Genero"]= input("Ingrese el genero del libro: ")


print("\n Punto 4")

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
conjunto3 = {9, 5, 11, 12, 13}
conjunto4 = {11, 22, 33, 44, 5}
conjunto5 = set()
conjunto3.add(input("Digite el valor del conjunto: "))
print (conjunto3)


inter= conjunto1 & conjunto2 & conjunto3 & conjunto4
print(inter)
soplaciclon= conjunto1|conjunto2|conjunto3|conjunto4
print(soplaciclon)
diff= conjunto1 - conjunto2 - conjunto3 - conjunto4
print(diff)


print("\n Punto 5")

n1 = input("Digite un numero: ")
n2 = int(n1)

sum = n1 + n2
print(sum)
