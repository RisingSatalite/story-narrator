import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import pyttsx4
import time
import threading

def list_files_in_folder(folder_path='Story'):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        
        # Create or open a text file to write the file names
        with open('Story.txt', 'w') as txt_file:
            for file_name in files:
                # Write each file name to the text file
                last = file_name[-4:]
                print(last)
                if(last != ".txt"):
                    continue
                #check if it is txt file, then continue
                rest = file_name[:-4]
                if(rest == "default"):
                    continue
                #check if it is default, then ingnore
                txt_file.write(rest + '\n')
        
        print(f"File list written to 'file_list.txt' successfully.")
    
    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' does not exist.")
        os.makedirs()
        #trying again
        list_files_in_folder(folder_path)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

class MyApp(App):

    def build(self):
        self.title = "Narrator"
        self.done_story = False
        self.engine = pyttsx4.init()
        layout = BoxLayout(orientation='vertical')

        # Create a label
        #self.label = Label(text="Hello, Kivy!")
        #layout.add_widget(self.label)

        play_button = Button(text="Play story", size_hint_y=None, height=200)
        play_button.bind(on_press=self.story_player)
        layout.add_widget(play_button)

        scroll_view = ScrollView()

        grid_layout = GridLayout(cols=4, spacing=1, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        story_list = []
        list_files_in_folder()
        with open('Story.txt', 'r') as file:
            for line in file:
                story_list.append(line.replace('\n', ''))

        for i in story_list:
            button_text = f" {i} "
            new_button = Button(text=button_text, size_hint_y=None, height=400)
            new_button.bind(on_press=lambda instance, idx=i: self.button_save_title(idx))
            grid_layout.add_widget(new_button)

        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)

        return layout

    def button_save_title(self, title):
        self.story_title = title
        print(title)

    def play_from_title(self):
        with open(f'Story/{self.story_title}.txt', 'r') as file:
    # Iterate over each line in the file
            for line in file:
        # Process the line (replace print with your desired operation)
                self.engine.say(line)
                self.engine.runAndWait()
                print(line)
                while (self.pause == True):
                    time.sleep(1)
        self.done_story = True

    def play_story_thread(self):
        story_thread = threading.Thread(target=self.play_from_title)
        story_thread.start()

        while (self.done_story == True):
            time.sleep(1)
        story_thread
        self.done_story = False

    def story_player(self, instance):
        def close_popup(instance):
            self.done_story = True
            popup.dismiss()
            time.sleep(2)
            self.done_story = False #just to make sure it closes
        def pause_story(instance):
            if(self.pause == True):
                self.pause = False
                print("false")
            else:
                self.pause = True
                print("true")
        popup_content = BoxLayout(orientation='vertical', spacing=10)

        new_button = Button(text="Play story")
        new_button.bind(on_press=lambda instance, idx=0: self.play_story_thread())
        popup_content.add_widget(new_button)

        #close button
        close_button = Button(text="Choose different story")
        close_button.bind(on_press=lambda instance, idx=0: close_popup(close_button))
        popup_content.add_widget(close_button)

        #pause button
        pause_button = Button(text="Pause")
        pause_button.bind(on_press=lambda instance, idx=0: pause_story(pause_button))
        popup_content.add_widget(pause_button)

        popup = Popup(title=f'Playing {self.story_title}', content=popup_content, size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    MyApp().run()
