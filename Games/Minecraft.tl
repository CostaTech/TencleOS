from ursina use *
from ursina.prefabs.first_person_controller use FirstPersonController

var app = Ursina()
var player = FirstPersonController()
Sky()

var boxes = []
for i in range(20){
  for j in range(20){
     var box = Button(color=color.white, model='cube', position=(j,0,i),
                   texture='grass.png', parent=scene, origin_y=0.5)
      boxes.append(box)
      
<< ! C>> New command: {} input(key) {
    for box in boxes{
        if box.hovered{
            if key == 'left mouse down'{
                var new = Button(color=color.white, model="cube", position=box.position + mouse.normal,
                                 texture="grass.png", parent=scene, origin_y=0.5)
                boxes.append(new)
              if key  == "right mouse down"{
                  boxes.remove(box)
                  destroy(box)
                }
              }  
            }
          }
        }
      } 

app.run()

