'''
  File: helpers.py
  Project: Palace

  Author: Talin Sharma @TalinTheDev
  Date: 6/15/2022
  License: Apache 2.0

  Summary:
    This file holds the helper functions required for the recreation of the Palace game.
'''


from os import system, name # For clearning the screen

# Function to clear the screen using os.system

def clear():
  system('cls' if name == 'nt' else 'clear')

def forEach(list, function):
    for i, v in enumerate(list):
        function(v)