import pygame
import random
import math
import os

# # # # # # # # # # # # # # # # # # # # #
###       Unfinished Duck Game        ###
###         Spring 2020 112 TP        ###
###             Janet Peng            ###
# # # # # # # # # # # # # # # # # # # # #


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

def generateBackground(numImgs, imgList, offsetRight, spacing, overlapY = 0):
    background = []
    oldItemX = offsetRight
    for i in range(numImgs):
        dist = oldItemX + int(abs(numImgs // 2 - i) * spacing)
        x = random.randrange(dist, dist + 20)
        img = random.choice(imgList)
        imgRect = img.get_rect()
        img = pygame.transform.scale(img, (int(imgRect.width * (random.randrange(8, 11) / 10)), 
                                           int(imgRect.height * (random.randrange(8, 11) / 10))))
        img = pygame.transform.flip(img, random.choice([True, False]), False)
        backgroundObj = BackgroundObject(x, img, overlapY)
        background.append(backgroundObj)
        oldItemX = x
    return background

# takes a list of items and returns True if they have been collected
# they have been collected if they are around the duck's "home" or starting point
# inspired by listFiles (http://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html)
def collectedItems(item):
        if isinstance(item, list):
            for elem in item:
                # check the if all the items in this list has been collected
                if collectedItems(elem) == False:
                    return False
            return True

        else:
            # base case
            if (isClose (item.rect.centerx, duckHome.rect.centerx, 80) and
                isClose (item.rect.centery, duckHome.rect.centery, 80)):
                # its close to home so it has been collected
                return True
            else:
                return False

# draw fence barricade
def drawBarricade(startX, n, image, crate = False, gate = False):
    barricadeList = []
    for i in range(n):
        y = height - i * 80
        if i == 3:
            if crate == True:
                platform = Platform(startX, y, crateImg, 25)
            elif gate == True:
                platform = Platform(startX, y, fenceGateImg, 100, False)
            else:
                platform = Platform(startX, y, image, 100, False)
        else:
            platform = Platform(startX, y, image, 100, False)
        barricadeList.append(platform)
    return barricadeList

def makeLoadString(imageName):
    filePath = str(os.getcwd())
    # get rid of file name
    filePath.replace('UnfinishedDuckGame.py', '')
    filePath += '\\media\\' + imageName + '.png'
    return filePath

#print (makeLoadString('hello'))

# # # # # # # # # # # # # # # # # # # # #
###           loading images          ###
# # # # # # # # # # # # # # # # # # # # #

# all images hand drawn by me :0

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

# person 2
person2Stand = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2standBody.png')
person2Active = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2runBody.png')
person2Scared = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2scaredBody.png')
person2Legs0 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2Legs0.png')
person2Legs1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2Legs1.png')
person2Legs2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2Legs2.png')
person2Legs = [person2Legs0, person2Legs1, person2Legs2, person2Legs1, person2Legs0]
person2Head = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person2Head.png')

# person 3
person3Stand = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3standBody.png')
person3Active = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3runBody.png')
person3Scared = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3scaredBody.png')
person3Legs0 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3Legs0.png')
person3Legs1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3Legs1.png')
person3Legs2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3Legs2.png')
person3Legs = [person3Legs0, person3Legs1, person3Legs2, person3Legs1, person3Legs0]
person3Head = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\person3Head.png')

# environment
lakeImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\lake.png')
caveImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\cave.png')
blanketImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\blanket.png')
signImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\sign.png')
tabSignImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tabSign.png')
lakeSignImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\lakeSign.png')
dragonSignImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\dragonSign.png')
crateImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\crate.png')
crateImg = pygame.transform.scale(crateImg, (80, 80))
fenceImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\fence.png')
fenceGateImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\fenceGate.png')

# stage 1 environment
barnImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\barn.png')
soilImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\soilPatch.png')

# wheat
wheat1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat1.png')
wheat2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat2.png')
wheat3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\wheat3.png')
wheatPlants = [wheat1, wheat2, wheat3]

# trees
tree1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tree1.png')
tree2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tree2.png')
tree3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tree3.png')
tree4 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tree4.png')
tree5 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\tree5.png')
trees = [tree1, tree2, tree3, tree4, tree5]

# distant houses
distantHouse1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\houseInDistance1.png')
distantHouse2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\houseInDistance2.png')
distantHouse3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\houseInDistance3.png')
distantHouses = [distantHouse1, distantHouse2, distantHouse3]

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
cowImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\cow.png')

# stage 2 objects
houseImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\house.png')
housePart2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\housePart2.png')
housePart3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\housePart3.png')
housePartsList = [housePart3, housePart2, houseImg]
doorImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\door.png')
flowerPatchImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\flowerPatch.png')
rock1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\rock1.png')
rock2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\rock2.png')
rock3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\rock3.png')
rock4 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\rock4.png')
rock5 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\rock5.png')
rockImgs = [rock1, rock2, rock3, rock4, rock5]
flower1 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\flower1.png')
flower2 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\flower2.png')
flower3 = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\flower3.png')
mailboxImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\mailbox.png')
newspaperImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\newspaper.png')
letterImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\letter.png')
shirtImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\shirt.png')
pantsImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\pants.png')
towelImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\towel.png')
sock1Img = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\sock1.png')
sock2Img = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\sock2.png')
laundryLineImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\laundryLine.png')
basketImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\basket.png')
ballImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\ball.png')
bbqImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\bbq.png')

# final objects
swordImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\sword.png')
bigRockImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\bigRock.png')
statueImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\statue.png')

# splash image
splashImg = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\media\\splash.png')

# # # # # # # # # # # # # # # # # # # # #
###     loading sounds and fonts      ###
# # # # # # # # # # # # # # # # # # # # #

# found on: https://freesound.org/
quack =  pygame.mixer.Sound('D:\\Documents\\Sophomore\\112\\tp\\media\\quack.wav')

titleFont =  pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\duckGameFont.TTF', 48)
heading = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\duckGameFont.TTF', 32) 
subheading = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\duckGameFont.TTF', 24)
paragraph = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\media\\duckGameFont.TTF', 18) 


# # # # # # # # # # # # # # # # # # # # #
###              classes              ###
# # # # # # # # # # # # # # # # # # # # # 

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

        self.visible = True

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
        if self.visible == True:
            screen.blit(self.image, (self.x, self.y))

class Game(object):
    def __init__(self):
        self.paused = False
        self.started = False
        self.showHitBoxes = False
        self.theSword = 'not found yet'
        self.statue = BackgroundObject(100, statueImg, 10)
        self.statue.visible = False

game = Game()

class GameObject(pygame.sprite.Sprite):
    allGameObjects = pygame.sprite.Group()
    allPeople = pygame.sprite.Group()
    # for all game Objects that are on screen (?)
    activeGameObjects = pygame.sprite.Group()
    globalX = 0

    @staticmethod
    def moveBackground(dir):
        #print(GameObject.globalX)
        duck.checkStage()
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

        self.visible = True

        # add it to the allGameObjects group
        pygame.sprite.Sprite.__init__(self, GameObject.allGameObjects)

    # move the object in the xDir, yDir given
    def move(self, xDir, yDir):
        self.x += xDir
        self.y += yDir
    
    # return the platform you(r bottom) is closest to
    def closestPlatform(self, L):
        closest = L[0]
        closestDist = abs(closest.rect.top - self.rect.bottom)
        for platform in L[1:]:
            newDist = abs(platform.rect.top - self.rect.bottom)
            if newDist < closestDist:
                closest = platform
                closestDist = newDist
        return closest

    # test to see if it hit platform, return what was hit or None
    def testHitPlatform(self):
        hitList = pygame.sprite.spritecollide(self, Platform.allPlatforms, False)
        if len(hitList) > 0:
            return self.closestPlatform(hitList)
        else:
            return None

    def checkIsSupported(self):
        if self.testHitPlatform() == None and self.rect.bottom < groundY: # or its above the ground plane
            self.falling = True
    
    # make the object fall until it hits a platform or the ground
    def fall(self):
        self.move(0, self.fallSpeed)

        # check if it hit a platform
        platformHit = self.testHitPlatform()
        if (platformHit and isClose(self.rect.bottom, platformHit.rect.top, 10)):
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
        self.checkIsSupported()
        if self.falling:
            self.fall()
        
        self.updateHitbox()

        if self.visible == True:
            screen.blit(self.image, (self.x, self.y))
            if game.showHitBoxes:
                pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

    def delete(self):
        self.kill()
        self.remove(self.groups())
        self.visible = False

class Cow(GameObject):
    def __init__(self, x, y, image, leftFence, rightFence):
        super().__init__(x, y, image)
        self.leftFence = leftFence
        self.rightFence = rightFence
        self.leftMost = self.leftFence.rect.left
        self.rightMost = self.rightFence.rect.right
        self.dir = 'right'
        self.xDir = 1
    
    def flip(self):
        self.xDir *= -1
        if self.dir == 'left':
            self.dir = 'right'
        else:
            self.dir = 'left'
        self.image = flipImage(self.image)

    def testHitPlatform(self):
        pass

    def checkIsSupported(self):
        pass

    def moveWithinFence(self):
        self.move(self.xDir, 0)
        if isClose(self.rect.right, self.rightMost, 10) and self.dir == 'right':
            self.flip()
        elif isClose(self.rect.left, self.leftMost, 10) and self.dir == 'left':
            self.flip()

    def updateBounds(self):
        # move cow bound postions
        self.leftMost = self.leftFence.rect.left
        self.rightMost = self.rightFence.rect.right

    def update(self):
        super().update()
        self.moveWithinFence()
        self.updateBounds()
    

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
            if isinstance(self, Duck) and self.heldItem == sprite:
                continue
            if dir == 'left':
                if isClose(sprite.rect.right, self.rect.left, 10) and sprite.visible:
                    return sprite
            elif dir == 'right':
                if isClose(sprite.rect.left, self.rect.right, 10) and sprite.visible:
                    return sprite
            elif dir == 'up':
                if isClose(sprite.rect.bottom, self.rect.bottom, 10) and sprite.visible:
                    return sprite
            elif dir == 'down':
                if isClose(sprite.rect.top, self.rect.bottom, 10) and sprite.visible:
                    return sprite

        return False

    # returns true if its being supported, starts falling otherwise
    #def checkIsSupported(self):
    #    if self.testHitPlatform() == None and self.rect.bottom < groundY: # or its above the ground plane
    #        self.falling = True
        #else:
        #    self.falling = False
        #    return True #it is supported

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
            if (sprite == False and self.rect.bottom < height):
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
        if game.showHitBoxes:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
            pygame.draw.rect(screen, (0, 0, 0), self.proxSprite.rect, 1)

class Duck(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        self.jumping = False
        self.jumpHeight = 12
        self.oldYPos = groundY

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

        # task stuff
        self.currStageTaskDict = None
        self.sowedSeeds = set() # set of seed (imgs) duck has sowed
    
    def walk(self, inX, inY):
        # restrain to 1900 (cave) - -6000 (sword)
        if -6100 <= GameObject.globalX <= 1900:
            super().walk(inX, inY)
            self.checkInLake()
            self.checkIsSupported()
            self.checkBackgroundMove()
            self.onCoolDown = False
        
        # this accounts for clipping
        elif 1900 < GameObject.globalX and self.dir == 'right':
            super().walk(inX, inY)
            self.checkInLake()
            self.checkIsSupported()
            self.checkBackgroundMove()
            self.onCoolDown = False
        elif -6100 > GameObject.globalX and self.dir == 'left':
            super().walk(inX, inY)
            self.checkInLake()
            self.checkIsSupported()
            self.checkBackgroundMove()
            self.onCoolDown = False
        #print(GameObject.globalX, self.dir)

    def fall(self):
        # fall until:
        # 1. reaches top of ground 
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
        elif isClose(self.rect.bottom, self.oldYPos, 5):
            self.falling = False


    # inspired by: https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
    def jump(self):
        if self.jumpHeight == 12:
            # get the original y position of the duck before jumping
            self.oldYPos = self.rect.bottom
        self.move(0, -self.jumpHeight)
        self.jumpHeight -= 1
        if self.jumpHeight == 0:
            self.jumping = False
            self.falling = True
            self.jumpHeight = 12

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
                item = items[0]
                # touching something, try to pick it up!
                # check if it's a platform you can't pick up
                if isinstance(item, Platform):
                    if item.canHold == True:
                        self.heldItem = item
                        self.heldItem.isHeld = True
                        self.heldItem.holder = duck

                        # change speeds accordingly
                        self.walkSpeed *= 4/self.heldItem.weight
                        self.runSpeed *= 4/self.heldItem.weight
                
                        # check if you completed any tasks
                        self.checkTasks()
                    
                # not a platform, can hold
                else:
                    self.heldItem = item
                    if item == game.theSword:
                        # flip it
                        item.image = pygame.transform.flip(item.image, False, True)
                        self.completeTask('wield the sword')
                    self.heldItem.isHeld = True
                    self.heldItem.holder = duck

                    # change speeds accordingly
                    self.walkSpeed *= 4/self.heldItem.weight
                    self.runSpeed *= 4/self.heldItem.weight
                
                    # check if you completed any tasks
                    self.checkTasks()
            
    
    # drop the held item
    def drop(self):
        if self.heldItem != None:
            # drop what you're holding
            if self.heldItem == game.theSword:
                # flip it when you drop it
                self.heldItem.image = pygame.transform.flip(self.heldItem.image, False, True)
            self.heldItem.falling = True
            self.heldItem.isHeld = False
            self.heldItem.holder = None
            self.heldItem = None
            
            # return to original speeds
            self.walkSpeed = self.originalWalkSpeed
            self.runSpeed = self.originalRunSpeed
            self.onCoolDown = True

            # check if you completed any tasks
            self.checkTasks()
    

    def checkStage(self):
        #print(GameObject.globalX)
        if self.currStageTaskDict == None:
            if GameObject.globalX < -500:
                # you've begun stage 1
                self.currStageTaskDict = stage1TaskDict
                checklist.taskDict = stage1TaskDict
                checklist.isVisible = True
                game.paused = True

        elif (self.currStageTaskDict.keys() == stage1TaskDict.keys() and
              GameObject.globalX < -3200):
            # progress to stage 2
            self.currStageTaskDict = stage2TaskDict
            checklist.taskDict = stage2TaskDict
            checklist.isVisible = True
            game.paused = True

            # start moving the people
            person2.state = 'idle'
            person3.state = 'idle'
            #person2, person3 = spawnStage2People(person2IdleLocations, mainHouse.rect.right, 
            #                                     person3IdleLocations, mainHouse.rect.right + 200)
            #initStage2(600, flowerDict, laundryDict)
            #pygame.sprite.LayeredUpdates.move_to_front(duck)
        
        # progress to final stage
        elif (self.currStageTaskDict.keys() == stage2TaskDict.keys() and 
              GameObject.globalX < -5300):
            game.theSword = initFinalStage()
            self.currStageTaskDict = finalStageTaskDict
            checklist.taskDict = finalStageTaskDict
            checklist.isVisible = True
            game.paused = True


    def checkMoveBasedTasks(self):
        # these tasks are dependent on movement only (not objects)
        if self.currStageTaskDict.keys() == stage2TaskDict.keys():
            # over chimney
            if (isClose(duck.rect.centerx, game.mainHouse.rect.right - 20, 10) and
                isClose(duck.rect.centery, game.mainHouse.rect.top, 10)):
                self.completeTask('break into the house to steal the keys')

                # kill door, move duck
                game.door.delete()
                duck.x = game.mainHouse.rect.centerx - 20
                duck.y = game.mainHouse.rect.bottom - 40
                duck.updateHitbox()
                duck.falling = False
                    
                # kill the barrier
                game.stage2BarricadeList[3].delete()
        elif self.currStageTaskDict.keys() == finalStageTaskDict.keys():
            #pygame.sprite.collide_rect(self, game.cave)
            #print(self.rect.centerx, game.cave.rect.right - 50)
            if (isClose(self.rect.centerx, game.cave.rect.right - 50, 10) and 
                self.heldItem == game.theSword):
                self.completeTask('slay the dragon')
                # win game!
                #game.won = True
                game.statue.visible = True
                game.finalMessage.visible = True
                
                #game.endMessage = visible

    def checkTasks(self):
        # holding something and has begun a stage
        if self.currStageTaskDict != None and self.heldItem != None:
            # stage 1
            if self.currStageTaskDict.keys() == stage1TaskDict.keys():
                # sow the seeds
                if self.heldItem.image in seedDict:
                    # check if your within the soil
                    if pygame.sprite.collide_rect(self, soilPatch):
                        self.sowedSeeds.add(self.heldItem.image)

                        if len(self.sowedSeeds) == 3:
                            # planted all the seeds
                            self.completeTask('sow the seeds')
                if (self.heldItem.image == keyImg and 
                    isClose(self.rect.centerx, game.fenceGate.rect.centerx, 50) and
                    isClose(self.rect.centery, game.fenceGate.rect.centery, 50)):
                    # holding keys near the gate
                    self.completeTask('free the cattle')
                    game.fenceGate.delete()
                    game.stage1Key.delete()
                    for sprite in game.stage1BarricadeList:
                        sprite.delete()

            # stage 2
            elif self.currStageTaskDict.keys() == stage2TaskDict.keys():
                if isClose(game.door.rect.centerx, mailbox.rect.centerx, 50):
                    self.completeTask('deliver the mail')
                laundryCount = 0
                for laundryItem in laundryItems:
                    if isClose(laundryItem.rect.centerx, laundryBasket.rect.centerx, 25):
                        laundryCount += 1
                # all laundry near basket
                if laundryCount == len(laundryItems):
                    self.completeTask('collect the laundry')

        else:
            # started a stage
            if self.currStageTaskDict != None:
                # stage 1
                if self.currStageTaskDict.keys() == stage1TaskDict.keys():
                    # prepare a salad
                    if collectedItems([[vegList], bowl]):
                        self.completeTask('prepare a salad')
                # stage 2
                elif self.currStageTaskDict.keys() == stage2TaskDict.keys():
                    # flower bouquets
                    if collectedItems(flowerList):
                        self.completeTask('assemble a flower bouquet for the picnic')
    
    def completeTask(self, task):
        if self.currStageTaskDict[task] == False:
            #not completed yet, complete it and show the checklist
            self.currStageTaskDict[task] = True
            checklist.isVisible = True
            # pause game
            game.paused = True

    def checkLakeTasks(self):
        if self.heldItem != None:
            # fill watering can
            if self.heldItem.image == wateringCanImg:
                self.completeTask('fill up the watering can')

            if self.heldItem.image in breadDict:
                self.completeTask('bake in the lake')
                
    # check if duck is in the lake
    def checkInLake(self):
        if (lake.rect.top < self.rect.bottom < lake.rect.bottom and
            lake.rect.left < self.rect.centerx < lake.rect.right):
            self.swimming = True
            self.checkLakeTasks()
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
        if self.currStageTaskDict != None:
            self.checkMoveBasedTasks()

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
        if game.showHitBoxes:
            pygame.draw.rect(screen, (0, 255, 0), self.beakHitBox.rect, 1)

class Person(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, headDictionary, walkSpeed, runSpeed, viewDist, idleActivities):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        self.headDictionary = headDictionary

        self.state = 'still' #idle' # angry, scared, idle, still = not moving at ALL
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
            else:
                # pick it up and move it away unless it's a unmovable platform
                if not isinstance(spriteX, Platform):
                    spriteX.y = self.rect.centery
                else:
                    #it's a platform
                    if spriteX.canHold == True:
                        spriteX.y = self.rect.centery
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
                if duck.heldItem == game.theSword:
                    # holding the sword
                    self.state = 'scared'
                else:
                    # chase the duck!
                    self.state = 'angry'
            # can't scare away if angry
            elif self.state != 'angry' and duck.quacking and random.random() < 0.05:
                self.state = 'scared'

                # scare the farmer task
                if duck.currStageTaskDict.keys() == stage1TaskDict.keys():
                    duck.completeTask('scare the farmer')
                elif duck.currStageTaskDict.keys() == stage2TaskDict.keys():
                    #it's person3 (the kid)
                    if (self.heldItem != None and self.imageDict['right']['leg'] == person3Legs
                        and self.heldItem.image == ballImg):
                       #scared the kid while he had the ball
                            duck.completeTask('play soccer with the kid')

            else:
                if self.state != 'scared':
                    self.state = 'stand'
                    self.updateBody()
                    self.legIndex = 0
                    self.lookTowards(duck)
        
        # duck is not within view
        else:
            # stay angry even if duck is out of view
            # this feature was changed, i think the person will stop chansince once out of view
            if self.state != 'still': # self.state != 'angry' and 
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
            self.y = duck.beakHitBox.rect.centery - self.rect.height // 2
            if duck.dir == 'right':
                self.x = duck.beakHitBox.rect.centerx
            elif duck.dir == 'left':
                self.x = duck.beakHitBox.rect.centerx - self.rect.width
            duck.checkTasks()
                
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

    def __init__(self, x, y, image, weight, canHold = True):
        super().__init__(x, y, image, weight)
        self.falling = False
        self.canHold = canHold
        pygame.sprite.Sprite.__init__(self, Platform.allPlatforms)



class Overlay(pygame.sprite.Sprite):
    def __init__(self, x, y, title, taskDict, width, height):
        self.x = x
        self.y = y
        self.title = title
        # linking tasks (keys) to if they are completed or not (T/F)
        if taskDict != None:
            self.taskDict = taskDict
        else:
            self.taskDict = {'wasd to move': False, 
                             'space to jump': False,
                             'j to grab an item': False,
                             'k to run': False,
                             'l to flap': False,
                             '; to quack': False}

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
        self.renderTaskList(self.x + 25, self.y + 75, 30)

class Splash(Overlay):
    def __init__(self, x, y, title, width, height, image):
        super().__init__(x, y, title, {}, width, height)
        self.margin = 50
        self.heading = titleFont.render(title, True, (83, 71, 56)) 
        self.headingRect = self.heading.get_rect() 
        self.headingRect.x = self.x + width // 2 - self.headingRect.width // 2
        self.headingRect.y = self.y + self.margin
        self.image = image
        self.imgX = self.margin
        self.imgY = self.margin * 3

        self.instructionsList = ['<enter>  -  begin', '<i>  -  learn more',
                                 '<delete>  -  quit']

        self.info = ['this is a single player',
                     'stealth game',
                     'the objective is to be a duck', 
                     'and do duck things',
                     '',
                     '<i>  -  back']
        
        self.onDisplay = self.instructionsList
        self.spacing = 80

    def renderInstructions(self):
        startY = 200
        startX = width // 2 + self.margin
        for item in self.onDisplay:
            text = subheading.render(item, True, (83, 71, 56))
            textRect = text.get_rect() 
            textRect.x = startX
            textRect.y = startY
            screen.blit(text, textRect) 
            startY += self.spacing

    def update(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        self.renderInstructions()
        screen.blit(self.heading, self.headingRect) 
        screen.blit(self.image, (self.imgX, self.imgY)) 

# messages rendered at bottom center of screen
class GameMessage(object):
    def __init__(self, messageList, displayTime = None):
        self.messageList = messageList
        self.messageIndex = 0

        self.updateText()

        self.visible = False
        self.displayTime = displayTime
        self.timer = 0
    
    def updateText(self):
        self.message = subheading.render(self.messageList[self.messageIndex], True, (83, 71, 56))
        self.textRect = self.message.get_rect() 
        self.textRect.centerx = width // 2
        self.textRect.y = height - 100
    
    # change to next message in list
    def changeMessage(self):
        if self.messageIndex < len(self.messageList) - 1:
            self.messageIndex += 1
            self.updateText()
        else:
            # no longer visible
            self.visible = False

    def update(self):
        screen.blit(self.message,  self.textRect)
        self.timer += 1
        if self.displayTime != None and self.timer % self.displayTime == 0:
            self.changeMessage()

game.finalMessage = GameMessage(['and  that  is  how  the  duck  saved  the  town', 
                                 'the  end', 
                                 '',
                                 'thank  you  for  playing',
                                 'unfinished  duck  game',
                                 'illustrated  and  programmed  by  janet  peng'], 60)

game.initialMessage = GameMessage(['',
                                   'this  is  a  story  about  a  duck',
                                   'who  calls  this  picnic  blanket  at  the  outskirts  of  town  home',
                                   '',
                                   'press  tab  to  check  your  to  do  list'], 70)

# # # # # # # # # # # # # # # # # # # # #
###           main game loop          ###
# # # # # # # # # # # # # # # # # # # # #

stage1Tasks = [ 'bake in the lake',
                'scare the farmer',
                'prepare a salad',
                'fill up the watering can',
                'sow the seeds',
                'free the cattle' ]

stage2Tasks = [ 'deliver the mail',
                'collect the laundry',
                'assemble a flower bouquet for the picnic',
                'play soccer with the kid',
                'break into the house to steal the keys' ]

# finalTasks.append('slay the dragon') when the duck gets the sword?
finalTasks = [ 'wield the sword',
               'slay the dragon' ]


stage1TaskDict = initiateTasks(stage1Tasks)
stage2TaskDict = initiateTasks(stage2Tasks)
finalStageTaskDict = initiateTasks(finalTasks)

# images (keys) : weight (value) - weight should be at least 4
vegDict = {lettuceImg: 10, carrotImg: 6, radishImg: 6}
seedDict = {lettuceSeedImg: 4, carrotSeedImg: 4, radishSeedImg: 4}
breadDict = {loafImg: 9, baguetteImg: 7, croissantImg: 6}
flowerDict = {flower1: 5, flower2: 5, flower3: 5}
mailDict = {letterImg: 5, newspaperImg: 6}
laundryDict = {shirtImg: 6, pantsImg: 8, towelImg: 6, sock1Img: 5, sock2Img: 5}

# returns all placed items in a list
def placeItems(imgWeightDict, xLo, xHi, yLo, yHi, falling = True):
    L = []
    for image in imgWeightDict:
        item = Item(random.randrange(xLo, xHi), 
                    random.randrange(yLo, yHi), image, imgWeightDict[image])
        #item.falling = falling
        L.append(item)
    return L

def initStage1(startX, vegDict, seedDict, breadDict):
    barnX = startX + random.randrange(500, 800)

    # higher spacing = less dense
    wheatField = generateBackground(90, wheatPlants, barnX - 450, 0.5)

    # place barn - place idle position near here
    barn = BackgroundObject(barnX, barnImg, 10)

    # place soil close to barn - place idle position near here
    soilX = barnX - 100
    soilPatch = BackgroundObject(soilX, soilImg, 200)

    # place vegetables and seeds close to soil
    soilMargin = 20
    vegList = []
    for image in vegDict:
        # 1 - 2 of each veg
        for i in range(random.randrange(1, 3)):
            veg = Item(soilX + soilMargin, 400, image, vegDict[image])
            vegList.append(veg)
            soilMargin += random.randrange(50, 70)
    placeItems(seedDict, soilX - 50, soilPatch.rect.right + 100, 275, 500)

    # place table relative to barn - place idle position near here
    tableX = barn.rect.right + random.randrange(80, 150)
    table = Platform(tableX, 250, tableImg, 50)

    # place bread items
    placeItems(breadDict, tableX - 50, table.rect.right + 50, 150, 300)
    # place bowl on top of table
    bowl = Item(tableX + 50, table.rect.top - 80, bowlImg, 12)

    # cattle pen
    cattleX = table.rect.right + random.randrange(100, 200)
    fenceRect = fenceImg.get_rect()
    fenceY = groundY - fenceRect.height
    backFenceX = cattleX
    frontFenceX = cattleX

    # bakground fences
    for i in range(5):
        if i == 0:
            firstFence = BackgroundObject(backFenceX, fenceImg)
        elif i == 4:
            lastFence = BackgroundObject(backFenceX, fenceImg)
        else:
            BackgroundObject(backFenceX, fenceImg)
        backFenceX += fenceRect.width
        
    cow = Cow(cattleX, 90, cowImg, firstFence, lastFence)
    
    # foreground fences with fence gates
    for i in range(5):
        if i == 2:
            game.fenceGate = Platform(frontFenceX, fenceY + 25, fenceGateImg, 100, False)
        else:
            Platform(frontFenceX, fenceY + 25, fenceImg, 100, False)
        frontFenceX += fenceRect.width


    # randomly place watering can
    Item(barnX + random.randrange(100, 300), random.randrange(groundY + 150, height - 100), 
         wateringCanImg, 12)

    # make a dictionary of all the locations the person can idle to
    personIdleLocations = {'barn': (barnX + 200, 350), 'veg': (soilX, soilPatch.rect.bottom),
                           'table': (tableX, 350)}
    # person
    person1HeadDict = {'idle': person1Head}
    person1ImageDict = {'idle': person1Stand, 'stand': person1Stand, 'still' : person1Stand, 
                        'angry': person1Active, 'scared': person1Scared}
    person1 = Person(barn.rect.right, 300, person1Stand, person1Legs, person1ImageDict, 
                     person1HeadDict, 2, 6, 150, personIdleLocations)
    person1.state = 'idle'

    # hat and keys
    game.stage1Key = SpecialItem(barnX + random.randrange(100, 300), random.randrange(groundY, height - 100), 
                            keyImg, 5, (50, 100))
    SpecialItem(barnX + random.randrange(100, 300), random.randrange(groundY, height - 100), 
                hatImg, 5, (15, -12))

    # right side barricade
    game.stage1BarricadeList = drawBarricade(backFenceX + fenceRect.width + 200, 6, fenceImg)
    #game.stage1Blockade = Platform(fenceX + fenceRect.width + 200, groundY - 150, barricadeImg, 100, False)

    return(barn, soilPatch, vegList, table, bowl)

def placeHouse(startX):
    housePartYList = []
    totalWidth = 0
    for elem in housePartsList:
        rect = elem.get_rect()
        totalWidth += rect.width
        housePartYList.append(groundY - rect.height + 10)
    houseX = startX + totalWidth
    for i in range(len(housePartsList)):
        housePartRect = housePartsList[i].get_rect()
        if i == len(housePartsList) - 1:
            mainHouse = Platform(houseX, housePartYList[i], housePartsList[i], 100, False)
            door = Platform(houseX + housePartRect.width // 2 - 85, 205, doorImg, 100, False)
            
        else:
            if i == 0:
                # place laundry line and tree
                laundryLine = BackgroundObject(houseX + housePartRect.width, laundryLineImg, -100)
                BackgroundObject(laundryLine.rect.right - 100, trees[random.randrange(len(trees))], 8)
            Platform(houseX, housePartYList[i], housePartsList[i], 100, False)
            houseX -= housePartRect.width


    return (mainHouse, door, laundryLine)

def initStage2(startX, flowerDict, laundryDict, mailDict):
    houseX = startX + random.randrange(500, 800)

    # higher spacing = less dense
    backgroundStartX = houseX - random.randrange(700, 850)
    village = generateBackground(6, distantHouses, backgroundStartX + 100, 200, 5)
    forest = generateBackground(12, trees, backgroundStartX, 50, 8)

    # place house parts - place idle position near 
    mainHouse, door, laundryLine = placeHouse(houseX)

    # place mailbox and mail around mailbox
    mailboxX = houseX - 200
    mailbox = Item(mailboxX, 300, mailboxImg, 20)
    placeItems(mailDict, mailboxX - 50, mailboxX + 50, 400, 500)

    # place garden soil, rocks and flowers
    flowerPatchCenterX = houseX + random.randrange(300, 500)
    flowerPatchRect = flowerPatchImg.get_rect()
    BackgroundObject(flowerPatchCenterX - flowerPatchRect.width // 2, flowerPatchImg, overlapY = 200)
    vertRadius = flowerPatchRect.height // 2
    hozRadius = flowerPatchRect.width // 2
    adjustment = 15
    angle = 0
    while angle < 360:
        rockImg = random.choice(rockImgs)
        # inspired by clock: http://www.cs.cmu.edu/~112/notes/notes-graphics.html
        rockX = flowerPatchCenterX - adjustment + hozRadius * math.cos(angle)
        rockY = 420 - vertRadius * math.sin(angle)
        BackgroundObject(rockX, rockImg, rockY - 280)
        angle += 20

    flowerList = []
    for image in flowerDict:
        # 1 - 2 of each flower
        for i in range(random.randrange(1, 3)):
            flower = Item(random.randrange(flowerPatchCenterX - hozRadius + adjustment * 2, 
                                           flowerPatchCenterX + hozRadius - adjustment * 2),
                          random.randrange(330, 430), image, flowerDict[image])
            flowerList.append(flower)


    # place landry line, laundry - place idle position near here
    laundryItems = placeItems(laundryDict, laundryLine.rect.left, laundryLine.rect.right, 200, 220, False)

    # randomly place basket
    laundryBasket = Platform(houseX + random.randrange(1200, 1500), 
                         random.randrange(groundY + 150, height - 100),
                         basketImg, 20)

    # randomly place bbq and crate (for house scaling)
    Platform(houseX + random.randrange(200, 350), random.randrange(groundY + 150, height - 100), 
             bbqImg, 40)
    Platform(houseX, random.randrange(groundY + 150, height - 100), crateImg, 25)

    # randomly place soccer ball
    SpecialItem(houseX + 600, random.randrange(groundY, height - 100), 
                ballImg, 6, (15, 100))

    # barricade
    game.stage2BarricadeList = drawBarricade(laundryLine.rect.right + 300, 6, fenceImg, False, True)

    # make a dictionary of all the locations the person can idle to
    person2IdleLocations = {'mail': (mailboxX, 350), 
                            'flower': (flowerPatchCenterX, flowerPatchRect.right),
                           'laundry': (laundryLine.rect.centerx, 350)}
    person3IdleLocations = {'lawn': (laundryLine.rect.centerx, 500), 
                            'garage': (laundryLine.rect.left, 350),
                           'house': (mainHouse.rect.left, 400)}
    return mainHouse, mailbox, door, laundryBasket, laundryItems, flowerList, person2IdleLocations, person3IdleLocations

# spawn in the stage 2 npcs
def spawnStage2People(idleLocations2, x2, idleLocations3, x3):
    person2HeadDict = {'idle': person2Head}
    person2ImageDict = {'idle': person2Stand, 'stand': person2Stand, 'still': person2Stand, 
                        'angry': person2Active, 'scared': person2Scared}

    person3HeadDict = {'idle': person3Head}
    person3ImageDict = {'idle': person3Stand, 'stand': person3Stand, 'still': person2Stand, 
                        'angry': person3Active, 'scared': person3Scared}

    person2 = Person(x2, 320, person2Stand, person2Legs, person2ImageDict, 
                     person2HeadDict, 2, 5, 100, idleLocations2)
    person3 = Person(x3, 400, person3Stand, person3Legs, person3ImageDict, 
                     person3HeadDict, 2, 5, 100, idleLocations3)
    return person2, person3

def initFinalStage():
    sword = Item(1130, 400, swordImg, 8)
    Platform(1000, 450, bigRockImg, 200, False)
    return sword

barn, soilPatch, vegList, table, bowl = initStage1(1000, vegDict, seedDict, breadDict)
game.mainHouse, mailbox, game.door, laundryBasket, laundryItems, flowerList, person2IdleLocations, person3IdleLocations= initStage2(3600, flowerDict, laundryDict, mailDict)

person2, person3 = spawnStage2People(person2IdleLocations, game.mainHouse.rect.right, 
                                     person3IdleLocations, game.mainHouse.rect.right + 200)


lake = BackgroundObject(-800, lakeImg, 230)
game.cave = BackgroundObject(-2200, caveImg, 180)
generateBackground(10, trees, -1600, 50, 8)
duckHome = BackgroundObject(50, blanketImg, 200)
# signs
Item(500, 200, signImg, 6)
#Item(300, 200, tabSignImg, 6)
Item(-50, 200, lakeSignImg, 6)
Item(-900, 200, dragonSignImg, 6)

# first set of barricades with crate
drawBarricade(800, 6, fenceImg, True)


duckImageDict = {'stand': duckBod, 'flap': duckFlapping, 'quack': duckQuacking}
duck = Duck(100, 350, duckBod, duckLegs, duckImageDict, 5, 100, 5)
duck.falling = False

checklist = Overlay(200, 150, 'to do', duck.currStageTaskDict, 400, 300)
splash = Splash(0, 0, 'unfinished  duck  game', width, height, splashImg)
menuDict = {'press delete to exit': False,
            'press shift to show hitboxes': False}
menu = Overlay(200, 150, 'menu', menuDict, 400, 300)



playing = True
while playing:
    time = clock.tick(20) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        
        elif event.type == pygame.KEYDOWN:
            if game.started == True:
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
                    game.paused = not game.paused
                    if game.paused == True:
                        #show checklist
                        checklist.isVisible = True
                        #displayCheckList()
                    else:
                        checklist.isVisible = False

                # see hitBoxes
                elif event.key == pygame.K_ESCAPE:
                    game.showHitBoxes = not game.showHitBoxes

                    #game.paused = not game.paused
                    #menu.visible = not menu.isVisible
            else:
                # game not started
                if event.key == pygame.K_i:
                    # show info
                    if splash.onDisplay == splash.instructionsList:
                        splash.onDisplay = splash.info
                        splash.spacing = 30
                    else:
                        splash.onDisplay = splash.instructionsList
                        splash.spacing = 80

                # start game
                elif event.key == pygame.K_RETURN:
                    game.started = True 
                    game.initialMessage.visible = True

            # can always exit game
            if event.key == pygame.K_DELETE:
                playing = False                         

    # check for key holds
    if game.started == True:
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

        screen.fill((212, 242, 255))
        pygame.draw.rect(screen, (100, 160, 110), (0, groundY, width, height - groundY))
        updateAll()
        if checklist.isVisible:
            checklist.update()
        
        if game.finalMessage.visible:
            game.finalMessage.update()
        if game.initialMessage.visible:
            game.initialMessage.update()
    else:
        # game not started, show splash
        splash.update()
    
    # menu
    #if menu.isVisible:
    #    menu.update()

    pygame.display.flip()

pygame.quit()