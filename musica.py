recebe_musica = []
recebe_album = []
recebe_artista = []
recebe_listas = {}


def cad_musica():
    recebe_musica.append(str(input('Musica: ')))
    recebe_album.append(str(input('Album: ')))
    recebe_artista.append(str(input('Artista: ')))
    recebe_listas.update({'Musica': recebe_musica, 'Album': recebe_album, 'Artista': recebe_artista})
    return cad_musica


def imprime():
    for chave, valor in recebe_listas.items():
        print(f'{chave}: {valor}')
    return imprime


cad_musica()

imprime()
