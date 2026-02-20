# APA https://console-menu.readthedocs.io/en/latest/installation.html
from cli.MenuHandler import MenuHandler
from setting.Setting import Setting

def start(name):
    MenuHandler.show_system_menu(Setting.SYSTEM_CANONICAL, Setting.SYSTEM_MISSION + "\n" + Setting.SYSTEM_SUPPORT_EMAIL)

if __name__ == '__main__':
    names = [
        'Roberto Brenes Mesen', 'Pedro Bull Narito', 'Maria Torres Alberatoe',
        'Luis Manual de la Torre', 'Hernan Derbez Pure', 'Eloisa Asofeifa Nuñez'
    ]
    start(".")