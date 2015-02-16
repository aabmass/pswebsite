########## Module wrapping menus and their creation ##########
from . import context

##
# @brief A class wrapping the menu objects.
#
# Note: These ARE the menus that go in the nav
class Menu:
    ##
    # @brief Create a new menu object
    #
    # @param name Actual string for the appearing menu
    # @param routeFuncName Route to the view for the given menuentry.
    # @param submenus Option arg: array of submenus of this menu
    #
    # @return 
    def __init__(self, name, routeFuncName, submenus=None):
        self.name = name
        self.routeFuncName = routeFuncName
        self.submenus = submenus
    
    def addToContext(self):
        context.projectVars["menus"].append(self)

def createApplicationMenus():
    menus = context.projectVars["menus"]

    menus.append(Menu("Home", "index"))
    menus.append(Menu("About", "about"))
    menus.append(Menu("Login", "login"))

