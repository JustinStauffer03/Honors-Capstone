# Import necessary modules from pygame for game development
import pygame
import sys
import random
from pygame.locals import *

# Initialize pygame modules and the mixer for sound effects and music
pygame.init()
pygame.mixer.init()

# Define basic color constants for easy reference and to improve readability
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

# Set the dimensions of the game window
WIDTH, HEIGHT = 1150, 825
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define fonts for different text elements in the game
FONT_NAME = "arial"
font = pygame.font.SysFont(FONT_NAME, 20)
largefont = pygame.font.SysFont(FONT_NAME, 100)
bangerfont = pygame.font.SysFont("papyrus", 28)
sfont = pygame.font.SysFont("star jedi", 28)
big_font = pygame.font.SysFont(FONT_NAME, 50)

# Defines a list of dictionaries containing the quiz questions, their options, correct answers, and a flag for answered status
questions = [
    # Each dictionary in the list represents a quiz question with its details
    {'Question': 'Which is the correct way to output "hello"? ',
      'options': ['print(hello)', 'print("hello")', 'output(hello)', 'output("hello")'],
      'answer': 'print("hello")', 'answered': False},
    {'Question': 'Which is the correct way to create a for loop that loops through three times? ',
      'options': ['for i in range(3):', 'for i in range(1,3):', 'loop(3):', 'for(i = 0, i <3, i++)'],
      'answer': 'for i in range(3):', 'answered': False},
    {'Question': 'Which of the following is used to comment a single line in Python? ',
      'options': ['// This is a comment', '/* This is a comment */', '# This is a comment', '<!-- This is a comment -->'],
      'answer': '# This is a comment', 'answered': False},
    {'Question': 'What is the purpose of the continue statement in a loop in Python?',
      'options': ['To exit the loop immediately and move to the next line of code after the loop.', 'To skip the current iteration of the loop and continue with the next iteration.', 'To repeat the current iteration of the loop indefinitely.', 'To pause the execution of the loop and wait for user input.'],
      'answer': 'To skip the current iteration of the loop and continue with the next iteration.', 'answered': False},
    {'Question': 'How would you create a variable, abc, that holds the value 123? ',
      'options': ['abc = 123', 'int abc = 123;', 'abc == 123', 'var abc = 123'],
      'answer': 'abc = 123', 'answered': False},
    {'Question': 'Which of the following is important in Python syntax regarding scope? ',
      'options': ['Curly braces { }', 'Semicolons ;', 'Parentheses ()', 'Indentation'],
      'answer': 'Indentation', 'answered': False},
    {'Question': 'How do you import the math module in Python? ',
      'options': ['include math', '#import math', 'import math', 'using math'],
      'answer': 'import math', 'answered': False},
    {'Question': 'What is the purpose of the len() function in Python? ',
      'options': ['Returns the size, in bytes, of object.', 'There is no len() function.', 'To return the size of the program.', 'Returns the length of an object as an int.'],
      'answer': 'Returns the length of an object as an int.', 'answered': False},
    {'Question': 'In Python, what keyword is used to declare a global variable? ',
      'options': ['Public', 'There is no keyword.', 'Local', 'Global'],
      'answer': 'Global', 'answered': False},
    {'Question': 'What is the default return value of a function in Python? ',
      'options': ['Zero', 'False', 'None', 'One'],
      'answer': 'None', 'answered': False},

    # New questions
    {'Question': 'Which of the following is the correct way to define a function in Python? ',
      'options': ['function myFunc() {}', 'def myFunc():', 'function myFunc():', 'define myFunc():'],
      'answer': 'def myFunc():', 'answered': False},

    {'Question': 'What does the *args syntax do in a Python function? ',
      'options': ['Allows the function to accept any number of positional arguments.', 'Allows the function to accept any number of keyword arguments.', 'Specifies the number of arguments the function will accept.', 'Creates a list of arguments the function will accept.'],
      'answer': 'Allows the function to accept any number of positional arguments.', 'answered': False},

    {'Question': 'What is the purpose of the __init__ method in a Python class? ',
      'options': ['To initialize the class attributes.', 'To define the main method of the class.', 'To initialize the instance of the class.', 'To destroy the instance of the class.'],
      'answer': 'To initialize the instance of the class.', 'answered': False},

    {'Question': 'How do you concatenate two strings in Python? ',
      'options': ['string1 + string2', 'concat(string1, string2)', 'string1 & string2', 'merge(string1, string2)'],
      'answer': 'string1 + string2', 'answered': False},

    {'Question': 'How would you handle an exception in Python? ',
      'options': ['try-catch', 'try-except', 'catch-finally', 'except-finally'],
      'answer': 'try-except', 'answered': False},

    {'Question': 'What is a dictionary in Python? ',
      'options': ['A mutable sequence of objects.', 'An immutable sequence of objects.', 'A collection of key-value pairs.', 'A collection of ordered items.'],
      'answer': 'A collection of key-value pairs.', 'answered': False},

    {'Question': 'How do you check the type of an object in Python? ',
      'options': ['type(object)', 'object.type()', 'checktype(object)', 'object.type'],
      'answer': 'type(object)', 'answered': False},

    {'Question': 'Which of the following is used to create a new list in Python? ',
      'options': ['list()', 'create_list()', 'new_list()', '[]'],
      'answer': '[]', 'answered': False},

    {'Question': 'What will be the output of print(2 ** 3) in Python? ',
      'options': ['8', '6', '9', '16'],
      'answer': '8', 'answered': False},

    {'Question': 'Which statement is used to terminate a loop in Python? ',
      'options': ['stop', 'break', 'exit', 'continue'],
      'answer': 'break', 'answered': False},

    {'Question': 'How do you check if a value is in a list in Python? ',
      'options': ['value in list', 'list.contains(value)', 'list.has(value)', 'list.includes(value)'],
      'answer': 'value in list', 'answered': False},

    {'Question': 'What will be the result of [1, 2, 3] * 2 in Python? ',
      'options': ['[1, 2, 3, 1, 2, 3]', '[1, 2, 3, 2, 3, 4]', '[2, 4, 6]', '[1, 2, 3] * 2'],
      'answer': '[1, 2, 3, 1, 2, 3]', 'answered': False},

    {'Question': 'Which keyword is used to define a class in Python? ',
      'options': ['class', 'def', 'new', 'type'],
      'answer': 'class', 'answered': False},

    {'Question': 'How do you remove a key from a dictionary in Python? ',
      'options': ['dict.remove(key)', 'dict.del(key)', 'del dict[key]', 'dict.pop(key)'],
      'answer': 'del dict[key]', 'answered': False},

    {'Question': 'What does the len() function do when applied to a list? ',
      'options': ['Returns the number of items in the list.', 'Returns the size of the list in bytes.', 'Returns the first item of the list.', 'Returns the last item of the list.'],
      'answer': 'Returns the number of items in the list.', 'answered': False},

    {'Question': 'How do you create a tuple in Python? ',
      'options': ['()', '[]', '{}', 'tuple()'],
      'answer': '()', 'answered': False},

    {'Question': 'What will be the output of len("Python")? ',
      'options': ['6', '7', '5', '8'],
      'answer': '6', 'answered': False},

    {'Question': 'How do you define a lambda function in Python? ',
      'options': ['lambda x: x + 1', 'def lambda(x): return x + 1', 'lambda x: {return x + 1}', 'function lambda(x) { return x + 1 }'],
      'answer': 'lambda x: x + 1', 'answered': False},

    {'Question': 'Which function is used to convert a string to an integer in Python? ',
      'options': ['int()', 'str()', 'float()', 'convert()'],
      'answer': 'int()', 'answered': False},

    {'Question': 'How can you read a file line by line in Python? ',
      'options': ['with open(file) as f: for line in f: print(line)', 'file.read_lines()', 'file.readlines()', 'open(file).read_lines()'],
      'answer': 'with open(file) as f: for line in f: print(line)', 'answered': False}
]



