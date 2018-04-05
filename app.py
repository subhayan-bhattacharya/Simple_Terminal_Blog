'''
Created on Jul 6, 2017

@author: bhatsubh
'''
from database import Database
from menu import Menu

Database.initialize()

menu = Menu()
menu.run_menu()