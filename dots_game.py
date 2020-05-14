import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
HEIGHT = 600
WIDHT = 600
ball_pos = (WIDHT/2, HEIGHT/2)
BALL_RADUIS = 20
ball_color = "Red"
my_circles = [ball_pos]

def mouseClick(pos):
   global ball_pos
   global my_circles
   global ball_color
   ball_pos = pos
   
   #check if any inside of circle
   ball_found = False
   for circle_pos in my_circles:
      d = distance(circle_pos, ball_pos)
      
      if d <= BALL_RADUIS:
         
         ball_pos =  circle_pos
         ball_color = "Yellow"
         ball_found = True
         
      if ball_found == False:
         my_circles.append(ball_pos)
         ball_color = "Red"
   
#image = simplegui.load_image("http://www.groupce.com/python/images/poke/image01.jpg")
def draw(canvas):
   for circle_pos in my_circles:
      canvas.draw_circle(circle_pos, BALL_RADUIS, 1, "black", ball_color)

def distance(pos1, pos2):
   x1 = pos1[0]
   x2 = pos2[0]
   y1 = pos1[1]
   y2 = pos2[1]   
   d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   return d

##create frame
frame = simplegui.create_frame("MOuse", WIDHT, HEIGHT)
    
#frame.set_canvas_background('white')
    
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseClick)

frame.start()
frame.start()