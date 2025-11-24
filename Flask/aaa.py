from flask import Flask

app= Flask(__name__) #Creare istanza Flask


@app.route('/')

def home():
    return 'Ciao Flask'

@app.route('/api/status')
def status():
    return {'status': 'OK', 'message': 'API funzionante'}


if __name__ == '__main__':
    app.run(debug=True)


    