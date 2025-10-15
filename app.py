# app.py - Detta är din huvudsakliga Flask-applikationsfil
from flask import Flask
# Skapa en Flask-applikationsinstans
# __name__ talar om för Flask var den ska hitta templates, statiska filer, etc.
app = Flask(__name__)
# Definiera en route - detta talar om för Flask vad som ska hända när någon besöker "/"
@app.route('/')
def hello_world():
    """
    Denna funktion körs när någon besöker din hemsidas startsida
    @app.route('/') dekoratören betyder att denna funktion hanterar förfrågningar till rot-URL:en
    """
    return '<h1>Hej!</h1>'
# Detta block körs endast när du kör denna fil direkt (inte när den importeras)
if __name__ == '__main__':
# Kör Flask-utvecklingsservern
# Detta är endast för lokal testning - Render kommer använda gunicorn istället
    app.run(debug=True, host='0.0.0.0', port=5000)
