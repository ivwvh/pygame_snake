import pygame
from setup import COLORS, CONTROLS, WIDTH, HEIGHT
from pygame.sprite import Sprite


SNAKE_SPEED = 30


class Section(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x, self.y = x, y
        self.previous_x, self.previous_y = 0, 0
        self.image = pygame.Surface((30, 30))
        self.image.fill(COLORS['white'])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,
                            self.y)
        self.current_direction = ''
        self.previous_direction = ''


class Snake(Sprite):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__()
        self.screen = screen
        self.body = []
        self.head = Section(500, 300)
        self.body.append(self.head)

    def change_head_direction(self) -> None:
        keys = pygame.key.get_pressed()
        self.body[0].previous_direction = self.body[0].current_direction
        if keys[CONTROLS['up']] and not self.body[0].current_direction == 'down':
            self.body[0].current_direction = 'up'
        if keys[CONTROLS['down']] and not self.body[0].current_direction == 'up':
            self.body[0].current_direction = 'down'
        if keys[CONTROLS['left']] and not self.body[0].current_direction == 'right':
            self.body[0].current_direction = 'left'
        if keys[CONTROLS['right']] and not self.body[0].current_direction == 'left':
            self.body[0].current_direction = 'right'

    def update_cords(self, index: int) -> None:
        self.body[index].previous_x, self.body[index].previous_y = (
            self.body[index].x,
            self.body[index].y
        )
        self.body[index].rect.center = (self.body[index].x,
                                        self.body[index].y)

    def add_section(self) -> None:
        self.body.append(Section(-50, -50))

    def move(self) -> None:
        for i, _ in enumerate(self.body):
            if i == 0:
                head = self.body[i]
                match head.current_direction:
                    case 'up':
                        self.update_cords(i)
                        head.y -= SNAKE_SPEED
                        head.previous_direction = head.current_direction
                    case 'down':
                        self.update_cords(i)
                        head.y += SNAKE_SPEED 
                        head.previous_direction = head.current_direction
                    case 'left':
                        self.update_cords(i)
                        head.x -= SNAKE_SPEED 
                        head.previous_direction = head.current_direction
                    case 'right':
                        self.update_cords(i)
                        head.x += SNAKE_SPEED
                        head.previous_direction = head.current_direction

                if head.rect.left >= WIDTH and head.current_direction == 'right':
                    head.x = -15
                if head.rect.right <= 0 and head.current_direction == 'left':
                    head.x = WIDTH
                if head.rect.bottom <= 0 and head.current_direction == 'up':
                    head.y = HEIGHT
                if head.rect.bottom >= HEIGHT and head.current_direction == 'down':
                    head.y = -15
            
            else:
                if self.body[i - 1].current_direction == 'down':
                    self.body[i].previous_x, self.body[i].previous_y = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].x, self.body[i].y = (
                        self.body[i - 1].previous_x,
                        self.body[i - 1].previous_y,
                    )
                    self.body[i].rect.center = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].previous_direction = self.body[i].current_direction
                    self.body[i].current_direction = 'down'

                if self.body[i - 1].current_direction == 'up':
                    self.body[i].previous_x, self.body[i].previous_y = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].x, self.body[i].y = (
                        self.body[i - 1].previous_x,
                        self.body[i - 1].previous_y,
                    )
                    self.body[i].rect.center = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].previous_direction = self.body[i].current_direction
                    self.body[i].current_direction = 'up'

                if self.body[i - 1].current_direction == 'left':
                    self.body[i].previous_x, self.body[i].previous_y = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].x, self.body[i].y = (
                        self.body[i - 1].previous_x,
                        self.body[i - 1].previous_y,
                    )
                    self.body[i].rect.center = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].previous_direction = self.body[i].current_direction
                    self.body[i].current_direction = 'left'

                if self.body[i - 1].current_direction == 'right':
                    self.body[i].previous_x, self.body[i].previous_y = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].x, self.body[i].y = (
                        self.body[i - 1].previous_x,
                        self.body[i - 1].previous_y,
                    )
                    self.body[i].rect.center = (
                        self.body[i].x,
                        self.body[i].y
                    )
                    self.body[i].previous_direction = self.body[i].current_direction
                    self.body[i].current_direction = 'right'

    def draw(self, screen: pygame.Surface) -> None:
        for section in self.body:
            screen.blit(
                section.image,
                (section.x, section.y)
            )

    def update(self) -> None:
        self.change_head_direction()
        self.move()
        self.draw(self.screen)


class Food(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x, self.y = x, y
        self.image = pygame.Surface((15, 15))
        self.image.fill(COLORS['white'])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,
                            self.y)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(
            self.image,
            (self.x, self.y)
        )
