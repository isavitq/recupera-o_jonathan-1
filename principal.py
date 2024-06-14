import pyrebase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = 360, 640

firebaseConfig = {
    'apiKey': "AIzaSyA8abNzTwQKwWrXM-K1TM-s877AqMtLm9A",
    'authDomain': "projeto-bd-5aaf2.firebaseapp.com",
    'databaseURL': "https://projeto-bd-5aaf2-default-rtdb.firebaseio.com",
    'projectId': "projeto-bd-5aaf2",
    'storageBucket': "projeto-bd-5aaf2.appspot.com",
    'messagingSenderId': "985808185709",
    'appId': "1:985808185709:web:69490eeeb0321f887ed264",
    'measurementId': "G-G5R9XVTE2S"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

class Home(BoxLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        Window.clearcolor = get_color_from_hex("#1eb88f")
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        self.add_widget(Image(source='IMG_9831-removebg-preview.png', size_hint=(None,None),size=(250,250)))
        self.add_widget(Label(text="Seja Bem-Vinda", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#1eb88f'))
        self.cadastrar_button.bind(on_press=self.entrar)
        self.login_button = Button(text=" Cadastre-se", background_color=get_color_from_hex('#1eb88f'))
        self.login_button.bind(on_press=self.cadastrar)
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

    def entrar(self, *args):
        self.parent.parent.current = 'Login'

    def cadastrar(self, *args):
        self.parent.parent.current = 'Cadastro'

class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10
        Window.clearcolor = get_color_from_hex("#ff8e31")

        self.add_widget(Label(text="Faça seu Login", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.add_widget(self.username_input)

        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#5e2129'))
        self.cadastrar_button.bind(on_press=self.login)
        self.add_widget(self.cadastrar_button)

    def login(self, *args):
        email = self.username_input.text
        senha = self.senha_input.text
        try:
            user = auth.sign_in_with_email_and_password(email, senha)
            self.parent.parent.current = 'Pratos'
        except Exception as e:
            print("Erro ao fazer login:", e)

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)

        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('#e6e5ee')))

        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=get_color_from_hex('#5e2129'))
        self.button_cadastrar.bind(on_press=self.cadastrar)
        self.add_widget(self.button_cadastrar)

    def cadastrar(self, *args):
        email = self.email_input.text
        senha = self.senha_input.text
        try:
            auth.create_user_with_email_and_password(email, senha)
            print("Usuário cadastrado com sucesso!")
            self.parent.parent.current = 'Login'
        except Exception as e:
            print("Erro ao cadastrar usuário:", e)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen(name='Home'))
        sm.add_widget(Screen(name='Login'))
        sm.add_widget(Screen(name='Cadastro'))
        sm.add_widget(Screen(name='Pratos'))

        home = Home()
        login = TelaLogin()
        cadastro = TelaCadastro()

        sm.get_screen('Home').add_widget(home)
        sm.get_screen('Login').add_widget(login)
        sm.get_screen('Cadastro').add_widget(cadastro)

        return sm

if __name__ == '__main__':
    MyApp().run()
