import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import colors


class environmentGrid():

    # Grid dimensions
    x_dimension = 5
    y_dimension = 5

    # Set an empty array for the grid
    env_grid = np.zeros((x_dimension, y_dimension))

    env_elements = {
        'rien': 0,
        'poussiere': 1,
        'diamant': 2,
        'pd': 3    # poussiere et diamant
        #'robot': 4
    }

    def __init__(self):
        pass

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
                static_chances_percentage =  [0] * 70 + [1] * 10 + [2] * 10 + [3] * 10
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

        # create discrete colormap
        cmap = colors.ListedColormap(['white', 'grey', 'blue', 'red'])
        bounds = [0, 1, 2, 3, 4]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()

        # Extent from 0 to 5 in x and 0 to 5 in y
        ax.imshow(a, cmap=cmap, norm=norm,
                  extent=[0, self.x_dimension, 0, self.y_dimension])

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k',
                linewidth=1)
        plt.xticks(np.arange(0, self.x_dimension + 1, 1))
        plt.yticks(np.arange(0, self.y_dimension + 1, 1))
        plt.show()



#Créer une fonction pour ajouter des diamants et de la possière sur la grille
#TODO get_élément() -> [[x,y,2],[x,y,2]]
#TODO retirerElementPosition(self.x, self.y, numéro_élément)
##########  TEST    ###########################################################

environment = environmentGrid()

a = environment.get_grid()
print(a)

a = environment.get_grid()
print(a)

environment.set_random_grid()
#print(a)

a = environment.get_grid()
print(a)

a = environment.get_grid()
print(a)

environment.set_random_grid()
#print(a)

a = environment.get_grid()
print(a)

print("-"*80)

environment.display_grid()