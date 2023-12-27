import os


class ClearMixin:
    def clear_screen(self):
        """
        Checks the operating system and uses
        the correct command to clear the console
        """
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

    def show_logo(self):
        LOGO = """
        ##############################################################
        #    #####                      #####                        #
        #   #     # #    # # ######    #     #   ##   #    # ######  #
        #   #     # #    # #     #     #        #  #  ##  ## #       #
        #   #     # #    # #    #      #  #### #    # # ## # #####   #
        #   #   # # #    # #   #       #     # ###### #    # #       #
        #   #    #  #    # #  #        #     # #    # #    # #       #
        #    #### #  ####  # ######     #####  #    # #    # ######  #
        ##############################################################
  """
        print(LOGO)
