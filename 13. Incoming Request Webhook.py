from flask import Flask, request
import requests

app = Flask(__name__)


#jangan lupa set di postman kirim JSON bukan TEXT
@app.route('/jsonexample', methods=['POST'])
#Methodnya harus sama dengan di postman
def jsonexample():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_ver = req_data['version info']['python']
    flask_ver = req_data['version info']['flask']
    example = req_data['example'][0]
    boolean_test = req_data['boolean_test']

    
    return 'language :{}, framework : {}, python_ver{},flask_ver{},example{},boolean_test{}'.format(language,framework,python_ver,flask_ver,example,boolean_test)

#Cara kerjanya seperti webhook. Postman send data via POST method ke alamat webhook kita : http://127.0.0.1:5000/json?language=python&framework=flask . Terus dari webhook kita return data yang di POST balik ke postman.

# Di postman, send Body JSON dengan method POST
# {
#     "language":"Python",
#     "framework":"Flask",
#     "version info":{
#         "python":3.6,
#         "flask":10
#     },
#     "example": ["query","form","json"],
#     "boolean_test": true
# }

#direct parameters
@app.route('/query_example', methods=['GET'])
def query():
    #methodnya args.get() bukan get() aja untuk get baca dict key dan args ambil valuenya di convert to string
    language = request.args.get('language')
    #get is python dict method to know if key / data available or not, so it will not come up with error if is not avaliable or not passed in parameters
    #bisa dikasih default value => request.args.get('language','ini default value')
    #Kalo yang di submit dari form web ini sendiri maka pakai form.get bukan args.get

    #nulisnya bisa juga seperti ini, jadi langsung akses dict key
    framework = request.args['framework']
    #args is like get request, if data / value not available it will come with error

    print(type(language))
    print(language)
    print(type(framework))
    print(framework)

    #flask wajib return sesuatu ke page html, tidak seperti fungsi di python yg optional
    return 'hallo'

if __name__ == '__main__':
    app.run(debug=True)
