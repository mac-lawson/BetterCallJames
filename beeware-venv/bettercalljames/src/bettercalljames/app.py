"""
An app to call James for him to preform your needs
"""
import toga
import webbrowser
from toga.style import Pack
from toga.style.pack import *

class BetterCallJames(toga.App):
    def startup(self):
        # Set up the main window
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, alignment=CENTER))

        # Create the heading label
        heading_label = toga.Label('Better Call James', style=Pack(text_align=CENTER, font_family='Helvetica', font_size=20, padding=(0, 0, 20, 0)))

        # Create the call button
        call_button = toga.Button('Call James', on_press=self.call_james, style=Pack(width=200, height=50, font_family='Helvetica', font_size=14))

        # Add the heading label and call button to the main box
        main_box.add(heading_label)
        main_box.add(call_button)

        # Set the main window to display the main box
        self.main_window = toga.MainWindow(title=self.name, size=(400, 200))
        self.main_window.content = main_box
        self.main_window.show()

    def call_james(self, widget):
        # Replace 123-456-7890 with the actual phone number
        print("[*] calling james...")
        phone_number = '1234567890'
        webbrowser.open('tel:' + phone_number)

def main():
    return BetterCallJames('Better Call James', 'com.example.bettercalljames')

if __name__ == '__main__':
    app = main()
    app.main_loop()

