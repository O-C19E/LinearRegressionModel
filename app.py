import joblib
import pandas as pd
import streamlit as st

model = joblib.load("lin_pipeline.joblib")

st.title("Parts-per-Hour Predictor")

c1, c2 = st.columns(2)
with c1:
    temp = st.slider("Injection temperature", 180.0, 300.0, 215.0)
    pressure = st.slider("Injection pressure", 80.0, 150.0, 115.0)
    cycle = st.slider("Cycle time (s)", 16.0, 60.0, 35.0)
    cooling = st.slider("Cooling time (s)", 8.0, 20.0, 12.0)
    viscosity = st.slider("Material viscosity", 100.0, 500.0, 250.0)
    ambient = st.slider("Ambient temperature", 18.0, 28.0, 23.0)
    age = st.slider("Machine age (years)", 0.0, 20.0, 8.0)
    experience = st.slider("Operator experience (months)", 1.0, 120.0, 22.0)
    maintenance = st.slider("Maintenance hours", 0.0, 100.0, 50.0)
with c2:
    hour = st.slider("Hour of day", 0, 23, 12)
    shift = st.selectbox("Shift", ["Day", "Evening", "Night"])
    machine = st.selectbox("Machine type", ["Type_A", "Type_B", "Type_C"])
    grade = st.selectbox("Material grade", ["Economy", "Standard", "Premium"])
    day = st.selectbox("Day of week", ["Monday", "Tuesday", "Wednesday",
                       "Thursday", "Friday", "Saturday", "Sunday"])

row = pd.DataFrame([{
    "Injection_Temperature": temp, "Injection_Pressure": pressure,
    "Cycle_Time": cycle, "Cooling_Time": cooling,
    "Material_Viscosity": viscosity, "Ambient_Temperature": ambient,
    "Machine_Age": age, "Operator_Experience": experience,
    "Maintenance_Hours": maintenance, "Hour": hour,
    "Cooling_to_Cycle_Ratio": cooling / cycle,      # engineered, as in the notebook
    "Shift": shift, "Machine_Type": machine,
    "Material_Grade": grade, "Day_of_Week": day,
}])

if st.button("Predict"):
    pred = model.predict(row)[0]
    st.metric("Predicted Parts_Per_Hour", f"{pred:.1f}")
    st.caption("Typical error is about ±2.8 parts/hour (test MAE).")