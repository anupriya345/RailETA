import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta


st.set_page_config(page_title="RailETA AI", layout="wide")
st.title("🚆 RailETA AI - Smarter Railways")
st.markdown("**Live Train ETA & Delay Prediction using AI**")


st.sidebar.header("Train Details")
train_no = st.sidebar.text_input("Train Number", "12555")
station = st.sidebar.selectbox("Check Station", ["Gorakhpur", "Lucknow", "Kanpur", "Delhi"])

if st.sidebar.button("Predict ETA"):
    
    # --- AI MODEL PART (Dummy Prediction Logic) ---
    # Real me yaha tum Random Forest lagaaoge
    delay = random.choice([0, 5, 15, 25, 45]) # AI ne predict kiya
    eta = datetime.now() + timedelta(minutes=30+delay)
    
    # --- DASHBOARD ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Predicted Delay", f"{delay} min", "-2 min vs yesterday")
    col2.metric("New ETA", eta.strftime("%I:%M %p"))
    col3.metric("Platform No.", f"{random.randint(1,4)}")

    st.divider()
    
    # Reason
    if delay > 20:
        reason = "Fog + High Traffic on Kanpur Route"
    else:
        reason = "On Time, Clear Track"
    st.warning(f"**AI Reason:** {reason}")

    # Graph
    st.subheader("📊 Past 7 Days Delay Analysis")
    data = pd.DataFrame({
        'Date': pd.date_range(end=datetime.today(), periods=7),
        'Delay (min)': [random.randint(0,50) for _ in range(7)]
    })
    st.line_chart(data, x='Date', y='Delay (min)')
    
    st.success("Goal: Smarter Mobility - Passenger time bachega, Railway management easy hoga.")
else:
    st.info("Train Number daal ke Predict ETA pe click karo.")
