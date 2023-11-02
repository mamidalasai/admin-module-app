from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.name = []
    self.email = []
    self.number = []
    self.joining_date = []
    self.role = []
    self.permission = []
    

    data = tables.app_tables.admin_teams.search()
    for row in data:
      self.name.append(row['name'])
      self.email.append(row['email'])
      self.number.append(row['number'])
      self.joining_date.append(row['joining_date'])
      self.role.append(row['role'])
      self.permission.append(row['permission'])
      
    
    self.label_7.text = self.name[-1]
    self.label_8.text = self.email[-1]
    self.label_9.text = self.number[-1]
    self.label_10.text = self.joining_date[-1]
    self.label_11.text = self.role[-1]
    self.label_13.text = self.permission[-1]
    print(self.permission)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.admin_teams')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.admin_teams.view_profile.edit_form')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.admin_teams.view_profile.update_form')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = tables.app_tables.admin_teams.search()
    a = -1
    for row in data:
      a += 1

    
    last = data[a]
    last.delete()
    self.label_7.text = ""
    self.label_8.text = ""
    self.label_9.text = ""
    self.label_10.text = ""
    self.label_11.text = ""
    self.label_13.text = ""
    
    
    
