import sys

import password_manager

import config

from Languages.LanguageEn import LanguageEn
from Languages.LanguagePl import LanguagePl


def main_menu():
    config.selected_language.print_main_menu_options()
    selected_option = input(config.selected_language.get_main_menu_info())
    if selected_option == "3":
        sys.exit()

    if selected_option == "1":
        password_manager.passwords_menu()
    elif selected_option == "2":
        start_app()
    else:
        print(config.selected_language.get_wrong_option_info())
        main_menu()


def select_language():
    selected_lang = input(config.selected_language.get_select_language_info())

    if selected_lang.upper() == "PL":
        config.selected_language = LanguagePl()
    elif selected_lang.upper() == "EN":
        config.selected_language = LanguageEn()
    else:
        print(f"{config.selected_language.get_wrong_option_info()} - \"{selected_lang}\" option not available.")
        select_language()


def start_app():
    select_language()
    main_menu()
