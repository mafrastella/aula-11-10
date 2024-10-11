assentos = [[0 for _ in range(8)] for _ in range(5)]

def reservar_assento(assentos, fileira, assento):
    
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 0:
            assentos[fileira][assento] = 1
            print(f"Assento reservado: Fileira {fileira + 1}, Assento {assento + 1}.")
        else:
            print(f"Assento já reservado: Fileira {fileira + 1}, Assento {assento + 1}.")
    else:
        print("Fileira ou assento inválido.")

def cancelar_reserva(assentos, fileira, assento):
    
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 1:
            assentos[fileira][assento] = 0
            print(f"Reserva cancelada: Fileira {fileira + 1}, Assento {assento + 1}.")
        else:
            print(f"Assento não está reservado: Fileira {fileira + 1}, Assento {assento + 1}.")
    else:
        print("Fileira ou assento inválido.")

def exibir_mapa_assentos(assentos):
    
    print("Mapa de Assentos:")
    for i, fileira in enumerate(assentos):
        linha = ' '.join(['[R]' if assento == 1 else '[ ]' for assento in fileira])
        print(f"Fileira {i + 1}: {linha}")

reservar_assento(assentos, 0, 2)  
reservar_assento(assentos, 1, 4)  
reservar_assento(assentos, 3, 6)  

cancelar_reserva(assentos, 1, 4)

exibir_mapa_assentos(assentos)
