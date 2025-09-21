# Wordle CLI (Python)

A simple terminal-based **Wordle game** built with Python.  
The program randomly selects a 5-letter word from a CSV file and gives the player **6 attempts** to guess it.  
After each guess, letters are marked as:
- Green → correct letter in the correct position  
- Yellow → correct letter in the wrong position  
- Gray → letter not in the word  

---

## How to Run

1. Make sure you have **Python 3** installed.  
2. Ensure `wordle.py` and `wordle.csv` are in the same folder.  
3. Run the game:
```bash
python wordle.py
