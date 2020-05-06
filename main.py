import pygame
from data.bird import Bird
from data.pipe import Pipe
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
font = pygame.font.SysFont('agencyfb', 30)

score_updated = score = None


def redraw_window(bird, pipes):
    global score, score_updated
    screen.fill((51, 51, 51))
    score_text = font.render(f'Score: {score}', 1, (200, 200, 200))
    screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 0))

    bird.update()
    bird.show()

    for i in range(len(pipes)-1, -1, -1):
        pipes[i].update()

        ishit = bird.hits(pipes[i])
        if ishit:
            score -= 1

        if bird.passed(pipes[i]) and not score_updated:
            score += 1
            score_updated = True

        pipes[i].show(ishit)
        ishit = False

        if pipes[i].offscreen():
            pipes.pop(i)

    pygame.display.update()


def main():
    global score, score_updated
    bird = Bird(screen, 40, HEIGHT//2)
    pipes = []
    pipes.append(Pipe(screen))

    score_updated = False
    score = 0

    frame_count = 0
    while True:
        clock.tick(60)

        frame_count += 1
        if frame_count % 150 == 0:
            pipes.append(Pipe(screen))
            score_updated = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()

        redraw_window(bird, pipes)


if __name__ == "__main__":
    main()
