import pygame

class ColorButton():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    def clicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

class ImageButton():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
    def clicked(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

class BorderedColorButton():
    def __init__(self, x, y, width, height, color, borderwidth, bordercolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.borderwidth = borderwidth
        self.bordercolor = bordercolor
        self.borderrect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect = pygame.Rect(self.x+self.borderwidth, self.y+self.borderwidth, self.width - (self.borderwidth*2), self.height - (self.borderwidth*2))
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.bordercolor, self.borderrect)
        pygame.draw.rect(surface, self.color, self.rect)
    
    def clicked(self):
        if pygame.mouse.get_pressed()[0] and self.borderrect.collidepoint(pygame.mouse.get_pos()):
            return True

class BorderedImageButton():
    def __init__(self, x, y, width, height, image, borderwidth, bordercolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.borderwidth = borderwidth
        self.bordercolor = bordercolor
        self.borderrect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect = pygame.Rect(self.x+self.borderwidth, self.y+self.borderwidth, self.width - (self.borderwidth*2), self.height - (self.borderwidth*2))
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.bordercolor, self.borderrect)
        surface.blit(pygame.transform.scale(self.image, self.rect.size), self.rect.topleft)
    
    def clicked(self):
        if pygame.mouse.get_pressed()[0] and self.borderrect.collidepoint(pygame.mouse.get_pos()):
            return True