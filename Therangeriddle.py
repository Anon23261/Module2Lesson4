# Task 1: Your Mood Today:

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week using the range function
for i in range(len(days_of_week)):
    mood = random.choice(moods)
    print(f"On {days_of_week[i]}, you were feeling {mood.lower()}.")
