'''Quiz Question
Program name suggestion:
👉 score_tracker.py
Question:
Write a Python program called score_tracker.py that keeps track of a player's highest score across multiple runs of the program.
Your program should:
Use a text file (e.g., "highscore.txt") to store and retrieve the highest score.
Read the current highest score from the file when the program starts.
Ask the user to enter their latest game score (as an integer).
Compare the new score with the saved high score.
If the new score is greater, display a congratulatory message and update the file with the new high score.
If the new score is not higher, tell the user their current high score remains unchanged.
The program should handle the case where the file doesn’t exist yet (e.g., on the very first run).
🧠 What this tests:
✅ Reading and writing files
✅ File modes (r, w, or wt)
✅ Type conversion (string ↔ int)
✅ Conditional logic
✅ Handling missing files gracefully'''

# ======================================================
# Program: persistent_file_io_tracker.py
# Purpose: Track the highest score across runs while
#          demonstrating key Python concepts and pitfalls:
#          - File handling and persistence
#          - Type conversion (str ↔ int)
#          - Functions
#          - Conditional logic
#          - Incrementing / comparing numbers
#          - Avoiding nested with-block pitfalls
#          - Correct use of .write() vs .read() return values
# ======================================================

FILENAME = 'highscore.txt'  # File to store persistent high score


# -----------------------------
# Function: read_high_score()
# -----------------------------
def read_high_score():
    """
    Reads the current high score from the file.
    
    Concepts / Learnings:
    - File handling: open file in read mode ('rt')
    - Type conversion: convert string to integer
    - Exception handling: file might not exist yet
    """
    try:
        with open(FILENAME, 'rt') as f:
            # f.read() returns the content as a string
            # We convert it to int for numeric comparisons
            high_score = int(f.read())
            return high_score
    except FileNotFoundError:
        # File does not exist yet → no high score
        return 0
    except ValueError:
        # File exists but is empty or corrupted → treat as 0
        return 0


# -----------------------------
# Function: write_high_score(score)
# -----------------------------
def write_high_score(score):
    """
    Writes a new high score to the file.
    
    Concepts / Learnings:
    - File handling: open file in write mode ('wt')
      * Write mode truncates the file automatically.
    - Type conversion: convert int to string before writing
    - .write() return value:
      * Returns the number of characters written
      * NOT the value written
      * Never use the return of .write() as data or a filename
    """
    with open(FILENAME, 'wt') as f:
        chars_written = f.write(str(score))  # write() only accepts strings
        # Debug info: shows number of characters written
        # print(f"Chars written: {chars_written}")


# -----------------------------
# Function: update_high_score(new_score)
# -----------------------------
def update_high_score(new_score):
    """
    Updates the high score if the new score is higher.
    
    Concepts / Learnings:
    - Functions: encapsulate logic for reuse
    - Conditional logic: decide whether to update
    - Persistence: data stored in a file remains across runs
    - Avoid nested with-blocks:
      * Do NOT nest reading inside writing
      * Ensures buffer is flushed and file is closed before reading
    """
    # Step 1: Read current high score
    current_high = read_high_score()

    # Step 2: Compare with new score
    if new_score > current_high:
        print(f"Congratulations! New high score: {new_score}")
        # Step 3: Write new high score
        write_high_score(new_score)
    else:
        print(f"No new high score. Current high score remains: {current_high}")

    # Step 4: Read back the high score from the file
    # ✅ Note: This is a separate top-level with block, not nested
    final_score = read_high_score()
    print(f"High score currently stored in the file: {final_score}")


# -----------------------------
# Example run
# -----------------------------
update_high_score(11)  # Test with a new score

'''Key lessons and errors addressed
Nested with blocks
Writing and immediately nesting reading can fail due to unflushed buffers.
Fixed by using two separate top-level with blocks.
.write() vs .read() return values
.write() → returns number of characters written, not the value itself.
.read() → returns string content, which can be converted to int.
File not existing
Handled with FileNotFoundError.
Empty or corrupted file
Handled with ValueError in read_high_score().
Type conversion
Always convert string ↔ int when reading/writing numeric data.
Persistence
File ensures high score remains across program runs.'''