# Initialize variables for tracking the current question and score
current_question = 0
score = 0
user_answers = [None] * len(questions)  # Initialize user answers to None

# Function to load an image, optionally resize it, and remove its white background
def load_image_remove_white_background(filename, size=None):
    image = pygame.image.load(filename).convert()  # Load and convert the image
    image.set_colorkey(WHITE)  # Set white as the transparent color
    if size:  # If a size is provided, resize the image
        image = pygame.transform.scale(image, size)
    return image

# Function to create a single confetti particle with random properties
def create_confetti():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)])
    size = random.randint(3, 6)
    fall_speed = random.uniform(0, 1)
    return {"x": x, "y": y, "color": color, "size": size, "fall_speed": fall_speed}

# Function to handle the animation and movement of confetti particles
def handle_confetti(confetti_particles, screen):
    for confetti in confetti_particles:
        confetti["y"] += confetti["fall_speed"]  # Move the confetti down
        pygame.draw.circle(screen, confetti["color"], (confetti["x"], confetti["y"]), confetti["size"])  # Draw the confetti
    return [confetti for confetti in confetti_particles if confetti["y"] <= HEIGHT]  # Remove off-screen confetti

# Function to animate confetti for a specified duration
def animate_confetti(duration, background_color, message):
    confetti_particles = [create_confetti() for _ in range(400)]  # Create a large number of confetti particles
    end_time = pygame.time.get_ticks() + duration
    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow quitting during the animation
                pygame.quit()
                sys.exit()
        screen.fill(background_color)  # Fill the background
        screen.blit(message, (460, 300))  # Display the message
        confetti_particles = handle_confetti(confetti_particles, screen)  # Update and draw confetti
        pygame.display.flip()  # Update the display

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)  # Render the text
    text_rect = text_surface.get_rect(center=(x, y))  # Get the text rectangle
    screen.blit(text_surface, text_rect)  # Draw the text on the screen

