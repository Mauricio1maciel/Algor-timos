precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
codigo, quantidade = map(int,input("Informe o código do item e a quantidade:").split())
valor_total = precos[codigo] * quantidade
print("Total: R$ %.2f"%valor_total)
