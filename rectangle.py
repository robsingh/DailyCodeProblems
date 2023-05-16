"""
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other. 
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""

def check_rectangle_overlap(rectangles):
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            rect1 = rectangles[i]
            rect2 = rectangles[j]

            x1,y1 = rect1["top_left"]
            w1,h1 = rect1["dimensions"]
            x2,y2 = rect2["top_left"]
            w2,h2 = rect2["dimensions"]

            if x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
                return True
    return False


rectangles = [
    {
        "top_left" : (1,4),
        "dimensions": (3,3)
    },
    {
        "top_left": (-1,3),
        "dimensions": (2,1)
    },
    {
        "top_left": (0,5),
        "dimensions": (4,3)
    }
]

overlap = check_rectangle_overlap(rectangles)
print(overlap)