import requests
from clarifai.rest import ClarifaiApp
import config
import webbrowser

def translate(data:str):
    a = requests.get("https://api.giphy.com/v1/gifs/translate?api_key=" +config.API_KEY + "&s="+data) 
    dat = a.json()
 #   print(dat['data']['url'])
    webbrowser.open_new(dat['data']['images']['fixed_height']['url'])
translate("Rutgers")

def random():
    a = requests.get("https://api.giphy.com/v1/gifs/random?api_key=" +config.API_KEY) 
    dat = a.json()
#    print(dat['data'])
    webbrowser.open_new(dat['data']['images']['fixed_height']['url'])
random()


def clarifai_test(url_:str):
    app = ClarifaiApp(api_key=config.CLARFAI)
    model = app.models.get("general-v1.3")
    b =model.predict_by_url(url=url_)
    for k in b['outputs']:
        for i in k['data']['concepts']:
            print(i['name'])

#clarifai_test("https://samples.clarifai.com/metro-north.jpg")

