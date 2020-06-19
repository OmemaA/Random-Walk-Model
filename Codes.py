import random
import turtle
import numpy as np
import math
from sympy import symbols, Eq, solve
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def task1(steps, prob, move, pos):
    x = pos
    if not move: 
        return x
    for _ in range(steps):
        if random.random() < prob: 
            x-=1
        else: 
            x+=1
    return x

def task2(prob, move1, move2):
    x, y = 0, 50
    steps = 0
    while x!=y:
        if random.random() < prob:
            x-=1
            x*=move1
            y+=1
            y*=move2
        else:
            x+=1
            x*=move1
            y-=1
            y*=move2
        steps+=1
    return steps

def task3(steps, p1=True, p2=True):
    orientation_prob = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    step_prob = [1/3, 1/3, 1/3]
    orientation = [0, 45, 90, 135, 180, 225, 270, 315]
    step_size = [0, 0.5, 1]
    coords = []
    old_x = 0
    old_y = 0
    if not p1:
        orientation_prob = [0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.2, 0.1]
    if not p2:
        step_prob = [0.2, 0.3, 0.5]
    for _ in range(steps):
        angle = np.random.choice(orientation, p=orientation_prob)
        step = np.random.choice(step_size, p=step_prob)
        new_x = old_x + step* math.cos(angle)
        new_y = old_y + step* math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <=100:
            coords.append((round(new_x),round(new_y)))
        else:
            print("X:", new_x, '\n', "Y:", new_y)
            reflected_angle = 270 +  angle
            m = (new_y-old_y)/(new_x-old_x)
            x, y = symbols('x y')
            line_eqn = Eq(m*(x-new_x)  + new_y - y, 0)
            print("Line Equation:", line_eqn)
            circle_eqn = Eq(x**2 + y**2 - 100**2, 0)
            print("Circle Equation:", circle_eqn)
            x1, y1 = solve((line_eqn, circle_eqn), (x,y))[0]
            x2, y2 = solve((line_eqn, circle_eqn), (x,y))[1]
            dist1 = math.sqrt((y1 - new_y)**2 + (x1 - new_x)**2)
            dist2 = math.sqrt((y2 - new_y)**2 + (x2 - new_x)**2)
            if dist1>dist2:
                x, y = x2, y2
            else:
                x, y = x1, y1
            #coords.append((round(x),round(y)))
            dist_rem = step-math.sqrt((new_y)**2 + (new_x)**2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            coords.append((round(new_x),round(new_y)))
        old_x = new_x
        old_y = new_y
    return coords


def task4(steps, prob, move):
    x = 0
    if not move: 
        return x
    for _ in range(steps):
        if random.random() < prob: 
            x-= np.random.uniform(0,1)
        else: 
            x+= np.random.uniform(0,1)
    return x

def task5(steps):
    coords = []
    old_x = 0
    old_y = 0
    for _ in range(steps):
        angle = np.random.uniform(0,(2*math.pi))
        step = np.random.uniform(0,1)
        new_x = old_x + step* math.cos(angle)
        new_y = old_y + step* math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <=100:
            coords.append((round(new_x),round(new_y)))
        else:
            print("X:", new_x, '\n', "Y:", new_y)
            reflected_angle = 270 +  angle
            m = (new_y-old_y)/(new_x-old_x)
            x, y = symbols('x y')
            line_eqn = Eq(m*(x-new_x)  + new_y - y, 0)
            print("Line Equation:", line_eqn)
            circle_eqn = Eq(x**2 + y**2 - 100**2, 0)
            print("Circle Equation:", circle_eqn)
            x1, y1 = solve((line_eqn, circle_eqn), (x,y))[0]
            x2, y2 = solve((line_eqn, circle_eqn), (x,y))[1]
            dist1 = math.sqrt((y1 - new_y)**2 + (x1 - new_x)**2)
            dist2 = math.sqrt((y2 - new_y)**2 + (x2 - new_x)**2)
            if dist1>dist2:
                x, y = x2, y2
            else:
                x, y = x1, y1
            #coords.append((round(x),round(y)))
            dist_rem = step-math.sqrt((new_y)**2 + (new_x)**2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            coords.append((round(new_x),round(new_y)))
        old_x = new_x
        old_y = new_y
    return coords

def task7(steps, p1=True):
    step_prob = [1/3, 1/3, 1/3]
    step_size = [0, 0.5, 1]
    coords = []
    old_x = 0
    old_y = 0
    if not p1:
        step_prob = [0.2, 0.3, 0.5]
    for _ in range(steps):
        angle = np.random.uniform(0, (math.pi*2))
        step = np.random.choice(step_size, p=step_prob)
        new_x = old_x + step* math.cos(angle)
        new_y = old_y + step* math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <=100:
            coords.append((round(new_x),round(new_y)))
        else:
            print("X:", new_x, '\n', "Y:", new_y)
            reflected_angle = 270 +  angle
            m = (new_y-old_y)/(new_x-old_x)
            x, y = symbols('x y')
            line_eqn = Eq(m*(x-new_x)  + new_y - y, 0)
            print("Line Equation:", line_eqn)
            circle_eqn = Eq(x**2 + y**2 - 100**2, 0)
            print("Circle Equation:", circle_eqn)
            x1, y1 = solve((line_eqn, circle_eqn), (x,y))[0]
            x2, y2 = solve((line_eqn, circle_eqn), (x,y))[1]
            dist1 = math.sqrt((y1 - new_y)**2 + (x1 - new_x)**2)
            dist2 = math.sqrt((y2 - new_y)**2 + (x2 - new_x)**2)
            if dist1>dist2:
                x, y = x2, y2
            else:
                x, y = x1, y1
            #coords.append((round(x),round(y)))
            dist_rem = step-math.sqrt((new_y)**2 + (new_x)**2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            coords.append((round(new_x),round(new_y)))
        old_x = new_x
        old_y = new_y
    return coords

def task8():
    old_x1 = random.randint(0,90)
    old_y1 = math.sqrt(100**2 - old_x1**2)

    old_x2 = random.randint(0,100)
    old_y2 = math.sqrt(100**2 - old_x2**2)

    dist = math.sqrt((old_y1-old_y2)**2 + (old_x1-old_x2)**2)
    step = 0
    coord1=[]
    coord2 =[]
    while dist!=1:
        old_x1, old_y1 = helper(old_x1, old_y1, coord1)
        old_x2, old_y2 = helper(old_x2, old_y2, coord2)
        step+=1
    return coord1, coord2

def helper(old_x, old_y, coords):
    angle = np.random.uniform(0,(2*math.pi))
    step = np.random.uniform(0,1)
    new_x = old_x + step* math.cos(angle)
    new_y = old_y + step* math.sin(angle)
    dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
    if dist_from_origin <=100:
        coords.append((round(new_x),round(new_y)))
    else:
        reflected_angle = 270 +  angle
        m = (new_y-old_y)/(new_x-old_x)
        x, y = symbols('x y')
        line_eqn = Eq(m*(x-new_x)  + new_y - y, 0)
        circle_eqn = Eq(x**2 + y**2 - 100**2, 0)
        x1, y1 = solve((line_eqn, circle_eqn), (x,y))[0]
        x2, y2 = solve((line_eqn, circle_eqn), (x,y))[1]
        dist1 = math.sqrt((y1 - new_y)**2 + (x1 - new_x)**2)
        dist2 = math.sqrt((y2 - new_y)**2 + (x2 - new_x)**2)
        if dist1>dist2:
            x, y = x2, y2
        else:
            x, y = x1, y1
        #coords.append((round(x),round(y)))
        dist_rem = step-math.sqrt((new_y)**2 + (new_x)**2)
        new_x = old_x+dist_rem*math.cos(reflected_angle)
        new_y = old_y+dist_rem*math.sin(reflected_angle)
        coords.append((round(new_x),round(new_y)))
    return new_x, new_y

# displaying graphs
def display(func):
    expected = 0
    walks=[]
    for _ in range(1000):
        if func == "task1":
            walks.append(task1(100, 0.5, True, 0))
        elif func == "task2":
            walks.append(task2(0.5, True, False))
        elif func == "task4":
            walks.append(task4(100, 0.5, True))
    expected= sum(walks)/1000
    plt.title('Distances travelled')
    plt.hist(walks, bins=50, color='blue')
    plt.xlabel('Distance from starting point')
    plt.ylabel(' Frequency')
    plt.grid(True)
    plt.show()
    return expected

# Displaying animation for random walk

def setup(func,steps, p1=True, p2=True):
    fig, ax = plt.subplots(figsize=(6,6))
    fig = plt.gcf()
    ax = fig.gca()
    circle = plt.Circle((0,0), 100, color='blue', fill=False)
    ax.add_artist(circle)
    # plt.savefig("blah.png")
    if func == "task3":
        coords = task3(steps, p1, p2)
    elif func == "task5":
        coords = task5(steps)
    elif func == "task7":
        coords = task7(steps, p1)
    # elif func == "task8":
        # coords = task8(steps)
    return coords, fig, ax

# initialization function 
def init(): 
    # creating an empty plot/frame 
    ax.set_xlim((-200,200))
    ax.set_ylim((-200,200))
    ln.set_data([], []) 
    return ln,
        
# animation function 
def animate(i):
    xdata.append(coords[int(i)][0])
    ydata.append(coords[int(i)][1])
    ln.set_data(xdata, ydata)
    return ln, 


# # Task 1
# mean = display("task1")
# print(mean)

# # Task 2
# mean = display("task2")
# print(mean)

# # Task 3 
# coords, fig, ax = setup("task3", 2000, True, True)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
#anim.save('random_walk.gif',writer='imagemagick') 


# # Task 4
# mean = display("task4")
# print(mean)

# # Task 5
# coords, fig, ax = setup("task3", 2000)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
#anim.save('random_walk.gif',writer='imagemagick') 


# # Task 7
# coords, fig, ax = setup("task3", 2000, True)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
#anim.save('random_walk.gif',writer='imagemagick') 


# # Task 8
# coords, fig, ax = setup("task3", 2000)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
#anim.save('random_walk.gif',writer='imagemagick') 
