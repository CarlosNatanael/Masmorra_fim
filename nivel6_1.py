import time
from utils.combate import combate

def nivel_verdade_1(player):
    print("Capítulo 6:  O Cárcere das Almas Perdidas\n")
    time.sleep(2)
    print("""
O vazio engoliu-me por um momento infinito, até que meu corpo atingiu algo frio e metálico. 
Quando abri os olhos, estava de joelhos em uma plataforma de ferro, flutuando no meio do nada.
    
    """)
    time.sleep(5)
    print("""
À minha volta, centenas de celas suspensas pairando no vazio, cada uma fechada por portas de arame farpado e luzes piscando em vermelho. 
De dentro, mãos esqueléticas se agarravam às grades, e vozes roucas sussurravam em uníssono:          
    """)
    print("\n(Liberta-nos... ou junte-se a nós.)\n")
    print("""
No centro de tudo, uma torre de ossos se erguia, e no topo, uma figura brilhante observava tudo com olhos impassíveis.          
    """)
    print("\nO Anjo da Obediência.\n")
    print("""
As celas não estavam presas ao chão—elas se moviam, girando lentamente como um carrossel macabro. 
Algumas tinham prisioneiros que pareciam humanos, outros eram criaturas que mal conseguia descrever. Todos repetiam a mesma coisa:
          
"Não merecemos estar aqui!"
    """)
    anjo = {
        "nome": "Anjo da Obediência",
        "classe": "Anjo caído",
        "vida": 120,
        "força": 60,
        "defesa": 70,
        "magia": 80,
        "nivel": 10,
        "habilidade": "Julgamento Divino"
    }
    
    if combate(player, [anjo]):
        print("\nAs celas se quebram! Você libertou os prisioneiros... mas a que custo?", 4)
        return True
    return False