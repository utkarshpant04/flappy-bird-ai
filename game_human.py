import pygame 
import os
import random

# pygame.init()

WIN_WIDTH = 600
WIN_HEIGHT = 800

bird_img = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird" + ".png")))
bird_img = pygame.transform.scale(bird_img, (100, 100))
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe" + ".png")))
pipe_img = pygame.transform.scale(pipe_img, (100, 800))
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg" + ".png")))

class Bird:
    IMG = bird_img
    MAX_ROT = 25
    ROT_VEL = 10
    TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.v = 0
        self.height = self.y

    def jump(self):
        self.vel = -10.5
        self.v = 0
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        self.v += 1.5*self.tick_count

        if d >= 16:
            d = 16
            self.v = 16
        if d < 0:
            d -= 2
            self.v = -2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROT + 25:
                self.tilt = self.MAX_ROT
        else:
            if self.tilt > -60:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        rotated_img = pygame.transform.rotate(self.IMG, self.tilt)
        new_rect = rotated_img.get_rect(center=self.IMG.get_rect(topleft=(self.x, self.y)).center)

        win.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.IMG)

    def over_collide(self):
        return self.y < 0 or self.y >= WIN_HEIGHT


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        win.blit(self.PIPE_TOP, (self.x, self.top))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        return False


class Game:

    def __init__(self):
        self.bird = Bird(200, 200)
        self.pipes = [Pipe(700)]
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")

    def draw_window(self):
        self.win.blit(bg_img, (0, 0))
        for pipe in self.pipes:
            pipe.draw(self.win)
        self.bird.draw(self.win)
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        score = 0
        self.win

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            self.bird.move()
            print(self.bird.v)
            rem = []
            add_pipe = False
            for pipe in self.pipes:
                if pipe.collide(self.bird):
                    run = False
                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x + pipe.PIPE_TOP.get_width() < self.bird.x:
                    add_pipe = True
                    pipe.passed = True
                pipe.move()

            if add_pipe:
                score += 1
                self.pipes.append(Pipe(600))

            for r in rem:
                self.pipes.remove(r)

            if self.bird.over_collide():
                run = False
            self.draw_window()

        pygame.quit()
        print("GAME OVER !!!")
        print("Score: {}".format(score))
        quit()


g = Game()
g.main()


