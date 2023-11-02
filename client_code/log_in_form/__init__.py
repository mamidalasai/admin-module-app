from ._anvil_designer import log_in_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class log_in_form(log_in_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.text_box_1.text
    password = self.text_box_2.text

    if email == "" and password == '':
      Notification("Enter Both Email and Password").show()
    elif email == "":
      Notification('Enter Your E-Mail').show()
    elif password == "":
      Notification("Enter Your Password").show()

    

    if email != "" and password != "":
      data = tables.app_tables.log_in_table.search()
      email_list = []
      password_list = []
  
      for i in data:
        email_list.append(i['email'])
        password_list.append(i['password'])
        
      if (email_list[0] == email and password_list[0] == password) or (email_list[1] == email and password_list[1] == password) or (email_list[2] == email and password_list[2] == password):
        alert("Log In Successfully")
        open_form('log_in_form.Home')
      else:
        alert('Wrong E-Mail / Password')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in_Home')

  def button_3_click(self, **event_args):
      #anvil.server.call('generate_google_login_url')
      pass