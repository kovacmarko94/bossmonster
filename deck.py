import pygame

class GameObject(pygame.Rect):

    objects = []

    def __init__(self, image, x, y, width = 80, height = 110):
        super().__init__(x, y, width, height)
        self.url = image
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        GameObject.objects.append(self) 

    @staticmethod
    def render(screen):
        for gameObject in GameObject.objects[::-1]:
            pygame.draw.rect(screen, (255, 255, 255), gameObject, 1)
            screen.blit(gameObject.image, (gameObject.x, gameObject.y))

    @staticmethod
    def onClick():
        mousePosition = pygame.mouse.get_pos()
        for gameObject in GameObject.objects:
            if gameObject.collidepoint(mousePosition):
                gameObject.handleClick()
                return

    @staticmethod
    def updateAll():
        for gameObject in GameObject.objects:
            gameObject.update()
    
    @staticmethod
    def first(gameObject):
        GameObject.objects.pop(GameObject.objects.index(gameObject))
        GameObject.objects.insert(0, gameObject)

    def handleClick(self):
        print(self)
    
    def update(self):
        pass

class Player:
    hand = []
    selectdCard = None

    @staticmethod
    def drawCard():        
        card = PlayerCard('./images/bosses/robobo.png', 0, 0)
        card = Player.setCardLocation(card)
        Player.hand.append(card)

    @staticmethod
    def handSize():
        return len(Player.hand)

    @staticmethod
    def setCardLocation(card):
        cardXPosition = 0
        cardYPosition = -110 / 3
        handSize = Player.handSize()
        if handSize == 0:
            cardXPosition = 260
        else:
            cardXPosition = Player.hand[handSize - 1].x + 90
        card.x = cardXPosition
        card.y = cardYPosition
        return card

    @staticmethod
    def playCard():
        if Player.selectdCard != None:
            card = CardInPlay('./images/bosses/robobo.png', 0, 0)
            GameObject.objects.remove(Player.selectdCard)
            Player.hand.remove(Player.selectdCard)
            Player.selectdCard = None
            Player.sortHand()

    @staticmethod
    def sortHand():
        temp = Player.hand
        Player.hand = []
        for card in temp:
            card = Player.setCardLocation(card)
            Player.hand.append(card)

class PlayerCard(GameObject):
    
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
    
    def handleClick(self):
        if Player.selectdCard == None:
            Player.selectdCard = self
            self.y += 30
        elif Player.selectdCard == self:
            Player.selectdCard = None
            self.y -= 30
        else:
            Player.selectdCard.y -= 30
            Player.selectdCard = self
            self.y += 30

class CardInPlay(GameObject):
    
    moving = None

    def __init__(self, image, x, y):
        super().__init__(image, x, y)
    
    def handleClick(self):
        self.move()

    def move(self):
        if CardInPlay.moving == None:
            CardInPlay.moving = self
            GameObject.first(self)
        elif CardInPlay.moving == self:
            CardInPlay.moving = None
    
    def update(self):
        if CardInPlay.moving == self:
            mousePosition = pygame.mouse.get_pos()
            self.x = mousePosition[0] - self.width / 2
            self.y = mousePosition[1] - self.height / 2

class Deck(GameObject):
    def __init__(self, image, cards, x, y):
        super().__init__(image, x, y)
        self.cards = cards

    def handleClick(self):
        pass

class RoomDeck(Deck):
    def __init__(self, image, cards, x, y):
        super().__init__(image, cards, x, y)

    def handleClick(self):
        Player.drawCard()

class SpellDeck(Deck):
    def __init__(self, image, cards, x, y):
        super().__init__(image, cards, x, y)

    def handleClick(self):
        Player.drawCard()

class Zoom(GameObject):
    def __init__(self, image, x, y, width = 240, height = 350):
        super().__init__(image, x, y, width, height)
    
    def update(self):
        mousePosition = pygame.mouse.get_pos()
        for gameObject in GameObject.objects:
            if gameObject.collidepoint(mousePosition):
                self.image = pygame.transform.scale(pygame.image.load(gameObject.url), (self.width, self.height))

    