import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class testGrid(GridLayout):
    def __init__(self,**kwargs):
        super(testGrid,self).__init__(**kwargs)
        self.cols = 4 # how many columns the grid has
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False) # Multiline false so you cant add new lines
        self.add_widget(self.name)
        print("TEST")
        


class MyApp(App):
    def build(self):
        return testGrid()

if __name__ == "__main__":
    MyApp().run()