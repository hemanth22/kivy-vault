import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
import json

Builder.load_file('hike.kv')

class MyGridLayout(Widget):

    oldsalary = ObjectProperty()

    def simpleiint(self):
        #with open('data.json') as f:
        #    data = json.load(f)

        jdata = '{"hemanth": "bitra","priyadharshini": "purushotham"}'
        data = json.loads(jdata)

        oldsalary = self.oldsalary.text
        result = data.get(oldsalary)
        #newsalary = self.newsalary.text
        #result_percent = round((((int(newsalary)-int(oldsalary)) / int(oldsalary)) * 100),2)
        #print('Your hike {0}%'.format(result_percent))
        self.ids.name_label2.text = f'{result}'
        self.ids.oldsalary.text = ''
        
    def copy_to_clipboard(self, instance):
        text_to_copy = self.ids.name_label2.text
        Clipboard.copy(text_to_copy)

class hikeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    hikeApp().run()