from typing import List

"""
Problem Name: Calculate the angle between hour hand and minute hand

Problem URL: https://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/

Problem Section: 

Problem Difficulty: Easy / Medium

Problem Statement:
This problem is known as Clock angle problem where we need to find angle between hands of an analog clock at a given time.
Examples: 

Input:  
h = 12:00
m = 30.00
Output: 
165 degree

Input:  
h = 3.00
m = 30.00
Output: 
75 degree

Resources:

Explation:
The idea is to take 12:00 (h = 12, m = 0) as a reference. Following are detailed steps.

1. Calculate the angle made by hour hand with respect to 12:00 in h hours and m minutes. 
2. Calculate the angle made by minute hand with respect to 12:00 in h hours and m minutes. 
3. The difference between the two angles is the angle between the two hands.

How to calculate the two angles with respect to 12:00? 
The minute hand moves 360 degrees in 60 minute(or 6 degrees in one minute) and hour hand moves 360 degrees in 12 hours(or 0.5 degrees in 1 minute). 
In h hours and m minutes, the minute hand would move (h*60 + m)*6 and hour hand would move (h*60 + m)*0.5. 

"""

# Python program to find angle
# between hour and minute hands

# Function to Calculate angle b/w
# hour hand and minute hand

# Time Complexity: O(1)


def calcAngle(h, m):

    # validate the input
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
        h += 1
        if(h > 12):
            h = h-12

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = min(360 - angle, angle)

    return angle


# Driver Code
h = 9
m = 60
print('Angle ', calcAngle(h, m))
