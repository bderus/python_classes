from Languages.Language import Language


class LanguagePl(Language):
    def __init__(self):
        Language.__init__(self, "PL")

    def print_main_menu_options(self):
        print("Witaj w App, wybierz jedną opcję z poniższego menu: ")
        print("1. Password Manager menu")
        print("2. Kółko i krzyżyk - Maciek")
        print("3. Kółko i krzyżyk - Piotrek")
        print("4. Wybierz język")
        print("5. Exit App")

    def get_wrong_option_info(self):
        return "Nierozpoznana opcja"

    def get_passwords_menu_info(self):
        return "Czy chciałbyś dodać (add) nowe hasło czy wyświetlić (view) istniejące hasła? Wpisz q aby cofnąć "

    def get_main_menu_info(self):
        return "Wpisz numer opcji aby kontynuować: "

    def get_select_language_info(self):
        return "Wybierz język aplikacji, dostępne języki: PL, EN: "