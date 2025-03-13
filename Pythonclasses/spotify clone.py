import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


# Database setup
def init_db():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_message(text):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()


def load_messages():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return [msg[0] for msg in messages]


class ChatApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.chat_log = GridLayout(cols=1, size_hint_y=None)
        self.chat_log.bind(minimum_height=self.chat_log.setter('height'))

        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.scroll.add_widget(self.chat_log)
        self.layout.add_widget(self.scroll)

        self.input_box = BoxLayout(size_hint=(1, 0.1))
        self.text_input = TextInput(multiline=False)
        self.send_button = Button(text='Send')
        self.send_button.bind(on_press=self.send_message)

        self.input_box.add_widget(self.text_input)
        self.input_box.add_widget(self.send_button)
        self.layout.add_widget(self.input_box)

        self.load_chat_history()

        return self.layout

    def send_message(self, instance):
        message = self.text_input.text.strip()
        if message:
            save_message(message)
            self.add_message_to_chat(message)
            self.text_input.text = ""

    def load_chat_history(self):
        messages = load_messages()
        for msg in messages:
            self.add_message_to_chat(msg)

    def add_message_to_chat(self, message):
        label = Label(text=message, size_hint_y=None, height=30)
        self.chat_log.add_widget(label)
        self.scroll.scroll_y = 0


if __name__ == "__main__":
    init_db()
    ChatApp().run()
