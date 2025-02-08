#kivy

#pyttsx3

#narrator

# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import pyttsx4

class MyApp(App):

    def build(self):
        self.selected_story = "default"
        self.engine = pyttsx4.init()

        layout = BoxLayout(orientation='vertical')

        # Create a label
        self.label = Label(text="Hello, Kivy!")

        # Create a button
        button = Button(text="Click me!")
        button.bind(on_press=self.button_click)

        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        play_button = Button(text="Play story")
        play_button.bind(on_press=self.story_player)
        layout.add_widget(play_button)

        story_list = []
        with open('Story.txt', 'r') as file:
    # Iterate over each line in the file
            for line in file:
        # Process the line (replace print with your desired operation)
                story_list.append(line.replace('\n', ''))

        for i in story_list:
            print(i)
            button_text = f"Button {i}"
            new_button = Button(text=button_text, size_hint_y=None, height=40)
            new_button.bind(on_press=lambda instance, idx=i: self.button_save_title(idx))
            layout.add_widget(new_button)

        return layout

    def button_click(self, instance):
        print("Button Clicked!")
        
        with open('Story/cat.txt', 'r') as file:
    # Iterate over each line in the file
            for line in file:
        # Process the line (replace print with your desired operation)
                print(line)

    def button_click_title(self, title):
        print("Button Clicked!")
        
        with open(f'Story/{title}.txt', 'r') as file:
    # Iterate over each line in the file
            for line in file:
        # Process the line (replace print with your desired operation)
                self.engine.say(line)
                self.engine.runAndWait()
                print(line)
    def button_save_title(self, title):
        self.title = title

    def play_from_title(self):
        with open(f'Story/{self.title}.txt', 'r') as file:
    # Iterate over each line in the file
            for line in file:
        # Process the line (replace print with your desired operation)
                self.engine.say(line)
                self.engine.runAndWait()
                print(line)

    def story_player(self):
        popup_content = BoxLayout(orientation='vertical', spacing=10)

        new_button = Button(text="Play story", size_hint_y=None, height=40)
        new_button.bind(on_press=self.play_from_title)

        popup = Popup(title='Choose a file', content=popup_content, size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    MyApp().run()
