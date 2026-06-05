import streamlit as st
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🎯",
    layout="wide"
)

# -------------------------
# Session Variables
# -------------------------
if "question_no" not in st.session_state:
    st.session_state.question_no = 1

if "scores" not in st.session_state:
    st.session_state.scores = []

if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

# -------------------------
# Sample Questions
# -------------------------
questions = {
    "Machine Learning Engineer": [
        "What is Overfitting?",
        "Explain Random Forest.",
        "What is Cross Validation?",
        "What is Gradient Descent?",
        "Difference between Bias and Variance?"
    ],

    "Python Developer": [
        "What is OOP?",
        "What is Inheritance?",
        "Explain List Comprehension.",
        "Difference between List and Tuple?",
        "What is Exception Handling?"
    ],

    "Data Analyst": [
        "What is Data Cleaning?",
        "What is SQL JOIN?",
        "Difference between INNER and LEFT JOIN?",
        "What is Power BI?",
        "What is EDA?"
    ]
}

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("🎯 Interview Settings")

role = st.sidebar.selectbox(
    "Select Job Role",
    list(questions.keys())
)

total_questions = len(questions[role])

# -------------------------
# Main Header
# -------------------------
st.title("🎯 AI Interview Preparation Assistant")

st.write(
    "Practice interviews, get feedback, and view performance reports."
)

# -------------------------
# Progress
# -------------------------
progress = int(
    ((st.session_state.question_no - 1) / total_questions) * 100
)

progress = min(progress, 100)

st.progress(progress)

# -------------------------
# Interview Section
# -------------------------
if st.session_state.question_no <= total_questions:

    current_question = questions[role][
        st.session_state.question_no - 1
    ]

    st.subheader(
        f"Question {st.session_state.question_no}/{total_questions}"
    )

    st.info(current_question)

    answer = st.text_area(
        "Enter Your Answer",
        height=200
    )

    if st.button("Submit Answer"):

        if answer.strip() == "":
            st.warning("Please enter an answer.")
        else:

            # -------------------------
            # Dummy Evaluation
            # Replace with OpenAI later
            # -------------------------
            score = min(
                10,
                max(4, len(answer.split()) // 5)
            )

            feedback = f"""
            Score: {score}/10

            Strengths:
            ✔ Answer submitted successfully

            Improvements:
            ✔ Add more technical details
            ✔ Give examples
            """

            st.session_state.scores.append(score)
            st.session_state.feedbacks.append(feedback)

            st.success(feedback)

            st.session_state.question_no += 1

            st.rerun()

# -------------------------
# Final Report
# -------------------------
else:

    st.header("📊 Final Interview Report")

    average_score = (
        sum(st.session_state.scores)
        / len(st.session_state.scores)
    ) * 10

    technical_score = average_score
    communication_score = max(
        60,
        average_score - 5
    )

    confidence_score = max(
        55,
        average_score - 10
    )

    readiness_score = (
        technical_score +
        communication_score +
        confidence_score
    ) / 3

    if readiness_score >= 80:
        status = "PASS ✅"

    elif readiness_score >= 60:
        status = "NEEDS IMPROVEMENT ⚠️"

    else:
        status = "NOT READY ❌"

    # Metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Technical",
        f"{technical_score:.1f}%"
    )

    col2.metric(
        "Communication",
        f"{communication_score:.1f}%"
    )

    col3.metric(
        "Confidence",
        f"{confidence_score:.1f}%"
    )

    col4.metric(
        "Readiness",
        f"{readiness_score:.1f}%"
    )

    st.divider()

    st.subheader("Final Result")

    st.success(f"Status: {status}")

    st.write(
        f"Overall Score: {readiness_score:.1f}%"
    )

    st.divider()

    st.subheader("Recommendations")

    st.write("""
    • Improve technical depth

    • Practice real interview questions

    • Learn advanced concepts

    • Work on communication skills
    """)

    st.divider()

    st.subheader("Question-wise Scores")

    report_df = pd.DataFrame({
        "Question No":
            range(
                1,
                len(st.session_state.scores) + 1
            ),
        "Score":
            st.session_state.scores
    })

    st.dataframe(
        report_df,
        use_container_width=True
    )

    if st.button("Restart Interview"):

        st.session_state.question_no = 1
        st.session_state.scores = []
        st.session_state.feedbacks = []

        st.rerun()