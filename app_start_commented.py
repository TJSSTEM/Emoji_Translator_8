# ============================================================
# 🚀 MY EMOJI TRANSLATOR
# A fun Python + Streamlit activity!
# ============================================================

import streamlit as st


# ============================================================
# 🎨 CHALLENGE 1: MAKE THE APP YOURS!
# ============================================================
# You can safely change the text and emojis in this section.
#
# Try:
# - Giving your app a new name
# - Changing the emojis
# - Writing your own welcome message


st.title("My Emoji Translator 💬➡️😎")

st.write("Turn your words into emojis! 🚀")

st.info("💡 Try typing: I love coding with python and my cat")


# ============================================================
# 👉 HOW TO USE THE APP
# ============================================================

with st.expander("👉 How to use this app"):
    st.write("""
    1. Type a sentence in the **Enter your text** box.
    2. The app will look for its **Magic Words**.
    3. Magic Words will be changed into emojis!
    4. Try adding your own Magic Words to the code.
    """)


# ============================================================
# 🧠 CHALLENGE 2: TEACH THE APP NEW WORDS!
# ============================================================
#
# This dictionary is the "brain" of our translator.
#
# Each word is connected to an emoji:
#
# "pizza": "🍕",
#
# 🎯 YOUR MISSION:
# Add at least 3 NEW words!
#
# ⚠️ Remember:
# - Put the word inside "quotation marks"
# - Add a colon :
# - Add your emoji
# - Add a comma ,
#
# Example:
#
# "soccer": "⚽",
# "pizza": "🍕",
# "rocket": "🚀",
#

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

    # 👇 ADD YOUR NEW MAGIC WORDS HERE!



}


# ============================================================
# ✨ SHOW OUR MAGIC WORDS
# ============================================================

st.subheader("✨ Magic Words We Know")

st.write(", ".join(EMOJI_DICT.keys()))

st.markdown("---")


# ============================================================
# 💬 TYPE YOUR SENTENCE
# ============================================================

user_input = st.text_input(
    "Enter your text to translate:",
    placeholder="Example: I love coding with my cat"
)


# ============================================================
# 🤖 THE TRANSLATOR
# ============================================================
# You don't need to change this part.
# This is where Python does the translating!

words = user_input.lower().split()

translated_words = []

for word in words:

    # Remove simple punctuation while looking for the word.
    clean_word = word.strip(".,!?")

    # Look for the word in our Emoji Dictionary.
    translated_word = EMOJI_DICT.get(clean_word, word)

    translated_words.append(translated_word)


# Put all the words back together.

output_sentence = " ".join(translated_words)


# ============================================================
# 😎 SHOW THE RESULT
# ============================================================

if output_sentence:

    st.subheader("😎 Your Emoji Sentence")

    st.success(output_sentence)


# ============================================================
# 🎉 CHALLENGE 3: ADD A SURPRISE!
# ============================================================
#
# What do you think these commands do?
#
# Remove the # from ONE of them and run your app!
#
# st.balloons()
#
# st.snow()
#
# Which one do you like better? 🎈❄️


# ============================================================
# 🏆 BONUS DESIGN CHALLENGE
# ============================================================
#
# Can you make your app different from everyone else's?
#
# Try changing:
#
# ⭐ The app title
# ⭐ The emojis
# ⭐ The welcome message
# ⭐ The instructions
# ⭐ Your Magic Words
#
# Be creative! 🚀
# ============================================================
