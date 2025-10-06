import streamlit as st
import numpy as np
import joblib

# Load pipeline model (hasil tuning + preprocessing)
model = joblib.load("best_xgb.pkl")  # pastikan sudah disimpan dengan preprocessingnya

st.title("🚲 Bike Demand Prediction App")

# Buat tab
tab1, tab2 = st.tabs(["🎯 Prediction", "📊 Model Performance"])

with tab1:
    st.header('Demand Prediction')
    # === Input user ===
    temperature = st.number_input("Temperature (°C)", min_value=-20, max_value=50, value=25)

    humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=60,)

    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])

    holiday = st.radio("Holiday?", ["Holiday", "No Holiday"])

    hour = st.number_input("Hour (0 - 23)", min_value=0, max_value=23, value=13,)

    weekend = st.radio("Weekend?", ["Yes (Weekend)", "No (Weekday)"])

    precipitation = st.radio("Precipitation?", ["Yes (Rain)", "No (No)"])

    # === Preprocessing manual untuk fitur tertentu ===
    # hour → sin & cos
    hour_rad = 2 * np.pi * hour / 24
    hour_sin = np.sin(hour_rad)
    hour_cos = np.cos(hour_rad)

    # holiday → 0/1
    holiday_val = 'Holiday' if holiday == "Holiday" else 'No Holiday'

    # weekend → 1 jika weekend
    weekend_val = 'Weekend' if weekend.startswith("Yes") else 'Weekday'

    # precipitation → 1 jika hujan
    precip_val = 1 if precipitation.startswith("Yes") else 0

    # === Buat data input sesuai fitur model ===
    input_data = {
        "Temperature(°C)": [temperature],
        "Humidity(%)": [humidity],
        "Seasons": [season],
        "Holiday": [holiday],
        "Hour_sin": [hour_sin],
        "Hour_cos": [hour_cos],
        "Weekend": [weekend_val],
        "Precipitation": [precip_val]
    }

    import pandas as pd
    input_df = pd.DataFrame(input_data)

    # === Prediksi ===
    if st.button("Predict Demand"):
        prediction = model.predict(input_df)
        st.success(f"🎯 Estimation demand: {int(prediction[0])} bike")

with tab2:
    # === Model Performance (pakai hasil evaluasi training/validasi) ===
    # Kalau sudah dihitung sebelumnya, masukkan nilai yang sesuai
    mae = 108.47
    rmse = 184.44
    r2 = 0.915

    st.markdown("### 📊 Model Performance (XGBoost)")
    st.write(f"**MAE**  : {mae:.2f}")
    st.write(f"**RMSE** : {rmse:.2f}")
    st.write(f"**R²**   : {r2:.3f}")
    #st.write(f"**MAPE** : {mape:.2f}%")
    st.markdown("[💻 Code (Google Colab)](https://colab.research.google.com/drive/1ZtdvQly4Of_Sg_xOh58pW10g-08PxGNI?usp=sharing)", help='Sign in with Gmail to view code')
# Footer (di luar tab, sehingga selalu muncul)
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 13px;">
        Igedeaguss © 2025
    </div>
    """,
    unsafe_allow_html=True
)

