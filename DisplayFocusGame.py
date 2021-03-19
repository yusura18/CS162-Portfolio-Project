# Author: Breanna Moore
# Date: 12/11/2020
# Description: Display for Focus game.

import pygame
import pygame_menu
import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        #self.master = master
        self.pack()
        #self.create_widgets()

    # def create_widgets(self):
    #     self.hi_there = tk.Button(self)
    #     self.hi_there["text"] = "Hello World\n(click me)"
    #     self.hi_there["command"] = self.say_hi
    #     self.hi_there.pack(side="top")
    #
    #     self.quit = tk.Button(self, text="QUIT", fg="red", command = self.master.destroy)
    #     self.quit.pack(side="bottom")
    #
    # def say_hi(self):
    #     print("Hi there, everyone!")


class Application:

    def __init__(self):
        pygame.init()
        self._FPS = 30
        self._framepersec = pygame.time.Clock()
        self._menu = None
        self._running = True
        self.size = self.weight, self.height = 1280, 800
        self._display_surf = pygame.display.set_mode(self.size) #pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((0,0,0))
        pygame.display.set_caption("Focus Game")
        self._color_red = pygame.Color(255, 0, 0)
        self._color_green = pygame.Color(0, 255, 0)
        self._color_blue = pygame.Color(0, 0, 255)
        self._color_orange = pygame.Color(255, 140, 0)
        self._color_board = pygame.Color(250, 235, 215)
        #pygame.draw.polygon(self._display_surf, (176,224,230), [(170,50), (1100,50), (1100,750), (176,750)], 0)
        #pygame.draw.polygon(self._display_surf, self._color_board,
        #                    [(490, 100), (790, 100), (940, 250), (940, 550), (790, 700), (490, 700), (340, 550), (340, 250)], 0)


    def create_menu(self):
        """"""
        self._menu = pygame_menu.Menu(300, 400, "Welcome", theme=pygame_menu.themes.THEME_SOLARIZED)
        self._menu.add_selector("Number of Players: ", [("One", 1), ("Two", 2)], onchange=self.set_number_players)
        self._menu.add_button("Play", self.start_the_game)
        self._menu.add_button("Quit", pygame_menu.events.EXIT)
        #self._menu.mainloop(self.get_display_surf())
        #pass

    def get_display_surf(self):
        """Return display surf"""
        return self._display_surf

    def get_menu(self):
        """Return menu"""
        #return self._menu
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while self._running:
            self.create_menu()
            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.update()
            self.on_loop()
            self.on_render()
            self._menu.mainloop(self.get_display_surf())

    def start_the_game(self):
        """"""
        if self._menu.is_enabled():
            self._menu.disable()
            pygame.draw.polygon(self._display_surf, (176, 224, 230), [(170, 50), (1100, 50), (1100, 750), (176, 750)], 0)
            pygame.draw.polygon(self._display_surf, self._color_board,
                            [(490, 100), (790, 100), (940, 250), (940, 550), (790, 700), (490, 700), (340, 550),
                            (340, 250)], 0)
            pygame.display.update()
        #pass

    def set_number_players(self, value, num_players):
        """"""
        pass


def main():
    """main function"""
    newgame = Application()
    newgame.on_execute()


if __name__ == '__main__':
    main()