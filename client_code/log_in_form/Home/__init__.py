from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.admin_teams')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.borrowers')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.lenders')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_settings')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.revenue_share')

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.risk_pool')

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_cms')

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_reports')

  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.ROI')

  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.performance_tracke')
    



    
    
    
    
    
    
    
    
    

 

