# Task 1: Your Mood Tracker:

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Times of the day
times_of_day = ["morning", "afternoon", "evening"]

# Outer loop for the days of the week
for day in days_of_week:
    # Inner loop for times of the day
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood.lower()}.")
