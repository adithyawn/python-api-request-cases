from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

    url = "https://panel.apiwha.com/send_message.php"

    querystring = {"apikey":"UT06JL95PBxxxxx","number":"+628126xxxx","text":"TEST","custom_data":"keyword","getnotpulledonly":"1"}

    response = requests.request("GET", url, params=querystring)

    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
    
    # Create response
    resp = response.text

    return '{}'.format(resp)

if __name__ == "__main__":
    app.run(debug=True)