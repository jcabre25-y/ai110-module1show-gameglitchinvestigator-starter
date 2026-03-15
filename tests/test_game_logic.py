from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_accepts_integer_input():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_rejects_blank_input():
    assert parse_guess("   ") == (False, None, "Enter a guess.")


def test_parse_guess_rejects_non_integer_input():
    assert parse_guess("4.2") == (False, None, "That is not a whole number.")


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "Correct!"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_check_guess_uses_numeric_comparison_not_string_comparison():
    outcome, message = check_guess(12, 9)
    assert outcome == "Too High"
    assert message == "Too high. Try a lower number."


def test_update_score_rewards_faster_wins():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 5) == 60


def test_update_score_never_goes_negative():
    assert update_score(0, "Too High", 2) == 0
    assert update_score(3, "Too Low", 2) == 0
