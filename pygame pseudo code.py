import pygame
import random

# # # # # # # # # # # # # # # # # # # # #
###         initializing game         ###
# # # # # # # # # # # # # # # # # # # # #
pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
groundY = 300
#globalX = 0


# create the display surface
screen = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen2 = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))

paused = False

# # # # # # # # # # # # # # # # # # # # #
###         helper functions          ###
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

# returns true is the two values are within n of each other
def isClose (value1, value2, n):
    if abs(value1 - value2) <= n:
        return True
    return False

def lowestSprite(spriteList):
    lowestVal = -1
    lowestSprite = None
    for sprite in spriteList:
        if sprite.rect.bottom > lowestVal:
            lowestVal = sprite.rect.bottom
            lowestSprite = sprite
    return lowestSprite

# distance between the center of 2 rects
def distance(rect1, rect2):
    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5

# randomly generate the map (place the platforms and objects)
# gerate idle location dictionaris based off of object locations
def generateMap():
    pass

def updateAll():
    for item in BackgroundObject.allBackgroundObjects:
        item.update()
    for item in GameObject.allGameObjects:
        item.update()
    
def displayCheckList():
    pass

# takes a list of tasks and initiates them into a dictionary linking to false (task not completed)
def initiateTasks(L):
    d = {}
    for elem in L:
        d[elem] = False
    return d

