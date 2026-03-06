import sys
from os.path import exists
import csv

#Detecciones para que el programa termine si no se ejecuta correctamente

if (len(sys.argv) != 2):
    sys.exit('Es necesario especifiar un fichero de entrada para ejecutar el script.')

if (not sys.argv[1].endswith('.csv')):
    sys.exit('El archivo de entrada especificado no es un .csv.')

if (not exists('./' + sys.argv[1])):
    sys.exit('El archivo especificado no existe.')

# Campos empleados en los CSV de Contactos de Google.
fieldnames = 'Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi','Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials','Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information','Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes','Language','Photo','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type','Phone 1 - Value','Organization 1 - Type','Organization 1 - Name','Organization 1 - Yomi Name','Organization 1 - Title','Organization 1 - Department','Organization 1 - Symbol','Organization 1 - Location','Organization 1 - Job Description'

#Diccionario para almacenar los nombres para las etiquetas y códigos con los que se guardará el contacto de estar marcado en las columnas del censo que son casillas booleanas
mapeo_columnas_ETQ_COD = {
    'JE': ['JE', 'JE'],
    'Claustro': ['Claustro', 'Claustro'],
    'JR': ['JR', 'JR'],
    'CD SSR': ['CD SSR', 'SSR'],
    'CD DIT': ['CD DIT', 'DIT'],
    'CD DIE/IEL': ['CD DIE', 'DIE'],
    'CD MAT': ['CD MAT', 'MAT'],
    'CD ELF': ['CD ELF', 'ELF'],
    'CD TFB': ['CD TFB', 'TFB'],
    'CD IOR': ['CD IOR', 'IOR'],
    'CD LIA': ['CD LIA', 'LIA']

} #cambiad este diccionario según los consejos u órganos que tengáis en cada escuela!!!!

# Genera un fichero 'output.csv' en modo escritura con los campos especficados en 'fieldnames'.
with open('output.csv', 'w', encoding='utf-8', newline='') as csvout:
    delegateswriter = csv.DictWriter(csvout, fieldnames=fieldnames)

    # Incluye los campos como cabeceras del fichero.
    delegateswriter.writeheader()

    # Abre el archivo 'input.csv' exportado del formulario de SlashDAT.
    with open(sys.argv[1], encoding='utf-8', newline='') as csvin:

        # Crea un objecto 'DictReader' que permite leer campos de un fichero CSV.
        peoplereader = csv.DictReader(csvin)

        #Por si nos hemos dejado alguna columna vacía para todos, que no ocasione problemas si se llegan a hacer operaciones como filtrados por si una fila contiene algun valor nulo en alguna columna
        columnas = peoplereader.fieldnames
        while '' in columnas:
            columnas.remove('')

        # Para cada persona registrada, cumplimenta los datos de contacto.
        for row in peoplereader:    
            if not row['Puesto'] == '': #Ignorar personas que estén en el censo, pero no sean delegados de clase. Es probable que ya estén agregados, y así ahorramos problemas.
                etiquetas = ['DA(escuela) 25/26'] #Lista con las etiquetas que se agregarán a google contacts
                codigo = [] #Para añadir al nombre del contacto a que órganos pertenece

                #Bucle para determinar datos adicionales con los que guardar el contacto
                for columna, transf in mapeo_columnas_ETQ_COD.items():
                    if row[columna] == 'TRUE':  
                        etiquetas.append(transf[0]) #Etiqueta de Google Contacts
                        codigo.append(transf[1]) #Código para el nombre del contacto

                codigo= ' - '.join(codigo) #Transformar a un string único

                if codigo != '':
                    codigo= ' - ' + codigo #Para separar visualmente los caracteres del código del resto del nombre si existe código para esta persona. Si no, se verá normal.

                delegateswriter.writerow({
                    'Name Prefix': '[DA(escuela) 25/26] ',
                    'Name': row['Nombre'].title() + ' ' + row['Apellidos'].title(),
                    'Given Name': row['Nombre'].title(),
                    'Family Name': row['Apellidos'].title() + ' [' + row['Puesto'][0].upper() + row['Grupo'] + ' ' + row['Titulación'] + codigo + ']',
                    'Group Membership': ' ::: '.join(etiquetas),  # Para guardar varias etiquetas por contacto
                    'E-mail 1 - Type': '* UPM',
                    'E-mail 1 - Value': row['Correo electrónico institucional'],
                    'Phone 1 - Type': 'Mobile',
                    'Phone 1 - Value': row['Teléfono móvil'],
                    'Organization 1 - Title': row['Puesto'][0] + (row['Grupo'] if row['Grupo'] != '' else 'Titulación'),
                    'Organization 1 - Department': row['Titulación']})
        print('Done!')


# Para usar este script, abre una terminal y escribe "python .\census_dels_ETIQ.py [nombrecsv].csv"
# .\census_dels_ETIQ.py => (asumiendo que tienes el editor abierto en la misma carpeta, si no poner la dirección del archivo)
# [nombrecsv] será el nombre del csv descargado del censo. En principio no será necesario hacer ninguna modificación al propio csv si se sigue el formato del censo 24/25.

# Posteriormente, se generará un output.csv. En google contacts, seleccionar el apartado "Contactos", pinchar en Crear contacto -> Crear varios contactos -> Importar contactos
# Tras esto, se crearán todos los nuevos contactos y el proceso habrá finalizado :)
