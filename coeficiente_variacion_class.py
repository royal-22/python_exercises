import math 

class CoeficienteVariacion: 
    def __init__(self, items, length) -> list:
        self.items = items 
        self.length = length

    def suma(self):
        suma = 0 
        for n in range(len(self.items)):
            suma += self.items[n]
        return suma

    def promedio(self, suma):
        promedio = 0 
        promedio = round((suma / self.length), 2)
        return promedio
    
    def varianza(self, promedio):
        v_suma = 0 
        for n in range(self.length): 
            v_suma = round(pow(promedio - self.items[n], 2), 2)
        return v_suma

    def desviaciónEstandar(self, promedio, varianza): 
        desviacion_estandar = 0
        desviacion_estandar = round(math.sqrt(varianza), 2)
        return desviacion_estandar

    def coeficienteVa(self, ds, promedio): 
        coeficiente = 0
        coeficiente = round((ds / promedio) * 100, 2)
        return f"El coeficiente de variación es {coeficiente} %"

# define the list of elementes
lista = CoeficienteVariacion([1.70, 1.50, 1.68, 1.70, 1.75, 1.80], 6 )

# call and print functions
summa = lista.suma()
print(summa)
promedio = lista.promedio(summa)
print(promedio)

varianza = lista.varianza(promedio)
print(varianza)

desviacion_estandar = lista.desviaciónEstandar(promedio, varianza)
print(desviacion_estandar)

coeficiente = lista.coeficienteVa(desviacion_estandar, promedio)
print(coeficiente)
