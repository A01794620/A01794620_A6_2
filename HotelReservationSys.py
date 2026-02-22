from setting.Setting import Setting
from cli.MenuHandler import MenuHandler

if __name__ == '__main__':
    MenuHandler.show_system_menu(Setting.SYSTEM_CANONICAL, Setting.SYSTEM_MISSION + "\n" + Setting.SYSTEM_SUPPORT_EMAIL)
