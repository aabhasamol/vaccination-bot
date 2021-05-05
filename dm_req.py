import tweepy
import requests
import datetime
import time
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = './last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def get_quote(response):
    min_age=45
    dates=''
    avail=''
    message=''
    vax_data=''
    for i in response["centers"]:

        name='Centre - ' + i['name']+', '+ i['district_name']       
        price=i["fee_type"]
 
        if price=="Paid":
            price = "Vaccination Price = " 
            try:
                for f in i['vaccine_fees']: 
                    price=price+str(f['fee'])+'\n'
            except Exception as e:
                price="Vaccine is Paid\n"
        else:
            price="Vaccination Price = 0\n"
        
        tweetpost=name+'\n'
        
        for j in i['sessions']:
            date=j['date']
            vaccine=j['vaccine']
            if min_age > j['min_age_limit']:
                min_age = j['min_age_limit']
            if vaccine!="" and vax_data!='':
                vax_data='Vaccine Given - '+ vaccine+'\n'
            elif vaccine!='':
                vax_data=''
                if price!='Free':
                    price=''
            
            capacity = j['available_capacity']
            if capacity!=0:
                dates+=date+' - '+str(capacity)+'\n'
                avail='Vaccines Available On:\n'
        
        if avail!='':
            tweetpost=tweetpost+avail+dates+vax_data+'The Minimum Age is: '+str(min_age)+'\n'+price+'Pincode: '+str(i['pincode'])+'\n'
            dates=''
            avail=''
            message+=tweetpost+'\n'
    if message!='':
        return message
    else:
        return "Nothing available"

def task(pincode):
    base = datetime.datetime.today()
    date_list = [base]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]
    try:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date_str[0])
        response = requests.get(URL).json()
        return get_quote(response)
    except Exception as e:
        print(e)
        return "Incorrect Input Format\nPlease keep the last 6 characters of your tweet as the pincode and try again"


def reply():
    cache = dict()
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#vaccineslot' in tweet.full_text.lower():
            twhandle=tweet.user.screen_name
            recipient=api.get_user(twhandle)
            recipient_id=recipient.id_str
            msg=tweet.full_text
            pin=msg[-6:]
            if pin not in cache:
                text=task(pin)
                if text=="Nothing available":
                    text="Nothing available for PIN: "+str(pin)
                cache[pin]=text
            else:
                text=cache[pin]
            try:
                api.send_direct_message(recipient_id=recipient_id, text=text)
            except tweepy.TweepError as e:
                api.update_status('@'+twhandle+' please enable permissions to DM and try again', tweet.id)
                print(e.reason)    
            try:    
                api.create_favorite(tweet.id)
            except tweepy.TweepError as e:
                print(e.reason)
            
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(600)