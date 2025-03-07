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
import sys
import os.path
import kivy
# Kivy Modules #
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# Google API #
"""from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError""" # likely unnecessary

date = datetime.datetime.now()

# Functions #

def fetchDay():
   """
   Function to find the corresponding school day to the current date.
   """
   df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEmrxJzhnV_wvnd2GkiyuVoBviY8kZOhGhBZd7EsraGpzn-9wmCycgWZXAr8tYXSJiBM2GQ-jeLvIt/pub?gid=0&single=true&output=csv')
   #df = df.sort_values(by=['MONTH'],axis=0,na_position='first') # no need
   print(df)
   #for item in df['MONTH']:
   # print(item)
   print(df.iloc[0,0])
   #input("debug")
   return df

# Classes #

class testGrid(GridLayout):
    """
    Main class to create the user interface.
    """
    def __init__(self,**kwargs):
        formatted_date = str((str(date.year) + "/" + str(date.month) + "/" + str(date.day)))
       # fetchDay(datetime.date.month,datetime.date.day)
        super(testGrid,self).__init__(**kwargs)
        self.cols = 2 # how many columns the grid has
        #self.name = TextInput(multiline=False) # Multiline false so you cant add new lines
        self.greeting=Label(text="Hello There")
        self.date=Label(text="The date is "+ formatted_date)
        self.add_widget(self.greeting)
        self.add_widget(self.date)

# App Runtime #

class MyApp(App):
    """
    App builder
    """
    def build(self):
        return testGrid()

if __name__ == "__main__":
    fetchDay()
    MyApp().run()
