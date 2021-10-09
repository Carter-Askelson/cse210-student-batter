import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.top_wall_list = None
        self.right_wall_list = None
        self.bottom_wall_list = None
        self.left_wall_list = None

        self.bat_list = None

    def setup(self):
        self.top_wall_list = arcade.SpriteList()
        self.right_wall_list = arcade.SpriteList()
        self.bottom_wall_list = arcade.SpriteList()
        self.left_wall_list = arcade.SpriteList()

        self.bat_list = arcade.SpriteList()

        self.brick_list = arcade.SpriteList()

        self.create_walls()
        self.create_bat()

        for row_num in range(4):
            self.create_bricks(row_num)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.top_wall_list.draw()
        self.bottom_wall_list.draw()
        self.right_wall_list.draw()
        self.left_wall_list.draw()

        self.bat_list.draw()

        self.brick_list.draw()

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
            self.top_wall_list.append(bricks)

    def create_bat(self):
        bat = arcade.Sprite(":resources:images/tiles/bridgeA.png", 0.3)
        bat.center_x = 300
        bat.center_y = 75
        self.bat_list.append(bat)

    def create_walls(self):
        # top wall
        for x in range(10, 600, 34):
            top_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            top_wall.center_x = x
            top_wall.center_y = 580
            self.top_wall_list.append(top_wall)

        # right wall
        for y in range(10, 600, 34):
            right_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            right_wall.center_x = 580
            right_wall.center_y = y
            self.right_wall_list.append(right_wall)

        # left wall
        for y in range(10, 600, 34):
            left_wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", 0.3)
            left_wall.center_x = 20
            left_wall.center_y = y
            self.left_wall_list.append(left_wall)

        # bottom wall
        for x in range(10, 600, 34):
            bottom_wall = arcade.Sprite(":resources:images/tiles/lava.png", 0.3)
            bottom_wall.center_x = x
            bottom_wall.center_y = 20
            self.bottom_wall_list.append(bottom_wall)
