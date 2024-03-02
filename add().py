def add(n, p, lista):
	i=p
	lista2=[]
	while i<len(lista):
		lista2.append(lista[i])
		del lista[i]
	lista.append(n)
	for k in range(0, len(lista2)):
		lista.append(lista2[k])