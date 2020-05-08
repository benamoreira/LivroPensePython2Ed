import time

ticks = time.time()
dt_epoca = time.gmtime(0)
dt_agora = time.localtime()

anos = dt_agora[0] - dt_epoca[0]
dias = dt_agora[2] - dt_epoca[2]
horas = dt_agora[3] - dt_epoca[3]
min = dt_agora[4] - dt_epoca[4]
seg = dt_agora[5] - dt_epoca[5]

qtde_total_dias = (anos * 365) + dias

print("Se passaram desde a Epoca: ", qtde_total_dias, "dias,", horas, "horas, ", min, "minutos e ", seg, "segundos")


