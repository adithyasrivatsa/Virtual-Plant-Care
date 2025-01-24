import streamlit as st
import datetime
import random
import time
import webbrowser

# Expanded Plant data
plant_data = {
    "Snake Plant (Sansevieria)": {
        "scientific_name": "Sansevieria trifasciata",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=6),
        "watering_interval": datetime.timedelta(days=7),
        "height": 40,  # cm
        "health": "Good",
        "care_instructions": "Water every 1-2 weeks, allow the soil to dry completely between watering.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Sansevieria_trifasciata"
    },
    "ZZ Plant (Zamioculcas zamiifolia)": {
        "scientific_name": "Zamioculcas zamiifolia",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=8),
        "watering_interval": datetime.timedelta(days=14),
        "height": 45,  # cm
        "health": "Healthy",
        "care_instructions": "Water when soil is dry, every 2 weeks. Prefers indirect light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Zamioculcas_zamiifolia"
    },
    "Pothos (Epipremnum aureum)": {
        "scientific_name": "Epipremnum aureum",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=4),
        "watering_interval": datetime.timedelta(days=5),
        "height": 25,  # cm
        "health": "Healthy",
        "care_instructions": "Water when the top inch of soil is dry. Keep in moderate to bright light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Epipremnum_aureum"
    },
    "Peace Lily (Spathiphyllum)": {
        "scientific_name": "Spathiphyllum",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=5),
        "watering_interval": datetime.timedelta(days=7),
        "height": 35,  # cm
        "health": "Good",
        "care_instructions": "Water when the soil is dry to the touch. Keep in moderate to low light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Spathiphyllum"
    },
    "Cast Iron Plant (Aspidistra elatior)": {
        "scientific_name": "Aspidistra elatior",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=6),
        "watering_interval": datetime.timedelta(days=10),
        "height": 60,  # cm
        "health": "Healthy",
        "care_instructions": "Water when the soil is dry. Tolerates low light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Aspidistra_elatior"
    },
    "Spider Plant (Chlorophytum comosum)": {
        "scientific_name": "Chlorophytum comosum",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=7),
        "watering_interval": datetime.timedelta(days=7),
        "height": 20,  # cm
        "health": "Good",
        "care_instructions": "Water when the soil is dry to the touch. Keep in bright, indirect light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Chlorophytum_comosum"
    },
    "Philodendron": {
        "scientific_name": "Philodendron spp.",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=6),
        "watering_interval": datetime.timedelta(days=7),
        "height": 40,  # cm
        "health": "Healthy",
        "care_instructions": "Water when the soil feels dry. Keep in moderate to bright light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Philodendron"
    },
    "Monstera Deliciosa": {
        "scientific_name": "Monstera deliciosa",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=4),
        "watering_interval": datetime.timedelta(days=7),
        "height": 70,  # cm
        "health": "Healthy",
        "care_instructions": "Water when the top inch of soil is dry. Keep in bright, indirect light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Monstera_deliciosa"
    },
    "English Ivy": {
        "scientific_name": "Hedera helix",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=3),
        "watering_interval": datetime.timedelta(days=5),
        "height": 25,  # cm
        "health": "Healthy",
        "care_instructions": "Water when the soil is dry. Prefers cool, moderate light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Hedera_helix"
    },
    "African Violet (Saintpaulia)": {
        "scientific_name": "Saintpaulia",
        "last_watered": datetime.datetime.now() - datetime.timedelta(days=5),
        "watering_interval": datetime.timedelta(days=7),
        "height": 15,  # cm
        "health": "Good",
        "care_instructions": "Water when the soil feels dry. Keep in bright, indirect light.",
        "wikipedia_link": "https://en.wikipedia.org/wiki/Saintpaulia"
    },
    # More plants can be added here following the same structure...
}

# Function to check if the plant needs watering
def check_watering(plant_name):
    plant = plant_data[plant_name]
    if datetime.datetime.now() > plant["last_watered"] + plant["watering_interval"]:
        return True
    return False

# Function to water the plant (update last watered time)
def water_plant(plant_name):
    plant_data[plant_name]["last_watered"] = datetime.datetime.now()

# Streamlit UI setup
st.title("🌱 Virtual Plant Care App 🌱")
st.subheader("Your personal plant care assistant")

# Sidebar - Plant Selection
selected_plant = st.sidebar.selectbox("Select a plant", list(plant_data.keys()))

# Watering reminder logic
if check_watering(selected_plant):
    st.sidebar.success(f"{selected_plant} needs watering!")
    if st.sidebar.button(f"💧 Water {selected_plant}"):
        water_plant(selected_plant)
        st.sidebar.success(f"You've watered {selected_plant}!")
else:
    st.sidebar.info(f"{selected_plant} is okay for now!")

# Plant details page
st.header(f"🌿 {selected_plant} Details 🌿")

plant = plant_data[selected_plant]

# Display plant information
st.write(f"**Scientific Name**: {plant['scientific_name']}")
st.write(f"**Height**: {plant['height']} cm")
st.write(f"**Health**: {plant['health']}")
st.write(f"**Care Instructions**: {plant['care_instructions']}")

# Add a link to Wikipedia for more information
if st.button("Learn more on Wikipedia"):
    webbrowser.open(plant["wikipedia_link"])

# Display last watered time
st.write(f"Last watered: {plant['last_watered'].strftime('%Y-%m-%d')}")

# Animation for watering the plant (simple GIF or text animation)
st.subheader("💧 Watering 💧")
if st.button(f"Water {selected_plant} Now!"):
    st.markdown('<p style="font-size:20px;color:green;">💦 Watering in progress...</p>', unsafe_allow_html=True)
    time.sleep(2)  # Simulate watering time
    st.balloons()  # Display balloons as a fun animation
    st.write(f"{selected_plant} has been watered! 💧")
    plant_data[selected_plant]["last_watered"] = datetime.datetime.now()  # Update watering time
    st.rerun()  # Refresh to show updated watering time

# Display plant growth tracking (simple random growth for fun)
st.subheader("📊 Growth 📊")
if st.button("Simulate Growth"):
    growth_increase = random.randint(1, 5)  # Random growth between 1-5 cm
    plant_data[selected_plant]["height"] += growth_increase
    st.write(f"{selected_plant} has grown by {growth_increase} cm! New height: {plant_data[selected_plant]['height']} cm.")

# Add a plant image (can be customized)
st.image("https://upload.wikimedia.org/wikipedia/commons/4/47/Aloe_vera_flowers.jpg", caption=f"{selected_plant} in all its glory!", use_container_width=True)

# Growth animation (simulating growth)
st.markdown("""
    <style>
        .grow {
            font-size: 1.5rem;
            color: green;
            animation: grow 2s ease-in-out;
        }

        @keyframes grow {
            0% { font-size: 1rem; }
            100% { font-size: 2rem; color: darkgreen; }
        }
    </style>
    <div class="grow">🌱</div>
""", unsafe_allow_html=True)

# Final message
st.write("Keep your plant happy and healthy!")
