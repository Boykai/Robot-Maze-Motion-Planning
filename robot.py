import numpy as np
import random
import time
import math
import pprint
import operator


class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.

        :param maze_dim: the location of the robot (an int, 14 <= maze_dim <= 16 and is even, i.e. 14)
        :return: NULL
        '''
        # Maze dimentional variables
        self.maze_dim = maze_dim
        self.goal_area = [[maze_dim / 2 - 1, maze_dim / 2 - 1],
                          [maze_dim / 2 - 1, maze_dim / 2],
                          [maze_dim / 2, maze_dim / 2 - 1],
                          [maze_dim / 2, maze_dim / 2]]

        # Exploration variables
        self.exploring = True
        self.location = [0, 0]
        self.locations_visited = []
        self.new_location_time_step = 0
        self.max_repeated_locations = maze_dim
        self.random_actions = 0

        # Directional variables
        self.heading = 'north'
        self.turns = ['left', 'forward', 'right']
        self.cardinal_dirctions = ['north', 'east', 'south', 'west']

        # Q-Learning variables
        self.environment = {}
        self.state_space = dict()
        self.learned_state_space = dict()

        # Shared variables
        self.time_step = 0
        self.turn_around = 0

        # Initalize random seed
        random.seed(0)

        
    def check_goal(self, location):
        '''
        Function checks if the robot is within the maze goal area. Returns True
        if the Robot is within goal, else returns False

        :param location: the location of the robot (a list of ints, i.e. [0, 0])
        :return: True, if the location is within the goal. False, if the location is not within the goal. (a bool)
        '''
        assert len(location) == 2
        assert location[0] >= 0
        assert location[1] >= 0
        assert location[0] < self.maze_dim
        assert location[1] < self.maze_dim

        return location in self.goal_area

    
    def explore_path(self, sensors):
    
        rotation = 0
        movement = 1
        sensor_arr = np.array(sensors)
        rotation_arr = [-90, 0, 90]
        longest = np.amax(sensor_arr)
        
        for i in range(len(sensor_arr)):
            if sensors[i] == longest:
                rotation = rotation_arr[i]
                if sensor_arr[i] >= 3:
                    movement = 3
                else:
                    movement = sensor_arr[i]
                    
        return rotation, movement
        
    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        rotation = 0
        movement = 0

        rotation, movement = self.explore_path(sensors)

        return rotation, movement