# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time, modulo relacionado con fechas y tiempo
print("modulo datetime")
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now() #antes de mandarlo llamar se tiene que inicializar el conteo


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
"""como solo hemos defindio año, mes y dia en horas, minutos y segundos 
aparecen cero"""

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time, modulo relacionado con el tiempo
print("modulo time")

current_time = time(21, 6, 0)
"""a diferencia de datetime que nos lo daba automatico aqui tenemos que establecer 
los valores de time porque el resultado seria cero en todas las referencias"""
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date
print("modulo date")

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas
print("operaciones con fechas")
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta, da diferencia entre dos fechas, es para trabajar con franjas de fechas
print("timedelta")

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
