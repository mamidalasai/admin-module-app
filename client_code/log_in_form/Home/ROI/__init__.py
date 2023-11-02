from ._anvil_designer import ROITemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ROI(ROITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    intial_investment = self.text_box_1.text
    tenure = self.text_box_2.text
    membership_type = self.drop_down_1.selected_value
    intrest_rate = self.text_box_3.text
    
    anvil.server.call('investment', intial_investment, tenure,membership_type, intrest_rate)


    initial_investment = float(self.text_box_1.text)
    tenure = float(self.text_box_2.text)
    membership_type = str(self.drop_down_1.selected_value)
    interest_rate = float(self.text_box_3.text)

    
    future_value = int(initial_investment*(1+interest_rate/100))*int(tenure/12)
    ROI = [(future_value-initial_investment)/initial_investment]*100

    self.label_5.text = f"Your ROI is {ROI[0]}%"
    self.label_6.text = f"Your Future value is {future_value}"