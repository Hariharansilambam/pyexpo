import random
import streamlit as st

st.title(f"GUESSING GAME")


name=st.text_input("Enter Your Name:")
st.write(f"YOUR NAME IS:{name}")


if 'guess_taken' not in st.session_state:
    st.session_state.guess_taken = 0
if 'num' not in st.session_state:
    st.session_state.num = random.randint(1, 100)
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

if not st.session_state.game_over:
    guess = st.number_input("I'm thinking of a number between 1 and 30, can you guess it?", min_value=1, max_value=100, step=1)
   
    if st.button("Submit"):
        st.session_state.guess_taken += 1
        if guess < st.session_state.num:
            st.write("You need to guess higher, Try again!")
        elif guess > st.session_state.num:
            st.write("You need to guess lower, Try again!")
        else:
            st.write(f"GOOD JOB! You guessed it in {st.session_state.guess_taken} guesses.")
            st.session_state.game_over = True
       
        if st.session_state.guess_taken >= 4 and guess != st.session_state.num:
            st.write(f"YOU LOSE! The number I was thinking of was {st.session_state.num}.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.num = random.randint(1, 100)
        st.session_state.guess_taken = 0
        st.session_state.game_over=False