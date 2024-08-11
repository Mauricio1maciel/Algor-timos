while True:
  N = int(input())
  if N == 0:
      break
  resultado = list(map(int,input().split()))
  vitoria_maria = 0
  vitoria_joao = 0
  for resultado in resultado:
    if resultado == 0:
       vitoria_maria = vitoria_maria + 1
    elif resultado == 1:
       vitoria_joao = vitoria_joao + 1
  print("Mary won %d times and John won %d times"%(vitoria_maria,vitoria_joao))