def matters_and_material(collegial=1, matter='matemática'):

    # em vez de 0,1,2... colocar as imagens codificadas em b64

    if collegial == 1:
        if matter == 'matemática':
            return {'conjuntos': ['principais', 'atenção', 'subconjuntos'], 'fórmula de bhaskara': [0, 1, 2]}

    elif collegial == 2:
        if matter == 'matemática':
            return {'conjuntos': [0, 1, 2], 'fórmula de bhaskara': [0, 1, 2]}


    elif collegial == 3:
        if matter == 'matemática':
            return {'conjuntos': [0, 1, 2], 'fórmula de bhaskara': [0, 1, 2]}

    else:
        pass

x = matters_and_material()
print(x['conjuntos'][2])