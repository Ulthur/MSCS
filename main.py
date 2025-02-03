<<<<<<< Updated upstream
import datetime
x = datetime.datetime.now()
print(str(x.year) + "/" + str(x.month) + "/" + str(x.day))
input()
=======


import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import datetime
date = datetime.datetime.now()
formatted_date = str((str(date.year) + "/" + str(date.month) + "/" + str(date.day)))


class testGrid(GridLayout):
    def __init__(self,**kwargs):
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
>>>>>>> Stashed changes
