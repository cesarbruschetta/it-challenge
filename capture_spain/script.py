
total = 171024
titulo = 12825
itens_pagina = 14359

espaco_pagina = 5
  
def init():
    
    count_pagina = 1
    resto = total + titulo + espaco_pagina
    while resto > 0:
        # print(resto)
        resto = (resto - itens_pagina)
        if resto > 0:
            resto += (titulo + espaco_pagina)
        count_pagina += 1

    print(count_pagina)
     
init()