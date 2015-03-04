########## Module wrapping menus and their creation ##########
from psbackend import context
from flask.ext.login import current_user

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
    def __init__(self, name, routeFuncName, visible=True, submenus=[]):
        self._name = name
        self._routeFuncName = routeFuncName
        self._submenus = submenus
        self._visible = visible
    
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

    @property
    def visible(self):
        return self._visible
    
    @visible.setter
    def visible(self, isVis):
        self._visible = isVis

    @property
    def submenus(self):
        return self._submenus

    @submenus.setter
    def submenus(self, subs):
        self._submenus = subs

    def displaySubmenus(self):
        """ Boolean of whether or not to render the submenu at all
            Checks that there is at least one visible submenu
        """
        if self._submenus:
            for m in self._submenus:
                if m.visible:
                    return True

        return False



class UserMenu(Menu):
    def __init__(self, name, routeFuncName, visible=True, submenus=[]):
        self.logoutMenu = Menu("Logout", "logout", False)
        submenus.append(self.logoutMenu)
        super().__init__(name, routeFuncName, visible, submenus)

    def isAuthenticated(self):
        return current_user and \
                current_user.is_authenticated()

    # Lets override visible() as a pseudo-hook
    @Menu.visible.getter
    def visible(self):
        # Change the names if we have auth
        if self.isAuthenticated():
            self.name = current_user.get_id()
            self.routeFuncName = "user"

            # Turn on the logout submenu
            self.logoutMenu.visible = True
        else:
            self.name = "Login"
            self.routeFuncName = "login"

            # Turn off the logout submenu
            self.logoutMenu.visible = False
        return super().visible


def createApplicationMenus():
    menus = context.projectVars["menus"]

    menus.append(Menu("Home", "index"))
    menus.append(Menu("About", "about"))

    # Add the user menu
    users = UserMenu("Login", "login")

    menus.append(users)

