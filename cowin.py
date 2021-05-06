from cowin_api import CoWinAPI
import json
import datetime
import numpy as np 
import os
from twilio.rest import Client
import selenium
from selenium import webdriver
import time
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from threading import Thread

state_id = '21'

district_id = '395'

min_age_limit = 18

time = datetime.datetime.now()

cowin = CoWinAPI()


# here im getting the centers and the vaccines
def vaccine_check():

    try:
        available_centers = cowin.get_availability_by_district(district_id)

    #outputing it to a json file and bringing it back

        json_output = json.dumps(available_centers, indent=4)

        f = open(f'tests/vaccinecheck[{time.strftime("%b %d %Y %H|%M")}].json', 'w')

        f.write(json_output)
        f.close()

        with open(f.name) as file:
            data = json.load(file)

        n = np.arange(100)

        for x in np.nditer(n): 

            if data["centers"][x]["sessions"][0]["min_age_limit"] == 45:
                print('')   
            else:
                print(time.strftime("%b %d %Y %H:%M"), data["centers"][x]["name"], '-- vaccines:', data["centers"][x]["sessions"][0]['available_capacity'], '-- age-limit:', data["centers"][x]["sessions"][0]["min_age_limit"])
                if data["centers"][x]["sessions"][0]["available_capacity"] >= 1:
                    twilio_send(),
    except : # catch the error
        pass # pass will basically ignore it

def twilio_send():

    client = Client()

    from_whatsapp_number='whatsapp:+14155238886'
        
    to_whatsapp_number='whatsapp:+917045139278'

    client.messages.create(body='there is an 18+ vaccine avlible!!!!!!!!! quickly kadu - book',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)


while True:
    vaccine_check()

    
