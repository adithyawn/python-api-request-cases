from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
 
    r = request.form['data']
    j = eval(r)

    print(j)
    print(type(j))

    if j['text'] == 'Test' :
        answer = 'UJI COBA TEST'
        print(answer)
        return {'autoreply':answer}

    elif j['text'] == 'Coba' :
        answer = 'Coba Aja'
        print(answer)
        return {'autoreply':answer}

    return {'autoreply':''}

if __name__ == '__main__':
    app.run(debug=True, port=8000)
