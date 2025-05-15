from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os


class PaginaConexao(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        prev_ip = ""
        prev_port = ""
        prev_nomeusuario = ""
        if os.path.isfile("detalhes.txt"):
            with open("detalhes.txt","r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port= d[1]
                prev_nomeusuario = d[2]

        # Campo IP
        self.add_widget(Label(text="IP: "))
        self.ip = TextInput(text=prev_ip, multiline=False, write_tab=False)
        self.add_widget(self.ip)

        # Campo Porta
        self.add_widget(Label(text="Porta: "))
        self.porta = TextInput(text=prev_port, multiline=False, write_tab=False)
        self.add_widget(self.porta)

        # Campo Nome de Usuário
        self.add_widget(Label(text="Nome: "))
        self.nomeusuario = TextInput(text=prev_nomeusuario, multiline=False, write_tab=False)
        self.add_widget(self.nomeusuario)

        # Botão Unir
        self.join = Button(text="Unir")
        self.join.bind(on_press=self.join_button)
        self.add_widget(self.join)

        # Configuração da ordem de foco
        self.ip.focus_next = self.porta
        self.porta.focus_next = self.nomeusuario
        self.nomeusuario.focus_next = self.ip  # Retorna ao primeiro campo

        self.porta.focus_previous = self.ip
        self.nomeusuario.focus_previous = self.porta
        self.ip.focus_previous = self.nomeusuario  # Retorna ao último campo

        # Vinculação do evento on_text_validate
        self.ip.bind(on_text_validate=self.mover_foco)
        self.porta.bind(on_text_validate=self.mover_foco)
        self.nomeusuario.bind(on_text_validate=self.mover_foco)

    def mover_foco(self, instance):
        """
        Move o foco para o próximo campo ao pressionar Enter.
        """
        proximo = instance.focus_next
        if proximo:
            instance.focus = False
            proximo.focus = True

    def join_button(self, instance):
        porta = self.porta.text
        ip = self.ip.text
        nomeusuario = self.nomeusuario.text
        print(f"Tentativa de unir {ip}:{porta} como {nomeusuario}")

        with open("detalhes.txt","w") as f:
            f.write(f"{ip},{porta},{nomeusuario}")

class EpicApp(App):
    def build(self):
        return PaginaConexao()

if __name__ == "__main__":
    EpicApp().run()
