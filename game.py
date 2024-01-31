import pygame
from snake import Snake, Food, Section
from setup import CONTROLS, WIDTH, HEIGHT, COLORS
from random import randint


pygame.init()
font = pygame.font.Font(None, 72)
text = font.render('Game Over', True, COLORS['white'])
place = text.get_rect(center=(WIDTH // 2, HEIGHT //2))


class Game:
    def __init__(self,
                 width=800,
                 height=800
                 ) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.snake = Snake(self.screen)
        self.food = []
        self.is_game_over = False
        self.snake.body.append(Section(0, 0))
        self.main_loop()

    def spawn_food(self) -> None:
        food = Food(
                randint(0, self.width - 30),
                randint(0, self.height - 30)
            )

        if food.rect.collidelist(
            [i.rect for i in self.snake.body]
        ) == -1:
            self.food.append(food)
        else:
            return self.spawn_food()
    
    def show_game_over(self) -> None:
        
        keys = pygame.key.get_pressed()
        if keys[CONTROLS['exit']]:
            print("!!!!!!!!!!!!!!!!!!!!!")
            self.is_game_over = False
            self.is_running = False
            
        self.screen.fill(COLORS['black'])
        self.screen.blit(text, place)
        pygame.display.flip()

    def handle_events(self) -> None:
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[CONTROLS['debug']]:
            self.snake.add_section()
        if not len(self.food):
            self.spawn_food()
        if self.snake.head.rect.colliderect(
            self.food[0].rect
        ):
            self.food.pop(0)
            self.snake.add_section()
            self.spawn_food()
        if not self.snake.head.rect.collidelist(
            [i.rect for i in self.snake.body][2::]
        ) == -1:
            self.is_game_over = True
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            if pressed_keys[CONTROLS['exit']]:
                self.is_running = False

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        self.snake.update()
        self.food[0].draw(self.screen)
        pygame.display.flip()

    def main_loop(self) -> None:
        while self.is_running:
            if not self.is_game_over:
                self.handle_events()
                self.render()
                self.clock.tick(20)
            else:
                self.show_game_over()


Game()
