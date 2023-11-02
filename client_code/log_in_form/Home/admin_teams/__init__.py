from ._anvil_designer import admin_teamsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_teams(admin_teamsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""

  def button_1_click(self, **event_args): 
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    email = self.text_box_2.text
    number = self.text_box_3.text
    joining_date = self.date_picker_1.date
    role = self.drop_down_1.selected_value
    permission = self.drop_down_2.selected_value

    email_list = []
    data = tables.app_tables.admin_teams.search()
    for i in data:
      email_list.append(i['email'])
    
    if name == "" or email == "" or number == "" or not joining_date or not role or not permission:
      Notification("Fill All Required Details").show()
    else:
      if email in email_list:
        alert("email already exist")
      else:
        anvil.server.call('teams', name, email, number, joining_date, role, permission)
        open_form('log_in_form.Home.admin_teams.view_profile')

   
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.admin_teams.view_profile')
      
    
      
    


    
    
    
    
    
    
    
    
    
    
    


