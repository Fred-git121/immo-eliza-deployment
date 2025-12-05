import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# -----------------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Immo Eliza | AI Valuation",
    page_icon=":european_post_office:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .main { padding-top: 0rem; }

    /* Submit Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        background-color: #007bff;
        color: white;
        border: none;
    }

    /* Metric Styling */
    div[data-testid="stMetricValue"] {
        font-size: 3.5rem;
        color: #00CC96;
        font-weight: 700;
        text-align: center;
    }
    div[data-testid="stMetricLabel"] {
        text-align: center;
        width: 100%;
    }

    /* Make Radio Buttons look cleaner */
    div[role="radiogroup"] > label {
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. LOAD ARTIFACTS
# -----------------------------------------------------------------------------
@st.cache_resource
def load_artifacts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(base_dir, 'artifacts')
    model_path = os.path.join(artifacts_dir, 'model.pkl')
    features_path = os.path.join(artifacts_dir, 'features.pkl')

    if not os.path.exists(model_path) or not os.path.exists(features_path):
        return None, None

    return joblib.load(model_path), joblib.load(features_path)


model, model_features = load_artifacts()

if model is None:
    st.error("🚨 System Error: Model artifacts not found.")
    st.stop()


# -----------------------------------------------------------------------------
# 4. DATA MAPPINGS
# -----------------------------------------------------------------------------
def get_province(zip_code):
    try:
        zip_code = int(zip_code)
        if 1000 <= zip_code < 1300:
            return "Brussels"
        elif 1300 <= zip_code < 1500:
            return "Walloon Brabant"
        elif 1500 <= zip_code < 2000:
            return "Flemish Brabant"
        elif 2000 <= zip_code < 3000:
            return "Antwerp"
        elif 3000 <= zip_code < 3500:
            return "Flemish Brabant"
        elif 3500 <= zip_code < 4000:
            return "Limburg"
        elif 4000 <= zip_code < 5000:
            return "Liege"
        elif 5000 <= zip_code < 6000:
            return "Namur"
        elif 6000 <= zip_code < 6600:
            return "Hainaut"
        elif 6600 <= zip_code < 7000:
            return "Luxembourg"
        elif 7000 <= zip_code < 8000:
            return "Hainaut"
        elif 8000 <= zip_code < 9000:
            return "West Flanders"
        elif 9000 <= zip_code < 10000:
            return "East Flanders"
        else:
            return "Missing"
    except:
        return "Missing"


# Full list of types dataset
PROPERTY_TYPES = {
    "Apartment": "apartment", "Studio": "studio", "Villa": "villa", "Penthouse": "penthouse",
    "Loft": "loft", "Bungalow": "bungalow", "Chalet": "chalet", "Mansion": "mansion",
    "Duplex": "duplex", "Triplex": "triplex", "Residence": "residence", "Ground Floor": "ground-floor",
    "Master House": "master-house", "Cottage": "cottage", "Mixed Building": "mixed-building",
    "Commercial Building": "commercial-building", "Investment Property": "investment-property",
    "Office Space": "office-space", "Business Surface": "business-surface",
    "Industrial Building": "industrial-building", "Student Flat": "student-flat", "Land": "land",
    "Development Site": "development-site", "Other": "other"
}

# -----------------------------------------------------------------------------
# 5. HERO HEADER
# -----------------------------------------------------------------------------
st.markdown("""
<div style="
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
    background-size: cover;
    background-position: center;
    padding: 60px 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    color: white;
">
    <h1 style="color: white; margin: 0; font-size: 3.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">Immo Eliza Real Estate Price Predictor</h1>
    <p style="color: #ddd; margin-top: 10px; font-size: 1.2rem; font-weight: 300;">Premium AI-Powered Real Estate Estimator</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. MAIN FORM
# -----------------------------------------------------------------------------
with st.form("prediction_form"):
    st.markdown("##### 📍 Location & Type")
    c1, c2, c3 = st.columns([1, 1, 2])

    with c1:
        zip_code = st.number_input("Zip Code", 1000, 9999, 1000)
        prov = get_province(zip_code)
        if prov != "Missing":
            st.success(f"Region: {prov}")
        else:
            st.warning("Region: Unknown")

    with c2:
        type_label = st.selectbox("Property Type", options=sorted(PROPERTY_TYPES.keys()))

    with c3:
        state_input = st.select_slider(
            "State of the property",
            options=["To Restore", "To Renovate", "Good", "Excellent", "New"],
            value="Good"
        )

    st.markdown("---")

    col_details, col_amenities = st.columns([1, 1])

    with col_details:
        st.markdown("##### 📏 Specifications")
        with st.container(border=True):
            livable_surface = st.number_input("Livable Surface (m²)", 0, 1000, 150, step=10)
            bedroom_count = st.number_input("Bedrooms", 0, 10, 3)

            kitchen = st.radio(
                "Kitchen Equipment",
                ["Hyper Equipped", "Installed", "Semi Equipped", "Not Installed"],
                horizontal=True
            )

    with col_amenities:
        st.markdown("##### 🏡 Amenities")
        with st.container(border=True):
            col_a, col_b = st.columns(2)
            with col_a:
                has_garden = st.toggle("🌳 Garden")
                has_terrace = st.toggle("☀️ Terrace")
            with col_b:
                has_pool = st.toggle("🏊 Pool")

            if has_garden:
                surface_garden = st.number_input("Garden Area (m²)", 0, 5000, 50, step=10)
            else:
                surface_garden = 0

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("💰 Calculate Valuation", type="primary")

# -----------------------------------------------------------------------------
# 7. LOGIC
# -----------------------------------------------------------------------------
if submitted:
    # A. MAPPINGS
    state_mapping = {'New': 6, 'Excellent': 5, 'Normal': 4, 'To be renovated': 2, 'To restore': 1}
    state_numeric = state_mapping.get(state_input, 3)
    kitchen_map = {
        "Hyper Equipped": "Super equipped",
        "Installed": "Fully equipped",
        "Semi Equipped": "Partially equipped",
        "Not Installed": "Not equipped"
    }
    mapped_kitchen = kitchen_map[kitchen]

    raw_type_value = PROPERTY_TYPES[type_label]

    # B. INPUT
    input_data = {
        'State of the property': state_numeric,
        'Number of bedrooms': bedroom_count,
        'Livable surface': livable_surface,
        'Kitchen equipment': mapped_kitchen,
        'Furnished': 0,
        'Garage': 0,
        'Garden': 1 if has_garden else 0,
        'Terrace': 1 if has_terrace else 0,
        'Surface garden': surface_garden,
        'Swimming pool': 1 if has_pool else 0,
        'province': prov,
        'type': raw_type_value,
        'postal_code': zip_code
    }

    # C. PREDICT
    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df)
    final_df = df.reindex(columns=model_features, fill_value=0)

    try:
        prediction = model.predict(final_df)[0]

        # D. RESULT
        st.markdown("---")
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            #st.balloons()
            st.markdown(
                """
                <div style="text-align: center; padding: 20px; background-color: #f9f9f9; border-radius: 10px; border: 1px solid #ddd;">
                    <h3 style="margin:0; color: #333;">Estimated Market Value</h3>
                </div>
                """, unsafe_allow_html=True
            )
            st.metric(label="", value=f"€ {prediction:,.2f}")
            st.info(f"Estimate for a **{state_input}** **{type_label}** in **{prov}**.")

        # E. SMARTER DEBUGGER
        with st.expander("🕵️ Debug: Check Inputs"):
            st.write(f"Raw Type sent to model: **{raw_type_value}**")

            # Identify active type column
            type_cols = [c for c in final_df.columns if "type" in c.lower() and final_df[c].iloc[0] == 1]

            if type_cols:
                st.success(f"✅ Active Feature: {type_cols[0]}")
            else:
                # If "Apartment" is the reference, NO column will be active. This is good!
                st.info(
                    f"ℹ️ No active type column. This is correct if **'{raw_type_value}'** is your Reference Category (baseline).")

    except Exception as e:
        st.error(f"Prediction Error: {e}")