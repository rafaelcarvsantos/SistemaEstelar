"""
Simple example showing some animated shapes
"""


import math
import pyglet
import random
from numpy import array
from numpy import tan
from numpy import rot90
from numpy import linalg
from numpy import sqrt
from numpy import power
import numpy as np

from pyglet import shapes
G = 6e-11
SolMass = array([2e30], dtype=float)
TerraMass = array([6e30], dtype=float)

def Gravity(Position1, Position2, Mass1, Mass2):

    Direction = (array(Position1) - array(Position2))*1e8
    Unit = Direction / abs(linalg.norm(Direction))
    Direction_norm = -((-G*Mass1*Mass2)/power(abs(linalg.norm(Direction)),2))*Unit
    Force =Direction_norm

    return Force

class Star():
    def __init__(self, positionx, positiony, mass,batch):
        # (random.choices(range(256), k=3))
        self.position=array([positionx,positiony])
        self.acceleration = array([0,0])
        self.mass = mass
        self.radius = mass/1e29
        self.circle = shapes.Circle(self.position[0],self.position[1], self.radius, color=(random.choices(range(256), k=3)), batch=batch)

class Planet():
    def __init__(self, positionx, positiony, mass,batch):
        # (random.choices(range(256), k=3))
        self.position = array([positionx, positiony])
        self.velocity = array([0.0, 0.0])
        self.acceleration = array([0.0, 0.0])
        self.mass = mass
        self.radius = mass/1e30
        self.circle = shapes.Circle(self.position[0],self.position[1], self.radius, color=(random.choices(range(256), k=3)), batch=batch)

    def ApplyForce(self,force):
        self.acceleration = (force) /self.mass
        self.velocity = self.velocity+ self.acceleration

