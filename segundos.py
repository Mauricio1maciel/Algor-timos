total_segs = int(input("Por Favor, entre com número de segundos que deseja converter: "))
dia = total_segs // 86400
restante = total_segs % 86400
horas = restante //  3600   
segs_restantes = restante % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60
print(dia,"dia,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")