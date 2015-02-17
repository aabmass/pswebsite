########## Module wrapping menus and their creation ##########
from psbackend import context

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
        self._name = name
        self._routeFuncName = routeFuncName
        self._submenus = submenus
    
    def addToContext(self):
        context.projectVars["menus"].append(self)

    # Properties
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def routeFuncName(self):
        return self._routeFuncName

    @routeFuncName.setter
    def routeFuncName(self, routeFuncName):
        self._routeFuncName = routeFuncName

class UserMenu(Menu):
    def __init__(self, name, routeFuncName, user, submenus=None):
        super().__init__(name, routeFuncName, submenus)
        self.user = user

        # Change the names if we have auth
        if self.isAuthenticated():
            self.name = self.user.get_id()
            self.routeFuncName = "user"

    def isAuthenticated(self):
        return self.user.is_authenticated()

def createApplicationMenus():
    menus = context.projectVars["menus"]

    menus.append(Menu("Home", "index"))
    menus.append(Menu("About", "about"))