def generateWheatField(numWheat, offsetRight, spacing):
    wheatField = []
    oldWheatX = offsetRight
    for i in range(numWheat):
        dist = oldWheatX + int(abs(numWheat // 2 - i) * spacing)
        x = random.randrange(dist, dist + 20)
        wheatImg = random.choice(wheatPlants)
        wheatImg = pygame.transform.scale(wheatImg, (random.randrange(10, 20), random.randrange(150, 190)))
        wheatImg = pygame.transform.flip(wheatImg, random.choice([True, False]), False)
        wheat = BackgroundObject(x, wheatImg)
        wheatField.append(wheat)
        oldWheatX = x
    return wheatField


# # # # # # # # # # # # # # # # # # # # #
###           loading images          ###
# # # # # # # # # # # # # # # # # # # # #

crate = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\crate.png')
crate = pygame.transform.scale(crate, (80, 80))

appleImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\apple.png')
appleImg = pygame.transform.scale(appleImg, (50, 50))

# duck bodies
duckBod = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckBod.png')

flap0 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckFlap0.png')
flap1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckFlap1.png')
flap2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckFlap2.png')
duckFlapping = [flap0, flap1, flap2, flap1, flap0]

quack0 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckQuack0.png')
quack1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\duckQuack1.png')
duckQuacking = [quack0, quack1]

# duck legs
duckLegs1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs1.png')
duckLegs2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs2.png')
duckLegs3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs3.png')
duckLegs4 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs4.png') # standing
duckLegs5 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs5.png')
duckLegs6 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs6.png')
duckLegs7 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\legs7.png')

duckLegs = [duckLegs4, duckLegs1, duckLegs2, duckLegs3, duckLegs4, duckLegs5, duckLegs6, duckLegs7]


# people
# person 1
person1Stand = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1standBody.png')
person1Active = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1runBody.png')
person1Scared = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1scaredBody.png')
person1Legs0 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1Legs0.png')
person1Legs1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1Legs1.png')
person1Legs2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1Legs2.png')
person1Legs = [person1Legs0, person1Legs1, person1Legs2, person1Legs1, person1Legs0]
person1Head = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person1Head.png')

heading = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\arialRound.TTF', 30) 
paragraph = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\arialRound.TTF', 14) 


# environment
lakeImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\realLake.png')

# stage 1 environment
barnImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\barn.png')
soilImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\soilPatch.png')

# wheat
wheat1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat1.png')
wheat2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat2.png')
wheat3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat3.png')
wheatPlants = [wheat1, wheat2, wheat3]

# stage 1 objects
carrotImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\carrot.png')
lettuceImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\lettuce.png')
radishImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\radish.png')
carrotSeedImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\carrotSeeds.png')
lettuceSeedImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\lettuceSeeds.png')
radishSeedImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\radishSeeds.png')
tableImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\table.png')
bowlImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\bowl.png')
croissantImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\croissant.png')
baguetteImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\baguette.png')
loafImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\loaf.png')
keyImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\key.png')
wateringCanImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wateringCan.png')
hatImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\hat.png')

# # # # # # # # # # # # # # # # # # # # #
###           loading sounds          ###
# # # # # # # # # # # # # # # # # # # # #

quack =  pygame.mixer.Sound('D:\\Documents\\Sophomore\\112\\tp\\media\\quack.wav')


# # # # # # # # # # # # # # # # # # # # #
###              classes              ###
# # # # # # # # # # # # # # # # # # # # # 

"""
all object
 -> moving objects
    -> duck
    -> people
 -> non moving objects
    -> passive items
    -> platforms (can jump on)

all objects have: (x,y), update, move, gravity/falling

 -> moving objects - walk cycle, speed, runspeed
    -> duck - jump, flap, quack, pickup, swim (make legs disappear)
    -> people - idle locations/activities, state (chase, idle, scared)
 -> non moving objects
    -> passive items - weight
    -> platforms (can jump on) - top surface
"""

# view area sprite around moving objects
class RectSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        # make a rectangle
        self.rect = pygame.Rect(x, y, width, height)


class BackgroundObject(pygame.sprite.Sprite):

    allBackgroundObjects = pygame.sprite.Group()

    def __init__(self, x, image, overlapY = 0):
        self.x = x
        self.image = image

        self.rect = self.image.get_rect()
        self.y = groundY - self.rect.height + overlapY
        self.rect.y = self.y
        self.rect.x = self.x
        # add it to the allGameObjects group
        pygame.sprite.Sprite.__init__(self, BackgroundObject.allBackgroundObjects)

    # move the object in the xDir, yDir given
    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
        self.rect.y = self.y
        self.rect.x = self.x
    # update the object on screen
    def update(self):
        screen.blit(self.image, (self.x, self.y))



class GameObject(pygame.sprite.Sprite):
    allGameObjects = pygame.sprite.Group()
    allPeople = pygame.sprite.Group()
    # for all game Objects that are on screen (?)
    activeGameObjects = pygame.sprite.Group()
    globalX = 0

    @staticmethod
    def moveBackground(dir):
        if duck.running:
            moveSpeed = duck.runSpeed
        else:
            moveSpeed = duck.walkSpeed

        if dir == 'left':
            xDir = -moveSpeed
            GameObject.globalX -= moveSpeed
        elif dir == 'right':
            xDir = moveSpeed
            GameObject.globalX += moveSpeed
        for sprite in GameObject.allGameObjects:
            # might want to just move active object to increase efficiency?
            # move it unless its the held item
            if duck.heldItem != sprite:
                sprite.move(xDir, 0)
            # move all the people's target locations /activity coords
        for sprite in BackgroundObject.allBackgroundObjects:
            sprite.move(xDir, 0)
        
        # update their idle dictionaries
        for person in GameObject.allPeople:
            d = person.idleActivities
            for key in d:
                value = d[key]
                x = value[0]
                d[key] = (x + xDir, value[1])


    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

        self.falling = True
        self.fallSpeed = 10

        # make a rectangle as its hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # add it to the allGameObjects group
        pygame.sprite.Sprite.__init__(self, GameObject.allGameObjects)

    # move the object in the xDir, yDir given
    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
    
    # test to see if it hit platform, return what was hit or None
    def testHitPlatform(self):
        if pygame.sprite.spritecollide(self, Platform.allPlatforms, False):
            return pygame.sprite.spritecollide(self, Platform.allPlatforms, False)[0]
        else:
            return None

    # make the object fall until it hits a platform or the ground
    def fall(self):
        self.move(0, self.fallSpeed)

        # check if it hit a platform
        platformHit = self.testHitPlatform()
        if (platformHit and isClose(self.rect.bottom, platformHit.rect.top, 5)):
            # snap the object to the top of the platform and make it no longer falling
            self.rect.bottom = platformHit.rect.top
            self.falling = False

        elif self.rect.bottom > groundY:
            self.falling = False
    
    # update the hitboxes
    def updateHitbox(self):
        self.rect.x = self.x
        self.rect.y = self.y

    # update the object on screen
    def update(self):
        if self.falling:
            self.fall()
        
        self.updateHitbox()

        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)



class MovingObject(GameObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist):
        super().__init__(x, y, image)
        self.walkCycleLegsList = walkCycleLegsList
        # body dictionary should come in the form: {scared: image, chase: image, flapList: [imageList]}
        self.bodyDictionary = bodyDictionary 

        # facing direction
        self.dir = 'right'

        self.state = 'stand'

        self.walkSpeed = walkSpeed
        self.runSpeed = runSpeed

        # start at the standing leg index (0)
        self.legIndex = 0

        self.running = False

        # n is how far around the thing can see
        self.viewDist = viewDist
        self.proxSprite = RectSprite(self.x-self.viewDist, self.y-self.viewDist, 
                                     self.rect.width+2*self.viewDist, self.rect.height+2*self.viewDist)
    
    def loadImageDict(self):
        imageDict = {'left': {'leg': flipImageList(self.walkCycleLegsList), 'body': {}}, 
                     'right': {'leg': self.walkCycleLegsList, 'body': {}}}

        for position in self.bodyDictionary:
            currImg = self.bodyDictionary[position]
            # start with right facing images
            imageDict['right']['body'][position] = currImg

            # flip them left
            if isinstance(currImg, list):
                left = flipImageList(currImg)
            else:
                left = flipImage(currImg)

            imageDict['left']['body'][position] = left

        return imageDict

    def getObjectsInView(self):
        objectsSeen = pygame.sprite.spritecollide(self, GameObject.allGameObjects, False)
        objectsSeen.remove(self)
        return objectsSeen

    def check(self, dir):
        # check if there is an object nearby in a direction
        # if there is, return the sprite, else return False
        objectsSeen = self.getObjectsInView()
        for sprite in objectsSeen:
            if dir == 'left':
                if isClose(sprite.rect.right, self.rect.left, 5):
                    return sprite
            elif dir == 'right':
                if isClose(sprite.rect.left, self.rect.right, 5):
                    return sprite
            elif dir == 'up':
                if isClose(sprite.rect.bottom, self.rect.bottom, 5):
                    return sprite
            elif dir == 'down':
                if isClose(sprite.rect.top, self.rect.bottom, 10):
                    return sprite

        return False

    # returns true if its being supported, starts falling otherwise
    def checkIsSupported(self):
        if self.testHitPlatform() == None and self.rect.bottom < groundY: # or its above the ground plane
            self.falling = True
        else:
            self.falling = False
            return True #it is supported

    # move using walk or run speeds
    def walk(self, inX, inY):
        if self.running:
            speed = self.runSpeed
        else:
            speed = self.walkSpeed

        # walk left only if theres nothing left of you or if there is something left of you, 
        # its bottom is above you
        # walk right is nothing right or right object is above you
        # walk up if nothing up or up objects bottom is above you
        # walk down if nothing below
        if inX < 0:
            sprite = self.check('left')
            if (sprite == False):
                # nothing left of you, move left
                self.move(-speed, 0)
            else:
                # something left of you, check its bottom
                if sprite.rect.bottom < self.rect.bottom:
                    self.move(-speed, 0)
        elif inX > 0:
            sprite = self.check('right')
            if (sprite == False):
                self.move(speed, 0)
            else:
                if sprite.rect.bottom < self.rect.bottom:
                    self.move(speed, 0)
            
        if inY < 0:
            sprite = self.check('up')
            if (sprite == False):
                self.move(0, -speed)
            else:
                if sprite.rect.bottom < self.rect.bottom:
                    self.move(0, -speed)
    
        elif inY > 0:
            sprite = self.check('down')
            if (sprite == False):
                self.move(0, speed)

        self.updateBody()
        self.updateLegs()
    
    # update body image
    def updateBody(self):
        self.currBodyImage = self.imageDict[self.dir]['body'][self.state]

    # animte legs using walkCycleLegsList
    def updateLegs(self):
        self.legIndex += 1
        if self.legIndex > len(self.walkCycleLegsList) - 1:
            self.legIndex = 0

    # update the hitboxes
    def updateHitbox(self):
        super().updateHitbox()
        self.proxSprite.rect.centerx = self.rect.centerx
        self.proxSprite.rect.centery = self.rect.centery

    # update the object on screen
    def update(self):
        if self.falling:
            self.fall()
        
        self.updateHitbox()
        screen.blit(self.currBodyImage, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
        pygame.draw.rect(screen, (0, 0, 0), self.proxSprite.rect, 1)

class Duck(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        # inspired by: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
        self.jumping = False
        self.jumpHeight = 10
        self.oldYPos = None

        self.flapping = False
        self.flapIndex = 0
        self.quacking = False
        self.quackIndex = 0
        self.swimming = False

        self.originalWalkSpeed = walkSpeed
        self.originalRunSpeed = runSpeed
        self.beakHitBox = RectSprite(self.x + self.rect.width * 0.85, 
                                                  self.y + self.rect.height * 0.1, 15, 10)

        self.heldItem = None
        self.onCoolDown = False

        # imageDict maps {left: {leg:[walk cycle list], body: {bodypos1: image}}, right: {flip left in a function}}
        self.imageDict = self.loadImageDict()
        self.currBodyImage = self.imageDict[self.dir]['body'][self.state]
    
    def walk(self, inX, inY):
        super().walk(inX, inY)
        self.checkInLake()
        self.checkIsSupported()
        self.checkBackgroundMove()
        self.onCoolDown = False

    def fall(self):
        # fall until:
        # 1. reaches top of ground, 
        # 2. hits a platform, 
        # 3. returns to original y position
        self.move(0, self.fallSpeed)

        # check if it hit a platform
        platformHit = self.testHitPlatform()
        if isClose(self.rect.bottom, groundY, 5):
            self.falling = False
        elif (platformHit and isClose(self.rect.bottom, platformHit.rect.top, 5)):
            # snap the object to the top of the platform and make it no longer falling
            self.rect.bottom = platformHit.rect.top
            self.falling = False
        elif self.rect.bottom == self.oldYPos:
            self.falling = False

    def jump(self):
        if self.jumpHeight == 10:
            # get the original y position of the duck before jumping
            self.oldYPos = self.rect.bottom
        self.move(0, -self.jumpHeight)
        self.jumpHeight -= 1
        if self.jumpHeight == 0:
            self.jumping = False
            self.falling = True
            self.jumpHeight = 10

    def flap(self):
        # act as a "cool down" after you pick something up and are forced to drop it, 
        # you start flapping and cant pick stuff up again until you stop flapping
        # do flap animation
        # when flap animation if finished: self.flapping = False
        self.currBodyImage = self.imageDict[self.dir]['body']['flap'][self.flapIndex]
        self.flapIndex += 1
        if self.flapIndex == len(self.imageDict[self.dir]['body']['flap']):
            self.flapIndex = 0
            self.flapping = False 
            self.state = 'stand'
            self.updateBody()

    def quack(self):
        self.currBodyImage = self.imageDict[self.dir]['body']['quack'][self.quackIndex]
        self.quackIndex += 1
        if self.quackIndex == len(self.imageDict[self.dir]['body']['quack']):
            self.quackIndex = 0
            self.quacking = False 
            self.state = 'stand'
            self.updateBody()
    
    def getObjectsTouching(self):
        itemsTouching = pygame.sprite.spritecollide(self.beakHitBox, PassiveObject.allPassiveObjects, False)
        #itemsTouching.remove(self)
        return itemsTouching

    # pickup the item if the beak is touching it
    def pickUp(self):
        # can't flap and pick up stuff
        if self.flapping == False and self.onCoolDown == False:
            items = self.getObjectsTouching()
            if len(items) != 0:
                # touching something, pick it up!
                self.heldItem = items[0]
                self.heldItem.isHeld = True
                self.heldItem.holder = duck

                # change speeds accordingly
                self.walkSpeed *= 4/self.heldItem.weight
                self.runSpeed *= 4/self.heldItem.weight
            
    
    # drop the held item
    def drop(self):
        if self.heldItem != None:
            # drop what you're holding
            self.heldItem.falling = True
            self.heldItem.isHeld = False
            self.heldItem.holder = None
            self.heldItem = None
            
            # return to original speeds
            self.walkSpeed = self.originalWalkSpeed
            self.runSpeed = self.originalRunSpeed
            self.onCoolDown = True

    # check if duck is in the lake
    def checkInLake(self):
        if (lake.rect.top < self.rect.bottom < lake.rect.bottom and
            lake.rect.left < self.rect.centerx < lake.rect.right):
            self.swimming = True
        else:
            self.swimming = False

    # check if duck approaches edges of screen, if it doesn, move the background
    def checkBackgroundMove(self):
        if isClose(self.rect.right, width, 100):
            GameObject.moveBackground('left')
        elif isClose(self.rect.left, 0, 100):
            GameObject.moveBackground('right')

    def updateBeak(self):
        if self.dir == 'right':
            self.beakHitBox = RectSprite(self.x + self.rect.width * 0.85, 
                                         self.y + self.rect.height * 0.1, 15, 10)
        elif self.dir == 'left':
            self.beakHitBox = RectSprite(self.x, 
                                         self.y + self.rect.height * 0.1, 15, 10)

    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
        self.updateBeak()
        if self.heldItem != None:
            self.heldItem.move(xDir, yDir)

    def update(self):
        if self.jumping:
            self.jump()
        if self.flapping:
            self.flap()
        if self.quacking:
            self.quack()

        if self.swimming == False:
            # only show legs when not swimming
            screen.blit(self.imageDict[self.dir]['leg'][self.legIndex], (self.x, self.y))
        super().update()
        pygame.draw.rect(screen, (0, 255, 0), self.beakHitBox.rect, 1)

class Person(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, headDictionary, walkSpeed, runSpeed, viewDist, idleActivities):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        self.headDictionary = headDictionary

        self.state = 'idle' # angry, scared, idle
        self.target = None # what or where the person is targeting

        # idleActivities is a dictionary with activities mapping to coordinate tuples
        self.idleActivities = idleActivities
        self.activity = None
        self.chooseLocation()

        # temporary target location to try and hit to get unstuck (this was not implemented, not sure if it needs to be)
        # self.tempTarget = (None, None)
        self.lastDeltaX = 0
        self.lastDeltaY = 0

        self.imageDict = self.loadImageDict()
        self.currBodyImage = self.imageDict[self.dir]['body'][self.state]

        self.heldItem = None

        pygame.sprite.Sprite.__init__(self, GameObject.allPeople)

    def loadImageDict(self):
        imageDict = {'left': {'leg': flipImageList(self.walkCycleLegsList), 'body': {}, 'head': {}}, 
                     'right': {'leg': self.walkCycleLegsList, 'body': {}, 'head': {}}}

        for position in self.bodyDictionary:
            currImg = self.bodyDictionary[position]
            # start with right facing images
            imageDict['right']['body'][position] = currImg

            # flip them left
            if isinstance(currImg, list):
                left = flipImageList(currImg)
            else:
                left = flipImage(currImg)

            imageDict['left']['body'][position] = left
        
        for position in self.headDictionary:
            currImg = self.headDictionary[position]
            imageDict['right']['head'][position] = currImg
            imageDict['left']['head'][position] = flipImage(currImg)
        
        return imageDict

    def tryMoveIn(self, dir):
        if self.running:
            speed = self.runSpeed
        else:
            speed = self.walkSpeed

        if dir in ['left', 'right']:
            if dir == 'left':
                i = -1
            else:
                i = 1
            spriteX = self.check(dir)
            if (spriteX == False):
                return i * speed
            elif spriteX.rect.bottom < self.rect.bottom:
                return i * speed
            return 0

        elif dir == 'up':
            if isClose(self.rect.bottom, groundY, 5):
                return 0
            spriteY = self.check(dir)
            if (spriteY == False):
                return -speed
            elif spriteY.rect.bottom < self.rect.bottom:
                return -speed
            return 0 
        
        elif dir == 'down':
            spriteY = self.check(dir)
            if (spriteY == False):
                return speed
            return 0

    def walk(self, inX, inY):
        self.checkIsSupported()
        self.checkForSpecialItem()
        deltaX = 0
        deltaY = 0

        if inX < 0:
            deltaX = self.tryMoveIn('left')
            self.dir = 'left'
                
        elif inX > 0:
            deltaX = self.tryMoveIn('right')
            self.dir = 'right'

        if inY < 0:
            deltaY = self.tryMoveIn('up')
            
        elif inY > 0:
            deltaY = self.tryMoveIn('down')

        if deltaX == 0 and deltaY == 0:
            self.legIndex = 0
            # we did not move
            # try moving in the opposite y dir
            
            if inY > 0:
                # if we tried to move down, try going up
                deltaY = self.tryMoveIn('up')

            elif inY < 0:
                # if we tried to move up, try going down
                deltaY = self.tryMoveIn('down')

            # if we still haven't moved, try moving in the x direction we have not tried
            if deltaY == 0:
                if inX > 0:
                    # we tried right, try left
                    deltaX = self.tryMoveIn('left')
                elif inX < 0:
                    deltaX = self.tryMoveIn('right')

            # boost to help get unstuck
            deltaX *= 2
            deltaY *= 2

        if self.lastDeltaX + deltaX == 0 and self.lastDeltaY + deltaY == 0:
            # we are stuck moving back and forth
            if self.lastDeltaX == -deltaX:
                # we're oscillating left and right
                #teporarily target somewhere left/right and then try again from there 
                # once we hit the temp target
                deltaY = self.tryMoveIn(random.choice(['down', 'up']))
            elif self.lastDeltaY == - deltaY:
                deltaX = self.tryMoveIn(random.choice(['left', 'right']))

        self.move(deltaX, deltaY)
        self.lastDeltaX = deltaX
        self.lastDeltaY = deltaY
        self.updateBody()
        self.updateLegs()

    def moveTowards(self, x, y):
        # if i hit an object on the side, i should try to move in the desired y dir
        # if i can't move in either directions, i should go down to go around the object
        # if that doesn't work, i should try and go up

        # if i hit an object above me, i should try and go in the desired 
        inX = 0
        inY = 0
        
        if y > self.rect.bottom:
            inY = 1
        elif y < self.rect.bottom:
            inY = -1
    
        if x > self.rect.centerx:
            inX = 1
        elif x < self.rect.centerx:
            inX = -1
        self.walk(inX, inY)

    def chooseLocation(self):
        # choose a new activity for the person to do
        newActivity = random.choice(list(self.idleActivities))
        while newActivity == self.activity:
            newActivity = random.choice(list(self.idleActivities))
        self.activity = newActivity
        self.timeStartingActivity = pygame.time.get_ticks()

    def idle(self):
        #currTime = pygame.time.get_ticks()

        # change the idle location of the person after some time passes
        #if currTime - self.timeStartingActivity > 5000:
            # 5% chance to change location
        if random.random() < 0.01:
            self.chooseLocation()

        location = self.idleActivities[self.activity]
        if isClose(location[0], self.rect.centerx, 3) and isClose(location[1], self.rect.centery, 3):
            # close enough, don't need to move
            self.legIndex = 0
            return

        self.moveTowards(location[0], location[1])
        

    def chase(self, other):
        self.running = True
        self.moveTowards(other.rect.centerx, other.rect.centery)
        if pygame.sprite.collide_rect(self, other):
            # if you hit the duck, duck drops item and flaps, person stop running and start idling
            duck.drop()
            duck.flapping = True
            self.state = 'idle'
            self.running = False
    
    def scared(self, other):
        # drop item
        if self.heldItem != None:
            self.heldItem.falling = True
            self.heldItem.isHeld = False
            self.heldItem.holder = None
            self.heldItem = None

        self.running = True
        inX = 0
        inY = 0
        if other.rect.centerx > self.rect.centerx:
            inX = -1
        elif other.rect.centerx < self.rect.centerx:
            inX = 1
        if other.rect.centery > self.rect.centery:
            inY = -1
        elif other.rect.centery < self.rect.centery:
            inY = 1
        self.walk(inX, inY)

        # no longer scared if far enough away
        if distance(self.rect, other.rect) >= 200:
            self.running = False
            self.state = 'idle'

    def lookTowards(self, other):
        if other.x < self.x:
            # look left
            self.dir = 'left'
        elif other.x > self.y:
            self.dir = 'right'

    # return True is other is within view(colliding with self.proxSprite)
    def withinView(self, other):
        if pygame.sprite.collide_rect(self.proxSprite, other):
            return True
        return False

    def checkForDuck(self):
        if self.withinView(duck):
            # duck is within view!
            if duck.heldItem != None:
                # chase the duck!
                self.state = 'angry'
            elif duck.quacking and random.random() < 0.05:
                self.state = 'scared'

                # scare the farmer task
                stage1TaskDict['scare the farmer'] = True

            else:
                if self.state != 'scared':
                    self.state = 'still'
                    self.updateBody()
                    self.legIndex = 0
                    self.lookTowards(duck)
        
        else:
            # stay angry even if duck is out of view
            if self.state != 'angry':
                self.state = 'idle'

    def checkForSpecialItem(self):
        if self.heldItem != None:
            # holding something, gotta move it
            self.heldItem.update()
        
        else:
            if self.state != 'scared':
            # not holding something and not scared, can pick stuff up
                collideList = pygame.sprite.spritecollide(self, SpecialItem.allSpecialItems, False)
                if len(collideList) > 0: # has something in it, pick it up
                    item = collideList[0]
                    self.heldItem = item
                    item.isHeld = True
                    item.holder = self
                    item.x = self.x + item.personLocation[0]
                    item.y = self.y + item.personLocation[1]

    def update(self):
        self.checkForDuck()

        if self.state == 'angry':
            self.chase(duck)
        elif self.state == 'idle':
            self.idle()
        elif self.state == 'scared':
            self.scared(duck)
        
        screen.blit(self.imageDict[self.dir]['leg'][self.legIndex], (self.x, self.y))
        super().update()
        screen.blit(self.imageDict[self.dir]['head']['idle'], (self.x, self.y))

class PassiveObject(GameObject):
    allPassiveObjects = pygame.sprite.Group()

    def __init__(self, x, y, image, weight):
        super().__init__(x, y, image)
        self.isHeld = False
        self.holder = None
        self.weight = weight

        # add it to the allPassiveObjects group
        pygame.sprite.Sprite.__init__(self, PassiveObject.allPassiveObjects)

    def move(self, xDir, yDir):
        super().move(xDir, yDir)
        if self.isHeld and isinstance(self.holder, Duck):
            self.y = duck.beakHitBox.rect.centery
            if duck.dir == 'right':
                self.x = duck.beakHitBox.rect.centerx
            elif duck.dir == 'left':
                self.x = duck.beakHitBox.rect.centerx - self.rect.width
                
class Item(PassiveObject):
    def __init__(self, x, y, image, weight):
        super().__init__(x, y, image, weight)
        
class SpecialItem(Item):
    allSpecialItems = pygame.sprite.Group()

    # these have interactions with people
    def __init__(self, x, y, image, weight, personLocation):
        super().__init__(x, y, image, weight)
        # location relative to person's x,y that the object will go
        self.personLocation = personLocation
        pygame.sprite.Sprite.__init__(self, SpecialItem.allSpecialItems)
    
    def update(self):
        super().update()
        if isinstance(self.holder, Person):
            self.x = self.holder.x + self.personLocation[0]
            self.y = self.holder.y + self.personLocation[1]

class Platform(PassiveObject):
    allPlatforms = pygame.sprite.Group()

    def __init__(self, x, y, image, weight):
        super().__init__(x, y, image, weight)
        self.falling = False
        pygame.sprite.Sprite.__init__(self, Platform.allPlatforms)



class Overlay(pygame.sprite.Sprite):
    def __init__(self, x, y, title, taskDict, width, height):
        self.x = x
        self.y = y
        self.title = title
        # linking tasks (keys) to if they are completed or not (T/F)
        self.taskDict= taskDict

        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = self.x
        self.rect.y = self.y

        self.isVisible = False

        self.heading = heading.render(title, True, (83, 71, 56)) 
        self.headingRect = self.heading.get_rect() 
        self.headingRect.x = self.x + 30
        self.headingRect.y = self.y + 20

    def renderTaskList(self, x, startY, spacing):
        for task in self.taskDict:
            taskText = ' - ' + task
            text = paragraph.render(taskText, True, (83, 71, 56))
            textRect = text.get_rect() 
            textRect.x = x
            textRect.y = startY
            screen.blit(text, textRect) 
            if self.taskDict[task] == True:
                # draw a line crossing it out
                pygame.draw.line(screen, (241, 97, 67), (textRect.left, textRect.centery),
                                (textRect.right, textRect.centery), 2)
            startY += spacing

    def update(self):
        pygame.draw.rect(screen, (236, 220, 189), self.rect)
        screen.blit(self.heading, self.headingRect) 
        self.renderTaskList(self.x + 50, self.y + 70, 30)



# # # # # # # # # # # # # # # # # # # # #
###           main game loop          ###
# # # # # # # # # # # # # # # # # # # # #

stage1Tasks = [ 'bake in the lake',
                'scare the farmer',
                'prepare a salad',
                'fill up the watering can',
                'sow the seeds',
                'free the cattle' ]

stage1TaskDict = initiateTasks(stage1Tasks)

# images (keys) : weight (value) - weight should be at least 4
vegDict = {lettuceImg: 10, carrotImg: 6, radishImg: 6}
seedDict = {lettuceSeedImg: 4, carrotSeedImg: 4, radishSeedImg: 4}
breadDict = {loafImg: 9, baguetteImg: 7, croissantImg: 6}

def placeItems(imgWeightDict, xLo, xHi, yLo, yHi):
    for image in imgWeightDict:
        Item(random.randrange(xLo, xHi), 
             random.randrange(yLo, yHi), image, imgWeightDict[image])

def initStage1(vegDict, seedDict, breadDict):
    idleLocations = {}
    barnX = random.randrange(500, 800)
    wheatField = generateWheatField(60, barnX - 200, 0.5)

    # place barn - place idle position near here
    barn = BackgroundObject(barnX, barnImg, 10)

    # place soil close to barn - place idle position near here
    soilX = barnX - 100
    BackgroundObject(soilX, soilImg, 200)

    # place vegetables and seeds close to soil
    soilMargin = 20
    for image in vegDict:
        # 2 of each veg
        for i in range(random.randrange(1, 3)):
            Item(soilX + soilMargin, 400, image, vegDict[image])
            soilMargin += random.randrange(50, 70)
    placeItems(seedDict, soilX, soilX + 200, 300, 500)

    # place table relative to barn - place idle position near here
    tableX = barn.rect.right + random.randrange(80, 150)
    table = Platform(tableX, 250, tableImg, 50)

    # place bread items and bowl close to table
    placeItems(breadDict, tableX - 50, table.rect.right + 50, 150, 300)

    # randomly place hat, watering can, keys(?)
    

initStage1(vegDict, seedDict, breadDict)

# higher spacing = less dense
#wheatField = generateWheatField(40, 300, 0.5)
#barn = BackgroundObject(500, barnImg, 10)
#soil = BackgroundObject(500, soilImg, 200)

lake = BackgroundObject(-800, lakeImg, 230)

box = Platform(200, 160, crate, 20)
box2 = Platform(200, 300, crate, 20)

idleActs1 = {'farm': (100, 200), 'garden': (300, 200)}

person1HeadDict = {'idle': person1Head}
person1ImageDict = {'idle': person1Stand, 'still': person1Stand, 'angry': person1Active, 'scared': person1Scared}
person1 = Person(500, 300, person1Stand, person1Legs, person1ImageDict, person1HeadDict, 2, 5, 100, idleActs1)
SpecialItem(300, 300, keyImg, 5, (50, 100))
SpecialItem(400, 300, hatImg, 5, (15, -12))

duckImageDict = {'stand': duckBod, 'flap': duckFlapping, 'quack': duckQuacking}
duck = Duck(100, 100, duckBod, duckLegs, duckImageDict, 5, 10, 5)

checklist = Overlay(200, 150, 'To Do', stage1TaskDict, 400, 300)



playing = True
while playing:
    time = clock.tick(20) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        
        elif event.type == pygame.KEYDOWN:
            # jump
            if event.key == pygame.K_SPACE and duck.jumping == False and duck.falling == False:
                # can't jump when jumping or falling
                duck.jumping = True

            # grab item
            elif event.key == pygame.K_j:
                pass   

            # flap
            elif event.key == pygame.K_l:
                duck.flapping = True
                duck.state = 'flap'

            # quack
            elif event.key == pygame.K_SEMICOLON:
                duck.drop()
                if duck.quacking == False:
                    quack.play()
                    duck.quacking = True

            # view checklist
            elif event.key == pygame.K_TAB:
                paused = not paused
                if paused == True:
                    #show checklist
                    checklist.isVisible = True
                    #displayCheckList()
                else:
                    checklist.isVisible = False

            # see menu
            elif event.key == pygame.K_ESCAPE:
                pass

            # exit game
            elif event.key == pygame.K_DELETE:
                playing = False                         

    keys = pygame.key.get_pressed()
    # check if running (holding k, else, not running)
    if keys[pygame.K_k]:
        duck.running = True 
    else:
        duck.running = False

    # check if trying to hold
    if keys[pygame.K_j]:
        if duck.heldItem == None:
            duck.pickUp()
    else:
        duck.drop()

    # check if moving in a direction
    if keys[pygame.K_w]:
        if duck.rect.bottom > groundY:
            duck.walk(0, -1)
    elif keys[pygame.K_s]:
        duck.walk(0, 1)
    elif keys[pygame.K_a]:
        duck.walk(-1, 0)
        duck.dir = 'left'
    elif keys[pygame.K_d]:
        duck.walk(1, 0)
        duck.dir = 'right'
    else:
        duck.legIndex = 0

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (100, 160, 110), (0, groundY, width, height - groundY))
    updateAll()
    if checklist.isVisible:
        checklist.update()
    pygame.display.flip()

pygame.quit()