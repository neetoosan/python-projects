import requests
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView, RecycleBoxLayout, RecycleLabel
from kivy.animation import Animation

# Replace with your Hugging Face API Key
HF_API_KEY = "your-huggingface-api-key"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"


def get_ai_response(prompt):
    """Function to get response from Hugging Face API"""
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()[0]['generated_text'].strip()


class ChatHistory(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        self.viewclass = 'RecycleLabel'
        self.layout_manager = RecycleBoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.layout_manager.bind(minimum_height=self.layout_manager.setter('height'))
        self.add_widget(self.layout_manager)

    def add_message(self, message):
        self.data.append({'text': message})
        self.layout_manager.height = len(self.data) * 30
        self.scroll_to_index(len(self.data) - 1)

    def scroll_to_index(self, index):
        self.scroll_y = 0 if index == 0 else 1


class AIAssistantApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="AI Assistant", size_hint=(1, 0.1))
        self.layout.add_widget(self.label)

        self.chat_history = ChatHistory()
        self.scroll_view = ScrollView(size_hint=(1, 0.5))
        self.scroll_view.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_view)

        self.text_input = TextInput(hint_text="Ask me anything...", size_hint=(1, 0.2), multiline=False)
        self.layout.add_widget(self.text_input)

        self.button = Button(text="Get Response", size_hint=(1, 0.1))
        self.button.bind(on_press=self.get_response)
        self.layout.add_widget(self.button)

        return self.layout

    def get_response(self, instance):
        user_input = self.text_input.text.strip()
        if user_input:
            self.animate_label()
            self.chat_history.add_message(f"You: {user_input}")
            self.text_input.text = ""
            response = get_ai_response(user_input)
            self.chat_history.add_message(f"AI: {response}")

    def animate_label(self):
        anim = Animation(color=(1, 0, 0, 1), duration=0.2) + Animation(color=(1, 1, 1, 1), duration=0.2)
        anim.start(self.label)


if __name__ == "__main__":
    AIAssistantApp().run()
