# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     t=(integer_list)
#     has =hash(t)
#     print(has)

#======================================================================================================================

#Next Question


# from itertools import product

# if __name__ == '__main__':

#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input()) 
#     permutations = list(product(range(x+1), range(y+1), range(z+1)))
    
#     validPermutations=[perm for perm in permutations if sum(perm)!=n]
#     print("[", end="")
#     print(", ".join([f"[{perm[0]}, {perm[1]}, {perm[2]}]" for perm in validPermutations]), end="")
#     print("]")

#=====================================================================================================================================
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float , line))
#         student_marks[name] = scores
#     query_name = input()
#     sum=0
#     count=0
    
#     for i in scores:=========================should've  used scores for queried nsme only ut instead i used for entire score input
        
#         sum+=scores[i]
#         count= count+1

#     if count!=0:
#         avg =float(sum/count)
# print(avg) 


# =========================optimised by chatGPT===============================================================================================
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
    
#     # Reading student names and scores
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores  # Store each student's scores in the dictionary
    
#     query_name = input()  # Student name to query
    
#     # Retrieve the scores for the queried student
#     scores = student_marks[query_name]
    
#     # Calculate the average
#     avg = sum(scores) / len(scores)  # Directly calculate average
    
#     # Print the average up to 2 decimal places
#     print(f"{avg:.2f}")

# ==========================================================================================================================================
# for i in range(5):
#     for j in range(0, i):
#         print("*", end='')


#     print()


# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*", end='')


#     print()


# def pyramid(rows):
#     for i in range(rows):
#         # Print spaces to center the stars
#         print("*" * (rows - i - 1) + " " * (2 * i + 1) + "*" * (rows - i - 1) )

# # Example usage
# pyramid(7)

# def pyramid(rows):
#     for i in range(rows):
#         # Print spaces to center the stars
#         print(" " * (rows - i - 1) + "*" * (2 * i + 1)  )

# # Example usage
# pyramid(7)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import math

# def flower_pattern(size):
#     for y in range(-size, size + 1):
#         for x in range(-size, size + 1):
#             distance = math.sqrt(x**2 + y**2)
#             # Condition to draw the petal shapes
#             if abs(distance - size) < 2 or abs(distance - size/2) < 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# # Example usage
# flower_pattern(10)

# ////////////////////////////////////////////////////////////////////////////////////////////////
# import turtle

# def draw_flower():
#     # Setup the turtle
#     window = turtle.Screen()
#     window.bgcolor("white")

#     flower = turtle.Turtle()
#     flower.shape("turtle")
#     flower.speed(5)
#     flower.color("red")

#     # Draw petals in a circle
#     for _ in range(36):
#         flower.circle(50, 60)  # Create a curved petal shape
#         flower.left(120)       # Move to the opposite side for symmetry
#         flower.circle(50, 60)
#         flower.right(150)      # Move back to original orientation

#     # Draw the stem
#     flower.color("green")
#     flower.right(90)
#     flower.forward(200)

#     # Draw leaves
#     flower.color("lightgreen")
#     flower.right(45)
#     flower.forward(50)
#     flower.backward(50)
#     flower.left(90)
#     flower.forward(50)
#     flower.backward(50)

#     window.exitonclick()

# # Call the function to draw the flower
# draw_flower()
import turtle

def draw_flower():
    # Setup the window and turtle
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.speed(100)  # Set the turtle's speed for faster drawing
    flower.width(3)   # Set the width of the turtle's pen

    # Draw petals with gradient effect
    flower.color("blue")
    for _ in range(36):  # 36 petals for a full circle
        flower.fillcolor("yellow")  # Change the fill color for a gradient effect
        flower.begin_fill()
        flower.circle(100, 60)  # Draw the petal with radius 100 and arc angle 60
        flower.left(120)
        flower.circle(100, 60)  # Draw the second half of the petal
        flower.end_fill()
        flower.left(10)  # Turn the turtle to draw the next petal

    # Draw the stem
    flower.color("green")
    flower.right(90)  # Position the turtle to draw the stem downwards
    flower.forward(200)

    # Draw leaves
    flower.color("lightgreen")
    flower.right(45)
    flower.forward(50)
    flower.backward(50)
    flower.left(90)
    flower.forward(50)
    flower.backward(50)

    # Draw more leaves on the other side
    flower.right(45)
    flower.forward(50)
    flower.backward(50)
    flower.left(90)
    flower.forward(50)
    flower.backward(50)

    window.exitonclick()

# Call the function to draw the flower
draw_flower()



