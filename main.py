#unificar pygame con logica de sudoky y frontend
import logicasudoku
import frontendsudoku

logica= logicasudoku.cuerpo(2,3)
imagenes= frontendsudoku.imagenessudoku(2,2)


i=True
while i:
    a=int(input("Ingrese un valor"))
    logica.pruebadeopciones(a)
    if a==3:
        i=False
    
