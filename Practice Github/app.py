import requests
from flask import Flask, request

CLIENT_ID = 'f25e1cf3ebd1c9cc9f8b'
CLIENT_SECRET = '197fd4206f7ad02c727c2519d98b27782e953f6d'

GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'

BASE_URL = 'https://api.github.com'

app = Flask(__name__)

@app.route('/')
def index():
    #Passing parameter client_id sebagai kewajiban
    return '<a href="https://github.com/login/oauth/authorize?client_id={}	">Login with Github</a>'.format(CLIENT_ID)

@app.route('/authorize')
def authorize():
    #http://127.0.0.1:5000/authorize?code=0e0b8a551634c99810ad
    code = request.args.get('code')

    data = {'code':code, 'client_id':CLIENT_ID, 'client_secret':CLIENT_SECRET}

    headers = {'Accept': 'application/json'}

    r = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers)

    token = r.json()['access_token']

    return '<h1>SUCESS!!.THE CODE IS : {}</h1>'.format(code)



if __name__ == '__main__':
    app.run(debug=True) 