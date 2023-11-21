import math
import numpy as np

def Translate(pos):
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]])

def RotateX(angle):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(angle), math.sin(angle), 0],
        [0, -math.sin(angle), math.cos(angle), 0],
        [0, 0, 0, 1]])

def RotateY(angle):
    return np.array([
        [math.cos(angle), 0, -math.sin(angle), 0],
        [0, 1, 0, 0],
        [math.sin(angle), 0, math.cos(angle), 0],
        [0, 0, 0, 1]])

def RotateZ(angle):
    return np.array([
        [math.cos(angle), math.sin(angle), 0, 0],
        [-math.sin(angle), math.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

def Scale(scaleFactor):
    return np.array([
        [scaleFactor, 0, 0, 0],
        [0, scaleFactor, 0, 0],
        [0, 0, scaleFactor, 0],
        [0, 0, 0, 1]])


