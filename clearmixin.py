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
         ______     __  __     __     ______        ______     ______     __    __     ______    
        /\  __ \   /\ \/\ \   /\ \   /\___  \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
        \ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
         \ \___\_\  \ \_____\  \ \_\   /\_____\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
          \/___/_/   \/_____/   \/_/   \/_____/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 

        """
        print(LOGO)
