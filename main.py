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
date = datetime.datetime.today()
import os.path
import kivy
import numpy as np
# Kivy Modules #
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window

# Functions #

with open("format.kv",encoding='utf8') as formatFile:
          Builder.load_string(formatFile.read())

def fetchDay():
    """
    Function to find the corresponding school day to the current date.
    """
    weekday = date.strftime('%A')
    # Get CSV from Google Sheets sharing link (so we don't have to use their godawful API), use Pandas to turn it into dataframe
    calendar = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEmrxJzhnV_wvnd2GkiyuVoBviY8kZOhGhBZd7EsraGpzn-9wmCycgWZXAr8tYXSJiBM2GQ-jeLvIt/pub?gid=0&single=true&output=csv')
    schoolday = None
    for i,row in calendar.iterrows(): # Sort through spreadsheet rows
        if str(row[0]) == str(date.month): # If row is current month
         for x,item in enumerate(row[1:]): # Sort through row
             if str(item) == str(date.day): # If cell is the current day
                 schoolday = calendar.iloc[i+1][x+1] # Go to the cell beneath the day by going down one row.
    return schoolday

def fetchPeriod():
    """
    Function to see what period it currently is.
    """
    time = datetime.datetime.now().time()
    hour = time.hour
    minute = time.minute
    formatted_time = int("".join(map(str,[hour,minute]))) # Reformat time as simple digits (ex: 08:10 = 810)
    period = None
    timetable = [ # Time ranges for each period
         ['Period 1',810,920],
         ['Period 2',920,1050],
         ['Lunch',1050,1140],
         ['Period 3',1140,1250],
         ['Period 4',1250,1420]
    ]
    for key in timetable: # Find corresponding period to time
        if key[1] <= formatted_time <= key[2]:
            period = key[0]
    if 1420 <= formatted_time <= 810: # If between school offtime (2:20 PM - 8:10 AM)
        period = ' not schooltime.'
    return period


# Classes #

class layout(FloatLayout):
    """
    Main class to create the user interface.
    """
    def __init__(self,**kwargs): # UI organization
        textColor = 'black'
        schoolday = fetchDay()
        formatted_date = str((str(date.year) + "/" + str(date.month) + "/" + str(date.day)))
        period = fetchPeriod()
        super(layout,self).__init__(**kwargs)
        self.theme = 'Light'
        # Adding UI elements
        Logo = Image(
            source='logo.png',
            size_hint=(None,None),
            size=(Window.width/3.5,Window.width/3.5),
            pos_hint={'center_x':0.5,'center_y':0.8},
        )
        self.add_widget(Logo)
        #self.add_widget()
        self.add_widget(Label(
            text='Merivale Secondary Calendar System',
            size_hint=(None,None),
            size=(Window.width/3.5,Window.width/3.5),
            pos_hint={'center_x':0.5,'center_y':0.6},
            color='black',
            font_size=20))
        self.add_widget(Label(
            size_hint=(None,None),
            size=(Window.width/2.5,Window.width/2.5),
            pos_hint={'center_x':0.5,'center_y':0.45},
            color='black',
            font_size=18,
            halign='center',
            text="The date is "+ formatted_date + '\n\n Today is a Day '+schoolday+' .'))
        self.add_widget(Label(
            size_hint=(None,None),
            size=(Window.width/2.5,Window.width/2.5),
            pos_hint={'center_x':0.5,'center_y':0.3},
            color='black',
            font_size=18,
            halign='center',
            text="It is currently "+  str(period) + '.'))
        themeButton = Button(
          text='Change Theme',
          size_hint=(None,None),
          size=(Window.width/4,Window.height/15),
          pos_hint={'center_x':0.5,'center_y':0.05},
          
        )
        themeButton.bind(on_press=self.changeTheme)
        self.add_widget(themeButton)
    def changeTheme(self,none):
        # TODO: Get this stupid thing to work
        # PROBLEMS:
        # Kivy has a demented way of handling function paramters so I need to figure out
        # how to get the damn thing to actually change and access variables
        if self.theme == 'dark':
            Window.clearcolor = 'black'
            textColor = 'white'
        elif self.theme == 'light':
            Window.clearcolor = 'white'
            textColor = 'black'

# App Runtime #

class AppRuntime(App):
    """
    App builder
    """
    Window.clearcolor = (1,1,1,1)
    
    def build(self):
        self.root = root = layout()
    
    
        

if __name__ == "__main__":
    AppRuntime().run()