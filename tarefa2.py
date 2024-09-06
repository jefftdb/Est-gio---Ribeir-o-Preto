def encontra_letra(frase):
    qtd = 0
    for l in frase:
        if l == 'a' or l=='A':
            qtd+=1

    if qtd > 0:
        return f"Existem {qtd} letras a"
    else:
        return f"Não há letra a"



print(encontra_letra('Estou testando AgorA.'))
