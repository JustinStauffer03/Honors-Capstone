This project is part of my Senior Honors Capstone at the University of Central Arkansas. It explores the effectiveness of gamification in computer science learningfor college students with varying levels of prior experience.
The game is a competitive, quiz-style challenge designed to test and reinforce understanding of Python programming concepts, along with garnering attention. Players answer 30 multiple-choice questions, with each question being 10 points, and a maximum score of 300. After playing, students provide me feedback via a Google Forms questionnaire to assess and evaluate engagement, learning impact, and gamification effectiveness.
The goal is to determine whether gamification can make computer science more engaging and and easier to learn for students with different backgrounds in programming.

Features include:
Blue central theme, for blue light engagement.
PNGs displayed for visual engagement as well.
30 multiple choice questions.
Ability to go back and forth between questions: previous and next buttons.
Once answered, the question cannot be answered again, it can be navigated back to however.
Confetti and green celebration screen for correct answers.
Red screen displayed with correct answer if incorrect.
Background music for an immersive experience.
Score tracking and displayed at the end of game.
Mouse tracking, for highlighting the answer mouse is hovering over.
Game will not end until all 30 questions are answered.

Resources:
Python
Pygame Library
Google Form: for game review analysis

Game Design & Flow: 
The goal was to create an engaging and educational experience, not just a basic quiz. I structured the game as followed to try to achieve this:
Start Screen: A visually appealing introduction to draw players in.
Question Navigation: Users can move between questions using Prev/Next buttons.
Answer Selection: Clicking on an option records the answer and provides immediate feedback.
Scoring System: Players garner points, and their final score is displayed at the end.

Pygame:
I chose the Pygame library because it allows for an interactive experience with smooth UI elements along with making the coding process smoother as it had a lot of pre-existing functions that were useful.
Confetti Animation: When a player gets a correct answer, colorful confetti rains down to simulate a reward effect. This helps reinforce correct answers positively.
Dynamic Hover Effects: Buttons and answer choices change color when hovered over to provide visual feedback improving usability and making it easier for the player.
Music & Sounds: Background music keeps the game lively and engaging.

Questions DataType:
The questions are stored in a list of dictionaries, making them easy to update and manage. Each question has:
The question text.
A list of possible answers.
The correct answer.
A flag to track if it has been answered.

Scoring System:
Correct answer: +10 points
Incorrect answer: No points awarded
Maximum possible score: 300 points

Research Purpose: 
This game is being used to study how gamification affects computer science education. The results will help determine:
1. Whether gamification improves engagement in learning Python.
2. If students with prior computer experience perform differently.
3. How students perceive game-based learning vs. traditional methods.


Data Collection & Analysis: 
1. Players’ final scores will be analyzed.
2. Feedback from the Google Form will be reviewed.
3. Results will contribute to research on gamification in CS education.
