import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import colors
import time

class EnvironmentGrid():

    # Grid dimensions
    x_dimension = 5
    y_dimension = 5

    # Set an empty array for the grid
    env_grid = np.zeros((x_dimension, y_dimension))

    env_elements = {
        'rien': 0,
        'poussiere': 1,
        'diamant': 2,
        'pd': 3,    # poussiere et diamant
        'robot': 4
    }

    # Create discrete colormap
    # white: rien, grey: poussiere, blue: diamant, red: pd, black: robot.
    cmap = colors.ListedColormap(['white', 'grey', 'blue', 'red', colors.to_rgba('g', 0.5)])
    bounds = [0, 1, 2, 3, 4, 5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots()

    def __init__(self):
        self.set_random_grid()
        
    
    #TODO initialise Timer a faire + fonction
    def set_random_grid(self):
        max_elements_per_line = 2
        env_grid = self.env_grid
        total_elements_per_line = 0
        for x in range(0, self.x_dimension):
            for y in range(0, self.y_dimension):
                # Get a random element between: rien, poussiere, diamant, pd.
                # 'static_chances_percentage' sets the percentage of chances
                # that each value is randomly selected. You may hard code these
                # percentages.
                static_chances_percentage = \
                    [0] * 70 + [1] * 10 + [2] * 10 + [3] * 10
                random_element = random.choice(static_chances_percentage)
                if total_elements_per_line >= max_elements_per_line:
                    random_element = 0
                elif random_element > 0:
                    total_elements_per_line += 1
                # Assign the element type to the line grid
                env_grid[x, y] = random_element
            # Reinitialize the counter for the next line x
            total_elements_per_line = 0
        self.env_grid = np.copy(env_grid)

    def get_grid(self):
        return self.env_grid

    def display_grid(self):
        data = self.env_grid

        # Extent from 0 to 5 in x and 0 to 5 in y
        self.ax.imshow(data, cmap=self.cmap, norm=self.norm,
                       extent=[0, self.x_dimension, 0, self.y_dimension])

        # draw gridlines
        self.ax.grid(which='major', axis='both', linestyle='-', color='k',
                     linewidth=1)
        plt.xticks(np.arange(0, self.x_dimension + 1, 1))
        plt.yticks(np.arange(0, self.y_dimension + 1, 1))

        # Note the call to plt.pause(x), which both draws the new data and runs
        # the GUI's event loop (allowing for mouse interaction).
        #plt.pause(2)
        time.sleep(2)
    # THIS FUNCTION IS SIMILAR TO THE PREVIOUS ONE, BUT CALL IT ONLY AT THE
    # END, BECAUSE OF THE PLOT SHOW AT THE END. OTHERWISE, IF YOU ONLY USE THE
    # PREVIOUS ONE, THE GRID WILL DISAPPEAR AFTER X SECONDS. IF YOU USE ONLY
    # THIS F UCTION, THE NEXT ITERATION THAT MODIFIES THE GRID WILL NOT SHOW.
    def display_grid_last(self):
        data = self.env_grid

        # Extent from 0 to 5 in x and 0 to 5 in y
        self.ax.imshow(data, cmap=self.cmap, norm=self.norm,
                       extent=[0, self.x_dimension, 0, self.y_dimension])

        # draw gridlines
        self.ax.grid(which='major', axis='both', linestyle='-', color='k',
                     linewidth=1)
        plt.xticks(np.arange(0, self.x_dimension + 1, 1))
        plt.yticks(np.arange(0, self.y_dimension + 1, 1))
        plt.show()

    # Add diamond at a random place if there is nothing at this location. If
    # there is a diamond already, add it in another place. If there is a dust
    # already, add the diamond with it.
    # robot_x: x cood of the robot. (int)
    # robot_y: y coord of the robot. (int)
    # element: element type number: rien, poussiere, diamant, pd. (int)
    def add_element(self, robot_x, robot_y, element):
        data = np.copy(self.env_grid)
        random_diamond_x = robot_x
        random_diamond_y = robot_y
        no_same_elem = True

        # Keep track of the element type, in case that the new one became a
        # 'pd' from a 'poussiere' plus a 'diamant'.
        new_elem_type = element

        while no_same_elem:
            random_diamond_x = random.randint(0, self.x_dimension - 1)
            random_diamond_y = random.randint(0, self.y_dimension - 1)
            data_at_new = data[random_diamond_x, random_diamond_y]

            # If the robot is at this position, do not add anything on it, just
            # redo the random.
            if data_at_new == self.env_elements['robot']:
                no_same_elem = False

            # If there is already a 'pd' (poussiere et diamand), nothing more
            # can be added, just redo the random.
            elif data_at_new == self.env_elements['pd']:
                no_same_elem = False

            # If we want to add a dust poussiere...
            elif element == self.env_elements['poussiere']:
                # a dust poussiere can be added here.
                if data_at_new == self.env_elements['rien']:
                    no_same_elem = False
                    break
                # but there is already a poussiere here, redo the random.
                elif data_at_new == self.env_elements['poussiere']:
                    no_same_elem = True

                # and there is a diamond here, the dust poussiere can be added
                # here, but the element type becomes a 'pd' instead.
                elif data_at_new == self.env_elements['diamant']:
                    no_same_elem = False
                    new_elem_type = self.env_elements['pd']
                    break

            # If we want to add a diamond...
            elif element == self.env_elements['diamant']:
                # a poussiere can be added here.
                if data_at_new == self.env_elements['rien']:
                    no_same_elem = False
                    break

                # but there is already a diamond here, redo the random.
                elif data_at_new == self.env_elements['diamant']:
                    no_same_elem = True

                # and there is a dust poussiere here, the dust poussiere can be
                # added here, but the element type becomes a 'pd' instead.
                elif data_at_new == self.env_elements['poussiere']:
                    no_same_elem = False
                    new_elem_type = self.env_elements['pd']
                    break

        # Add the element in the environment.
        self.env_grid[random_diamond_x, random_diamond_y] = new_elem_type

    # Remove the element at the given position.
    # x: x cood of the element to remove. (int)
    # y: y coord of the element to remove. (int)
    def remove_element(self, x, y, elem=0):
        # Check if the grid contains an element at the given position.
        self.env_grid[x, y] -= elem

    # Add the robot in the grid.
    # robot_x: x cood of the robot. (int)
    # robot_y: y coord of the robot. (int)
    def add_robot(self, robot_x, robot_y):
        element = self.env_grid[robot_x, robot_y]
        self.env_grid[robot_x, robot_y] = element + self.env_elements['robot']

    # Paul
    def getListPD(self):
        lPD = []
        for i in range(0, self.x_dimension):
            for j in range(0, self.y_dimension):
                if (self.env_grid[i, j] in [1, 2, 3, 5, 6, 7]):
                    lPD.append([i, j, self.env_grid[i, j]])
        return lPD

    def getElementPos(self, x, y):
        return self.env_grid[x,y]


    def lancerEnvironmnent(self,agent, timer):
        t1 = time.time()
        while(time.time()-t1 < timer):
            time.sleep(random.random()*4 + 1)
            self.add_element(agent.x,agent.y,random.randint(1,2))

##########  TEST    ###########
"""
environment = EnvironmentGrid()


#environment.set_random_grid()
a = environment.get_grid()
print(a)
print("-"*80)

environment.display_grid()
environment.add_element(2, 3, environment.env_elements['poussiere'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['diamant'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['poussiere'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['diamant'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['poussiere'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['diamant'])
print("&"*80)
print(a)
environment.display_grid()
environment.add_element(2, 3, environment.env_elements['poussiere'])
print("&"*80)
print(a)
print("%"*80)

environment.remove_element(0, 0, 1)
environment.display_grid()
environment.remove_element(0, 1)
environment.display_grid()
environment.remove_element(0, 2)
environment.display_grid()
environment.remove_element(1, 0)
environment.display_grid()
environment.remove_element(2, 0)

environment.add_robot(0, 0)
print(a)

environment.display_grid_last()
print("##############finiiiiiiiiiiiiiiiiiiiiii")
"""
