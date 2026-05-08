possibilidade=[True,False]
print('---------------------------------------------------')
print('Formula: (M v N) ^ ¬(O v P) ^ (¬M v Q) v (¬N v R)')
print('---------------------------------------------------')
contador=0
for M in possibilidade:
    for N in possibilidade:
        for O in possibilidade:
            for Q in possibilidade:
                for P in possibilidade:
                    for R in possibilidade:
                        if (M or N) and not (O or P) and (not M or Q) and (not N or R):
                            res_f='Verdadeiro'
                        else:
                            res_f='Falso'
                        contador += 1
                        print(f'M = {M} \tN = {N} \tO = {O} \tQ = {Q} \tP = {P} \tR = {R} \t Fórmula = {res_f}')
print(f'Contador ={contador}')