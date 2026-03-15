import random
import streamlit as st
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")


def reset_game(low: int, high: int):
    # FIX: AI helped group the reset logic so new games clear all related Streamlit session state together.
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.feedback = None

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

if "secret" not in st.session_state:
    reset_game(low, high)
elif st.session_state.difficulty != difficulty:
    # FIX: AI suggested resetting the stored game state when difficulty changes so the range and secret stay aligned.
    reset_game(low, high)
    st.session_state.difficulty = difficulty

st.session_state.difficulty = difficulty

if "feedback" not in st.session_state:
    st.session_state.feedback = None

st.subheader("Make a guess")

col1, col2 = st.columns(2)
with col1:
    new_game = st.button("New Game 🔁")
with col2:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    reset_game(low, high)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

with st.form("guess_form", clear_on_submit=True):
    # FIX: AI suggested using a Streamlit form so pressing Enter submits the guess instead of only updating the textbox.
    raw_guess = st.text_input("Enter your guess:")
    submit = st.form_submit_button("Submit Guess 🚀")

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        if guess_int < low or guess_int > high:
            st.error(f"Your guess must be between {low} and {high}.")
        else:
            # FIX: We moved attempt/history updates to valid in-range guesses after testing the mismatch in the live game.
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)
            outcome, message = check_guess(guess_int, st.session_state.secret)

            feedback_level = None
            if show_hint:
                feedback_level = "success" if outcome == "Win" else "warning"

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.session_state.feedback = {
                    "level": "success",
                    "text": (
                        f"You won! The secret was {st.session_state.secret}. "
                        f"Final score: {st.session_state.score}"
                    ),
                }
            else:
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"
                    st.session_state.feedback = {
                        "level": "error",
                        "text": (
                            f"Out of attempts! "
                            f"The secret was {st.session_state.secret}. "
                            f"Score: {st.session_state.score}"
                        ),
                    }
                elif feedback_level is not None:
                    st.session_state.feedback = {
                        "level": feedback_level,
                        "text": message,
                    }
                    # FIX: AI helped identify that rerunning here refreshes the UI immediately so debug info is not one step behind.
                    st.rerun()

# FIX: We render status and debug info after guess handling so the page shows the current state on the same interaction.
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

if st.session_state.feedback:
    feedback = st.session_state.feedback
    if feedback["level"] == "success":
        st.success(feedback["text"])
    elif feedback["level"] == "warning":
        st.warning(feedback["text"])
    else:
        st.error(feedback["text"])
    st.session_state.feedback = None

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
