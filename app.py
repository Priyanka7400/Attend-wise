import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Attend-Wise",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Attend-Wise")
st.subheader("Smart Attendance Tracking & Predictive Optimization Platform")

st.markdown("---")

# Sidebar inputs
st.sidebar.header("Attendance Input")
conducted = st.sidebar.number_input("Total Conducted Lectures", min_value=1, value=40, step=1)
attended = st.sidebar.number_input("Total Attended Lectures", min_value=0, max_value=int(conducted), value=20, step=1)
target_pct = st.sidebar.slider("Target Attendance (%)", min_value=50, max_value=95, value=75, step=5)

# Metrics calculation
current_pct = (attended / conducted) * 100

st.metric("Current Attendance Rate", f"{current_pct:.2f}%")

if current_pct < target_pct:
    req_classes = math.ceil((target_pct * conducted - 100 * attended) / (100 - target_pct))
    st.error(f"⚠️ Target Short! You need to attend *{req_classes}* continuous lectures to reach {target_pct}%.")
else:
    safe_bunks = math.floor((100 * attended - target_pct * conducted) / target_pct)
    st.success(f"🎉 Safe Zone! You can miss up to *{safe_bunks}* upcoming lectures while maintaining at least {target_pct}%.")
