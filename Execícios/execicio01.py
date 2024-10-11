estoque = [20, 15, 10, 30, 5]

def atualizar_estoque(estoque, produto, quantidade):
   
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print(f"Venda realizada: {quantidade} unidades do produto {produto + 1}.")
        else:
            print(f"Estoque insuficiente para o produto {produto + 1}.")
    else:
        print("Produto inválido.")

def adicionar_estoque(estoque, produto, quantidade):
   
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade
        print(f"Adicionado: {quantidade} unidades ao produto {produto + 1}.")
    else:
        print("Produto inválido.")

def exibir_estoque(estoque):
   
    print("Estoque atual:")
    for i, quantidade in enumerate(estoque):
        print(f"Produto {i + 1}: {quantidade} unidades")

atualizar_estoque(estoque, 0, 3)  
atualizar_estoque(estoque, 3, 2) 
adicionar_estoque(estoque, 4, 10) 

exibir_estoque(estoque)
