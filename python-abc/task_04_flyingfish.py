#!/usr/bin/python3
"""
Class FlyingFish that inherits both from fish class and bird class
"""


class Fish:
    """
    Fish class with swim and habitat methods
    """
    def swim(self):
        """
        Method that indicates that the fish is swimming
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method that indicates that the fish lives in the water
        """
        print("The fish lives in water")

class Bird:
    """
    Bird class with fly and habitat methods
    """
    def fly(self):
        """
        Method that indicates that the bird is flying
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method that indicates that the bird lives in the sky
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    Class that overides methods from the parents to define unique behaviors for
    swimming, flying, and habitat.
    """
    def fly(self):
        """
        Method that indicates that the flying fish is soaring
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Method that indicates that the flying fish is swimming
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Method that indicates that flying fish lives both in water and sky
        """
        print("The flying fish lives both in water and sky!")
