import pygame
import sys
import random
from pygame.locals import *
pygame.init()
pygame.mixer.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
LIGHT_BLUE = (173,216,230)
RED = (255,0,0)
WIDTH, HEIGHT = 1150,825
screen = pygame.display.set_mode((WIDTH,HEIGHT))
FONT_NAME = "arial"
questions = [
    {'Question': 'Which is the correct way to output "hello"? ',
      'options': ['print(hello)', 'print("hello")','output(hello)', 'output("hello")' ],
      'answer': 'print("hello")','answered':False  },
    {'Question': 'Which is the correct way to create a for loop that loops through three times? ',
        'options': ['for i in range(3):', 'for i in range(1,3):','loop(3):', 'for(i = 0, i <3, i++)' ],
        'answer': 'for i in range(3):','answered':False  },
    {'Question': 'Which of the following is used to comment a single line in Python? ', 
     'options': ['// This is a comment', '/* This is a comment */','# This is a comment', '<!-- This is a comment -->' ], 
     'answer': '# This is a comment','answered':False  },
     {'Question': 'What is the purpose of the continue statement in a loop in Python?', 
      'options': ['To exit the loop immediately and move to the next line of code after the loop.', 'To skip the current iteration of the loop and continue with the next iteration.','To repeat the current iteration of the loop indefinitely.', 'To pause the execution of the loop and wait for user input.' ], 
      'answer': 'To skip the current iteration of the loop and continue with the next iteration.', 'answered':False },
      {'Question': 'How would you create a variable, abc, that holds the value 123? ', 
      'options': ['abc = 123', 'int abc = 123;','abc == 123', 'var abc = 123' ], 
      'answer': 'abc = 123', 'answered':False },
      {'Question': 'Which of the following is important in Python syntax regarding scope? ', 
      'options': ['Curly braces { }', 'Semicolons ;','Parentheses ()', 'Indentation' ], 
      'answer': 'Indentation', 'answered':False },
      {'Question': 'How do you import the math module in Python? ', 
      'options': ['include math', '#import math','import math', 'using math' ], 
      'answer': 'import math', 'answered':False },
       {'Question': 'What is the purpose of the len() function  in Python? ', 
      'options': ['Returns the size, in bytes, of object.', 'There is no len() function.','To return the size of the program. ', 'Returns the length of an object as an int.' ], 
      'answer': 'Returns the length of an object as an int.', 'answered':False },
      {'Question': 'In Python, what keyword is used to declare a global variable? ', 
      'options': ['Public', 'There is no keyword.','Local', 'Global' ], 
      'answer': 'Global', 'answered':False },
      {'Question': 'What is the default return value of a function in Python? ', 
      'options': ['Zero', 'False','None', 'One' ], 
      'answer': 'None', 'answered':False }]
current_question = 0
score = 0
user_answers = [None] * len(questions) 
pygame.display.set_caption("Pymification")
font = pygame.font.SysFont(FONT_NAME, 20)
largefont =pygame.font.SysFont(FONT_NAME, 100)
bangerfont = pygame.font.SysFont("papyrus", 28)
sfont = pygame.font.SysFont("star jedi", 28)
big_font = pygame.font.SysFont(FONT_NAME, 50)
def load_image_remove_white_background(filename, size=None):
    # Load the image
    image = pygame.image.load(filename).convert()
    # Set the colorkey to white, which makes it transparent
    image.set_colorkey(WHITE)
    # If a size (width, height) tuple is provided, scale the image
    if size is not None:
        image = pygame.transform.scale(image, size)
    return image
def create_confetti():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)])
    size = random.randint(3, 6)
    fall_speed = random.uniform(0, 1)
    return {"x": x, "y": y, "color": color, "size": size, "fall_speed": fall_speed}

def handle_confetti(confetti_particles, screen):
    for confetti in confetti_particles:
        # Move
        confetti["y"] += confetti["fall_speed"]

        # Draw
        pygame.draw.circle(screen, confetti["color"], (confetti["x"], confetti["y"]), confetti["size"])

    # Remove off-screen confetti and return updated list
    return [confetti for confetti in confetti_particles if confetti["y"] <= HEIGHT]