# Function to draw the choice options for a question
def draw_choices(question, mouse_pos):
    gap = 10  # Gap between options
    box_height = 50  # Height of each option box
    box_width = WIDTH // 2 + 200  # Width of the option box
    startx = WIDTH // 2 - box_width // 2  # Starting x-coordinate for the options
    total_gap = (len(question["options"]) - 1) * gap  # Total gap space between options
    total_box_height = len(question["options"]) * box_height  # Total height of all option boxes combined
    start_y = HEIGHT // 2 - (total_box_height + total_gap) // 2  # Starting y-coordinate for the options

    for i, choice in enumerate(question['options']):  # Iterate through each option
        rect_y = start_y + i * (box_height + gap)  # Y-coordinate for this option
        rect = pygame.Rect(startx, rect_y, box_width, box_height)  # Option rectangle

        if rect.collidepoint(mouse_pos):  # If mouse is over the option, highlight it
            color = CYAN  # Highlight color
        else:
            color = LIGHT_BLUE if i % 2 == 0 else BLUE  # Alternate colors for options

        pygame.draw.rect(screen, color, rect)  # Draw the option rectangle
        pygame.draw.rect(screen, WHITE, rect, 2)  # Draw a white border for the option
        draw_text(choice, font, BLACK, WIDTH // 2, rect_y + box_height // 2)  # Draw the option text

# Function to draw navigation buttons (Prev and Next)
def draw_navigation_buttons():
    prev_button_rect = pygame.Rect(50, HEIGHT - 100, 100, 50)  # Rectangle for the Prev button
    next_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 100, 100, 50)  # Rectangle for the Next button

    pygame.draw.rect(screen, BLUE, prev_button_rect)  # Draw the Prev button
    pygame.draw.rect(screen, BLUE, next_button_rect)  # Draw the Next button

    draw_text("Prev", font, WHITE, 50 + 50, HEIGHT - 75)  # Text for Prev button
    draw_text("Next", font, WHITE, WIDTH - 150 + 50, HEIGHT - 75)  # Text for Next button

    return prev_button_rect, next_button_rect  # Return the rectangles for button handling

# Function to handle clicks on navigation buttons
def handle_navigation_buttons(prev_button_rect, next_button_rect, mouse_pos):
    global current_question  # To modify the global current_question variable

    if prev_button_rect.collidepoint(mouse_pos) and current_question > 0:  # If Prev is clicked and not on the first question
        current_question -= 1  # Move to the previous question

    if next_button_rect.collidepoint(mouse_pos) and current_question < len(questions) - 1:  # If Next is clicked and not on the last question
        current_question += 1  # Move to the next question

# Function to check if all questions have been answered
def all_questions_answered():
    return all(answer is not None for answer in user_answers)  # Check if any answer is None

# Function to calculate the final score based on correct answers
def calculate_score():
    score = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question['answer']:  # If the user's answer matches the correct answer
            score += 10  # Increment score
    return score

