from password_manager import display, add, search, delete
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDFloatingActionButton
from kivy.lang import Builder

toolbar_helper = '''
MDBottomAppBar:

	MDToolbar:
	    title: "Password Manager"
	    icon: "plus"
	    type: "bottom"
	    mode: "center"
	    right_action_items: [["delete", lambda x: app.delete_by_username()], ["magnify", lambda x: app.search_by_username()]]
	    on_action_button: app.get_username()
'''

input_field = '''
MDTextField:
	hint_text: "Enter the name"
	helper_text: "Enter the person's name here"
	helper_text_mode: "on_focus"
	pos_hint: {'center_x': 0.5, 'center_y': 0.25}
	size_hint_x: None
	width: 300
'''

email_field = '''
MDTextField:
	hint_text: "Enter your email id"
	helper_text: "Enter the person's email id here"
	helper_text_mode: "on_focus"
	pos_hint: {'center_x': 0.5, 'center_y': 0.25}
	size_hint_x: None
	width: 300
'''

password_field = '''
MDTextField:
	hint_text: "Enter your password"
	helper_text: "Enter the password here"
	helper_text_mode: "on_focus"
	pos_hint: {'center_x': 0.5, 'center_y': 0.25}
	size_hint_x: None
	width: 300
'''

platform_field = '''
MDTextField:
	hint_text: "Enter the platform"
	helper_text: "Enter the platform of the account((e.g) => 'facebook', 'github'): "
	helper_text_mode: "on_focus"
	pos_hint: {'center_x': 0.5, 'center_y': 0.25}
	size_hint_x: None
	width: 300
'''

