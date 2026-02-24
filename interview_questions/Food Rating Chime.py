"""
Given a list of Food Names, allow the user to input ratings from the terminal, then return the list with the highest rating, lowest rating, and average rating.
"""

"""
This problem is a classic **Data Processing** task. You are essentially taking a static list of items, enriching that list with user-provided data, and then performing basic statistical analysis on the results.

Here is a breakdown of how the logic functions:

### 1. The Input Phase

The program starts with a predefined list (e.g., `["Pizza", "Sushi", "Tacos"]`). It then enters a loop to interact with the user via the terminal.

* **Prompt:** For every item in the list, the program asks: *"What is the rating for [Food Name]?"*
* **Storage:** You'll need a way to pair the food name with its new rating. A **Dictionary** (in Python) or an **Object/Map** (in JavaScript) is perfect for this.

---

### 2. The Calculation Phase

Once you have all the ratings, you need to "crunch" the numbers. This involves three specific metrics:

* **Highest Rating:** Finding the maximum value in your collection.
* **Lowest Rating:** Finding the minimum value in your collection.
* **Average Rating:** Summing all ratings and dividing by the total number of items.

The formula for the average is:


$$\text{Average} = \frac{\sum_{i=1}^{n} \text{rating}_i}{n}$$

---

### 3. The Output Phase

Finally, the program displays the results. A well-designed solution would look something like this in the terminal:

| Food Name | Rating |
| --- | --- |
| Pizza | 9 |
| Sushi | 10 |
| Tacos | 8 |

**Results:**

* **Highest:** 10 (Sushi)
* **Lowest:** 8 (Tacos)
* **Average:** 9.0

---

### Key Considerations for Implementation

If you are going to code this, keep these "real-world" hurdles in mind:

* **Data Validation:** What happens if the user types "Great" instead of "5"? You'll need to ensure the input is a number.
* **Empty Lists:** If the list of Food Names is empty, your code might crash when trying to calculate an average (division by zero).
* **Tie-Breakers:** What if two foods have the same highest rating? Your code should decide whether to return one or both.

**Would you like me to provide a code implementation for this in a specific language like Python, JavaScript, or C++?**
"""


def food_rating_system():
    # 1. Initialize the list of foods
    foods = ["Pizza", "Sushi", "Tacos", "Burgers", "Salad"]
    ratings = {}

    print("--- Food Rating Terminal ---")
    print("Please enter a rating from 1 to 10 for each item.\n")

    # 2. Input Phase with Validation
    for food in foods:
        while True:
            try:
                score = float(input(f"How would you rate {food}? "))
                if 1 <= score <= 10:
                    ratings[food] = score
                    break
                else:
                    print("Please enter a number between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    # 3. Calculation Phase
    scores = list(ratings.values())
    
    # Calculate metrics
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    # Find which foods have the high/low scores (handles ties)
    best_foods = [name for name, score in ratings.items() if score == highest_score]
    worst_foods = [name for name, score in ratings.items() if score == lowest_score]

    # 4. Output Phase
    print("\n" + "="*30)
    print("FINAL RESULTS")
    print("="*30)
    
    print(f"Average Rating: {average_score:.2f}")
    print(f"Highest Rating: {highest_score} ({', '.join(best_foods)})")
    print(f"Lowest Rating:  {lowest_score} ({', '.join(worst_foods)})")
    print("="*30)

if __name__ == "__main__":
    food_rating_system()