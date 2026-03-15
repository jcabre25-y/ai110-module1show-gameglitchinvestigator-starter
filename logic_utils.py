def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored difficulty rules into logic_utils.py with AI help so the app uses one source of truth.
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: AI suggested validating and trimming input before counting a guess, which we verified in the live form.
    if raw is None:
        return False, None, "Enter a guess."

    cleaned = raw.strip()
    if cleaned == "":
        return False, None, "Enter a guess."

    try:
        value = int(cleaned)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: We removed the broken mixed string/number comparison after AI helped trace the wrong hint behavior.
    if guess == secret:
        return "Win", "Correct!"

    if guess > secret:
        return "Too High", "Too high. Try a lower number."

    return "Too Low", "Too low. Try a higher number."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: AI helped simplify scoring so it now follows one predictable rule based on the guess outcome.
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return max(0, current_score - 5)

    return current_score
