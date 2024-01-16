frase = 'curso em Video Python'
print(frase)
"Fatiamento"
print(frase[3])
print(frase[3:14])
print(frase[:14])
print(frase[1:16:2])
print(frase[::2])

print("""Lorem ipsum dolor sit amet. Et suscipit delectus aut repellendus nihil et
neque explicabo. Ut aliquam aspernatur eum velit quia vel Quis veritatis ea repudiandae 
voluptates.Aut incidunt galisum eos velit illo hic molestiae repellat sed quia
nulla in minima ratione vel velit earum. """)

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Video'))
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
print(frase.capitalize())
