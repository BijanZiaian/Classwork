import arcade


WIDTH = 640
HEIGHT = 480

# x , y , radius
x = int(input("please enter the x value: "))
y = int(input("please enter the y value: "))
radius = int(input("please enter the radius value: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.DARK_VANILLA)

# End drawing
arcade.finish_render()
arcade.run()