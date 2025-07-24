import pyfiglet
from colorama import Fore, Back, Style
from colorama import init
init()
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

userText = input("what would you like to print?")
f = pyfiglet.Figlet(font='slant')
print(Fore.RED + f.renderText(userText))


# Suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuupppppppppppperrrrrrrrrlong
# comment
def example(): return {'has_key() is deprecated': True}.has_key(
    {'f': 2}.has_key(''))
