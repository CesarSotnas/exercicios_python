import json

f = open("dados.json")

dados = json.load(f)
menor_valor = 10000000000
maior_valor = 1
valor_total = 0
dias_superior_media = 0

for i in dados:
    valor_total += int(i["valor"])
    
    if(i["valor"] > 0 ):
        if(i["valor"] < menor_valor):
            menor_valor = i["valor"]
            
    if(i["valor"] > 0):
        if(i["valor"] > maior_valor):
            maior_valor = i["valor"]
    

media_mensal = valor_total / 30
media_mensal = round(media_mensal, 2)

for i in dados:
    if(i["valor"] > media_mensal):
        dias_superior_media += 1

print(f"Média mensal: {media_mensal}")
print(f"Menor valor de faturamento: {round(menor_valor, 2)}")
print(f"Maior valor de faturamento: {round(maior_valor, 2)}")
print(f"Número de dias no mês superior a média mensal: {dias_superior_media}")
