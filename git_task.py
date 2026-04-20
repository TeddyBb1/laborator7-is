import random
import pygame


WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
BACKGROUND_COLOR = (0, 0, 0)
REGENERATE_INTERVAL_MS = 5000


def generate_color_grid():
    """Generează o matrice 10x10 cu culori random RGB."""
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(screen, color_grid):
    """Desenează grila colorată în fereastră."""
    screen.fill(BACKGROUND_COLOR)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = color_grid[row][col]
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()


def main():
    """Rulează aplicația și regenerează grila la fiecare 5 secunde."""
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")

    color_grid = generate_color_grid()
    running = True

    last_update_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()

        if current_time - last_update_time >= REGENERATE_INTERVAL_MS:
            color_grid = generate_color_grid()
            last_update_time = current_time

        draw_grid(screen, color_grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()