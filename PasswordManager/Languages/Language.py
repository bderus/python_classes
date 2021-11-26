from abc import ABC, abstractmethod


class Language(ABC):
    def __init__(self, selected_lang):
        self.selected_lang = selected_lang

    def get_selected_lang(self):
        return self.selected_lang

    @abstractmethod
    def print_main_menu_options(self):
        pass

    @abstractmethod
    def get_main_menu_info(self):
        pass

    @abstractmethod
    def get_passwords_menu_info(self):
        pass

    @abstractmethod
    def get_wrong_option_info(self):
        pass

    @abstractmethod
    def get_select_language_info(self):
        pass
