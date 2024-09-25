import math

def end_wall(circle_start,wall_length,wall_number):
    return circle_start+wall_number-1+(wall_length-1)*wall_number

square = 361527

circle = math.ceil(math.sqrt(2*(square-1)/8+1/4)-1/2)
circle_start = 8*((circle-1)*((circle)/2))+2
wall_length = 8*circle/4

for i in range(1,5):
    end_wall = end_wall(circle_start,wall_length,i)
    if square <= end_wall:
        distance_to_middle = abs(square-(end_wall-wall_length/2))
        print(distance_to_middle + circle)
        break