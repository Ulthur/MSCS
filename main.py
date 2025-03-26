"""
ICS4U - Software Development Project
Merivale Secondary Calendar System
Emin Suhonjic, Osaid El Dali, Justin Yuan
Program to display the current school day and any special
events corresponding to the Merivale High School calendar.
"""

# Libraries #
import pandas as pd
import datetime
import os.path
import kivy
import numpy as np
# Kivy Modules #
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
# Google API #
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError

date = datetime.datetime.today()

# Functions #

def fetchDay():
    """
    Function to find the corresponding school day to the current date.
    """
    weekday = date.strftime('%A')
    calendar = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEmrxJzhnV_wvnd2GkiyuVoBviY8kZOhGhBZd7EsraGpzn-9wmCycgWZXAr8tYXSJiBM2GQ-jeLvIt/pub?gid=0&single=true&output=csv')
    schoolday = None
    for i,row in calendar.iterrows():
        if str(row[0]) == str(date.month):
         for x,item in enumerate(row[1:]):
             if str(item) == str(date.day):
                 schoolday = calendar.iloc[i+1][x+1]
    return schoolday

def fetchPeriod():
    """
    Function to see what period it currently is.
    """
    time = datetime.datetime.now().time()
    hour = time.hour
    minute = time.minute
    formatted_time = int("".join(map(str,[hour,minute])))
    period = None
    print(formatted_time)
    timetable = [
         ['Period 1',810,920],
         ['Period 2',920,1050],
         ['Lunch',1050,1140],
         ['Period 3',1140,1250],
         ['Period 4',1250,1420]
    ]
    for key in timetable:
        if key[1] <= formatted_time <= key[2]:
            period = key[0]
    if 1420 <= formatted_time <= 810:
        period = ' not schooltime.'
    return period

# Classes #

class layout(GridLayout):
    """
    Main class to create the user interface.
    """
    def __init__(self,**kwargs):
        schoolday = fetchDay()
        formatted_date = str((str(date.year) + "/" + str(date.month) + "/" + str(date.day)))
        period = fetchPeriod()
        super(layout,self).__init__(**kwargs)
        self.cols = 1 # UI organization
        self.add_widget(Image(source='logo.png',width=20,height=20))
        self.add_widget(Label(font_size = 20,halign='center',text="Merivale Highschool Calendar System"))
        self.add_widget(Label(font_size = 28,halign='center',text="The date is "+ formatted_date + '\n Today is a Day '+schoolday+' .'))
        self.add_widget(Label(font_size = 22,halign='center',text="It is currently "+period))
        

# App Runtime #

class MyApp(App):
    """
    App builder
    """
    def build(self):
        return layout()

if __name__ == "__main__":
    MyApp().run()