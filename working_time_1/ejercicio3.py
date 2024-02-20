'''3. Crea una función llamada verificar_calificacion que reciba tres
parámetros: nota1, nota2 y nota3
↪ Dentro de la función calcular el promedio de notas
↪ Si el promedio es mayor o igual a 6, entonces la función debe
retornar un mensaje “Aprobado”, en caso contrario
“Reprobado”
● Guardar en un archivo llamado ejercicio3.py'''

def verificar_calificacion(nota1,nota2,nota3):
    promedio= round((nota1+nota2+nota3)/3,2)
    if promedio >= 6:
        print(f'El promedio es: {promedio}. El alumno esta Aprobado')
    else:
        print(f'El promedio es {promedio}. El alumno esta reprobado')

verificar_calificacion(10,9,2)
    