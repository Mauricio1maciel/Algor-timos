a, b, s =input().split()
a = int(a)
b = int(b)
s = int(s)
MaiorAB = (a + b + abs(a - b))/2
maior = (MaiorAB + s + abs(MaiorAB - s)) / 2
maior = int(maior)
print(maior," eh o maior")