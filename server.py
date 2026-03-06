from flask import Flask, request, send_file, render_template_string
import csv
import os
from io import StringIO, BytesIO

app = Flask(__name__)

# HTML template for the upload page
template = """
<!doctype html>
<html>
    <head>
        <title>CSV Modifier</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h2 {
                color: #333;
            }
            input[type="file"], input[type="text"], input[type="submit"] {
                padding: 10px;
                margin: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                background-color: #28a745;
                color: white;
                cursor: pointer;
                border: none;
            }
            input[type="submit"]:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Upload a CSV file</h2>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept=".csv" required>
                <br><br>
                <label for="prefix">Name Prefix:</label>
                <input type="text" name="prefix" value="[DAT 24/25]">
                <br><br>
                <input type="submit" value="Upload and Process">
            </form>
        </div>
    </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    prefix = request.form.get('prefix', '[DAT 24/25]')
    
    if file.filename == '':
        return "No selected file"
    
    if not file.filename.endswith('.csv'):
        return "Invalid file format. Please upload a CSV file."
    
    input_data = StringIO(file.read().decode("utf-8"))
    output_data = StringIO()
    
    fieldnames = ['Name','Given Name','Additional Name','Family Name','Yomi Name','Given Name Yomi',
                  'Additional Name Yomi','Family Name Yomi','Name Prefix','Name Suffix','Initials',
                  'Nickname','Short Name','Maiden Name','Birthday','Gender','Location','Billing Information',
                  'Directory Server','Mileage','Occupation','Hobby','Sensitivity','Priority','Subject','Notes',
                  'Language','Photo','Group Membership','E-mail 1 - Type','E-mail 1 - Value','Phone 1 - Type',
                  'Phone 1 - Value','Organization 1 - Type','Organization 1 - Name','Organization 1 - Yomi Name',
                  'Organization 1 - Title','Organization 1 - Department','Organization 1 - Symbol',
                  'Organization 1 - Location','Organization 1 - Job Description']

    reader = csv.DictReader(input_data)
    writer = csv.DictWriter(output_data, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        writer.writerow({
            'Name Prefix': prefix,
            'Name': row['Nombre'].title() + ' ' + row['Apellidos'].title(),
            'Given Name': row['Nombre'].title(),
            'Family Name': row['Apellidos'].title() + ' [' + row['Puesto'][0] + row['Grupo'] + ' ' + row['Titulación'] + ']',
            'Group Membership': prefix + ' ::: * myContacts',
            'E-mail 1 - Type': '* UPM',
            'E-mail 1 - Value': row['Correo electrónico institucional'],
            'Phone 1 - Type': 'Mobile',
            'Phone 1 - Value': row['Teléfono móvil'],
            'Organization 1 - Title': row['Puesto'] + (row['Grupo'] if row['Grupo'] != '' else 'Titulación'),
            'Organization 1 - Department': row['Titulación']
        })
    
    output_data.seek(0)
    output_bytes = BytesIO(output_data.getvalue().encode("utf-8"))
    return send_file(output_bytes, as_attachment=True, download_name="output.csv", mimetype="text/csv")

if __name__ == '__main__':
    app.run(debug=True)
