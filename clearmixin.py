import os


class ClearMixin:
    def clear_screen(self):
        """
        Checks the operating system and uses
        the correct command to clear the console
        """
        if os.name == 'nt':
            # Clear screen command for windows
            os.system('cls')
        elif os.name == 'posix':
            # Clear screen command for Linux
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
