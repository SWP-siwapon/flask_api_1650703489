flask --app=main.py run --host=0.0.0.0 --port=8000
[13:20]
from flask import Flask

app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello,Bu'

if name == 'main':
    app.run(debug=True,port=80)
