import time
import random
from utils.combate import combate



def nivel_cinco(player):
    print(""" 
    Nível 5: A Sala do Guardião

    Logo após atravessar o portal você se depara com uma sala...
    era um vasto templo circular, iluminado por chamas azuis que não queimavam—apenas flutuavam, presas no ar como estrelas cativas. 
    No centro, um trono de ossos se erguia, e sobre ele...

    """)
    time.sleep(5)
    print(""" 
    diferente do velho misterioso que você encontrou no início,
    agora ele se parecia com um deus caído - três metros de altura, pele pálida como a lua.
          
    À sua frente, ergue-se Eldramar,
    agora revelado em sua verdadeira forma - um titã de sombras e luz pútrida.
    
    "Ou devo chamá-lo de... invasor?"
     """)
    time.sleep(5)

    if not fase_um(player):
        return False

    