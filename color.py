from colorama import Fore, Back, Style

def color_factory(color):
    def f(s):
        return color + s + Fore.RESET
    return f

color_red = color_factory(Fore.RED)
color_green = color_factory(Fore.GREEN)
