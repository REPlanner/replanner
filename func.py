def calculate_ones(a):
    import numpy as np
    count=0
    for v in np.nditer(a):
        if v==1:
            count+= 1
    print(count)


def NFZ_distance(Agent,NFZ_list,boundary):
    x_dis=0
    y_dis=0
    for i in range(len(NFZ_list)):
        x_dis += (Agent-NFZ_list[i])[0]
        y_dis += (Agent-NFZ_list[i])[1]
    return (x_dis%boundary,y_dis%boundary)




def assign_weights(agent):
    import math

    points = agent.goals
#     print(points)
    for i in range(len(points)):
        a = points[i][0]-agent.x
        b = points[i][1]-agent.y

        c = math.sqrt(a**2+b**2)

        agent.visited[i]=c


def calculate_distance(Agent_list,POI):
    import math

    list_val =[]
    for i in range(len(Agent_list)):
        a = Agent_list[i].x-POI.x
        b = Agent_list[i].y-POI.y
        
        c = math.sqrt(a**2+b**2)

        list_val.append(c)

    val, idx = min((val, idx) for (idx, val) in enumerate(list_val))
    

    return (idx,val)


def create_output_files(sin_list, name):
    
    import re
    import random
    
    height = random.randint(10,15)

    new = ""
    for x in sin_list:
        try:
            new = new+str(x[0])+" "+str(x[1])+" "+str(height)+"\n"
        except:
            break

    out_file = open("outputs/"+name, "w")
    out_file.write(new)
    out_file.close()