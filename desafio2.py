def relacion(a,b):

	print("Se inicio el archivo")
	print("Actualizando linea 4")
	if a>b:
		return a
	elif a<b:
		return b
	elif a==b:
		return a,b

print(relacion(4,4))