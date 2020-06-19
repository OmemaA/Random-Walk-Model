import random
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
    orientation_prob = [1/4, 1/4, 1/4, 1/4]
    step_prob = [1/3, 1/3, 1/3]
    orientation = [0, 90, 180, 270]
    step_size = [0, 0.5, 1]
    coords = []
    old_x = 0
    old_y = 0
    if not p1:
        orientation_prob = [0.2, 0.4, 0.1, 0.3]
    if not p2:
        step_prob = [0.2, 0.3, 0.5]
    for _ in range(steps):
        angle = math.radians(np.random.choice(orientation, p=orientation_prob))
        step = np.random.choice(step_size, p=step_prob)
        new_x = old_x + step * math.cos(angle)
        new_y = old_y + step * math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <= 100:
            coords.append((new_x, new_y))
        else:
            reflected_angle = (3/2)*math.pi + angle
            dist1 = math.sqrt((new_x)**2+(new_y)**2)
            dist2 = math.sqrt((old_x)**2+(old_y)**2)
            dist_rem = (dist1-dist2)-(100-dist2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            bound = math.sqrt((new_x)**2+(new_y)**2)
            while bound >= 100:
                reflected_angle = math.pi-reflected_angle
                dist1 = math.sqrt((new_x)**2+(new_y)**2)
                dist2 = math.sqrt((old_x)**2+(old_y)**2)
                dist_rem = (dist1-dist2)-(100-dist2)
                new_x = old_x+dist_rem*math.cos(reflected_angle)
                new_y = old_y+dist_rem*math.sin(reflected_angle)
                bound = math.sqrt((new_x)**2+(new_y)**2)
            coords.append((new_x, new_y))
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
        angle = math.radians(np.random.uniform(0, (360)))
        step = np.random.uniform(0,1)
        print(angle, step)
        new_x = old_x + step * math.cos(angle)
        new_y = old_y + step * math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <= 100:
            coords.append((new_x, new_y))
        else:
            reflected_angle = (3/2)*math.pi + angle
            dist1 = math.sqrt((new_x)**2+(new_y)**2)
            dist2 = math.sqrt((old_x)**2+(old_y)**2)
            dist_rem = (dist1-dist2)-(100-dist2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            bound = math.sqrt((new_x)**2+(new_y)**2)
            while bound >= 100:
                reflected_angle = math.pi-reflected_angle
                dist1 = math.sqrt((new_x)**2+(new_y)**2)
                dist2 = math.sqrt((old_x)**2+(old_y)**2)
                dist_rem = (dist1-dist2)-(100-dist2)
                new_x = old_x+dist_rem*math.cos(reflected_angle)
                new_y = old_y+dist_rem*math.sin(reflected_angle)
                bound = math.sqrt((new_x)**2+(new_y)**2)
            coords.append((new_x, new_y))
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
        angle = math.radians(np.random.uniform(0, (360)))
        step = np.random.choice(step_size, p=step_prob)
        new_x = old_x + step * math.cos(angle)
        new_y = old_y + step * math.sin(angle)
        dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
        if dist_from_origin <= 100:
            coords.append((new_x, new_y))
        else:
            reflected_angle = (3/2)*math.pi + angle
            dist1 = math.sqrt((new_x)**2+(new_y)**2)
            dist2 = math.sqrt((old_x)**2+(old_y)**2)
            dist_rem = (dist1-dist2)-(100-dist2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            bound = math.sqrt((new_x)**2+(new_y)**2)
            while bound >= 100:
                reflected_angle = math.pi-reflected_angle
                dist1 = math.sqrt((new_x)**2+(new_y)**2)
                dist2 = math.sqrt((old_x)**2+(old_y)**2)
                dist_rem = (dist1-dist2)-(100-dist2)
                new_x = old_x+dist_rem*math.cos(reflected_angle)
                new_y = old_y+dist_rem*math.sin(reflected_angle)
                bound = math.sqrt((new_x)**2+(new_y)**2)
            coords.append((new_x, new_y))
        old_x = new_x
        old_y = new_y
    return coords

def task8():
    angle1, angle2 = np.random.uniform(high=360.0, size=2)
    r1, r2 = np.random.uniform(high=100.0, size=2)

    old_x1 = r1* math.cos(math.radians(angle1))
    old_y1 = r1* math.sin(math.radians(angle1))
    old_x2 = r2* math.cos(math.radians(angle2))
    old_y2 = r2* math.sin(math.radians(angle2))

    dist = math.sqrt((old_y1-old_y2)**2 + (old_x1-old_x2)**2)
    step = 0
    coord1=[]
    coord2 =[]
    while dist >=1:
        dist = math.sqrt((old_y1-old_y2)**2 + (old_x1-old_x2)**2)
        old_x1, old_y1 = helper(old_x1, old_y1, coord1)
        old_x2, old_y2 = helper(old_x2, old_y2, coord2)
        step+=1
    return coord1, coord2, step

def helper(old_x, old_y, coords):
    angle = math.radians(np.random.uniform(0, (360)))
    step = np.random.uniform(0,1)
    new_x = old_x + step * math.cos(angle)
    new_y = old_y + step * math.sin(angle)
    dist_from_origin = math.sqrt((new_y)**2 + (new_x)**2)
    if dist_from_origin <= 100:
        coords.append((new_x, new_y))
    else:
        reflected_angle = (3/2)*math.pi + angle
        dist1 = math.sqrt((new_x)**2+(new_y)**2)
        dist2 = math.sqrt((old_x)**2+(old_y)**2)
        dist_rem = (dist1-dist2)-(100-dist2)
        new_x = old_x+dist_rem*math.cos(reflected_angle)
        new_y = old_y+dist_rem*math.sin(reflected_angle)
        bound = math.sqrt((new_x)**2+(new_y)**2)
        while bound >= 100:
            reflected_angle = math.pi-reflected_angle
            dist1 = math.sqrt((new_x)**2+(new_y)**2)
            dist2 = math.sqrt((old_x)**2+(old_y)**2)
            dist_rem = (dist1-dist2)-(100-dist2)
            new_x = old_x+dist_rem*math.cos(reflected_angle)
            new_y = old_y+dist_rem*math.sin(reflected_angle)
            bound = math.sqrt((new_x)**2+(new_y)**2)
        coords.append((new_x, new_y))
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
    plt.savefig(func + ".png")
    plt.show()
    return expected

# Displaying animation for random walk

def setup(func,steps, p1=True, p2=True):
    fig, ax = plt.subplots(figsize=(6,6))
    fig = plt.gcf()
    ax = fig.gca()
    circle = plt.Circle((0,0), 100, color='blue', fill=False)
    ax.add_artist(circle)
    if func == "task8":
        coord1, coord2, steps = task8()
        return coord1, coord2, steps, fig, ax
    elif func == "task3":
        coords = task3(steps, p1, p2)
    elif func == "task5":
        coords = task5(steps)
    elif func == "task7":
        coords = task7(steps, p1)
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

# Task 3 
# coords, fig, ax = setup("task3", 10000, True, True)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
# ani.save('task3.gif',writer='imagemagick')


# # Task 4
# mean = display("task4")
# print(mean)

# # Task 5
# coords, fig, ax = setup("task5", 2000)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
# anim.save('random_walk.gif',writer='imagemagick') 

# # Task 7
# coords, fig, ax = setup("task7", 10000, True)
# xdata, ydata = [], []
# ln, = plt.plot(xdata, ydata, color='red')
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coords)-1, num=len(coords)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# plt.show()
#anim.save('random_walk.gif',writer='imagemagick') 


# # Task 8
# fig, ax = plt.subplots(figsize=(6,6))
# fig = plt.gcf()
# ax = fig.gca()
# circle = plt.Circle((0,0), 100, color='blue', fill=False)
# ax.add_artist(circle)
# lst = []
# for i in range(10000):
#     coord1, coord2, steps = task8()
#     task.append(steps)

# avg = sum(steps)/10000

# coord1, coord2, steps = task8()

# x1data, y1data = [], []
# x2data, y2data = [], []
# ln, = plt.plot(x1data, y1data, color='purple')
# ln2, = plt.plot(x2data, y2data, color='red')

# # initialization function 
# def init(): 
#     # creating an empty plot/frame 
#     ax.set_xlim((-200,200))
#     ax.set_ylim((-200,200))
#     # ax.set_title("Task 5")/
#     ln.set_data([], []) 
#     ln2.set_data([], [])
#     return ln,ln2,

# # animation function 
# def animate(i):
#     x1data.append(coord1[int(i)][0])
#     y1data.append(coord1[int(i)][1])
#     ln.set_data(x1data, y1data)
#     x2data.append(coord2[int(i)][0])
#     y2data.append(coord2[int(i)][1])
#     ln2.set_data(x2data, y2data)
#     return ln,ln2,


# # call the animator
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coord1)-1, num=len(coord1)), interval=20,
#                         init_func=init, blit=True, repeat=False) 
# ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(coord2)-1, num=len(coord2)), interval=20,
#                         init_func=init, blit=True, repeat=False)
# plt.show()
# # ani.save('task8.gif', writer='imagemagick', fps=60)
