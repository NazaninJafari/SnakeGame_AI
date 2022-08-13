from re import L
import arcade
import random

Screen_w = 800 
Screen_h = 600

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.AMERICAN_ROSE
        self.width = 10
        self.height = 20
        self.center_x = Screen_w // 2
        self.center_y = 45
        self.speed = 2
        self.score = 5
        self.radius = 15 
        self.body = []
        self.change_x = 0
        self.change_y = 0
        
    def draw(self):
        #rasme mar bar hasbe toolesh 
        for i in range (len(self.body)):
            arcade.draw_circle_filled(self.body[i][0] , self.body[i][1] , self.radius, self.color)
        

    def move(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        #mokhtasat makan feli dar badan mar beriz 
        self.body.append([self.center_x , self.center_y])
        #pak kardan rade paye harkate mar
        if len(self.body) > 1 :
            del self.body[0]
    
    def eat(self,p):
        if p == 'apple' :
            self.score += 1
            self.body.append([self.center_x, self.center_y])
        elif p == 'poire' :
            self.score += 2
            self.body.append([self.center_x, self.center_y])
        elif p == 'poo' :
            self.score -= 1       

class Apple(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.texture = arcade.load_texture('w1.jpeg')
        self.width = 45
        self.height = 45
        self.center_x = random.randint(self.width,Screen_w - self.width)
        self.center_y = random.randint(self.height, Screen_h - self.height)
    
class Poire(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('w3.jpeg')
        self.width = 30
        self.height = 30
        self.center_x = random.randint(self.width,Screen_w - self.width)
        self.center_y = random.randint(self.height, Screen_h - self.height)
    

class Poo(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('w4.jpeg')
        self.width = 30
        self.height = 30
        self.center_x = random.randint(self.width,Screen_w - self.width)
        self.center_y = random.randint(self.height, Screen_h - self.height)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(Screen_w, Screen_h, 'Snake Game')
        arcade.set_background_color(arcade.color.BLACK)
        self.snake = Snake()
        self.apple = Apple()
        self.poire = Poire()
        self.poo = Poo()

    def on_draw(self):
        arcade.start_render()       
        arcade.draw_text('score: '+str(self.snake.score), Screen_w - 100, Screen_h - 20, arcade.color.WHITE, 12, font_name='arial')
        
        if self.snake.center_x <= 0 or self.snake.center_x >= Screen_w or self.snake.center_y<=0 or self.snake.center_y >= Screen_h or self.snake.score <= 0 :
            arcade.draw_text('GAME OVER', 250, 300, arcade.color.RED, 50)
            arcade.exit()   
        else :
            self.snake.draw()
            self.apple.draw()
            self.poire.draw()
            self.poo.draw()
    
    def on_update(self, delta_time: float):
        
        if self.snake.center_x < self.apple.center_x :
            self.snake.change_x = 1
        elif self.snake.center_x > self.apple.center_x :
            self.snake.change_x = -1
        elif self.snake.center_x == self.apple.center_x :
            self.snake.change_x = 0    
        
        if self.snake.center_y > self.apple.center_y :
            self.snake.change_y = -1
        elif self.snake.center_y < self.apple.center_y :
            self.snake.change_y = 1
        elif self.snake.center_y == self.apple.center_y:
            self.snake.change_y = 0                
        
        self.snake.move()

        #mosavi shodan mokhtasat 2 shey dar arcade == true
        if arcade.check_for_collision(self.snake , self.apple):
            self.snake.eat('apple')
            self.apple = Apple()
        elif arcade.check_for_collision(self.snake , self.poire):
            self.snake.eat('poire')
            self.poire = Poire()
        elif arcade.check_for_collision(self.snake , self.poo):           
            self.snake.eat('poo')
            self.poo = Poo()

game = Game()
arcade.run()