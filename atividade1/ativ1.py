idadeDias = input("Digite sua idade em dias: ")
anos = int(idadeDias) / 365
meses = (int(idadeDias) % 365) / 30
dias = (int(idadeDias) % 365) % 30

print(f'{anos:.0f} anos.')
print(f'{meses:.0f} meses.')
print(dias, 'dias.')
