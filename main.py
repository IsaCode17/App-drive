from flask import Flask, request, render_template
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_to_drive():
    if request.method == 'POST':
        file_url = request.form['file_url']
        
        # Autenticación
        creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/drive'])
        drive_service = build('drive', 'v3', credentials=creds)

        # Subir archivo a Google Drive
        file_metadata = {
            'name': 'Archivo subido desde URL',
            'mimeType': 'application/octet-stream'
        }
        media = {'mimeType': 'application/octet-stream', 'body': file_url}
        drive_service.files().create(body=file_metadata, media_body=media).execute()

        return 'Archivo subido correctamente a Google Drive!'

    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run(debug=True)
      
