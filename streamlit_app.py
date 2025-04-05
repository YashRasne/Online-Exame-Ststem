import streamlit as st

# ----------------------------
# 🧠 Mock Question Bank
# ----------------------------
QUESTIONS = [
    {
        "id": 1,
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5"],
        "answer": "4"
    },
    {
        "id": 2,
        "question": "Capital of France?",
        "options": ["Berlin", "Paris", "London"],
        "answer": "Paris"
    },
    {
        "id": 3,
        "question": "Which is a programming language?",
        "options": ["Python", "Snake", "Lizard"],
        "answer": "Python"
    }
]

# ----------------------------
# 🚀 Streamlit Frontend
# ----------------------------

st.title("📝 Online Exam System (Single File)")

st.markdown("### Please answer the following questions:")

user_answers = {}

# Render questions
for q in QUESTIONS:
    st.subheader(q["question"])
    selected = st.radio("Select one:", q["options"], key=q["id"])
    user_answers[q["id"]] = selected

# Submit button
if st.button("Submit Exam"):
    score = 0
    total = len(QUESTIONS)

    for q in QUESTIONS:
        if user_answers[q["id"]] == q["answer"]:
            score += 1

    st.success(f"✅ You scored {score} out of {total}!")

    # Show correct answers
    st.markdown("### 📘 Correct Answers:")
    for q in QUESTIONS:
        st.write(f"**{q['question']}** — ✅ {q['answer']}")
