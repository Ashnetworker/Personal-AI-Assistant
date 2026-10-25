import streamlit as st
from datetime import date
from supabase import create_client
SUPABASE_URL = st.secerets["SUPABASE_URL"]
SUPABASE_KEY = st.secerets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL,SUPABASE_KEY)

st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Personal AI Assistant")
st.write("Your personal life and work life, managed together.")

st.divider()

st.subheader("📅 Today's Dashboard")
st.write(f"Today's date: {date.today().strftime('%d %B %Y')}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Personal Life")
    personal_task = st.text_input(
        "Add a personal task",
        key="personal_task"
    )

    if st.button("Add Personal Task"):
        if personal_task.strip():
            st.session_state.setdefault("personal_tasks", [])
            st.session_state.personal_tasks.append(personal_task.strip())
            st.success("Personal task added!")
        else:
            st.warning("Please enter a task.")

    for i, task in enumerate(
        st.session_state.get("personal_tasks", []), 1
    ):
        st.write(f"{i}. {task}")

with col2:
    st.subheader("💼 Work Life")
    work_task = st.text_input(
        "Add a work task",
        key="work_task"
    )

    if st.button("Add Work Task"):
        if work_task.strip():
            st.session_state.setdefault("work_tasks", [])
            st.session_state.work_tasks.append(work_task.strip())
            st.success("Work task added!")
        else:
            st.warning("Please enter a task.")

    for i, task in enumerate(
        st.session_state.get("work_tasks", []), 1
    ):
        st.write(f"{i}. {task}")

st.divider()

st.subheader("📋 Combined Schedule")

personal_tasks = st.session_state.get("personal_tasks", [])
work_tasks = st.session_state.get("work_tasks", [])

if not personal_tasks and not work_tasks:
    st.info("No tasks yet. Add your first task above!")

for task in personal_tasks:
    st.write(f"🏠 Personal: {task}")

for task in work_tasks:
    st.write(f"💼 Work: {task}")

st.divider()

st.caption(
    "Prototype Version 1.0 | Built step by step with Python and Streamlit"
)
