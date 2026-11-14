import random
import streamlit as st

st.title("Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100.")

# Remember the game between button clicks
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.won = False

# Restart the game
if st.button("New game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.won = False

# Show the guessing controls until you win
if not st.session_state.won:
    with st.form("guess_form"):
        guess = st.number_input(
            "Enter your guess:",
            min_value=1,
            max_value=100,
            value=50,
            step=1
        )
        submitted = st.form_submit_button("Guess")

    if submitted:
        st.session_state.guesses += 1

        if guess < st.session_state.secret_number:
            st.warning("Too low!")
        elif guess > st.session_state.secret_number:
            st.warning("Too high!")
        else:
            st.session_state.won = True
            st.rerun()

if st.session_state.won:
    st.success(
        f"You got it in {st.session_state.guesses} guesses!"
    )

st.write(f"Guesses: {st.session_state.guesses}")