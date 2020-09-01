import os
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__ == '__main__':
     speak("Todays Top Headlines from various Sources...")
     url = os.environ.get("News_Api")
     news = requests.get(url).text
     news_dict = json.loads(news)
     articles = news_dict["articles"]
     lenght = len(articles)
     for index, art in enumerate(articles, 1):
         speak(art['title'])
         if index != lenght:
             speak("Next News...")
     speak("Thank You...")


















