from sprites_object import *

class ObjectHadler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.animate_sprite_path = "resources/sprites/animated_sprites/"
        add_sprite = self.add_sprites
        
        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5,1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5,7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5,3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5,4.25)))
        add_sprite(AnimatedSprite(game, pos=(7.5,2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5,5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5,1.5)))
        add_sprite(AnimatedSprite(game,path=self.animate_sprite_path + "red_light/0.png",pos=(14.5,7.5)))
        add_sprite(AnimatedSprite(game,path=self.animate_sprite_path + "red_light/0.png",pos=(12.5,7.5)))
        add_sprite(AnimatedSprite(game,path=self.animate_sprite_path + "red_light/0.png",pos=(9.5,7.5)))
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
    
    def add_sprites(self,sprite):
        self.sprite_list.append(sprite)