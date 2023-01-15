import pygame


win_width = 852
win_height = 480

# spritesPath = "Pygame\\Random game\\sprites\\"
spritesPath = "/media/rperret/OS/Users/julo5/Desktop/python/projects/Pygame/Random game/sprites/"

walkRight = [
    pygame.image.load(
        spritesPath + "R1.png"
    ),
    pygame.image.load(
        spritesPath + "R2.png"
    ),
    pygame.image.load(
        spritesPath + "R3.png"
    ),
    pygame.image.load(
        spritesPath + "R4.png"
    ),
    pygame.image.load(
        spritesPath + "R5.png"
    ),
    pygame.image.load(
        spritesPath + "R6.png"
    ),
    pygame.image.load(
        spritesPath + "R7.png"
    ),
    pygame.image.load(
        spritesPath + "R8.png"
    ),
    pygame.image.load(
        spritesPath + "R9.png"
    ),
]
walkLeft = [
    pygame.image.load(
        spritesPath + "L1.png"
    ),
    pygame.image.load(
        spritesPath + "L2.png"
    ),
    pygame.image.load(
        spritesPath + "L3.png"
    ),
    pygame.image.load(
        spritesPath + "L4.png"
    ),
    pygame.image.load(
        spritesPath + "L5.png"
    ),
    pygame.image.load(
        spritesPath + "L6.png"
    ),
    pygame.image.load(
        spritesPath + "L7.png"
    ),
    pygame.image.load(
        spritesPath + "L8.png"
    ),
    pygame.image.load(
        spritesPath + "L9.png"
    ),
]
bg = pygame.image.load(
    spritesPath + "bg.jpg"
)
char = pygame.image.load(
    spritesPath + "standing.png"
)


pygame.init()
pygame.display.set_caption("Game")
window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = True
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y + 15, 25, 47)

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                window.blit(walkRight[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y + 15, 25, 47)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)
        pygame.draw.circle(window, (0,255,0), (self.x, self.y), 1)
        pygame.draw.circle(window, (255, 255, 0), (self.x + 20, self.y + 15), 1)


class enemy(object):
    walkRight = [
        pygame.image.load(
            spritesPath + "/R1E.png"
        ),
        pygame.image.load(
            spritesPath + "/R2E.png"
        ),
        pygame.image.load(
            spritesPath + "/R3E.png"
        ),
        pygame.image.load(
            spritesPath + "/R4E.png"
        ),
        pygame.image.load(
            spritesPath + "/R5E.png"
        ),
        pygame.image.load(
            spritesPath + "/R6E.png"
        ),
        pygame.image.load(
            spritesPath + "/R7E.png"
        ),
        pygame.image.load(
            spritesPath + "/R8E.png"
        ),
        pygame.image.load(
            spritesPath + "/R9E.png"
        ),
        pygame.image.load(
            spritesPath + "/R10E.png"
        ),
        pygame.image.load(
            spritesPath + "/R11E.png"
        ),
    ]
    walkLeft = [
        pygame.image.load(
            spritesPath + "/L1E.png"
        ),
        pygame.image.load(
            spritesPath + "/L2E.png"
        ),
        pygame.image.load(
            spritesPath + "/L3E.png"
        ),
        pygame.image.load(
            spritesPath + "/L4E.png"
        ),
        pygame.image.load(
            spritesPath + "/L5E.png"
        ),
        pygame.image.load(
            spritesPath + "/L6E.png"
        ),
        pygame.image.load(
            spritesPath + "/L7E.png"
        ),
        pygame.image.load(
            spritesPath + "/L8E.png"
        ),
        pygame.image.load(
            spritesPath + "/L9E.png"
        ),
        pygame.image.load(
            spritesPath + "/L10E.png"
        ),
        pygame.image.load(
            spritesPath + "/L11E.png"
        ),
    ]

    def __init__(self, x, y, widht, height, end):
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 5
        self.hitbox = (self.x + 20, self.y + 5, 25, 50)
        self.hits = 0

    def draw(self, window):
        self.move()
        # if self.walk_count + 1 >= 33:
        #     self.walk_count = 0

        # if self.vel > 0:
        #     window.blit(self.walkRight[self.walk_count // 3], (self.x, self.y))
        #     self.walk_count += 1
        # else:
        #     window.blit(self.walkLeft[self.walk_count // 3], (self.x, self.y))
        #     self.walk_count += 1
        self.hitbox = (self.x + 20, self.y + 5, 25, 50)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)
        pygame.draw.circle(window, (0,255,0), (self.x, self.y), 1)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):
        self.hits += 1
        print(self.hits)


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


on_plateform = False
ground = win_height


def gravity():
    global y
    global on_plateform
    if on_plateform is False:
        if man.y + man.height < ground:
            man.y += g_force
        else:
            man.y = man.y

def redraw_game_win():
    # window.blit(bg, (0, 0))
    window.fill((255, 255, 255))
    man.draw(window)
    goblin.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()


lunched = True
cooldown = 0
man = player(10, win_height - 64, 64, 64)
goblin = enemy(100, win_height - 64, 64, 64, 450)
bullets = []
while lunched:
    clock.tick(27)

    if cooldown > 0:
        cooldown += 1
    if cooldown > 3:
        cooldown = 0

    ### Borders
    if man.y > win_height - man.height:
        man.y = win_height - man.height
    if man.x + man.width + man.vel > win_width:
        man.x = win_width - man.width
    if man.x <= 0:
        man.x = 0
    if man.y < 0:
        man.y = win_height
    ###

    ### Player Mouvement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] == 1:
        man.right = True
        man.left = False
        man.standing = False
        man.x += man.vel
    elif keys[pygame.K_q] == 1:
        man.right = False
        man.left = True
        man.standing = False
        man.x -= man.vel
    else:
        man.standing = True
        man.walk_count = 0

    if keys[pygame.K_LSHIFT] == 1:
        sprint = True
    else:
        sprint = False

    if sprint is True:
        man.vel = 10
    else:
        man.vel = 5

    if man.is_jump is False:
        if keys[pygame.K_SPACE] == 1:
            man.is_jump = True
        gravity()
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
    ###

    if keys[pygame.K_z] == 1 and cooldown == 0:
        if man.left is True:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(
                    int(man.x + man.width // 2),
                    int(man.y + man.height // 2),
                    5,
                    (0, 0, 0),
                    facing,
                )
            )
        cooldown = 1

    for bullet in bullets:
        if bullet.x < win_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
        if (
            goblin.hitbox[0] < bullet.x < goblin.hitbox[0] + goblin.hitbox[2]
            and goblin.hitbox[1] < bullet.y < goblin.hitbox[1] + goblin.hitbox[3]
        ):
            goblin.hit()
            bullets.pop(bullets.index(bullet))

    redraw_game_win()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False

pygame.quit()
