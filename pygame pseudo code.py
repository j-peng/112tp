import pygame
import random

# # # # # # # # # # # # # # # # # # # # #
###         initializing game         ###
# # # # # # # # # # # # # # # # # # # # #
pygame.init()

clock = pygame.time.Clock()

width = 400
height = 400
groundY = 200

# create the display surface
screen = pygame.display.set_mode((width, height))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen2 = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))

paused = False

# # # # # # # # # # # # # # # # # # # # #
###           loading images          ###
# # # # # # # # # # # # # # # # # # # # #

crate = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\crate.png')
crate = pygame.transform.scale(crate, (80, 80))
duck = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\duckBod.png')
duck = pygame.transform.scale(duck, (80, 80))
person = pygame.image.load('D:\\Documents\\Sophomore\\112\\tp\\person.png')
person = pygame.transform.scale(person, (100, 100))


heading = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\arialRound.TTF', 24) 
paragraph = pygame.font.Font('D:\\Documents\\Sophomore\\112\\tp\\arialRound.TTF', 12) 

# # # # # # # # # # # # # # # # # # # # #
###           loading sounds          ###
# # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # #
###              classes              ###
# # # # # # # # # # # # # # # # # # # # # 

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

# check it two rectangles collide
# inspired by: https://www.geeksforgeeks.org/find-two-rectangles-overlap/
def collide(rect1, rect2):
    if ((rect1.x > rect2.x + rect2.width) or (rect2.x > rect1.x + rect1.width) or
        (rect1.y < rect2.y + rect2.height) or (rect2.y < rect1.y + rect1.height)):
        return False
    return True

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
class ViewArea(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        # make a rectangle
        self.rect = pygame.Rect(x, y, width, height)


class GameObject(pygame.sprite.Sprite):
    allGameObjects = pygame.sprite.Group()

    # for all game Objects that are on screen
    activeGameObjects = pygame.sprite.Group()

    @staticmethod
    def moveBackground(dir):
        if dir == 'left':
            xDir = -5
        elif dir == 'right':
            xDir = 5

        for sprite in GameObject.allGameObjects:
            # might want to just move active object to increase efficiency?
            sprite.move(xDir, 0)

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

        self.falling = True
        self.fallSpeed = 5

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
        self.bodyDictionary = bodyDictionary 
        self.walkSpeed = walkSpeed
        self.runSpeed = runSpeed

        self.running = False

        # n is how far around the thing can see
        self.viewDist = viewDist
        self.proxSprite = ViewArea(self.x-self.viewDist, self.y-self.viewDist, 
                                   self.rect.width+2*self.viewDist, self.rect.height+2*self.viewDist)

    def isColliding(self, dir):
        # check if there is a collision in a direction
        if dir == 'left':
            collisionList = pygame.sprite.spritecollide(self, GameObject.allGameObjects, False)
            collisionList.remove(self)
            if len(collisionList) != 0:
                # hit something, return the lowest sprite
                return lowestSprite(collisionList)
            return False
        elif dir == 'up':
            pass
    
    def getObjectsInView(self):
        objectsSeen = pygame.sprite.spritecollide(self.proxSprite, GameObject.allGameObjects, False)
        objectsSeen.remove(self)
        return objectsSeen

    def check(self, dir):
        # check if there is an object nearby in a direction
        # if there is, return the sprite, else return False
        objectsSeen = self.getObjectsInView()
        for sprite in objectsSeen:
            if dir == 'left':
                if isClose(sprite.rect.right, self.proxSprite.rect.left, 5):
                    return sprite
            elif dir == 'right':
                if isClose(sprite.rect.left, self.proxSprite.rect.right, 5):
                    return sprite
            elif dir == 'up':
                if isClose(sprite.rect.bottom, self.proxSprite.rect.bottom, 5):
                    return sprite
            elif dir == 'down':
                if isClose(sprite.rect.top, self.proxSprite.rect.bottom, 5):
                    return sprite

        return False

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
        """
        checkLeft = self.isColliding('left')
        if inX < 0:
            # move left if nothing is on left side or the thing it hits bottom is above self.bottom
            if checkLeft == False:
                self.move(-speed, 0)
            elif checkLeft.rect.bottom < self.rect.bottom:
                self.move(-speed, 0)
        elif inX > 0:
            self.move(speed, 0)
        
        if inY < 0:
            if checkLeft == False:
                self.move(0, -speed)
            elif checkLeft.rect.bottom < self.rect.bottom:
                self.move(0, -speed)

        elif inY > 0:
            self.move(0, speed)
        """

    # update the hitboxes
    def updateHitbox(self):
        super().updateHitbox()
        self.proxSprite.rect.centerx = self.rect.centerx
        self.proxSprite.rect.centery = self.rect.centery

    # update the object on screen
    def update(self):
        super().update()
        pygame.draw.rect(screen, (0, 0, 0), self.proxSprite.rect, 1)

class Duck(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        self.jumping = False
        self.jumpHeight = 10
        self.oldYPos = None
    
    def walk(self, inX, inY):
        super().walk(inX, inY)

        self.checkIsSupported()
        self.checkBackgroundMove()

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
        pass

    def quack(self):
        pass

    def swim(self):
        pass
    
    # pickup the item if the beak is touching it
    def pickUp(self, other):
        pass
    
    # drop the held item
    def drop(self):
        pass

    # returns true if its being supported, starts falling otherwise
    def checkIsSupported(self):
        if self.testHitPlatform() == None and self.rect.bottom < groundY: # or its above the ground plane
            self.falling = True
        else:
            self.falling = False
            return True #it is supported

    # check if duck approaches edges of screen, if it doesn, move the background
    def checkBackgroundMove(self):
        if isClose(self.rect.right, width, 50):
            GameObject.moveBackground('left')
        elif isClose(self.rect.left, 0, 50):
            GameObject.moveBackground('right')

    def update(self):
        if self.jumping:
            self.jump()
        super().update()

class Person(MovingObject):
    def __init__(self, x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist, idleActivities):
        super().__init__(x, y, image, walkCycleLegsList, bodyDictionary, walkSpeed, runSpeed, viewDist)

        self.state = 'angry' # chase, scared
        self.target = None # what or where the person is targeting
    
    def moveTowards(self, x, y):
        # move towards (x, y)
        # check if its colliding into any objects, 
        # if it is, the person's bottom must be greater than the object's bottom 
        # so it appears as if it's infront of the object
        # to go around object,
        # if you will cross from the bottom (collide with person top and item bottom)
            # move up until self.bottom == item.bottom
            # then only move in the x direction desired until no longer colliding
        # if you will cross from the top (self.bottom == item. top)
            # then only move in the x direction desired until no longer colliding
        # if you will cross from the left (person.right = item.left)
            # only move in y direction desired until no longer colliding
        # if you will cross from the right (person.left = item.right)
            # only move in y direction desired until no longer colliding

        # have person begin curving before it hits object by checking whats close to it?
        # check sprites that hit the person's "vision" (circle centered at person)

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

    def idle(self):
        self.moveTowards(x, y)
        pass

    def chase(self, other):
        self.running = True
        self.moveTowards(other.rect.centerx, other.rect.bottom)

        if pygame.sprite.collide_rect(self, other):
            # if you hit the duck, stop running and start idling
            self.state = 'idle'
            self.running = False
    
    def scared(self):
        pass

    def update(self):
        if self.state == 'angry':
            self.chase(duck)
        super().update()

class PassiveObject(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.isHeld = False
        pass

class Item(PassiveObject):
    def __init__(self, x, y, image, weight):
        pass

class Platform(PassiveObject):
    allPlatforms = pygame.sprite.Group()

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.falling = False
        pygame.sprite.Sprite.__init__(self, Platform.allPlatforms)



class Overlay(pygame.sprite.Sprite):
    def __init__(self, x, y, title, taskList, width, height):
        self.x = x
        self.y = y
        self.title = title
        self.taskList= taskList

        # make a rectangle as its hitbox
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.x = self.x
        self.rect.y = self.y

        self.isVisible = False

        self.heading = heading.render('To Do', True, (0, 0, 0)) 
        self.headingRect = self.heading.get_rect() 
        self.headingRect.x = self.x
        self.headingRect.y = self.y

    def renderTaskList(self, x, startY, spacing):
        for task in self.taskList:
            text = paragraph.render(task, True, (0, 0, 0))
            textRect = text.get_rect() 
            textRect.x = x
            textRect.y = startY
            screen.blit(text, textRect) 
            startY += spacing

    def update(self):
        pygame.draw.rect(screen, (150, 150, 150), self.rect)
        screen.blit(self.heading, self.headingRect) 
        self.renderTaskList(self.x + 20, self.y + 50, 20)



# # # # # # # # # # # # # # # # # # # # #
###           main game loop          ###
# # # # # # # # # # # # # # # # # # # # #

box = Platform(200, 160, crate)
box2 = Platform(200, 300, crate)
person = Person(300, 300, person, [], {}, 1, 2, 10, [])
duck = Duck(100, 100, duck, 1, 2, 5, 10, 5)
checklist = Overlay(100, 100, 'hi', ['apple', 'banana', 'clemintine?'], 200, 200)

def updateAll():
    for item in GameObject.allGameObjects:
        item.update()

def displayCheckList():
    pass

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
                pass

            # quack
            elif event.key == pygame.K_SEMICOLON:
                pass

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

    # check if moving in a direction
    if keys[pygame.K_w]:
        if duck.rect.bottom > groundY:
            duck.walk(0, -1)
    elif keys[pygame.K_s]:
        duck.walk(0, 1)
    elif keys[pygame.K_a]:
        duck.walk(-1, 0)
    elif keys[pygame.K_d]:
        duck.walk(1, 0)
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (100, 100, 100), (0, groundY, width, height - groundY))
    updateAll()
    if checklist.isVisible:
        checklist.update()
    pygame.display.flip()

pygame.quit()