# 🐢 Project: Turtle Marathon

## 1. Project Objective

To create six turtles of different colours that race horizontally across a screen measuring 500 pixels in width and 400 pixels in height.

The player places a bet on which coloured turtle will win. Each turtle moves at a randomly generated pace, making the outcome unpredictable. The first turtle to cross the finishing boundary is declared the winner.

## 2. Modules Required

- **Turtle module:** Imports `Turtle` and `Screen` to create and control graphical objects.
- **Random module:** Generates random movement distances to determine each turtle's racing pace.

## 3. Process and Implementation

### Step 1: Screen Setup and User Input

I created a `Screen` object to access screen methods such as `setup()` and `textinput()`.

- `screen.setup(width=500, height=400)` establishes the dimensions of the racing screen.
- `screen.textinput("Title", "Prompt")` displays a title and prompt, allowing the player to place a bet on which turtle colour will win.

### Step 2: Creating Contestant Colours and Starting Coordinates

I created two lists:

- `contestant_tag`: Contains six different turtle colours.
- `turtle_location`: Contains six sets of starting coordinates.

Each colour represents an individual contestant, while each coordinate determines its starting position on the screen.

### Step 3: Pairing the Two Lists Using `zip()`

I introduced the `zip()` function to combine corresponding elements from both lists into tuples.

I converted the resulting pairs into a list called `paired` and created an auxiliary empty list called `all_racers` to store the Turtle objects.

The resulting pairs are:

| Index | Contestant colour | Starting coordinate |
|---:|---|---|
| 0 | red | (-230, -100) |
| 1 | orange | (-230, -50) |
| 2 | yellow | (-230, -20) |
| 3 | green | (-230, 30) |
| 4 | blue | (-230, 90) |
| 5 | purple | (-230, 150) |

For example, the first tuple is:

`("red", (-230, -100))`

This means the red contestant will start at coordinate (-230, -100).

### Step 4: Creating and Storing Turtle Objects

I used a `for` loop to iterate through each colour and its corresponding starting coordinate within `paired`.

Inside the loop, I created a new Turtle object using:

`Racer = Turtle(shape="turtle")`

I then appended each newly created object into `all_racers`.

The purpose of using `all_racers` is to store all six Turtle objects in one list. This avoids having to create six separate variables, such as `racer1`, `racer2` and so on.

It also allows me to iterate through all six existing Turtle objects later when controlling their movements.

### Step 5: Assigning Colours and Starting Positions

Within the same loop, I used:

- `Racer.penup()` to prevent the turtle from drawing a line when moving to its starting position.
- `Racer.color(contestant_tag)` to assign the corresponding colour to the turtle.
- `Racer.goto(turtle_location[0], turtle_location[1])` to position the turtle using its X and Y coordinates.

Because the loop processes each tuple individually, every Turtle object receives its corresponding colour and starting position.

### Step 6: Calculating the Racing Boundaries

The screen width is 500 pixels, giving horizontal boundaries of -250 and +250.

I selected -230 as the starting coordinate and +230 as the finishing threshold to maintain a margin from the screen edges.

My approximate calculation was:
The 20 + 20 represents the approximate 20-pixel width of the turtle's square bounding area, divided by two to account for its half-width when positioning its centre.
`500 / 2 - (20 + 20) / 2 = 230`

These are chosen racing boundaries rather than the actual screen edges.

### Step 7: Drawing the Finishing Line

To draw a vertical finishing line, I created another Turtle object.

I used `penup()` before positioning the turtle to prevent unwanted lines from appearing.

Next, I used:

- `goto(200, -180)` to position the drawing turtle at the lower part of the screen.
- `setheading(90)` to orient the turtle northwards.
- `pendown()` to begin drawing.
- `forward(360)` to draw a straight vertical line.

### Step 8: Controlling the Race

Initially, I set `no_winner = True` to indicate that the race had not yet produced a winner.

I then used a `while` loop to keep the race running and a `for` loop to iterate through the Turtle objects stored in `all_racers`.

This allows me to control all six existing turtles without creating new objects.

### Step 9: Generating Random Movement

I used:

`random.randint(1, 10)`

to generate a random movement distance between 1 and 10 for each turtle.

Each turtle receives a random movement distance during each iteration, making the race unpredictable.

### Step 10: Identifying the Winner

I established a conditional statement using:

`if racer.xcor() > 230:`

The `xcor()` method retrieves the turtle's current horizontal position.

When a turtle exceeds the finishing threshold:

- `racer.pencolor()` retrieves its current pen colour.
- The winning colour is assigned to `winner_color`.
- `no_winner` is changed to `False` to terminate the race.

The programme then announces the winning turtle.

## 4. Key Learning Outcomes

Through this assignment, I practised:

1. **Cartesian coordinates:** Understanding how X and Y coordinates determine graphical positioning.
2. **Lists and tuples:** Organising contestant colours and starting positions.
3. **The `zip()` function:** Pairing corresponding elements from two lists.
4. **Object-oriented programming:** Creating, configuring and storing multiple Turtle objects.
5. **Loops:** Using nested iteration to initialise and control multiple objects.
6. **Randomisation:** Generating unpredictable movement distances.
7. **Conditional logic:** Detecting when a turtle reaches the finishing boundary.

The most significant takeaway was understanding how screen dimensions translate into coordinate positions and how multiple Turtle objects can be managed efficiently through a list.

## 5. Acknowledgement
This assignment was completed as part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp. The assignment provided the foundation for practising Python Turtle graphics and applying fundamental programming concepts.

This assignment was completed as part of Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp. The assignment provided the foundation for practising Python Turtle graphics and applying fundamental programming concepts.
