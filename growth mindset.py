import streamlit as st
import random
import time
import datetime

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Header
st.title("🌱 Growth Mindset Challenge")
st.subheader("Develop a growth-oriented mindset through daily challenges!")

# Daily Reflection Question
st.header("📝 Daily Reflection")
reflection_question = "What was the biggest challenge you faced today?"
st.write(reflection_question)

reflection_answer = st.text_area("Write your answer here:")
if reflection_answer:
    st.success("Thank you for sharing your thoughts!")

# Mood Tracker
st.header("😊 Mood Tracker")
mood = st.radio("How are you feeling today?", ["Happy 😊", "Neutral 😐", "Sad 😔"])
if mood == "Happy 😊":
    st.success("Great! Keep spreading positivity! 🌟")
elif mood == "Neutral 😐":
    st.info("Try a deep breath and focus on something you enjoy. 💙")
else:
    st.warning("It’s okay to feel low. Take a break and be kind to yourself. 💖")

# Habit Tracker
st.header("📅 Daily Habit Tracker")
habits = ["Read for 15 minutes 📖", "Exercise for 10 minutes 🏃", "Write one positive thought ✍"]
completed_habits = st.multiselect("Which habits did you complete today?", habits)
if completed_habits:
    st.success(f"Well done! You completed: {', '.join(completed_habits)}")



# Visualization - Progress Over Time
st.header("📊 Your Progress Over Time")
days = list(range(1, 8))
progress_data = [random.randint(30, 100) for _ in days]
st.line_chart({"Progress %": progress_data})

# Weekly Challenge
st.header("🔥 Weekly Growth Challenge")
weekly_challenges = [
    "Meditate for 10 minutes today.",
    "Identify one limiting belief and replace it with a positive thought.",
    "Write down three things you are grateful for.",
]
st.write("Your challenge for today: ")
st.write(random.choice(weekly_challenges))

# Daily Good Deed
st.header("🌟 Daily Good Deed")
good_deeds = [
    "Help someone in need today.",
    "Send a kind message to a friend or family member.",
    "Spend 10 minutes reflecting on what you’re grateful for.",
]
st.write("Try to complete this good deed today:")
st.write(random.choice(good_deeds))

# Gratitude Journal
st.header("📖 Gratitude Journal")
st.write("Write down three things you are grateful for today.")
gratitude_1 = st.text_input("1.")
gratitude_2 = st.text_input("2.")
gratitude_3 = st.text_input("3.")
if gratitude_1 or gratitude_2 or gratitude_3:
    st.success("Great! Practicing gratitude helps develop a positive mindset.")

# Mindfulness Exercise (Breathing Guide)
st.header("🌬️ Mindfulness Breathing Exercise")
st.write("Follow this simple breathing exercise to calm your mind.")

if st.button("Start Breathing Exercise"):
    st.write("🟢 Inhale... (4 seconds)")
    time.sleep(4)
    st.write("🔵 Hold... (4 seconds)")
    time.sleep(4)
    st.write("🔴 Exhale... (6 seconds)")
    time.sleep(6)
    st.success("Well done! Take a deep breath and continue your day with a fresh mind.")

# Footer
st.write("🌱 Keep learning and growing every day!")