import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import datetime
from features.system_settings import safety_settings, generation_config_daily_plans, system_instruction_daily_plans

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                safety_settings=safety_settings,
                system_instruction=system_instruction_daily_plans,
                generation_config=generation_config_daily_plans)

st.info("Note: Dost AI Daily Plans is a AI based features which is just a Prototype right now. Please use it with caution and consult a doctor for professional advice.")

st.header("📅Daily Plans Maker", anchor="daily-plans", divider="rainbow")
with st.expander("What is Daily Plans Maker?"):
    st.write("Daily Plans Maker is a tool that uses Google Artificial Intelligence Model to help you create daily plans based on your preferences. DostAI will help you to create a daily plan for you to follow.")
st.divider()

st.subheader("Enter your details to create your daily plans:")
with st.form(key="daily-plans-form"):
    schedule_type = st.selectbox("What is your schedule for today?*", ["Holiday", "Workday", "Weekend"])
    time = st.time_input("When do you want to start your day?*", datetime.time(8, 0))
    plan_type = st.multiselect("What type of plans would you like to create?*", ["Health Exercise", "Diet Plan", "Trip Plan"])
    any_other = st.text_area("Any other preferences or details you would like to add or Preplanned work?*", height=100, placeholder="Example: I want to go for a walk in the evening.")
    st.markdown("*Required**")
    submit_button = st.form_submit_button(label="Create Plans")

    if submit_button:
        if not schedule_type or not time or not plan_type or not any_other:
            st.error("Please fill all the required fields.")
            st.stop()
        else:
            st.success("Please wait while DostAI is processing your request...")
st.divider()

with st.spinner("Processing your request..."):
    if schedule_type and time and plan_type and any_other is not None:
        st.subheader("Daily Plans:")
        prompt = f"""Today is {schedule_type} and I want to start my day at {time}. I would like to create a plan for {', '.join(plan_type)} and {any_other}."""
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("Please fill all the required fields to create your daily plans.")
