import pygame

def main():
    running = True
    clock = pygame.time.Clock()
    dt = 0
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        
        
        
        dt = clock.tick(60) / 1000

        







if __name__ == "__main__":
    main()