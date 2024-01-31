
document.addEventListener('DOMContentLoaded', function () {
    const upButton = document.getElementById('upButton');
    const downButton = document.getElementById('downButton');

    upButton.addEventListener('click', () => {
        if (paddle_left.rect.top > 0) {
            paddle_left.rect.y -= 10;
        }
    });

    downButton.addEventListener('click', () => {
        if (paddle_left.rect.bottom < HEIGHT) {
            paddle_left.rect.y += 10;
        }
    });
// i should link it to py
    const paddle_left = new Paddle(10, HEIGHT / 2 - PADDLE_HEIGHT / 2);
    const paddle_right = new Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT / 2 - PADDLE_HEIGHT / 2);
    const ball = new Ball();

    const all_sprites = new Set();
    all_sprites.add(paddle_left, paddle_right, ball);

    function gameLoop() {
        for (const event of pygame.event.get()) {
            if (event.type === pygame.QUIT) {
                pygame.quit();
                sys.exit();
            }
        }

        all_sprites.update();
        screen.fill(BLACK);
        pygame.draw.line(screen, WHITE, (WIDTH / 2, 0), (WIDTH /2, HEIGHT), 2);
        all_sprites.draw(screen);
        pygame.display.flip();
        clock. Tick(FPS);
        requestAnimationFrame(gameLoop);}
    gameLoop();
});
