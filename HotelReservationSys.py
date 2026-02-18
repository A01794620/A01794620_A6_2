from cli.MenuHandler import MenuHandler

def start(name):
    MenuHandler.menu_dynamic_handler()
    print(name)

if __name__ == '__main__':
    names = [
        'Roberto Brenes Mesen', 'Pedro Bull Narito', 'Maria Torres Alberatoe',
        'Luis Manual de la Torre', 'Hernan Derbez Pure', 'Eloisa Asofeifa Nuñez'
    ]
    start(names[0])