def animate_confetti(duration, background_color, message):
    confetti_particles = [create_confetti() for _ in range(400)]
    end_time = pygame.time.get_ticks() + duration

    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(background_color)
        screen.blit(message, (460, 300))
        confetti_particles = handle_confetti(confetti_particles, screen)
        pygame.display.flip()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_choices(question,mouse_pos):
    gap = 10
    box_height = 50
    box_width = WIDTH // 2 + 200
    startx = WIDTH // 2 - box_width // 2
    total_gap = (len(question["options"]) - 1) * gap
    total_box_height = len(question["options"]) * box_height
    start_y = HEIGHT // 2 - (total_box_height + total_gap) // 2
    for i, choice in enumerate(question['options']):
        rect_y = start_y + i * (box_height + gap)
        rect = pygame.Rect(startx, rect_y, box_width, box_height)
        
        # Check if the mouse is hovering over the option
        if rect.collidepoint(mouse_pos):
            color = CYAN  # Highlight color when mouse hovers
        else:
            color = LIGHT_BLUE if i % 2 == 0 else BLUE
        
        pygame.draw.rect(screen, color, rect)  # Draw the rectangle with the color
        pygame.draw.rect(screen, WHITE, rect, 2)  # Draw the white border
        draw_text(choice, font, BLACK, WIDTH // 2, rect_y + box_height // 2)
def draw_navigation_buttons():
    prev_button_rect = pygame.Rect(50, HEIGHT - 100, 100, 50)
    next_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 100, 100, 50)

    pygame.draw.rect(screen, BLUE, prev_button_rect)
    pygame.draw.rect(screen, BLUE, next_button_rect)

    draw_text("Prev", font, WHITE, 50 + 50, HEIGHT - 75)
    draw_text("Next", font, WHITE, WIDTH - 150 + 50, HEIGHT - 75)

    return prev_button_rect, next_button_rect

def handle_navigation_buttons(prev_button_rect, next_button_rect, mouse_pos):
    global current_question

    if prev_button_rect.collidepoint(mouse_pos) and current_question > 0:
        current_question -= 1

    if next_button_rect.collidepoint(mouse_pos) and current_question < len(questions) - 1:
        current_question += 1
def all_questions_answered():
    return all(answer is not None for answer in user_answers)
def calculate_score():
    score = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question['answer']:
            score += 10  # or your scoring logic
    return score
def game_loop():
    global current_question, score
    confetti_particles = []
    backgroundimage = load_image_remove_white_background('backgroundmain.png',(1150,825))
    robot_image = load_image_remove_white_background('robot1.png',(250,250))
    gamestart = load_image_remove_white_background('gamestart.png',(250,250))
    python = load_image_remove_white_background('python.png',(250,250))
   
  
    while not all_questions_answered():
        screen.blit(backgroundimage, (0,0))
        screen.blit(robot_image, (900, 50))
        screen.blit(gamestart, (10, -15))
        screen.blit(python, (500, 550))
        
        robot = bangerfont.render("Think you got it??", True, BLACK)
        screen.blit(robot, (900,110))
        question = questions[current_question]
        draw_text(question['Question'], font, BLACK, WIDTH // 2, HEIGHT // 4)
        mouse_pos = pygame.mouse.get_pos()
        draw_choices(question, mouse_pos)
        pygame.display.flip()
         
                
        waiting_for_input = True
        while waiting_for_input:
            prev_button_rect, next_button_rect = draw_navigation_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                mouse_pos = pygame.mouse.get_pos()
                draw_choices(question, mouse_pos)
                pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    if prev_button_rect.collidepoint(mouse_x, mouse_y) or next_button_rect.collidepoint(mouse_x, mouse_y):
                        handle_navigation_buttons(prev_button_rect, next_button_rect, (mouse_x, mouse_y))
                        waiting_for_input = False
                        break
                    if questions[current_question]['answered']:
                        continue 
                    for i, choice in enumerate(question["options"]):
                        gap = 10
                        box_height = 50
                        total_gap = (len(question["options"])-1) * gap 
                        total_box_heigth = len(question["options"]) * box_height
                        start_y = HEIGHT // 2 - (total_box_heigth+ total_gap) // 2
                        rect_y = start_y + i * (box_height + gap)
                        rect = pygame.Rect(WIDTH // 4, rect_y, WIDTH // 2,box_height)
                        if rect.collidepoint(mouse_x, mouse_y):
                            pygame.draw.rect(screen, CYAN, rect, 5) 
                            if all_questions_answered():
                                final_score = calculate_score()
                               # ... code to display final score and end the quiz ...
                                return  # Exit the game_loop
                            user_answers[current_question] = choice
                            questions[current_question]['answered'] = True
                            waiting_for_input = False
                            if current_question < len(questions) - 1:
                                current_question += 1
                        waiting_for_input = False

    # End of game
    final_score = calculate_score()
    backgroundimage = load_image_remove_white_background('backgroundmain.png',(1150,825))
    scoreimage = pygame.image.load('finalscore.png')
    scoreimage = pygame.transform.scale(scoreimage, (250,250))
    gameover = pygame.image.load('gameover.png')
    gameover = pygame.transform.scale(gameover, (200,200))
    screen.blit(backgroundimage,(0,0))
    screen.blit(scoreimage,(430,300))
    screen.blit(gameover,(460,80))
    pygame.display.flip()
    score = largefont.render(f" {final_score}", True,BLACK)
    screen.blit(score, (490, 450))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
pygame.mixer.music.load('Solve The Puzzle.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.75)
game_loop()
