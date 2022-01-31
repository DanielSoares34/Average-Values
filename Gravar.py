arquivo = open('arqText.txt', 'w')

arquivo.write('curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura do arquivo de texto

leitura =open('arqText.txt', 'r')
print(leitura.read())
leitura.close()