from ._anvil_designer import edit_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class edit_form(edit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    data = tables.app_tables.admin_teams.search()
    a = -1
    for row in data:
      a += 1

    self.text_box_1.text = data[a]['name']
    self.text_box_2.text = data[a]['email']
    self.text_box_3.text = data[a]['number']
    self.date_picker_1.date = data[a]['joining_date']
    self.drop_down_1.selected_value = data[a]['role'] 
    self.drop_down_2.selected_value = data[a]['permission']
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.admin_teams.view_profile')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
  
    

    data = tables.app_tables.admin_teams.search()
    a = -1
    for row in data:
      a += 1

    
    data[a]['name'] = self.text_box_1.text
    data[a]['email'] = self.text_box_2.text
    data[a]['number'] = self.text_box_3.text
    data[a]['joining_date'] = self.date_picker_1.date
    data[a]['role'] = self.drop_down_1.selected_value
    data[a]['permission'] = self.drop_down_2.selected_value
    
    print(a)
    open_form('log_in_form.Home.admin_teams.view_profile')