# Main game loop
def game_loop():
    global current_question, score
    confetti_particles = []
    backgroundimage = load_image_remove_white_background('backgroundmain.png', (1150, 825))
    robot_image = load_image_remove_white_background('robot1.png', (250, 250))
    gamestart = load_image_remove_white_background('gamestart.png', (250, 250))
    python = load_image_remove_white_background('python.png', (250, 250))

    while not all_questions_answered():  # Main game loop, runs until all questions are answered
        screen.blit(backgroundimage, (0, 0))  # Display the background image
        screen.blit(robot_image, (900, 50))  # Display the robot image
        screen.blit(gamestart, (10, -15))  # Display the game start image
        screen.blit(python, (500, 550))  # Display the Python logo

        robot = bangerfont.render("Think you got it??", True, BLACK)  # Render a text
        screen.blit(robot, (900, 110))  # Display the rendered text
        question = questions[current_question]  # Get the current question
        draw_text(question['Question'], font, BLACK, WIDTH // 2, HEIGHT // 4)  # Display the question text
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
        draw_choices(question, mouse_pos)  # Draw the choice options for the current question
        pygame.display.flip()  # Update the display

        waiting_for_input = True
        while waiting_for_input:  # Wait for the user to select an option or navigate
            prev_button_rect, next_button_rect = draw_navigation_buttons()  # Draw navigation buttons and get their rectangles
            for event in pygame.event.get():  # Event handling loop
                if event.type == pygame.QUIT:  # If the user closes the window
                    pygame.quit()
                    sys.exit()
                mouse_pos = pygame.mouse.get_pos()  # Update mouse position
                draw_choices(question, mouse_pos)  # Redraw choices to update hover effects
                pygame.display.flip()  # Update the display
                if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks the mouse
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get the click position
                    # Check if the user clicked on navigation buttons and handle accordingly
                    if prev_button_rect.collidepoint(mouse_x, mouse_y) or next_button_rect.collidepoint(mouse_x, mouse_y):
                        handle_navigation_buttons(prev_button_rect, next_button_rect, (mouse_x, mouse_y))
                        waiting_for_input = False
                        break

                    # Skip if the question is already answered
                    if questions[current_question]['answered']:
                        continue
                    
                    # Check which option was clicked
                    for i, choice in enumerate(question["options"]):
                        gap = 10
                        box_height = 50
                        total_gap = (len(question["options"]) - 1) * gap
                        total_box_height = len(question["options"]) * box_height
                        start_y = HEIGHT // 2 - (total_box_height + total_gap) // 2
                        rect_y = start_y + i * (box_height + gap)
                        rect = pygame.Rect(WIDTH // 4, rect_y, WIDTH // 2, box_height)

                        if rect.collidepoint(mouse_x, mouse_y):  # If the user clicked an option
                            pygame.draw.rect(screen, CYAN, rect, 5)  # Highlight the selected option

                            if all_questions_answered():
                                final_score = calculate_score()  # Calculate final score if all questions answered
                                return

                            user_answers[current_question] = choice  # Update the user's answer for the current question
                            questions[current_question]['answered'] = True  # Mark the current question as answered

                            waiting_for_input = False
                            if choice == question["answer"]:  # If the user selected the correct answer
                                textright = big_font.render("Correct!", True, BLACK)  # Render "Correct!" message
                                animate_confetti(3000, GREEN, textright)  # Animate confetti for correct answer

                                screen.fill(GREEN)  # Fill screen with green to indicate correct answer
                                pygame.display.flip()  # Update the display
                            else:
                                textwrong = big_font.render("Incorrect", True, BLACK)  # Render "Incorrect" message
                                correctanswer = font.render(f"The correct answer was: {question['answer']} ", True, BLACK)  # Show the correct answer
                                screen.fill(RED)  # Fill screen with red to indicate incorrect answer
                                screen.blit(textwrong, (460, 300))  # Display "Incorrect" message
                                screen.blit(correctanswer, (250, 370))  # Display the correct answer
                                pygame.display.flip()  # Update the display

                                pygame.time.wait(3000)  # Wait for a few seconds before continuing

                            if current_question < len(questions) - 1:  # If there are more questions
                                current_question += 1  # Move to the next question

                            waiting_for_input = False  # End waiting for input

    # End of the game - calculate and display final score
    final_score = calculate_score()
    backgroundimage = load_image_remove_white_background('backgroundmain.png', (1150, 825))
    scoreimage = pygame.image.load('finalscore.png')  # Load final score image
    scoreimage = pygame.transform.scale(scoreimage, (250, 250))  # Scale the final score image
    gameover = pygame.image.load('gameover.png')  # Load game over image
    gameover = pygame.transform.scale(gameover, (200, 200))  # Scale the game over image
    screen.blit(backgroundimage, (0, 0))  # Display background image
    screen.blit(scoreimage, (430, 300))  # Display final score image
    screen.blit(gameover, (460, 80))  # Display game over image
    pygame.display.flip()  # Update the display
    score_text = largefont.render(f" {final_score}", True, BLACK)  # Render the final score text
    screen.blit(score_text, (485, 450))  # Display the final score
    pygame.display.flip()  # Update the display

    while True:  # Keep the final score displayed until the user closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Load and play background music
pygame.mixer.music.load('Solve The Puzzle.ogg')
pygame.mixer.music.play(-1)  # Loop the music
pygame.mixer.music.set_volume(0.75)

# Start the game loop
game_loop()
