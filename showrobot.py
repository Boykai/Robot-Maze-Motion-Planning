from maze import Maze
import turtle
import sys
from robot import Robot

class ShowRobot(object):
    '''
    Creates a Turtle maze object to display robot exploration during testing
    the robot agent.
    '''
    def __init__(self, test_maze):
        '''
        Takes in test_maze.txt information to create and display maze
        
        test_maze: file path for maze dimensional information (string)
        '''
        # Intialize the maze dimensions from txt file.
        # Maze is centered on (0,0), squares are 20 units in length.
        self.test_maze = test_maze
        self.sq_size = 20
        self.origin = test_maze.dim * self.sq_size / -2

        # Intialize the window and drawing turtle.
        self.window = turtle.Screen()
        self.env = turtle.Turtle()
        self.env.speed(0)
        self.env.hideturtle()
        self.env.penup()
        
