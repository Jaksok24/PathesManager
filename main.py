import streamlit as st
import datetime
import json

st.set_page_config(page_title="Pathes Manager", page_icon=":wrench:")

minigameTypes = [
    "conversation",
    "notebook",
    "photo",
    "safe"
]

minigameData = []

# --- Init session state ---
if "pathProcess" not in st.session_state:
    st.session_state.pathProcess = []
    st.session_state.conversationNodes = []
    st.session_state.conversationChoice = []
    st.session_state.notebookPages = []

# --- Main form ---
with st.container(border=True):
    st.subheader("Dane ścieżki", anchor=False)

    pid = st.text_input("ID", key="id")
    category = st.text_input("Category", key="category")
    isPremium = st.selectbox("Is Premium", ["false", "true"], key="isPremium")
    minAge = st.number_input("Min Age", min_value=0, max_value=100, key="minAge")
    rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1, key="rating")
    shortDescription = st.text_input("Short Description", key="shortDescription")
    visitors = st.text_input("Visitors", key="visitors")
    expTime = st.number_input("Exp Time", min_value=0, max_value=1000, key="expTime")
    bgPhotoUrl = st.text_input("Bg Photo Url", key="bgPhotoUrl")
    displayName = st.text_input("Display Name", key="displayName")
    latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=0.0, step=0.0001, key="latitude")
    longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=0.0, step=0.0001, key="longitude")
    description = st.text_area("Description", key="description")

    st.subheader("PathProcess", anchor=False, divider="red")

    ppId = st.text_input("ID PathProcess", key="ppId")
    pointsReward = st.text_input("Points Reward", key="pointsReward")
    fabula = st.text_area("Fabula", key="fabula")
    npcName = st.text_input("NPC Name", key="npcName")
    ppDescription = st.text_area("Description", key="ppDescription")
    blePointId = st.text_input("BLE Point ID", key="blePointId")
    title = st.text_input("Title", key="title")
    type_ = st.selectbox("Type", ["conversation", "minigame"], key="type_")
    minigameType = st.selectbox("Minigame Type", minigameTypes, key="minigameType")
    npcDialogue = st.text_area("NPC Dialogue", key="npcDialogue")
    order = st.number_input("Order", min_value=0, step=1, key="order")
    
    if minigameType == "conversation":
        from services.conversation import add_conversation
        minigameData = add_conversation()
    if minigameType == "notebook":
        from services.notebook import add_notebook
        minigameData = add_notebook()

    left, right = st.columns(2)
    with left:
        if st.button("➕ Dodaj punkt", use_container_width=True):
            if minigameType == "conversation":
                from services.conversation import add_point_conversation
                add_point_conversation()
            if minigameType == "notebook":
                from services.notebook import add_page_notebook
                add_page_notebook()
    with right:
        submit_button = st.button("📦 Generuj JSON", type="primary", use_container_width=True)

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
        "coordinates":
        {
            "latitude": latitude,
            "longitude": longitude
        },
        "description": description,
        "publishedAt": f"{datetime.datetime.now().isoformat()}",
        "pathProcess": 
        {
            "id": ppId,
            "pointsReward": pointsReward,
            "fabula": fabula,
            "npcName": npcName,
            "description": description,
            "blePointId": blePointId,
            "title": title,
            "type": type_,
            "minigameType": minigameType,
            "npcDialogue": npcDialogue,
            "order": order,
            "minigameConfig": minigameData
        }
    }
]

st.subheader("Podgląd JSON", anchor=False)
st.json(data, expanded=True)

if submit_button:
    st.session_state.clear()
    st.download_button(
        label="📥 Pobierz JSON",
        data=json.dumps(data, indent=4, ensure_ascii=False),
        file_name="path.json",
        mime="application/json",
        use_container_width=True,
        type="primary"
    )
