"""
Viewers for PySmash
"""
from abc import ABC, abstractmethod
import pygame

class CharaterView(ABC):
    """
    Abstract Class for PySmash View
    """
    def __init__(self, game):
        """
        Construct a View object with the game as a parameter

        Args:
            game (Game): game to view
        """
        self._game = game

    @property
    def game(self):
        """
        Property that returns the game being viewed
        """
        return self._game

    @abstractmethod
    def draw(self):
        """
        A method that is an abstract method that does nothing
        """
        pass

class WindowView(CharaterView):
    """
    Class that draws the viewer to a PyGame window
    """
    def __init__(self, game, x_dim, y_dim):
        """
        Construct a WindowView object and create the window itself

        Args:
            game (Game): Game object to draw to screen
            x_dim (int): x dimension of window
            y_dim (int): y dimension of window
        """
        super().__init__(game)
        self.screen = pygame.display.set_mode([x_dim, y_dim])

    def draw(self):
        """
        Implement the 'draw' method, which draws the stage and sprites to
        the screen
        """
        self.game.all_sprites.update()
        self.screen.fill((255, 255, 255))
        self.game.all_sprites.draw(self.screen)
        pygame.display.flip()
