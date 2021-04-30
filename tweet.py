import tweepy
import requests
import datetime
import time
from config import *

def get_quote(response):
    data = response.json()
    for i in data["centers"]:
        
        name='Vaccination Centre - ' + i['name']+'\nVaccines Available On:'
        price=i["fee_type"]
        
        if price=="Paid":
            price = "Vaccination Price = " 
            for f in i['vaccine_fees']: 
                price+=f['fee']
        else:
            price="Vaccination Price = 0"
        
        tweetpost=name+'\n'
        
        for j in i['sessions']:
            date=j['date']
            vaccine=j['vaccine']
        
            if vaccine!="":
                vax_data='Vaccine Given - '+ vaccine+'\n'
            else:
                vax_data=''
                price=''
            
            capacity = j['available_capacity']
            tweetpost=tweetpost+date+' - '+str(capacity)+'\n'

        tweetpost=tweetpost+vax_data+price+'\n'
        posttweet(tweetpost)
        time.sleep(60)

def posttweet(data):
    try:
        api.update_status(data)
    except tweepy.TweepError as e:
        print(e.reason)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

district_id = 240 # Ranchi
numdays = 1

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

def action():
    for datenow in date_str:
       URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=834001&date={}".format(datenow)
       response = requests.get(URL)
       get_quote(response)
    
while True:
    action()
    time.sleep(28800)