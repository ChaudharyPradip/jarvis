# from PyDictionary import PyDictionary
import requests
import datetime
from googletrans import Translator
import re

#dictinary
def dictionary(task):
    task = task.replace("meaning","")
    dict = PyDictionary()
    meaning = dict.meaning(task)
    print(meaning)
    return meaning


#New fetching
def news():    
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    results = list(map(lambda text : f'{results.index(text) + 1}. {text}', results))
    return '\n '.join(results)


#Date time
def getTime():
    today = datetime.datetime.now();
    return today.strftime("%b %d %Y %H:%M:%S")


#translator
def translate(sentence):
    translator = Translator()
    sentence = sentence.replace("translate", "").strip()
    regex = re.compile("in.*")
    search = regex.search(sentence)
    sentence = sentence.rstrip(search.group())
    lang = search.group().split()[1] or "hindi"
    
    
    LANGUAGES = {'ar': 'arabic','bn': 'bengali','zh-cn': 'chinese (simplified)','nl': 'dutch','en': 'english','fr': 'french',
                 'de': 'german','el': 'greek','gu': 'gujarati','hi': 'hindi','it': 'italian','ja': 'japanese','la': 'latin',
                 'mr': 'marathi','ne': 'nepali','pa': 'punjabi','ru': 'russian','es': 'spanish','ta': 'tamil','hu': 'hungarian',}

    try:
        for i in LANGUAGES:
            if LANGUAGES[i] == lang:
                translated = translator.translate(sentence, dest= i )
                return translated.text
    except Exception as e:
        return


#Weather of any place
def weather():
    api_key = "39df13051eb0c57132d0de5ed840e8c0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "surat"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        res = f"Temperature(in celcius unit) is {round((current_temperature - 273), 2)}°C\nAtmospheric pressure(in hPa unit) is {current_pressure}\nHumidity(in percentage) is {current_humidity}\nWeather Description :- {weather_description}"
        return res
    else:
        print(" City Not Found ")


# wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        return "Good Morning Sir !"

    elif hour>= 12 and hour<18:
        return "Good Afternoon Sir !"

    else:
        return "Good Evening Sir !"