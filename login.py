from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from functools import partial
from kivy.uix.modalview import ModalView


class Login(BoxLayout):
    def _init_(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super()._init_(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Image(source='https://lens.google.com/search?ep=gsbubb&hl=pt-BR&re=df&p=AbrfA8pO9NZPnR1YT13djdcOWg4JUXaDNG7wCYnOYfeBOg5sgSWdnvwevQBZJeh3V48dQOIFIRmzbf9iJGFpwSshxyg9sp44w0dLZWm9luH-JUbyAFUkqBI3kzYXm9QXhRu7c3GogPWOY8eev-8RoQ-_X8B6jkj5iCkC7BKR68LJyvIvFXm5OUkDY3QVwmYEaa7iYDSFPnCrE-hNw6umTh_1#lns=W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsIkVrY0tKR1V5TjJSaFl6RTVMVFUyTldJdE5ETTJZaTA1TkdJMkxUVXlPV1V5TnpWa05qWTVaQklmV1hoc2FYSlNUbTA0WkZsamMwZEZNRGhCY0VaUVRqbHlSRzlpZHpsU1p3PT0iLG51bGwsbnVsbCxudWxsLDEsbnVsbCxbbnVsbCxbbnVsbCxudWxsLFs1MDAwMCw1MDIyMl1dXV0='))
      self.add_widget(Label(text="LOGIN", font_size=40, font_name='Georgia', color=get_color_from_hex('##0f0360')))

        
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('##0f0360'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('##0f0360'), font_size=20))
        self.add_widget(self.senha_input)
        
        
        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75))
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=(0, 0, 1))
        self.login_button.bind(on_release=partial(self.create_new_window, self.arg1, self.arg2))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def create_new_window(self, arg1, arg2, instance):
            new_window = NewWindow(arg1, arg2)
            new_window.open()
            Window.clearcolor = (1, 1, 1, 1)

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class NewWindow(BoxLayout):
    def _init_(self, arg1, arg2, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super()._init_(**kwargs)
        self.arg1 = 'value1'
        self.arg2 = 'value2'
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('##e6e5ee')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.celular_input = TextInput(hint_text="Digite o número do seu celular ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))
        self.add_widget(self.button_cadastrar)

    def entrar_interface_login(self, arg1, arg2, instance):
            entrar_login = Login(arg1, arg2)
            entrar_login.open()
            Window.clearcolor = (1, 1, 1, 1)


    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if _name_ == '_main_':
    MyApp().run()
