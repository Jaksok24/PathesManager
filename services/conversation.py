import streamlit as st

@st.dialog("Dodaj punkt", dismissible=True)
def add_point_conversation():
    nodeId = st.text_input("Node Id", key="cNodeId")
    isEndNode = st.selectbox("Is End Node", ["true", "false"], key="cIsEndNode")
    sender = st.selectbox("Sender", ["npc", "user"], key="cSender")
    message = st.text_area("Message", key="cMessage")
    
    if st.button("Dodaj punkt", use_container_width=True, type="primary"):
        node = {
            nodeId: {
                "isEndNode": isEndNode,
                "sender": sender,
                "id": nodeId,
                "message": message
            }
        }
        st.session_state.conversationNodes.append(node)
        st.rerun()

def add_conversation():
    description = st.text_area("Conversation Description", key="cDescription")
    title = st.text_input("Conversation Title", key="cTitle")
    dificulty = st.text_input("Dificulty", key="cDificulty")
    theme = st.text_input("Theme", key="cTheme")
    durationEstimate = st.number_input("Duration Estimate", min_value=0, step=1, key="cDurationEstimate")
    characterBackground = st.text_input("Character Background", key="cCharacterBackground")
    
    return {
        "description": description,
        "title": title,
        "startNodeId": "greeding",
        "metadata": 
        {
            "dificulty": dificulty,
            "theme": theme,
            "durationEstimate": durationEstimate,
            "characterBackground": characterBackground
        },
        "nodes": st.session_state.conversationNodes
    }
