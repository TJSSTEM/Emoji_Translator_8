
# ============================================================
# 🚀 MY EMOJI TRANSLATOR
# A fun 10-minute Python + Streamlit activity!
# ============================================================

import streamlit as st
import random
import re


# ============================================================
# 🎨 CHALLENGE 1: MAKE THE APP YOURS!
# ============================================================
#
# 🎯 YOUR MISSION:
# Change the app title and welcome message!
#
# Try:
# - Adding your name
# - Changing the emojis
# - Giving your app a funny name
#
# Example:
# st.title("The Crazy Emoji Machine 🤪")


st.title("My Emoji Translator 💬➡️😎")

st.write("Turn your words into emojis using Python! 🚀")

st.info("💡 You are about to become a Python programmer!")


# ============================================================
# 🎨 PICK YOUR FAVORITE COLOR!
# ============================================================
# No coding required! Just select your favorite color.

st.subheader("🎨 Choose Your App's Color")

theme = st.selectbox(
    "Pick your favorite color:",
    ["💙 Blue", "🩷 Pink", "💚 Green", "💜 Purple"]
)

COLORS = {
    "💙 Blue": "#DCEEFF",
    "🩷 Pink": "#FFE0F0",
    "💚 Green": "#DFF8E5",
    "💜 Purple": "#EDE0FF"
}

st.markdown(
    f"""
    <div style="
        background-color: {COLORS[theme]};
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: #222222;
        font-size: 20px;
        font-weight: bold;
    ">
        ✨ Welcome to your Emoji Lab! ✨
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 👉 HOW TO USE THE APP
# ============================================================

with st.expander("👉 How to use this app"):
    st.write("""
    1. Choose your favorite color.
    2. Type a sentence or generate a funny one.
    3. Watch Python turn words into emojis!
    4. Add your own Magic Words to the code.
    5. Complete the challenges and celebrate!
    """)


# ============================================================
# 🧠 CHALLENGE 2: TEACH PYTHON NEW WORDS!
# ============================================================
#
# This dictionary is the "brain" of our translator.
#
# Each word is connected to an emoji.
#
# 🎯 YOUR MISSION:
# Add at least 3 NEW words!
#
# ⚠️ Remember:
# - Put the word inside "quotation marks"
# - Add a colon :
# - Add your emoji inside quotation marks
# - Add a comma ,
#
# Example:
#
# "soccer": "⚽",
# "pizza": "🍕",
# "rocket": "🚀",
#
# 👇 ADD YOUR OWN WORDS BELOW!


EMOJI_DICT = {
    "love": "❤️",
    "happy": "😊",
    "sad": "😢",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "coding": "💻",
    "win": "🏆",
    "python": "🐍",
    "fire": "🔥",

    # 👇 ADD 3 NEW MAGIC WORDS HERE!



}


# ============================================================
# ✨ SHOW OUR MAGIC WORDS
# ============================================================

st.subheader("✨ Magic Words We Know")

st.write(", ".join(EMOJI_DICT.keys()))

st.caption(f"🧠 Your translator knows {len(EMOJI_DICT)} words!")


# ============================================================
# 🎲 RANDOM FUNNY SENTENCE GENERATOR
# ============================================================
#
# Press the button to get a funny sentence!
#
# 🎯 BONUS CHALLENGE:
# Add your own funny sentence to the list!


st.markdown("---")

st.subheader("🎲 Need a Funny Sentence?")

funny_sentences = [
    "My cat loves pizza",
    "I love python and coding",
    "My dog is happy",
    "The sun is on fire",
    "I win with my cat",
    "My dog loves coding",
    "My happy cat loves python",

    # 👇 BONUS: ADD A FUNNY SENTENCE HERE!

]


# Remember the generated sentence when Streamlit reruns.
if "sentence" not in st.session_state:
    st.session_state.sentence = ""

if st.button("🎲 Surprise Me!"):
    st.session_state.sentence = random.choice(funny_sentences)


# ============================================================
# 💬 TYPE YOUR SENTENCE
# ============================================================

st.subheader("💬 Enter Your Sentence")

user_input = st.text_input(
    "Type something funny:",
    placeholder="Example: I love python and my cat",
    key="sentence"
)


# ============================================================
# 🤖 THE EMOJI TRANSLATOR
# ============================================================
#
# You don't need to change this part!
#
# Python will:
# 1. Read your sentence.
# 2. Look for Magic Words.
# 3. Replace matching words with emojis.
# 4. Show the result!
#
# This also works with punctuation and capital letters.


def translate_to_emoji(sentence):

    # Find words while keeping spaces and punctuation.
    parts = re.findall(
        r"[A-Za-z]+|[^A-Za-z]+",
        sentence
    )

    translated = []

    for part in parts:

        # Look for the word in our dictionary.
        emoji = EMOJI_DICT.get(part.lower(), part)

        translated.append(emoji)

    return "".join(translated)


output_sentence = translate_to_emoji(user_input)


# ============================================================
# 😎 SHOW THE RESULT
# ============================================================

if user_input.strip():

    st.subheader("😎 Your Emoji Sentence")

    st.success(output_sentence)

    st.caption("✨ Python translated your sentence!")


# ============================================================
# 🏆 CHALLENGE 3: THE EMOJI CHALLENGE!
# ============================================================
#
# Can you create the funniest emoji sentence?
#
# Try:
# - A sentence with 3 different emojis
# - A sentence about your favorite food
# - A sentence about a crazy animal
# - A sentence using your NEW Magic Words


st.markdown("---")

st.header("🏆 The Emoji Challenge!")

st.write("Can you complete these missions?")

challenge1 = st.checkbox(
    "🎨 I customized my app!"
)

challenge2 = st.checkbox(
    "🧠 I added 3 new Magic Words!"
)

challenge3 = st.checkbox(
    "😂 I created a funny emoji sentence!"
)


# ============================================================
# 🎉 CELEBRATION TIME!
# ============================================================
#
# When all challenges are checked,
# students can celebrate!


if challenge1 and challenge2 and challenge3:

    st.success("🏆 ALL CHALLENGES COMPLETED!")

    if st.button("🎉 CELEBRATE MY SUCCESS!"):

        st.balloons()

        st.success(
            "🎉 CONGRATULATIONS! "
            "YOU ARE OFFICIALLY A PYTHON PROGRAMMER! 🐍💻"
        )

else:

    st.info(
        "🚀 Complete all 3 challenges to unlock your celebration!"
    )


# ============================================================
# 🌟 BONUS CHALLENGE (IF YOU HAVE EXTRA TIME!)
# ============================================================
#
# Want to make your app even cooler?
#
# Try changing:
#
# ⭐ The app title
# ⭐ The welcome message
# ⭐ The Magic Words
# ⭐ The funny sentences
# ⭐ The emojis
#
# You can also experiment with these commands:
#
# st.snow()
#
# st.balloons()
#
# What happens when you remove the #?
#
# ============================================================
# 🎓 YOU JUST LEARNED SOME COMPUTER SCIENCE!
# ============================================================
#
# Dictionary = Stores words and their emojis
# Variable   = Remembers information
# Loop       = Repeats an action
# Condition  = Makes a decision
# Function   = Gives instructions to the computer
#
# 🚀 GREAT JOB, FUTURE PROGRAMMER!
# ============================================================
