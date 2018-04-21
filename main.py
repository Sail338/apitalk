import requests
import config
import webbrowser

def translate(data:str):
    a = requests.get("https://api.giphy.com/v1/gifs/translate?api_key=" +config.API_KEY + "&s="+data) 
    dat = a.json()
    print(dat['data']['url'])
    webbrowser.open_new(dat['data']['images']['fixed_height']['url'])
translate("Rutgers")

def random():
    a = requests.get("https://api.giphy.com/v1/gifs/random?api_key=" +config.API_KEY) 
    dat = a.json()
    print(dat['data']['url'])
    webbrowser.open_new(dat['data']['images']['fixed_height']['url'])
random()

