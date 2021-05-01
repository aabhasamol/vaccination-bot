import tweepy
import requests
import datetime
import time
from config import *
from collections import OrderedDict

def get_quote(response):
    data = response.json()
    dates=''
    avail=''
    for i in data["centers"]:
        if i['district_name']=='Bangalore Urban':
            name='Centre - ' + i['name']+', Bangalore'
        else:
            name='Centre - ' + i['name']+', '+ i['district_name']
        
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
            if capacity!=0:
                dates+=date+' - '+str(capacity)+'\n'
                avail='Vaccines Available On:\n'
        
        if avail!='':
            tweetpost=tweetpost+avail+dates+vax_data+price+'\n'
            dates=''
            avail=''
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

numdays = 1

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
district_id=[240, 265] # ranchi, bangalore urban

def action():
    pincode=[]
    for j in district_id:
        pin = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}'.format(j, date_str[0]))
        pins = pin.json()
        for f in pins['centers']:
            pincode.append(f['pincode'])
    pincode = list(OrderedDict.fromkeys(pincode))
    for pin in pincode:
       URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin, date_str[0])
       response = requests.get(URL)
       get_quote(response)
    
while True:
    action()
    time.sleep(28800)