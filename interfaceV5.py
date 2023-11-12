from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.button import MDFlatButton



class noAuthScreen(Screen):
    def update_time(self, interval):
        self.ids.time_label.text = datetime.now().strftime('%H:%M        %d.%m.%Yг.')

    def __init__(self, **kwargs):
        super(noAuthScreen, self).__init__(**kwargs)

    def login(self, *args):
        app = MDApp.get_running_app()  # Получаем текущий экземпляр приложения
        login_field = self.ids.login_field
        password_field = self.ids.password_field

        login = login_field.text
        password = password_field.text

        if not login or not password:
            app.show_dialog("Заполните оба поля.")
        else:
            # Выполнить авторизацию
            if login == "admin" and password == "admin":
                # Вход успешен
                sm = self.parent  # Получаем доступ к родительскому экрану
                sm.current = "inAuthScreen"
                login_field.text = ""  # Очищаем поле логина
                password_field.text = ""  # Очищаем поле пароля
            else:
                app.show_dialog("Неуспешная авторизация. Пожалуйста, проверьте введенные данные.")

    def register(self, *args):
        app = MDApp.get_running_app()  # Получаем текущий экземпляр приложения
        #app.show_dialog("Регистрация")
        sm = self.parent  # Получаем доступ к родительскому экрану
        sm.current = "noAuthScreenReg"  # Переход на экран регистрации
        app.change_window_size(400, 650)  # Изменить размер окна

    def create_organization(self, *args):
        app = MDApp.get_running_app()
        app.dialog.open()

    def open_organization(self, *args):
        app = MDApp.get_running_app()
        app.dialog.open()

    def load_organization(self, *args):
        app = MDApp.get_running_app()
        app.dialog.open()

    def clone_organization(self, *args):
        app = MDApp.get_running_app()
        app.dialog.open()


class noAuthScreenReg(Screen):
    def returnBack(self, *args):
        app = MDApp.get_running_app()
        sm = self.parent  # Получаем доступ к родительскому экрану
        sm.current = "noAuthScreen"  # Переход на экран регистрации
        app.change_window_size(1000, 650)  # Изменить размер окна

class inAuthScreen(Screen):
    def update_time(self, interval):
        self.ids.time_label.text = datetime.now().strftime('%H:%M  %d.%m.%Yг.')

    def __init__(self, **kwargs):
        super(inAuthScreen, self).__init__(**kwargs)

    def create_organization(self, *args):
        app = MDApp.get_running_app()
        app.show_dialog("Создание организации")

    def open_organization(self, *args):
        app = MDApp.get_running_app()
        app.show_dialog("Открытие организации")

    def load_organization(self, *args):
        app = MDApp.get_running_app()
        app.show_dialog("Загрузка организации")

    def clone_organization(self, *args):
        app = MDApp.get_running_app()
        app.show_dialog("Клонирование организации")

    def returnBack(self, *args):
        app = MDApp.get_running_app()
        sm = self.parent  # Получаем доступ к родительскому экрану
        sm.current = "noAuthScreen"  # Переход на экран регистрации
        #app.change_window_size(1000, 650)  # Изменить размер окна


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        Window.size = (1000, 650)
        Window.bind(on_resize=self.on_resize)
        Window.borderless = True

        self.dialog = MDDialog(
            title="Сначала авторизуйтесь",
            text="Для выполнения этого действия требуется авторизация.",
            buttons=[MDRaisedButton(text="OK", on_release=self.close_dialog)])

        Builder.load_file("Auth_Windows/noAuth.kv")


        self.screen_manager = ScreenManager(transition=FadeTransition())        #SwapTransition(), FadeTransition(), NoTransition(),SlideTransition()
        #Экраны в ScreenManager
        self.screen_manager.add_widget(noAuthScreen(name="noAuthScreen"))
        self.screen_manager.add_widget(noAuthScreenReg(name="noAuthScreenReg"))
        self.screen_manager.add_widget(inAuthScreen(name="inAuthScreen"))
        return self.screen_manager

    def on_start(self):
        # Вызываем метод update_time каждую секунду
        Clock.schedule_interval(self.screen_manager.get_screen('noAuthScreen').update_time, 1)
        Clock.schedule_interval(self.screen_manager.get_screen('inAuthScreen').update_time, 1)

    def show_dialog(self, text):
        self.dialog.text = text
        self.dialog.open()
    def close_dialog(self, instance):
        if hasattr(self, 'dialog'):
            self.dialog.dismiss()

    def toggle_resize(self, enabled):
        if enabled:
            Window.bind(on_resize=self.on_resize)
        else:
            Window.unbind(on_resize=self.on_resize)

    def change_window_size(self, width, height):
        self.toggle_resize(False)
        Window.size = (width, height)
        Window.create_window()
        self.toggle_resize(True)

    def on_resize(self, instance, width, height):
        Window.size = (1000, 650)


if __name__ == "__main__":
    MyApp().run()
