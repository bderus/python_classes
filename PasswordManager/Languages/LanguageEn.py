from Languages.Language import Language


class LanguageEn(Language):
    def __init__(self):
        Language.__init__(self, "EN")

    def print_main_menu_options(self):
        print("Welcome to App, please select one option from menu below: ")
        print("1. Password Manager menu")
        print("2. Choose language")
        print("3. Exit App")

    def get_wrong_option_info(self):
        return "Invalid option"

    def get_passwords_menu_info(self):
        return "Would you like to add a new password or view existing ones (view, add), type q to go back "

    def get_main_menu_info(self):
        return "Select option number to continue: "

    def get_select_language_info(self):
        return "Please select App language, available languages: PL, EN: "
