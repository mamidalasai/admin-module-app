from ._anvil_designer import Log_in_HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Log_in_Home(Log_in_HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_sign_up_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def carrer_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def location_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
