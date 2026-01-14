# Conversor de moedas
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"{valor_reais:.2f} reais equivale a:")
print(f"Dólar: {valor_dolar:.2f}")
print(f"Euro: {valor_euro:.2f}")
