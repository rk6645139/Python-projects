# from collections import deque

# def water_jug_problem(jug1, jug2, target):
#     # Each state is represented as (x, y) where:
#     # x = amount in jug1, y = amount in jug2
#     visited = set()
#     queue = deque([(0, 0)])  # start with both empty

#     while queue:
#         x, y = queue.popleft()

#         # If solution found
#         if x == target or y == target:
#             print(f"Reached target: ({x}, {y})")
#             return True

#         # If state already visited, skip
#         if (x, y) in visited:
#             continue
#         visited.add((x, y))

#         # Possible next moves
#         next_states = set()

#         # Fill jugs
#         next_states.add((jug1, y))   # fill jug1
#         next_states.add((x, jug2))   # fill jug2

#         # Empty jugs
#         next_states.add((0, y))      # empty jug1
#         next_states.add((x, 0))      # empty jug2

#         # Pour jug1 -> jug2
#         pour = min(x, jug2 - y)
#         next_states.add((x - pour, y + pour))

#         # Pour jug2 -> jug1
#         pour = min(y, jug1 - x)
#         next_states.add((x + pour, y - pour))

#         # Add next states to queue
#         for state in next_states:
#             if state not in visited:
#                 queue.append(state)

#     print("No solution found.")
#     return False

# # Example usage
# water_jug_problem(4, 3, 2)
from collections import deque

def water_jug_problem(jug1, jug2, jug3):
    visited =set()
    queue=deque([((0,0),[])])

    while queue:
        (x,y), path =queue.popleft()


        if x==target or  y==target:
            path.append((x,y))
            print("\mSolution found! Steps:")
            for step in path:
                print(step)

            return True
        
        if(x,y)in visited:
            continue
        visited.add((x,y))

        next_steps=[

            ((jug1, y), "Fill jug1"),
            ((x, jug2),"Fill jug2"),
            ((0,y), "Empty jug1"),
            ((x,0), "Empty jug2"),
            ((x- min(x, jug2-y), y+min(x, jug2-y)), "Pour Jug1 -> jug2"),
            ((x+min(x, jug1-x), y-min(y, jug1-x)), "Pour Jug2 -> jug1"),

        ]

        print("No solution possible")
        return False
    

if __name__ =="__main__":
    jug1=int(input("Enter capacity of jug1:"))
    jug2=int(input("enter capacity of jug2:"))
    target =int(input("enter target amount:"))

    water_jug_problem(jug1, jug2, target)

