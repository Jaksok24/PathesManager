import streamlit as st

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

@st.dialog("Dodaj punkt", width="medium", dismissible=True)
def add_point_conversation():
    nodeId = st.text_input("Node Id", key="cNodeId")
    isEndNode = st.selectbox("Is End Node", ["true", "false"], key="cIsEndNode")
    sender = st.selectbox("Sender", ["npc", "user"], key="cSender")
    message = st.text_area("Message", key="cMessage")
    
    choices = []
    with st.form(border=True, clear_on_submit=True, key="choice"):
        nextNodeId = st.text_input("Next Node Id", key="cNextNodeId")
        choiceId = st.text_input("Choice Id", key="cChoiceId")
        choiceText = st.text_input("Choice Text", key="cChoiceText")
        
        if st.form_submit_button("Dodaj wybór", use_container_width=True):
            choice = {
                "nextNodeId": nextNodeId,
                "id": choiceId,
                "text": choiceText
            }
            choices.append(choice)
    
    if st.button("Dodaj punkt", use_container_width=True, type="primary"):
        node = {
            nodeId: {
                "isEndNode": isEndNode,
                "sender": sender,
                "id": nodeId,
                "message": message,
                "choices": choices
            }
        }
        st.session_state.conversationNodes.append(node)
        st.rerun()
