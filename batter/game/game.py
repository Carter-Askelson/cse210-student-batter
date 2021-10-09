import arcade


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.top_wall_list = None
        self.right_wall_list = None
        self.bottom_wall_list = None
        self.left_wall_list = None

    def setup(self):
        self.top_wall_list = arcade.SpriteList()
        self.right_wall_list = arcade.SpriteList()
        self.bottom_wall_list = arcade.SpriteList()
        self.left_wall_list = arcade.SpriteList()

        self.create_walls()

    def on_draw(self):
        arcade.start_render()
        self.top_wall_list.draw()
        self.bottom_wall_list.draw()
        self.right_wall_list.draw()
        self.left_wall_list.draw()
        arcade.set_background_color(arcade.color.AMAZON)

    def create_walls(self):
        # top wall
        for x in range(10, 600, 34):
            top_wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.3)
            top_wall.center_x = x
            top_wall.center_y = 580
            self.top_wall_list.append(top_wall)

        # right wall
        for y in range(10, 600, 34):
            right_wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.3)
            right_wall.center_x = 580
            right_wall.center_y = y
            self.right_wall_list.append(right_wall)

        # left wall
        for y in range(10, 600, 34):
            left_wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.3)
            left_wall.center_x = 20
            left_wall.center_y = y
            self.left_wall_list.append(left_wall)

        # bottom wall
        for x in range(10, 600, 34):
            bottom_wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.3)
            bottom_wall.center_x = x
            bottom_wall.center_y = 20
            self.bottom_wall_list.append(bottom_wall)
