import turtle
turtle.shape('turtle')
finn = turtle.clone()
finn.shape('square')
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)
charlie = turtle.clone()
charlie.shape('triangle')
charlie.goto(50,100)
charlie.goto(100,0)
charlie.goto(0,0)
finn.goto(300,300)
finn.stamp()
finn.goto(100,100)
turtle.stamp()
turtle.goto(0,200)
turtle.clearstamps()






turtle.mainloop()

