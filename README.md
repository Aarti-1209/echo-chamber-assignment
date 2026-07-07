Echo Chamber 9000
A Streamlit web app built for MirAI School of Technology's Virtual Summer Internship 2026 — Assignment 1: The Identity Echo Interface.
Demo
Front Page
Show Image
Successful Transmission
Show Image
Validation Warning
Show Image
Overview
This app collects a user's Name and Message, waits for an execution command (Transmit button), and conditionally processes the input based on validation checks. It also includes an advanced feature that estimates the token cost of the submitted message.
Features

UI Shell — Custom app title and instructional text using st.title() and st.write().
Multi-Data Collection — Two st.text_input() fields for Name and Message.
Action Gate — A single st.button() ("Transmit") that gates all output logic.
Conditional Routing — Handles edge cases:

Empty Name → st.error()
Empty Message (Name filled) → st.warning()
Both fields filled → st.success()


Token Cost Estimator (Advanced Challenge) — Calculates the message's character length and estimates token consumption (characters / 4), displayed via st.info().
Extra Metrics — Character count, word count, and token estimate shown side by side using st.metric().
Transmission Log — Keeps a session history of all successful transmissions using st.session_state.

Tech Stack

Python
Streamlit

How to Run Locally
git clone https://github.com/Aarti-1209/echo-chamber-assignment.git
cd echo-chamber-assignment
python -m venv venv
venv\Scripts\Activate
pip install streamlit
streamlit run app.py
The app will be available at http://localhost:8501.
Project Structure
echo-chamber-assignment/
├── app.py
├── requirements.txt
├── screenshot/
│   ├── frontpage.png
│   ├── success.png
│   └── warning.png
└── README.md
Author
Aarti — MirAI AI Builder Track, Summer Internship 2026
