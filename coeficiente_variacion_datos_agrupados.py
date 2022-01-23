import math


# Primero la marca de clase del intervalo luego la frecuencia
# [14,18], [16, 15], [18, 20],[20, 7]
# [7.5, 2], [10.5, 6], [13.5, 10], [16.5, 18], [19.5, 16], [22.5, 3]
# [5, 2], [15, 3], [25, 3], [35, 7], [45, 5]
lista_de_datos = [[14,18], [16, 15], [18, 20],[20, 7]]
x1_fi = 0
total = 0
v_suma = 0 


for n in lista_de_datos:
    x1_fi += (n[0] * n[1])
    #print(x1_fi)

for n in lista_de_datos: 
    total += n[1]
    #print(total)

promedio = round(x1_fi / total, 2)
print(promedio) 

def varianza (lista_de_datos, promedio, total):
    global v_suma
    for n in lista_de_datos: 
        v_suma += round(n[1] * pow(promedio - n[0], 2), 2)
        round(v_suma, 2)
    return round(v_suma / total, 2)


varianza_n = (varianza(lista_de_datos, promedio, total))
print(varianza_n)

d_s = round(math.sqrt(varianza_n),2)
print(d_s)

def coeficienteVariación(desviación_e, promedio):
    coeficiente = round((desviación_e / promedio) * 100 , 2)
    return f"El coeficiente de variación es {coeficiente}"
    
print(coeficienteVariación(d_s, promedio))
