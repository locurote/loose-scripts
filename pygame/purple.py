from random import randint
import base64
import gzip

import pygame as pg

BOOP_AUDIO = "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"

def main():
    pg.init()
    screen = pg.display.set_mode((600 * 16 / 9, 600))
    clock = pg.time.Clock()
    running = True

    # ball
    ball_rad = 20
    ball_pos = pg.Vector2(ball_rad, ball_rad)
    ball_vel = pg.Vector2(400, 400)
    ball_colors = [
        "indigo",
        "blueviolet",
        "darkviolet",
        "hotpink",
        "deeppink",
        "magenta",
        "darkorchid",
        "mediumorchid",
        "orchid",
    ]
    ball_color = ball_colors[0]

    # fps text
    def_font = pg.font.get_default_font()
    font = pg.font.Font(def_font, size=22)

    text = None
    fps_update_delay = 0.05
    fps_update_timer = 0

    # audio setup
    pg.mixer.init(44100, -16, 2, 2048)
    audio_gzip = base64.b64decode(BOOP_AUDIO)
    audio = gzip.decompress(audio_gzip)
    bounce_sound = pg.mixer.Sound(buffer=audio)
    bounce_sound.set_volume(0.5)
    channel = pg.mixer.Channel(0)

    while running:
        delta = clock.tick(60) / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill("purple")

        pg.draw.circle(screen, ball_color, ball_pos, ball_rad)

        # check for collisions
        x = ball_pos.x + ball_vel.x * delta
        if x + ball_rad > screen.get_width() or x - ball_rad < 0:
            ball_color = ball_colors[randint(0, len(ball_colors) - 1)]
            channel.play(bounce_sound)
            ball_vel.x *= -1

        y = ball_pos.y + ball_vel.y * delta
        if y + ball_rad > screen.get_height() or y - ball_rad < 0:
            ball_color = ball_colors[randint(0, len(ball_colors) - 1)]
            channel.play(bounce_sound)
            ball_vel.y *= -1

        # move ball
        ball_pos = ball_pos + ball_vel * delta

        fps_update_timer += delta
        if fps_update_timer > fps_update_delay:
            text = font.render("%.3f fps" % clock.get_fps(), True, "white")
            fps_update_timer = 0

        if text is not None:
            screen.blit(text, (20, 20))

        pg.display.flip()


if __name__ == "__main__":
    main()
