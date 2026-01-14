# 6 Calculadora de salário por horas trabalhadas
numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número de funcionários = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")
