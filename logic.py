from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json

Builder.load_file("design.kv")

class LoginScreen(Screen):
	def sign_up(self):
		self.manager.current="sign_up_screen"

class Rootwidget(ScreenManager):
	pass


class SignUpScreen(Screen):
	def add_user(self,username,password):
		users={'username':username,'password':password}
		with open("users.json","a") as file:
			json.dump(users,file)
			print("SUCCESS")

		self.manager.current="Sign_Up_Screen_Success"


class SignUpScreenSuccess(Screen):
	def go_to_login(self):
		self.manager.transition.direction="right"
		self.manager.current="login_screen"

class MainApp(App):
	def build(self):
		return Rootwidget()


if __name__=="__main__":
	MainApp().run()