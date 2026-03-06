import sys
from os.path import exists
import csv

if (len(sys.argv) != 2):
    sys.exit('Es necesario especifiar un fichero de entrada para ejecutar el script.')

if (not sys.argv[1].endswith('.csv')):
    sys.exit('El archivo de entrada especificado no es un .csv.')

if (not exists('./' + sys.argv[1])):
    sys.exit('El archivo especificado no existe.')

# Campos empleados en los CSV de Contactos de Google.
fieldnames = 'Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi','Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials','Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information','Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes','Language','Photo','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type','Phone 1 - Value','Organization 1 - Type','Organization 1 - Name','Organization 1 - Yomi Name','Organization 1 - Title','Organization 1 - Department','Organization 1 - Symbol','Organization 1 - Location','Organization 1 - Job Description'

# Genera un fichero 'output.csv' en modo escritura con los campos especficados en 'fieldnames'.
with open('output.csv', 'w', encoding='utf-8', newline='') as csvout:
    delegateswriter = csv.DictWriter(csvout, fieldnames=fieldnames)

    # Incluye los campos como cabeceras del fichero.
    delegateswriter.writeheader()

    # Abre el archivo 'input.csv' exportado del formulario de SlashDAT.
    with open(sys.argv[1], encoding='utf-8', newline='') as csvin:

        # Crea un objecto 'DictReader' que permite leer campos de un fichero CSV.
        peoplereader = csv.DictReader(csvin)

        # Para cada persona registrada, cumplimenta los datos de contacto.
        for row in peoplereader:
            delegateswriter.writerow({
                'Name Prefix': '[FDC 24] ',
                'Name': row['Nombre'] + ' ' + row['Apellidos'],
                'Given Name': row['Nombre'],
                'Family Name': row['Apellidos'] + ' [' + row['Turno'] + ' ' + row['Club'] + ']',
                'Group Membership': 'FDC 24 ::: * myContacts',
                'E-mail 1 - Type': '* UPM',
                'E-mail 1 - Value': row['Correo UPM'],
                'Phone 1 - Type': 'Mobile',
                'Phone 1 - Value': row['Teléfono'],
                'Organization 1 - Title': 'FDC 24' + row['Turno'],
                'Organization 1 - Department': row['Club']})
        print('Done!')
