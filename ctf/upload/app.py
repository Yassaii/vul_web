from flask import Flask, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'

@app.route('/')
def index():
    return '''
        <h1>Upload ton avatar</h1>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # LA FAILLE : Aucune vérification de l'extension 
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f"Fichier {file.filename} bien reçu dans {UPLOAD_FOLDER}"

# Le flag est caché dans un fichier sur le serveur
# Chemin : /ctf/upload/flag.txt
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)
    app.run(port=5002)