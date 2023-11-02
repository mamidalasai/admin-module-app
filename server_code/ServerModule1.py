import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def investment(initial_investment, tenure, membership_type, intrest_rate):
  app_tables.roi_table.add_row(initial_investment=initial_investment, tenure=tenure, membership_type=membership_type, intrest_rate=intrest_rate)



@anvil.server.callable
def generate_google_login_url():
  return anvil.google.drive.login()


@anvil.server.callable
def teams(name, email, number, joining_date, role, permission):
  app_tables.admin_teams.add_row(name=name, email=email, number=number, joining_date=joining_date, role=role, permission=permission)
