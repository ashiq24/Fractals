# Happy L Fractals
A simple tool to draw fractal from it's L-system description.
## Sample Interface
![alt text](https://raw.githubusercontent.com/ashiq24/Fractals/main/interface.PNG)

## Input Description
Axiom: The initial string for the generation.
Rules: A set of production rules. Rules are taken in form of Python Dictionaries.
Angle: Required Angle of roation for the fractals.
Side Length: Length of each side of the Fractals.
Sample input for Piano-Gosper-Curve is:
                Axiom = FX
                Rules = {\"X\":\"X+YF++YF-FX--FXFX-YF+\", \"Y\":\"-FX+YFYF++YF+FX--FX-Y"}
                Iterations = 4 \n \
                Angle = 60 \n \
                Side Length = 3"
