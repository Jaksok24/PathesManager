import streamlit as st
import datetime
import json

st.set_page_config(page_title="Pathes Manager", page_icon=":wrench:", layout="wide")

# --- Init session state ---
if "pathProcess" not in st.session_state:
    st.session_state.pathProcess = []


# --- Dialog do dodawania punktów ---
@st.dialog("Dodaj punkt", dismissible=True)
def add_point_dialog():
    title = st.text_input("Title")
    description = st.text_area("Description")
    fabula = st.text_area("Fabula")
    minigameType = st.text_input("Minigame Type")
    order = st.number_input("Order", min_value=1, step=1)
    pointsReward = st.number_input("Points Reward", min_value=0, step=1)
    type_ = st.text_input("Type", value="minigame")

    if st.button("✅ Dodaj punkt"):
        point = {
            "title": title,
            "description": description,
            "fabula": fabula,
            "minigameType": minigameType,
            "order": order,
            "pointsReward": pointsReward,
            "type": type_
        }
        st.session_state.pathProcess.append(point)
        st.success("Punkt dodany!")
        st.rerun()  # zamyka dialog i odświeża aplikację


# --- Layout ---
left, right = st.columns(2)

with left:
    st.subheader("Dane ścieżki", anchor=False)

    pid = st.text_input("ID")
    category = st.text_input("Category")
    isPremium = st.selectbox("Is Premium", ["false", "true"])
    minAge = st.number_input("Min Age", min_value=0, max_value=100)
    rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1)
    shortDescription = st.text_input("Short Description")
    visitors = st.text_input("Visitors")
    expTime = st.number_input("Exp Time", min_value=0, max_value=1000)
    bgPhotoUrl = st.text_input("Bg Photo Url")
    displayName = st.text_input("Display Name")
    latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=0.0, step=0.0001)
    longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=0.0, step=0.0001)
    description = st.text_area("Description")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Dodaj punkt", use_container_width=True):
            add_point_dialog()
    with col2:
        submit_button = st.button("📦 Generuj JSON", type="primary", use_container_width=True)


# --- JSON Preview ---
with right:
    data = [
        {
            "id": pid,
            "category": category,
            "isPremium": isPremium,
            "minAge": minAge,
            "rating": rating,
            "shortDescription": shortDescription,
            "visitors": visitors,
            "expTime": expTime,
            "bgPhotoUrl": bgPhotoUrl,
            "displayName": displayName,
            "coordinates": {
                "latitude": latitude,
                "longitude": longitude
            },
            "description": description,
            "publishedAt": f"{datetime.datetime.now().isoformat()}",
            "pathProcess": st.session_state.pathProcess
        }
    ]

    st.subheader("Podgląd JSON", anchor=False)
    st.json(data, expanded=True)

    if submit_button:
        st.download_button(
            label="📥 Pobierz JSON",
            data=json.dumps(data, indent=4, ensure_ascii=False),
            file_name="path.json",
            mime="application/json",
            use_container_width=True,
            type="primary"
        )
