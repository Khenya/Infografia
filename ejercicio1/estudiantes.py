import csv

estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]

class Evaluador:
    
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(estudiantes, min_asistencia= 60, max_extras= 5):
        lista_notas = []
        for estudiante in estudiantes:
            nombre_completo = f"{estudiante['nombre'].capitalize()} {estudiante['apellido'].capitalize()}"
        
        if 'notas' in estudiante:
            notas = estudiante['notas']
            total_notas = sum(notas.values())
            n_materias = len(notas)
            promedio = total_notas / n_materias
        else:
            promedio = 0

        asistencia = estudiante.get('asistencia', 0)
        extras = sum(estudiante.get('extras', []))
        
        if asistencia < min_asistencia  :
            promedio = 0
        elif extras <= max_extras:
            promedio += extras

        promedio = min(promedio, 100) 
        
        lista_notas.append({
            'nombre_completo': nombre_completo,
            'promedio': promedio
        })
        return lista_notas

    def obtener_mejor_estudiante(estudiantes):
        lita_notas = calcular_promedios(estudiantes)
        mejor_estudiante = max(lita_notas, key=lambda estudiante: estudiante['promedio'])
        return mejor_estudiante

    def salvar_datos(estudiantes, nombre_archivo):
        print('salvando datos')
        lista_notas= calcular_promedios(estudiantes)
        for estudiante in lista_notas:
            observacion = 'APROBADO' if estudiante['promedio'] > 50 else 'REPROBADO'

        
def comparar_archivo_notas(archivo):
    with open('ejemplo_notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = 'notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')