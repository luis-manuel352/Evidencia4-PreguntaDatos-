# Importa el módulo requerido para usar datos de tipo Date.
import datetime

# Los datos string se preguntan y procesan sin intermediación.
# Los datos numéricos se preguntan por intermediación.

datoStr = input("dame un dato string: ")
datoEntero = input("dame un dato entero: ")
datoFloat = input("dame un dato flotante: ")
# Los datos date se preguntan por intermediación.
datoFecha = input("dame una fecha yyyy/mm/dd: ")

anio= datoFecha[0:4]
mes= datoFecha[5:7]
dia= datoFecha[-2:]
print(anio)
print(mes)
print(dia)

datoFecha = datetime.datetime(int(anio), int(mes), int(dia))

print(datoStr)
print(type(datoStr))
print(datoEntero)
print(type(datoEntero))
print(datoFloat)
print(type(datoFloat))
print(datoFecha)
print(type(datoFecha))