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

class Overlay(object):
    def __init__(self, width, height, title, color):
        self.width = width
        self.height = height
        self.title = title
        self.color = color
    
    def drawOverlay(self):
        pygame.draw.rect(screen, self.color, 
                         ((width - self.width) // 2, (height - self.height) // 2, 
                         self.width, self.height))
        print(screen, self.color, (width - self.width) // 2, (height - self.height) // 2, self.width, self.height)

class Component(object):
    showHitBoxes = True
    allComponents = []
    # make an update all for the super class
    # like redraw all
    @staticmethod
    def updateAll():
        for component in allComponents:
            component.update()

    def __init__(self, x, y, image, size, weight):
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.weight = weight
        self.hitBox = pygame.Rect(self.x, self.y, self.size, self.size)
        self.isHeld = False
        Component.allComponents.append(self)

    def updateHitBoxes(self):
        self.hitBox = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        self.gravity()
        screen.blit(self.image, (self.x, self.y))
        if self.showHitBoxes == True:
            pygame.draw.rect(screen, (255, 0, 0), self.hitBox, 1)

    def gravity(self):
        pass
        #for item in PlatformObject.platoformObjects:
            # loop through items to find the one directly below you
            #if self.hitBox.bottom < groundY and self.isHeld == False:
                #self.y += self.weight
                #self.updateHitBoxes()

    def move(self, xDist, yDist):
        self.x += xDist
        self.y += yDist
        self.updateHitBoxes()

class ActiveComponent(Component):
    # things that move on its own like the duck and npcs
    def __init__(self, x, y, image, size, weight, legList):
        super().__init__(x, y, image, size, weight)

        self.legIndex = 0
        self.legList = legList
        self.walking = False
        self.running = False

class Person(ActiveComponent):
    def __init__(self, x, y, image, size, weight, legList, idlePositions):
        super().__init__(x, y, image, size, weight, legList)

        self.idlePositions = idlePositions

        self.walkSpeed = 1
        self.runSpeed = 2

    def targetDuck(self):
        pass

    def idle(self):
        pass

class Character(ActiveComponent):
    def __init__(self, x, y, image, size, weight, legList):
        super().__init__(x, y, image, size, weight, legList)
        self.currBod = image

        self.bod = image

        self.flapIndex = 0
        self.flapList = rightDuckFlapping

        self.quackIndex = 0
        self.quackList = rightDuckQuacking

        self.dir = 'right'
        self.beakHitBox = None
        self.heldObject = None

        self.speed = 10

        self.quacking = False
        self.flapping = False

        # inspired by: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
        self.jumping = False
        self.jumpHeight = 5

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

        if self.jumping == True:
            yDist -= self.jumpHeight * 5
            self.jumpHeight -= 1
            if self.jumpHeight < -5:
                self.jumpHeight = 5
                self.jumping = False

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
            if self.heldObject != None:
                self.heldObject.isHeld = False
                self.heldObject = None
        screen.blit(self.currBod, (self.x, self.y))
        screen.blit(self.legList[self.legIndex], (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.beakHitBox, 1)

class Object(Component):
    # passive components that don't move on its own
    def __init__(self, x, y, image, size, weight):
        super().__init__(x, y, image, size, weight)

    def flip(self, direction):
        if direction == 'left':
            self.x -= duck.size * 0.9
        else:
            self.x += duck.size * 0.9

class PlatformObject(Object):
    platformObjects = []
    # object you can jump on
    def __init__(self, x, y, image, size, weight):
        super().__init__(x, y, image, size, weight)
        self.platformObjects.append(self)
        self.topSurface = self.y



# # # # # # # # # # # # # # # # # # # # #
###         creating objects          ###
# # # # # # # # # # # # # # # # # # # # #

duck = Character(100, 100, duckRight, 200, 6, duckLegs)
apple = Object(500, 200, appleImg, 50, 6)
crate = PlatformObject(500, 100, crate, 80, 10)
toDo = Overlay(500, 500, 'To Do', (255, 255, 255))


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
            if event.key == pygame.K_e:
                if duck.heldObject == None:
                    # try to pick something up
                    if duck.beakHitBox.colliderect(apple.hitBox):
                        duck.heldObject = apple
                        apple.isHeld = True
                        duck.speed = 10 * (4 / duck.heldObject.weight)
                        #duck.jumpHeight -= duck.heldObject.weight * 0.5

                else:
                    # drop object
                    duck.heldObject = None
                    duck.speed = 10
                    apple.isHeld = False
                    #duck.jumpHeight = 5
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                duck.walking = True
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                duck.walking = True
                # double clicking left or right should make the duck run
                lastClickTime = pygame.time.get_ticks
                if event.key == pygame.K_LEFT:
                    lastKey = 'left'
                else:
                    lastKey = 'right'
                
            elif event.key == pygame.K_SPACE and duck.jumping == False:
                # if space is pressed and we're not jumping, we should jump
                duck.jumping = True

            elif event.key == pygame.K_TAB:
                print('hi')
                toDo.drawOverlay() # won't draw cos background color covers
 

    keys = pygame.key.get_pressed()
    duck.move(keys)
    screen.fill((200, 235, 250))
    pygame.draw.rect(screen, green, pygame.Rect(0, groundY, width, height - groundY))
        
    #apple.update()
    #crate.update()
    #duck.update()
    Component.updateAll()
    pygame.display.flip()

pygame.quit()