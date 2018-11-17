
import pygame
from deck import GameObject, Deck, Zoom, RoomDeck, SpellDeck, Player, CardInPlay

pygame.init()

displayWidth = 1250
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Boss Monster')

# SETUP GAME
zoom = Zoom('./images/bosses/back.png', 10, 100)
bossDeck = Deck('./images/bosses/back.png', [1,2,3], 260, 250)
epicHeroDeck = Deck('./images/epics/back.png', [1,2,3], 370, 250)
heroDeck = Deck('./images/heroes/back.png', [1,2,3], 480, 250)
roomDeck = RoomDeck('./images/room/back.png', [1,2,3], 900, 250)
spellDeck = SpellDeck('./images/spells/back.png', [1,2,3], 1120, 250)

while True:
    gameDisplay.fill((0, 0, 0))
    GameObject.updateAll()

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP: 
            GameObject.onClick()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Player.playCard()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    zoom.update()

    GameObject.render(gameDisplay)
    pygame.display.update()