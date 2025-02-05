import pandas as pd
import datetime
x = datetime.datetime.now()

def fetchDay():
   df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSEmrxJzhnV_wvnd2GkiyuVoBviY8kZOhGhBZd7EsraGpzn-9wmCycgWZXAr8tYXSJiBM2GQ-jeLvIt/pub?gid=0&single=true&output=csv')
   df = df.sort_values(axis=0,na_position='first')
   print(df)
   #for item in df['MONTH']:
   # print(item)
   input()
fetchDay()

import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import datetime
date = datetime.datetime.now()



class testGrid(GridLayout):
    def __init__(self,**kwargs):
        formatted_date = str((str(date.year) + "/" + str(date.month) + "/" + str(date.day)))
       # fetchDay(datetime.date.month,datetime.date.day)
        super(testGrid,self).__init__(**kwargs)
        self.cols = 2 # how many columns the grid has
        self.add_widget(Label(text="The date is "+ formatted_date))
        self.name = TextInput(multiline=False) # Multiline false so you cant add new lines
        self.add_widget(self.name)

        


        
        


class MyApp(App):
    def build(self):
        return testGrid()
        

if __name__ == "__main__":
    MyApp().run()
