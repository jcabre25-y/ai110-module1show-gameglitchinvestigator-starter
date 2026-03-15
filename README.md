# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  This project is a Streamlit number guessing game where the player tries to guess a secret number within a limited number of attempts based on the selected difficulty.
- [x] Detail which bugs you found.
  I found that the attempts counter and debug info could get out of sync, the first submitted guess did not immediately appear in history, pressing Enter did not properly submit the guess, and the game logic could compare values incorrectly and give misleading hints.
- [x] Explain what fixes you applied.
  I moved the core game logic into `logic_utils.py`, fixed numeric guess comparison, corrected attempt and history updates, reset session state properly for new games and difficulty changes, and updated the Streamlit flow so the UI refreshes immediately after valid guesses.

## 📸 Demo

- [x] Fixed game demo completed in Streamlit.
  In the repaired version, the game starts with the correct number of attempts for the selected difficulty, valid guesses are added to history right away, pressing Enter submits through the form, and the debug panel matches the current game state after each guess.
  Add your screenshot of the fixed winning game here before submission if your instructor expects an image.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
