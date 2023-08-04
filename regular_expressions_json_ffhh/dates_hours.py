from datetime import datetime

fecha_hora = datetime.now()
print(fecha_hora)

#fechas
año = fecha_hora.year
mes = fecha_hora.month
dia = fecha_hora.day

#horas
hora = fecha_hora.hour
minutos = fecha_hora.minute
segundos = fecha_hora.second
microsegundos = fecha_hora.microsecond

print("la hora es {}:{}:{}".format(hora,minutos,segundos))

