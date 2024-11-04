def remover_duplicados_por_link(lista):
    links_vistos = set()
    lista_unica = []
    
    for produto in lista:
        if produto.link not in links_vistos:
            links_vistos.add(produto.link)
            lista_unica.append(produto)
    
    return lista_unica