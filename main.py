nome = 'wendell xavier'
tamanho = len(nome)
contador = 0
novo = ''
input_usuario = input(f'Qual letra deseja mudar da palavra: {nome} ?: ')

while contador < tamanho:
    letra = nome [contador]
    if letra == input_usuario:
        novo += input_usuario.upper()
    else:
        novo += letra
    contador += 1
print(novo)        