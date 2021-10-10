import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.walls_list = None
        self.brick_list = None
        self.bat_list = None
        self.physics_engine = None

        self.bat_list = None
        self.radius = 10 
        self.y = 104
        self.velocity_up = 200 #it autos up
        self.velocity_right = 200 #it autos to the right
        self.x = 300
        self.message_color = arcade.color.SKY_BLUE

        self.bat = arcade.Sprite(":resources:images/tiles/bridgeA.png", 0.3)
        self.bat.center_x = 300
        self.bat.center_y = 75

    def setup(self):
        self.walls_list = arcade.SpriteList()

        self.bat_list = arcade.SpriteList()

        self.brick_list = arcade.SpriteList()

        self.create_walls()
        self.create_bat()
        
        for row_num in range(4):
            self.create_bricks(row_num)

        self.physics_engine = arcade.PhysicsEngineSimple(self.bat, self.walls_list)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.walls_list.draw()
        self.bat_list.draw()
        self.brick_list.draw()

        arcade.draw_text("GAME OVER.", 43, 275, self.message_color, 60)
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.RED)
        self.bat_list.draw()


    def update(self, delta_time): #update updates on it's own this is an event listener!!!
        #left and right
        self.physics_engine.update()

        self.x += self.velocity_right * delta_time 
        is_at_right = self.x > self.width - self.radius - 40
        is_at_left = self.x - 40 < self.radius
        

        #is_bat_left = self.x > self.bat.center_x - 30
        #is_bat_right = self.x < self.bat.center_x + 30
        is_bat_right = self.x < self.bat.center_x + 30 #position is less than 330
        is_bat_left = self.x > self.bat.center_x - 30 #position is greater than 270
        if is_at_right or is_at_left:
            self.velocity_right *= -1

        #up and down
        self.y += self.velocity_up * delta_time 
        is_at_top = self.y > self.width - self.radius - 40
        is_at_bottom = self.y < self.radius + 40
        is_at_bat_top = self.y < self.radius + self.bat.center_y + 19 # position less than 75 + 19 + 10 = 104
        is_at_bat_bottom = self.y > self.bat.center_y - 5 #position greater than 75 - 10 = 65
        
        if is_at_top or (is_at_bat_top and is_at_bat_bottom and is_bat_right and is_bat_left):
            self.velocity_up *= -1
        if is_at_bottom:
            self.velocity_up = 0
            self.velocity_right = 0
            self.message_color = arcade.color.BLACK
        #hello
        

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT:
            self.bat.change_x = -5
        elif symbol == arcade.key.RIGHT:
            self.bat.change_x = 5

    def create_bricks(self, row_num):

        y_coordinate = 0

        if row_num == 1:
            y_coordinate = 25
        elif row_num == 2:
            y_coordinate = 50
        elif row_num == 3:
            y_coordinate = 75

        for x in range(80, 525, 22):
            bricks = arcade.Sprite(":resources:images/items/coinGold.png", 0.3)
            bricks.center_x = x
            bricks.center_y = 400 + y_coordinate
            self.brick_list.append(bricks)

    def create_bat(self):
        self.bat = arcade.Sprite(":resources:images/tiles/bridgeA.png", 0.3)
        self.bat.center_x = 300
        self.bat.center_y = 75
        self.bat_list.append(self.bat)

    def create_walls(self):
        # top wall
        for x in range(10, 600, 34):
            top_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            top_wall.center_x = x
            top_wall.center_y = 580
            self.walls_list.append(top_wall)

        # right wall
        for y in range(10, 600, 34):
            right_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            right_wall.center_x = 580
            right_wall.center_y = y
            self.walls_list.append(right_wall)

        # left wall
        for y in range(10, 600, 34):
            left_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            left_wall.center_x = 20
            left_wall.center_y = y
            self.walls_list.append(left_wall)

        # bottom wall
        for x in range(10, 600, 34):
            bottom_wall = arcade.Sprite(":resources:images/tiles/lava.png", 0.3)
            bottom_wall.center_x = x
            bottom_wall.center_y = 20
            self.walls_list.append(bottom_wall)
