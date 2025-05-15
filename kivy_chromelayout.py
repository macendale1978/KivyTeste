import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

kivy.require('1.10.1')

class ChromeMenuApp(App):
    def build(self):
        trigger_button = Button(text='☰ Menu', size_hint=(None, None), size=(150, 40))
        trigger_button.bind(on_release=self.show_menu)
        return trigger_button

    def show_menu(self, btn):
        content = BoxLayout(orientation='vertical', spacing=5, padding=10)
        menu_items = [
            {'text': 'Nova guia', 'icon': None},
            {'text': 'Nova janela', 'icon': None},
            {'text': 'Histórico', 'icon': None},
            {'text': 'Downloads', 'icon': None},
            {'text': 'Configurações', 'icon': None},
            {'text': 'Sair', 'icon': None},
        ]

        for item in menu_items:
            menu_button = Button(text=item['text'], size_hint_y=None, height=40, halign='left', padding=[10, 0])
            menu_button.bind(on_release=self.on_menu_item_click)
            content.add_widget(menu_button)

        self.menu_popup = Popup(title='Menu', content=content, size_hint=(None, None), size=(200, len(menu_items) * 45), auto_dismiss=True, anchor_x='right', anchor_y='top', pos=(btn.x + btn.width - 200, btn.y - (len(menu_items) * 45) + btn.height))
        self.menu_popup.open()

    def on_menu_item_click(self, btn):
        print(f'Opção selecionada: {btn.text}')
        self.menu_popup.dismiss()

if __name__ == '__main__':
    ChromeMenuApp().run()