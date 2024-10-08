from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Switchtosportsmode import Switchtosportsmode 




class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def switchtosportsmode_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Switchtosportsmode())

  def back_link_click(self, widget):
    """This method is called when the button is clicked"""
    self.webview.go_back()

  def on_backbutton_clicked(self, **event_args):
    """This method is called when the button is clicked"""
    self..go_back()

  
    
    


