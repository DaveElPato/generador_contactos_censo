Hola mis queridos compañeros secretarios y secretarias de las distintas delegaciones de la UPM. Aquí tenéis un README con, en principio, todas las instrucciones necesarias para usar estos scripts. Sólo tendréis que modificar los archivos .py en los distintos strings para reflejar como querréis que se guarden los contactos de vuestra escuela. Cualquier cosa, no dudéis en escribirme y preguntarme ;)


# ESPAÑOL

## Scripts para automatizar la lectura de censos de delegados e importar los contactos

## Existen dos scripts para delegados: census_inicial y census_post_elecciones 

El censo inicial (census_inicial) está pensado para usarse una vez que hayan salido todos los delegados de grupo/clase y estén reflejados en el Excel del censo. Se aporta un ejemplo de dicho excel.

### Pasos para ejecutar el script
- Descargar el script
- Crear una carpeta nueva y mover el script a dicha carpeta
- Mover el csv a usar a la misma carpeta (Exportado de una tabla excel, o Google Sheets)
- Editar el archivo .py para actualizar la fecha y el nombre de la etiqueta "[DA(escuela) XX/XX+1]" al año actual y vuestra delegación (u otra etiqueta que se vaya a usar, en el caso de scripts como el de FDC)
- Verificar que los nombres de las columnas en el csv concuerdan con los parámetros del script (si se usa el mismo formato que el censo de ejemplo, deberían coincidir de antemano)
- Abrir una terminal y ejecutar: python census.py input.csv (o como se llame el csv)
- Abrir Google Contacts en un navegador, seleccionar "Contactos", pulsar "Crear contacto", "Crear varios contactos", "Importar contactos", seleccionar el output.csv y dejar que la magia ocurra :)

El censo post elecciones (census_post_elecciones) está pensado para usarse una vez se hayan llevado a cabo las elecciones de delegado de curso, titulación, consejos, Junta de Escuela, Claustro... entre otros. Antes de usarse, se deben borrar los contactos que se agregaron cuando se hizo el censo inicial. Para ello, en Google Contacts seleccionar la etiqueta [Da(escuela) XX/XX+1], y después "Eliminar todos los contactos y esta etiqueta".

El script se ejecuta de la misma manera que el script anterior. Si se añaden nuevas columnas al censo (ej. COA, CG), añadir nuevos elementos al diccionario "mapeo_columnas_ETQ_COD", siendo la llave (key) el nombre de la columna y los valores una lista con el nombre de eitqueta deseado y el código deseado. Tras ello, se repite el proceso de generar el output.csv, borrar los contactos agregados la última vez y volver a importarlos.

Adicionalmente, pueden existir más scripts para propósitos similares, como FDC (Fiesta de Clubes), Foros de Empleo, u otros eventos. El modo de empleo es el mismo, sólo se debe modificar el script a gusto para reflejar la información que se desee guardar de dichos contactos.

También hay disponibles dos csv de ejemplo (inicial y post) para ver el formato que seguirían los datos a interpretar, en el caso de que no se tenga disponible el censo u otro caso en el que sea necesario.

# ENGLISH

## Scripts for the automatization of DAT censuses

## There are two scripts for delegates: census_inicial and census_post_elecciones

The initial census (census_inicial) should be used when all the group/class delegates have been elected, succesfully reflected in the census Excel.

### Steps for executing the scripts
- Download the script
- Put it in a separate new folder
- Add there the csv from the census you want to manage (exported from an excel table, or Google Sheets)
- Edit the file to update the date and name of the tag "[DA(escuela) XX/XX+1]" to reflect the current year and your delegation (or other tags if using other scripts, such as FDC)
- Check if the column names in the csv match the parameters in the script (if using the same format for the census as the example one, they should match beforehand)
- Open a console and run: python census.py input.csv (or whatever the csv file name is)
- Go to Google Contacts in the web browser, select "Contacts", press "Create contact", "Create multiple contacts", "Import contacts", select the output.csv and wait for the magic :)

The post elections census (census_post_elecciones) is meant to be used when the elections for year delegate, course delegate, department councils, Junta de Escuela, Claustro... and more have been celebrated. Before using, the contacts created when the script was last used should be deleted. To do this, select the [DA(escuela) XX/XX+1] tag, and then "Delete all contacts and delete this label".

This script is executed in the same way as the previous one. If more columns are to be added to the census (e.g. COA, CG), add new elements to the dictionary "mapeo_columnas_ETQ_COD", with the key being the name of the column and the values a list with the desired tag name and the desired code. Afterwards, the process of generating the output.csv, deleting the contacts added last time and importing them again is repeated.

Additionally, it is possible that more scripts for similar purposes, such as FDC, employment fairs, or other events can exist. The steps to use them are the same, the script must be modified to reflect the information wanted to save for the contacts in question.

Furthermore, there are two example csv files available (initial and post) in order to see the format of the data to be used, in case the census is not available or other cases in which they may be needed.

