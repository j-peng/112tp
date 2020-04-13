import pygame
import random

# # # # # # # # # # # # # # # # # # # # #
###         initializing game         ###
# # # # # # # # # # # # # # # # # # # # #
pygame.init()

clock = pygame.time.Clock()

height = 600
width = 1100

# create the display surface
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height))

size = 200

# colors
green = (100, 200, 100)

# top of ground
groundY = height * 5/8

# # # # # # # # # # # # # # # # # # # # #
###           loading images          ###
# # # # # # # # # # # # # # # # # # # # #

# loading helper functions
# flips 1 image horizontally
def flipImage(image):
    return pygame.transform.flip(image, True, False)

# flips a list of images all horizontally
def flipImageList(L):
    temp = []
    for elem in L:
        elem = flipImage(elem)
        temp.append(elem)
    return temp

# duck bodies
duckRight = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckBod.png')
duckLeft = flipImage(duckRight)
duckRightHold = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckHold.png')
duckLeftHold = flipImage(duckRightHold)

flap1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckFlap1.png')
flap2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckFlap2.png')
flap3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckFlap3.png')
rightDuckFlapping = [flap1, flap2, flap3]
leftDuckFlapping = flipImageList(rightDuckFlapping)

quack1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckQuack1.png')
quack2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckQuack2.png')
rightDuckQuacking = [quack1, quack2]
leftDuckQuacking = flipImageList(rightDuckQuacking)

lean1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckLean1.png')
lean2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckLean2.png')
rightDuckLeaning = [lean1, lean2]
leftDuckLeaning = flipImageList(rightDuckLeaning)

leanHold1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckLeanHold1.png')
leanHold2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckLeanHold2.png')
rightDuckLeanHold = [leanHold1, leanHold2]
leftDuckLeanHold = flipImageList(rightDuckLeanHold)

# duck legs
legs1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs1.png')
legs2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs2.png')
legs3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs3.png')
legs4 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs4.png') # standing
legs5 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs5.png')
legs6 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs6.png')
legs7 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\legs7.png')

duckLegs = [legs4, legs1, legs2, legs3, legs4, legs5, legs6, legs7]
leftDuckLegs = flipImageList(duckLegs)

appleImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\apple.png')
appleImg = pygame.transform.scale(appleImg, (50, 50))
crate = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\crate.png')
crate = pygame.transform.scale(crate, (80, 80))


# # # # # # # # # # # # # # # # # # # # #
###           loading sounds          ###
# # # # # # # # # # # # # # # # # # # # #

quack =  pygame.mixer.Sound('D:\\Documents\\Sophomore\\112\\tp\\quack.wav')



# # # # # # # # # # # # # # # # # # # # #
###              classes              ###
# # # # # # # # # # # # # # # # # # # # # 

class Component(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x, y, image):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = image
       self.x = x
       self.y = y
       self.fallSpeed = 2
       self.falling = True

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = self.x
       self.rect.y = self.y
    
    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
        self.rect.x += xDir
        self.rect.y += yDir
        
        # check that the object is still supposrted or on the ground
        if (not pygame.sprite.spritecollide(self, platforms, False) 
            and self.rect.bottom < groundY):
            self.falling = True
        else:
            self.falling = False

    def gravity(self):
        self.move(0, self.fallSpeed)
            
        self.fallSpeed *= 1.1

        # if the sprite hits a platform and the platform is below the sprite, it's no longer falling
        if pygame.sprite.spritecollide(self, platforms, False):
            platform = pygame.sprite.spritecollide(self, platforms, False)[0]
            if self.rect.bottom > platform.rect.top:
                self.falling = False

    def doMovements(self):
        if self.falling:
            self.gravity()

    def update(self):
       screen.blit(self.image, (self.x, self.y))
       pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

class Duck(Component):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.speed = 10

        self.jumping = False
        self.jumpHeight = 8
    
    def jump(self):
        self.move(0, -self.jumpHeight)
        #self.y -= self.jumpHeight
        self.jumpHeight -= 1
        if self.jumpHeight <= 0:
            self.falling = True
        if self.jumpHeight == -8:
            self.jumpHeight = 8
            self.jumping = False
    
    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
        self.rect.x += xDir
        self.rect.y += yDir

        if self.jumping == False:
            # if not colliding with platform and bottom is not touching ground, it's falling
            if (not pygame.sprite.spritecollide(self, platforms, False) 
                and self.rect.bottom < groundY):
                self.falling = True
            else:
                self.falling = False

    def doMovements(self):
        if self.jumping:
            self.jump()
        elif self.falling:
            self.gravity()

platforms = pygame.sprite.Group()

class Platform(Component):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        platforms.add(self)
        self.falling = True
    
    def gravity(self):
        self.move(0, self.fallSpeed)
            
        self.fallSpeed *= 1.1

        #for platform in 
        print(self.rect.bottom, groundY)
        if self.rect.bottom > groundY:
            self.falling = False

# # # # # # # # # # # # # # # # # # # # #
###           main game loop          ###
# # # # # # # # # # # # # # # # # # # # #

duck = Duck(100, 100, duckRight)
crate = Platform(300, 200, crate)

playing = True
while playing:
    time = clock.tick(20) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and duck.jumping == False:
                duck.jumping = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if duck.rect.bottom > groundY:
            duck.move(0, -duck.speed)
    elif keys[pygame.K_s]:
        duck.move(0, duck.speed)
    elif keys[pygame.K_a]:
        duck.move(-duck.speed, 0)
    elif keys[pygame.K_d]:
        duck.move(duck.speed, 0)
    
    duck.doMovements()

    screen.fill((200, 235, 250))
    pygame.draw.rect(screen, green, pygame.Rect(0, groundY, width, height - groundY))
    duck.update()
    crate.update()
    pygame.display.flip()

pygame.quit()