class Password_ManagerApp(MDApp):
	def build(self):
		screen = Screen()
		scroll = ScrollView()
		list_view = MDList()
		scroll.add_widget(list_view)
		passwords = display()
		for password in passwords:
			icon = IconLeftWidget(icon='account')
			name = password["User_name"].title()
			content = OneLineIconListItem(text=name)
			content.add_widget(icon)
			list_view.add_widget(content)
		screen.add_widget(scroll)
		toolbar = Builder.load_string(toolbar_helper)
		screen.add_widget(toolbar)
		# add_btn = MDFloatingActionButton(icon="plus", pos_hint={'center_x': 0.85, 'center_y': 0.15}, on_release=self.get_username)
		# screen.add_widget(add_btn)
		return screen

	def get_username(self):
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.add_username_dialog.dismiss())
		next_btn = MDRaisedButton(text="next", on_release=self.get_account)
		self.add_username_dialog = MDDialog(title="Add password-step:1", buttons=[next_btn, close_btn])
		self.name_field = Builder.load_string(input_field)
		self.add_username_dialog.add_widget(self.name_field)
		self.add_username_dialog.open()

	def get_account(self, obj):
		add_dict["username"] = self.name_field.text
		self.add_username_dialog.dismiss()
		next_btn = MDRaisedButton(text="next", on_release=self.get_password)
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.add_account_dialog.dismiss())
		self.add_account_dialog = MDDialog(title="Add password-step:2", buttons=[next_btn, close_btn])
		self.account = Builder.load_string(email_field)
		self.add_account_dialog.add_widget(self.account)
		self.add_account_dialog.open()

	def get_password(self, obj):
		add_dict["account"] = self.account.text
		self.add_account_dialog.dismiss()
		next_btn = MDRaisedButton(text="next", on_release=self.get_platform)
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.add_password_dialog.dismiss())
		self.add_password_dialog = MDDialog(title="Add password-step:3", buttons=[next_btn, close_btn])
		self.password = Builder.load_string(password_field)
		self.add_password_dialog.add_widget(self.password)
		self.add_password_dialog.open()

	def get_platform(self, obj):
		add_dict["password"] = self.password.text
		self.add_password_dialog.dismiss()
		next_btn = MDRaisedButton(text="next", on_release=self.show_result)
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.add_platform_dialog.dismiss())
		self.add_platform_dialog = MDDialog(title="Add password-step:4", buttons=[next_btn, close_btn])
		self.platform = Builder.load_string(platform_field)
		self.add_platform_dialog.add_widget(self.platform)
		self.add_platform_dialog.open()		

	def show_result(self, obj):
		add_dict["platform"] = self.platform.text
		self.add_platform_dialog.dismiss()
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.result_dialog.dismiss())
		self.result_dialog = MDDialog(title="Process Finished!", buttons=[close_btn])
		# print(add_dict)
		result = add(add_dict)
		if result == "Success":
			label = MDLabel(text="The process was done successfully!!", halign="center")
		else:
			label = MDLabel(text="Invalid input, Process Failed!!", halign="center")

		self.result_dialog.add_widget(label)
		self.result_dialog.open()

	def search_by_username(self):
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.search_username_dialog.dismiss())
		next_btn = MDRaisedButton(text="next", on_release=self.search_by_account)
		self.search_username_dialog = MDDialog(title="Search password-step:1", buttons=[next_btn, close_btn])
		self.search_name_field = Builder.load_string(input_field)
		self.search_username_dialog.add_widget(self.search_name_field)
		self.search_username_dialog.open()

	def search_by_account(self, obj):
		search_dict["username"] = self.search_name_field.text
		self.search_username_dialog.dismiss()
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.search_account_dialog.dismiss())
		next_btn = MDRaisedButton(text="next", on_release=self.retreive_password)
		self.search_account_dialog = MDDialog(title="Search password-step:2", buttons=[next_btn, close_btn])
		self.search_account_field = Builder.load_string(email_field)
		self.search_account_dialog.add_widget(self.search_account_field)
		self.search_account_dialog.open()

	def retreive_password(self, obj):
		search_dict["account"] = self.search_account_field.text
		self.search_account_dialog.dismiss()
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.search_result_dialog.dismiss())
		self.search_result_dialog = MDDialog(title="Password Info: ", buttons=[close_btn])
		result = search(search_dict)
		result_label = MDLabel(text=result, halign='center')
		self.search_result_dialog.add_widget(result_label)
		self.search_result_dialog.open()

	def delete_by_username(self):
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.delete_username_dialog.dismiss())
		next_btn = MDRaisedButton(text="next", on_release=self.delete_result)
		self.delete_username_dialog = MDDialog(title="Delete Password-step:1", buttons=[next_btn, close_btn])
		self.delete_name_field = Builder.load_string(input_field)
		self.delete_username_dialog.add_widget(self.delete_name_field)
		self.delete_username_dialog.open()

	# def delete_by_account(self, obj):
	# 	delete_dict["username"] = self.delete_name_field.text
	# 	self.delete_username_dialog.dismiss()
	# 	close_btn = MDFlatButton(text="close", on_release=lambda x: self.delete_account_dialog.dismiss())
	# 	next_btn = MDRaisedButton(text="next", on_release=self.delete_result)
	# 	self.delete_account_dialog = MDDialog(title="Delete Password-step:2", buttons=[next_btn, close_btn])
	# 	self.delete_account_field = Builder.load_string(email_field)
	# 	self.delete_account_dialog.add_widget(self.delete_account_field)
	# 	self.delete_account_dialog.open()

	def delete_result(self, obj):
		username = self.delete_name_field.text
		self.delete_username_dialog.dismiss()
		close_btn = MDFlatButton(text="close", on_release=lambda x: self.delete_result_dialog.dismiss())
		self.delete_result_dialog = MDDialog(title="Deletion Process Result:", buttons=[close_btn])
		end = delete(username)
		print(end)
		delete_result_label = MDLabel(text=end, halign="center")
		self.delete_result_dialog.add_widget(delete_result_label)
		self.delete_result_dialog.open()

# delete_dict = {"username": ''}
search_dict = {"username": '', "account": ''}
add_dict = {"username": '', "account": '', "password": '', "platform": ''}
Password_ManagerApp().run()