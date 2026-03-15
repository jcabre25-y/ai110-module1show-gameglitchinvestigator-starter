# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

in the developer dedug info the atempts were 3 but on the attemtps left it states 5

when i selected the textbox i got a message press enter to apply, i pressed enter to apply and the number was not saved in history under debug mode the only thing that chnaged was the attempts left. this option was for normal mode.

when initialyy submitting the number the number does not get saved in history but the attepts left does decrease 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
i used ChatGPT (Codex) on this project. I used it like a teammate to review the files, explain what parts of the code were broken, and help me update the game logic. I also used it to generate a pytest case and explain why one pytest command failed while another one passed.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct AI suggestion was to refactor the game logic into `logic_utils.py` and remove the broken path where the secret number was being compared as a string instead of a number. That suggestion was correct because after the change the hints matched the guesses and the pytest regression test passed. I also verified it in the live Streamlit game by checking Developer Debug Info and seeing that the guess history and feedback matched the secret number.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One AI suggestion was misleading at first because it fixed the comparison logic but did not fully account for how Streamlit reruns the page after a submit. After the first version of the fix, the game would show a hint like "too low," but the attempts and history stayed one step behind until the next guess. I verified that by running the game, entering `22`, and seeing the hint update while the debug info still showed the previous state. That showed me the first suggestion was incomplete, so I added a rerun and moved the debug display lower in the file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

i applied the suggesion and then ran pytest

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

the secret number was teh correct number that was meant to be guesed

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

i would say that this is reruns maske the app reactive by constantly restating the app
and session state saved the variables for each user session.

- What change did you make that finally gave the game a stable secret number?

on my end the secret number did not chnage 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

i would allow the ai to comment where it thnks the issue it before coding. i would want to commit after ai change, incase i need to revert back to the working code. i would tell it to create a testcase and then tell it to provide testcase input and output examples.

  - This could be a testing habit, a prompting strategy, or a way you used Git.


- What is one thing you would do differently next time you work with AI on a coding task?

i would commit frequntly after the code implementation and make sure its working as expected. i would make like an md file just to provide a high level overview as to what file is interating with what, also what aleady works.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

it thought me that i need to first let the ai analzye the pottential issues with the code. I would then have it commet the code to better pinpoint the area that needs to be updated,

