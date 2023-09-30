# Implementing naiveTSP using python
# Time complexity -> O(n!) because it uses a brute-force approach that generates all possible permutations of cities and calculates the total distance for each permutation.


import itertools
import time


def naiveTSP(m):
    n = len(m)        # Number of citites
    startCity = 0    
    cities = list(range(n)) # Creating list of cities
    cities.remove(startCity) 

    minDistance = float('inf') # minimum distance initialised to infinity
    bestRoute = []

    for perm in itertools.permutations(cities):  #Generating all possible permutations of cities to visit, excluding the starting city
        # print(perm)
        currentRoute = list(perm)
        currentDistance = calTotalDistance(startCity,currentRoute, m)

        # print(currentDistance)
        if currentDistance < minDistance:  #Updating minimum distance and best route if found
            minDistance = currentDistance
            bestRoute = [startCity]+currentRoute+[startCity]

    return bestRoute, minDistance

def calTotalDistance(startCity,route, m):
    totalDistance = 0
    currentCity=startCity

    for nextCity in route:
        totalDistance += m[currentCity][nextCity]
        # print(totalDistance)
        currentCity=nextCity

    totalDistance+=m[currentCity][startCity]    

    return totalDistance


#### Test Cases: range(4-14)cities  #####

connectivity_matrix=[
 [    # 4 cities
          [0, 10, 15, 20], 
          [10, 0, 35, 25],
          [15, 35, 0, 30],
          [20, 25, 30, 0]
]
, [ # 5 cities
    [0, 12, 15, 20, 10],
    [12, 0, 35, 25, 9],
    [15, 35, 0, 30, 18],
    [20, 25, 30, 0, 17],
    [10, 9, 18, 17, 0]
]
,[  # 6 cities
    [0, 12, 15, 20, 10, 8],
    [12, 0, 35, 25, 9, 14],
    [15, 35, 0, 30, 18, 12],
    [20, 25, 30, 0, 17, 6],
    [10, 9, 18, 17, 0, 19],
    [8, 14, 12, 6, 19, 0]
]
, [  # 7 cities
    [0, 10, 15, 20, 25, 30, 35],
    [10, 0, 5, 15, 20, 25, 30],
    [15, 5, 0, 10, 15, 20, 25],
    [20, 15, 10, 0, 5, 10, 15],
    [25, 20, 15, 5, 0, 5, 10],
    [30, 25, 20, 10, 5, 0, 5],
    [35, 30, 25, 15, 10, 5, 0]
]
, [ # 8 cities
    [0, 10, 15, 20, 25, 30, 35, 40],
    [10, 0, 5, 15, 20, 25, 30, 35],
    [15, 5, 0, 10, 15, 20, 25, 30],
    [20, 15, 10, 0, 5, 10, 15, 20],
    [25, 20, 15, 5, 0, 5, 10, 15],
    [30, 25, 20, 10, 5, 0, 5, 10],
    [35, 30, 25, 15, 10, 5, 0, 5],
    [40, 35, 30, 20, 15, 10, 5, 0]
]
, [  # 9 cities
    [0, 10, 15, 20, 25, 30, 35, 40, 45],
    [10, 0, 5, 15, 20, 25, 30, 35, 40],
    [15, 5, 0, 10, 15, 20, 25, 30, 35],
    [20, 15, 10, 0, 5, 10, 15, 20, 25],
    [25, 20, 15, 5, 0, 5, 10, 15, 20],
    [30, 25, 20, 10, 5, 0, 5, 10, 15],
    [35, 30, 25, 15, 10, 5, 0, 5, 10],
    [40, 35, 30, 20, 15, 10, 5, 0, 5],
    [45, 40, 35, 25, 20, 15, 10, 5, 0]
]
,[  # 10 cities
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    [10, 0, 5, 15, 20, 25, 30, 35, 40, 45],
    [15, 5, 0, 10, 15, 20, 25, 30, 35, 40],
    [20, 15, 10, 0, 5, 10, 15, 20, 25, 30],
    [25, 20, 15, 5, 0, 5, 10, 15, 20, 25],
    [30, 25, 20, 10, 5, 0, 5, 10, 15, 20],
    [35, 30, 25, 15, 10, 5, 0, 5, 10, 15],
    [40, 35, 30, 20, 15, 10, 5, 0, 5, 10],
    [45, 40, 35, 25, 20, 15, 10, 5, 0, 5],
    [50, 45, 40, 30, 25, 20, 15, 10, 5, 0]
]
, [ # 11 cities
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    [10, 0, 5, 15, 20, 25, 30, 35, 40, 45, 50],
    [15, 5, 0, 10, 15, 20, 25, 30, 35, 40, 45],
    [20, 15, 10, 0, 5, 10, 15, 20, 25, 30, 35],
    [25, 20, 15, 5, 0, 5, 10, 15, 20, 25, 30],
    [30, 25, 20, 10, 5, 0, 5, 10, 15, 20, 25],
    [35, 30, 25, 15, 10, 5, 0, 5, 10, 15, 20],
    [40, 35, 30, 20, 15, 10, 5, 0, 5, 10, 15],
    [45, 40, 35, 25, 20, 15, 10, 5, 0, 5, 10],
    [50, 45, 40, 30, 25, 20, 15, 10, 5, 0, 5],
    [55, 50, 45, 35, 30, 25, 20, 15, 10, 5, 0]
]
,[  # 12 cities                        
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    [10, 0, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    [15, 5, 0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    [20, 15, 10, 0, 5, 10, 15, 20, 25, 30, 35, 40],
    [25, 20, 15, 5, 0, 5, 10, 15, 20, 25, 30, 35],
    [30, 25, 20, 10, 5, 0, 5, 10, 15, 20, 25, 30],
    [35, 30, 25, 15, 10, 5, 0, 5, 10, 15, 20, 25],
    [40, 35, 30, 20, 15, 10, 5, 0, 5, 10, 15, 20],
    [45, 40, 35, 25, 20, 15, 10, 5, 0, 5, 10, 15],
    [50, 45, 40, 30, 25, 20, 15, 10, 5, 0, 5, 10],
    [55, 50, 45, 35, 30, 25, 20, 15, 10, 5, 0, 5],
    [60, 55, 50, 40, 35, 30, 25, 20, 15, 10, 5, 0]
]

# ,[   # 13 cities
       ######*** my laptop overheated after reaching city 13 adn 14 ***######

#     [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
#     [10, 0, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
#     [15, 5, 0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
#     [20, 15, 10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
#     [25, 20, 15, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40],
#     [30, 25, 20, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35],
#     [35, 30, 25, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30],
#     [40, 35, 30, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25],
#     [45, 40, 35, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20],
#     [50, 45, 40, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15],
#     [55, 50, 45, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10],
#     [60, 55, 50, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5],
#     [65, 60, 55, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
# ]
# ,
#  [  # 14 cities
#     [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
#     [10, 0, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
#     [15, 5, 0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
#     [20, 15, 10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
#     [25, 20, 15, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
#     [30, 25, 20, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40],
#     [35, 30, 25, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35],
#     [40, 35, 30, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30],
#     [45, 40, 35, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25],
#     [50, 45, 40, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20],
#     [55, 50, 45, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15],
#     [60, 55, 50, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5, 10],
#     [65, 60, 55, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 5],
#     [70, 65, 60, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]
# ]
]


# code to the compare the execution time as we increase the number of cites.
i=4
for connectivity_matrix in connectivity_matrix:
    start_time = time.time()
    result=naiveTSP(connectivity_matrix)
    # for i in range(len(result)):
    print(f"Best route: {result[0]}" )
    print(f"Minimum distance:{result[1]}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for naiveTSP with {i} cities==>{execution_time}\n")
    i+=1


# Final conclusion of the result:
# Time complexity is O(n!) because this approach generates all possible permutations of cities and calculates the total distance for each permutation.
# But this appraoch could work for small number of cities from[4-9] as it generated permutations fairly quickly
# For 12 cities it took 30 seconds to arrive at a solution
# For 13-14 cities it could not compute the optimal result as my laptop got overheated
# In conclusion this method cannot be used in a real world problem
