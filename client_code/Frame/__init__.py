from ._anvil_designer import FrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Aboutus import Aboutus
from ..Contactus import Contactus

#This is your startup form. It has a sidebar with navigation links and a content panel where page content will be added.
class Frame(FrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #Present users with a login form with just one line of code:
    #anvil.users.login_with_form()

  #If using the Users service, uncomment this code to log out the user:
  # def signout_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   anvil.users.logout()
  #   open_form('Logout')


  def signup_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_form()
    open_form('Frame')

  def login_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    open_form('Frame')

  def home_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home())
    self.home_link.background = app.theme_colors['Primary Container']

  def aboutus_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Aboutus())
    self.home_link.background = app.theme_colors['Primary Container']

  def contactus_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Contactus())
    self.home_link.background = app.theme_colors['Primary Container']
    










