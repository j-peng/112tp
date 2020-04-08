import pygame
import random


# # # # # # # # # # # # # # # # # # # # #
###         initializing game         ###
# # # # # # # # # # # # # # # # # # # # #
pygame.init()

clock = pygame.time.Clock()

height = 750
width = 1100

# create the display surface
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height))

size = 200

# colors
green = (100, 200, 100)



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



# # # # # # # # # # # # # # # # # # # # #
###           loading sounds          ###
# # # # # # # # # # # # # # # # # # # # #

quack =  pygame.mixer.Sound('D:\\Documents\\Sophomore\\112\\tp\\quack.wav')



# # # # # # # # # # # # # # # # # # # # #
###              classes              ###
# # # # # # # # # # # # # # # # # # # # #

class Component(object):
    showHitBoxes = True
    def __init__(self, x, y, image, size):
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.hitBox = pygame.Rect(self.x, self.y, self.size, self.size)

    def updateHitBoxes(self):
        self.hitBox = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        screen.blit(self.image, (self.x, self.y))
        if self.showHitBoxes == True:
            pygame.draw.rect(screen, (255, 0, 0), self.hitBox, 1)

    def move(self, xDist, yDist):
        self.x += xDist
        self.y += yDist
        self.updateHitBoxes()


class Character(Component):
    def __init__(self, x, y, image, size):
        super().__init__(x, y, image, size)
        self.currBod = image

        self.bod = image

        self.legIndex = 0
        self.legList = duckLegs

        self.flapIndex = 0
        self.flapList = rightDuckFlapping

        self.quackIndex = 0
        self.quackList = rightDuckQuacking

        self.dir = 'right'
        self.beakHitBox = None
        self.heldObject = None

        self.speed = 10

        self.walking = False
        self.running = False
        self.jumping = False
        self.quacking = False
        self.flapping = False

    def updateHitBoxes(self):
        if self.dir == 'right':
            self.beakHitBox = pygame.Rect(self.x + self.size * 0.9, self.y + self.size * 0.14, 25, 10)
        elif self.dir == 'left':
            self.beakHitBox = pygame.Rect(self.x + self.size * 0.12, self.y + self.size * 0.14, 25, 10)

    def move(self, keys):
        xDist = 0
        yDist = 0
        if keys[pygame.K_UP]:
            yDist = -self.speed
        elif keys[pygame.K_DOWN]:
            yDist = self.speed
        elif keys[pygame.K_LEFT]:
            xDist = -self.speed
            self.bod = duckLeft
            self.legList = leftDuckLegs
            self.flapList = leftDuckFlapping
            self.quackList = leftDuckQuacking

            if self.dir == 'right':
                # changed direction
                self.dir = 'left'
                if self.heldObject!= None:
                    self.heldObject.flip('left')

        elif keys[pygame.K_RIGHT]:
            xDist = self.speed
            self.bod = duckRight
            self.legList = duckLegs
            self.flapList = rightDuckFlapping
            self.quackList = rightDuckQuacking

            if self.dir == 'left':
                # changed direction
                self.dir = 'right'
                if self.heldObject!= None:
                    self.heldObject.flip('right')

        if keys[pygame.K_w]:
            self.flapping = True
        else:
            self.flapping = False
            self.currBod = self.bod

        if keys[pygame.K_q]:
            self.quacking = True
        else:
            self.quacking = False

        if self.heldObject != None:
            self.heldObject.move(xDist, yDist)

        self.y += yDist
        self.x += xDist
        if xDist == 0 and yDist == 0:
            # if it didn't move, it's not walking so give it standing legs
            self.walking = False
            self.legIndex = 0
        self.updateHitBoxes()

    def updateLegs(self):
        self.legIndex += 1
        if self.legIndex > len(duckLegs) - 1:
            self.legIndex = 0

    def flap(self):
        self.currBod = self.flapList[self.flapIndex]
        self.flapIndex += 1
        if self.flapIndex > 2:
            # once you reach the last flap state, switch between the last 2
            self.flapIndex = 0

    def quack(self):
        quack.play()
        self.currBod = self.quackList[self.quackIndex]
        self.quackIndex += 1
        self.quackIndex %= len(self.quackList)

    def update(self):
        if self.walking == True:
            self.updateLegs()
        if self.flapping == True:
            self.flap()
        if self.quacking == True:
            self.quack()
            # can't quack and hold
            self.heldObject = None

        screen.blit(self.currBod, (self.x, self.y))
        screen.blit(self.legList[self.legIndex], (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.beakHitBox, 1)

class Object(Component):
    def __init__(self, x, y, size, weight, image):
        super().__init__(x, y, image, size)
        self.weight = weight

    def flip(self, direction):
        if direction == 'left':
            self.x -= duck.size * 0.9
        else:
            self.x += duck.size * 0.9


# # # # # # # # # # # # # # # # # # # # #
###         creating objects          ###
# # # # # # # # # # # # # # # # # # # # #

duck = Character(100, 100, duckRight, 200)
apple = Object(500, 200, 50, 6, appleImg)



# # # # # # # # # # # # # # # # # # # # #
###           main game loop          ###
# # # # # # # # # # # # # # # # # # # # #


playing = True
while playing:
    time = clock.tick(20) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if duck.heldObject == None:
                    # try to pick something up
                    if duck.beakHitBox.colliderect(apple.hitBox):
                        duck.heldObject = apple
                        duck.speed = 10 * (4 / duck.heldObject.weight)

                else:
                    # drop object
                    duck.heldObject = None
                    duck.speed = 10
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_UP or
                  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                duck.walking = True
            
            #elif (event.key == pygame.K_q):
                # quack
                
            
            #elif (event.key == pygame.K_w):
                # flap
            #    duck.flapping = True

    keys = pygame.key.get_pressed()
    duck.move(keys)
    screen.fill((200, 235, 250))
    pygame.draw.rect(screen, green, pygame.Rect(0, height * 3/4, width, height * 1/4))
        
    apple.update()
    duck.update()
    pygame.display.flip()

pygame.quit()