class ShapesDemo(pyglet.window.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Shapes")
        self.batch = pyglet.graphics.Batch()
        self.time = 0
        self.Start = 0
        self.centerx = height/2
        self.centery = width/2
        self.Sol = Star(self.centerx,self.centery,SolMass,self.batch)
        self.Terra = Planet(self.centerx+300,self.centery,TerraMass*0.9,self.batch)
        self.Terra2 = Planet(self.centerx + 350, self.centery, TerraMass * 0.8, self.batch)
        self.Terra3 = Planet(self.centerx + 450, self.centery, TerraMass*2, self.batch)
        self.Terra4 = Planet(self.centerx + 500, self.centery , TerraMass * 1.5, self.batch)
        self.Terra.ApplyForce([0, 2e31])
        self.Terra2.ApplyForce([0,-2.85e31])
        self.Terra3.ApplyForce([0, 6.2e31])
        self.Terra4.ApplyForce([0, 4.5e31])
        self.Planets = []
        self.Planets.append(self.Terra)
        self.Planets.append(self.Terra2)
        self.Planets.append(self.Terra3)
        self.Planets.append(self.Terra4)





    def on_draw(self):
        """Clear the screen and draw shapes"""
        self.clear()
        self.batch.draw()

    def on_key_press(self,symbol, modifier):
        if symbol == pyglet.window.key.SPACE:
            self.Start = 1
        else:
            pass

    def update(self, delta_time):
        self.time += delta_time
        if self.Start == 0:
            pass
        if self.Start == 1:
            """Animate the shapes"""
            for i in self.Planets:
                if abs(i.circle.position[0]-self.Sol.circle.position[0]) < 30 and abs(i.circle.position[1]-self.Sol.circle.position[1]) < 30:
                   i.acceleration = [0,0]
                else:
                    i.circle.position = i.circle.position + i.velocity
                    i.ApplyForce((Gravity(self.Sol.circle.position, i.circle.position, self.Sol.mass, i.mass)))
                    print(i.acceleration)






if __name__ == "__main__":

    demo = ShapesDemo(1500,1500)
    pyglet.clock.schedule_interval(demo.update, 1 / 30)
    pyglet.app.run()



"""
Simple example showing some animated shapes
"""


import math
import pyglet
import random
from numpy import array
from numpy import tan
from numpy import rot90
from numpy import linalg
from numpy import sqrt
from numpy import power
import numpy as np

from pyglet import shapes
G = 6e-11
SolMass = array([2e30], dtype=float)
TerraMass = array([6e30], dtype=float)

def Gravity(Position1, Position2, Mass1, Mass2):

    Direction = (array(Position1) - array(Position2))*1e8
    Unit = Direction / abs(linalg.norm(Direction))
    Direction_norm = -((-G*Mass1*Mass2)/power(abs(linalg.norm(Direction)),2))*Unit
    Force =Direction_norm

    return Force

class Star():
    def __init__(self, positionx, positiony, mass,batch):
        # (random.choices(range(256), k=3))
        self.position=array([positionx,positiony])
        self.acceleration = array([0,0])
        self.mass = mass
        self.radius = mass/1e29
        self.circle = shapes.Circle(self.position[0],self.position[1], self.radius, color=(random.choices(range(256), k=3)), batch=batch)

class Planet():
    def __init__(self, positionx, positiony, mass,batch):
        # (random.choices(range(256), k=3))
        self.position = array([positionx, positiony])
        self.velocity = array([0.0, 0.0])
        self.acceleration = array([0.0, 0.0])
        self.mass = mass
        self.radius = mass/1e30
        self.circle = shapes.Circle(self.position[0],self.position[1], self.radius, color=(random.choices(range(256), k=3)), batch=batch)

    def ApplyForce(self,force):
        self.acceleration = (force) /self.mass
        self.velocity = self.velocity+ self.acceleration

class ShapesDemo(pyglet.window.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Shapes")
        self.batch = pyglet.graphics.Batch()
        self.time = 0
        self.Start = 0
        self.centerx = height/2
        self.centery = width/2
        self.Sol = Star(self.centerx,self.centery,SolMass,self.batch)
        self.Terra = Planet(self.centerx+300,self.centery,TerraMass*0.9,self.batch)
        self.Terra2 = Planet(self.centerx + 350, self.centery, TerraMass * 0.8, self.batch)
        self.Terra3 = Planet(self.centerx + 450, self.centery, TerraMass*2, self.batch)
        self.Terra4 = Planet(self.centerx + 500, self.centery , TerraMass * 1.5, self.batch)
        self.Terra.ApplyForce([0, 2e31])
        self.Terra2.ApplyForce([0,-2.85e31])
        self.Terra3.ApplyForce([0, 6.2e31])
        self.Terra4.ApplyForce([0, 4.5e31])
        self.Planets = []
        self.Planets.append(self.Terra)
        self.Planets.append(self.Terra2)
        self.Planets.append(self.Terra3)
        self.Planets.append(self.Terra4)





    def on_draw(self):
        """Clear the screen and draw shapes"""
        self.clear()
        self.batch.draw()

    def on_key_press(self,symbol, modifier):
        if symbol == pyglet.window.key.SPACE:
            self.Start = 1
        else:
            pass

    def update(self, delta_time):
        self.time += delta_time
        if self.Start == 0:
            pass
        if self.Start == 1:
            """Animate the shapes"""
            for i in self.Planets:
                if abs(i.circle.position[0]-self.Sol.circle.position[0]) < 30 and abs(i.circle.position[1]-self.Sol.circle.position[1]) < 30:
                   i.acceleration = [0,0]
                else:
                    i.circle.position = i.circle.position + i.velocity
                    i.ApplyForce((Gravity(self.Sol.circle.position, i.circle.position, self.Sol.mass, i.mass)))
                    print(i.acceleration)






if __name__ == "__main__":

    demo = ShapesDemo(1500,1500)
    pyglet.clock.schedule_interval(demo.update, 1 / 30)
    pyglet.app.run()



