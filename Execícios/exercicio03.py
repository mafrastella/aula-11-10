vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

def calcular_total_vendas(vendas):
   
    return sum(vendas)

def calcular_media_vendas(vendas):
    
    return sum(vendas) / len(vendas)

def mes_maxima_venda(vendas):
    
    max_venda = max(vendas)
    mes = vendas.index(max_venda) + 1  
    return mes, max_venda

total_vendas = calcular_total_vendas(vendas_mensais)
media_vendas = calcular_media_vendas(vendas_mensais)
mes, max_venda = mes_maxima_venda(vendas_mensais)

print(f"Total de vendas no ano: {total_vendas}")
print(f"Média mensal de vendas: {media_vendas:.2f}")
print(f"Mês com a máxima venda: Mês {mes} com {max_venda} unidades vendidas.")
