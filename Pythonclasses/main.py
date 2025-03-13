from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window


class SmartCalculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=4, padding=10, spacing=10, **kwargs)

        Window.clearcolor = (0.15, 0.15, 0.15, 1)  # Set background color

        self.display = TextInput(font_size=40, readonly=True, halign='right', size_hint_y=0.25,
                                 background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.add_widget(self.display)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C',)
        ]

        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=28,
                    size_hint=(0.25, 0.2),
                    background_color=(0.2, 0.2, 0.2, 1),
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                self.add_widget(button)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += text


class SmartCalculatorApp(App):
    def build(self):
        return SmartCalculator()


if __name__ == "__main__":
    SmartCalculatorApp().run()
