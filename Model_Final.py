import io
import random
import operator
import matplotlib.animation
import matplotlib.pyplot
import agentframework
import csv
import requests
import bs4


#Web scraping
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print (td_ys, td_xs)

def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a.x-agents_row_b.x)**2) + ((agents_row_a.y-agents_row_b.y)**2))**0.5

# Reading CSV data
f = open('in.txt', newline='')
reader = csv.reader(f, quoting= csv.QUOTE_NONNUMERIC)

# Make envrionment list
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

# Check data is read correctly    
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

num_of_agents=10
num_of_iterations= 100
neighbourhood = 20

# Set the axis
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents
agents=[]
for i in range (num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
carry_on = True

def update (frame_number):
    fig.clear()
    global carry_on

# Move the agents
for j in range (num_of_iterations):
    for i in range (num_of_agents):
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
    if random.random() >= 10:
        carry_on = False
        print("Stopping conditions")

# Show data - addition of envrionment data
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    print(agents[i].x, agents[i].y)

def gen_function(b=[0]):
    a = 0 
    global carry_on
    while (a < 10) & (carry_on):
        yield a
        a = a+1

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()       

for agents_row_a in agents: 
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

# extra from I/O
f = open("environment.txt", "w")
for line in environment:
    f.write(str(line))
f.close()

"""
a = agentframework.Agent(environment, agents)
print(a.y, a.x)
a.move()
print(a.y, a.x)
b = agentframework.Agent(environment, agents)
print(b.y, b.x)
b.move()
print(b.y, b.x)
""" 

