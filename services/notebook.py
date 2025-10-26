import streamlit as st

def add_notebook():
    hints = []
    
    notebookTitle = st.text_input("Notebook Title", key="notebookTitle")
    theme = st.text_input("Theme", key="notebookTheme")
    backgroundStory = st.text_area("Background Story", key="notebookBackgroundStory")
    objective = st.text_area("Objective", key="notebookObjective")
    
    with st.form(border=True, clear_on_submit=True, key="notebookHint"):
        hintId = st.text_input("Hint Id", key="notebookHintId")
        hintText = st.text_area("Hint Text", key="notebookHintText")
        if st.form_submit_button("Dodaj podpowiedź", use_container_width=True):
            hint = {
                hintId : hintText
            }
            hints.append(hint)

    return {
        "minigameConfig": {
            "notebookTitle": notebookTitle,
            "hints": hints,
            "theme": theme,
            "backgroundStory": backgroundStory,
            "objective": objective,
            "pages": st.session_state.notebookPages
        }
    }

@st.dialog("Dodaj stronę", width="medium", dismissible=True)
def add_page_notebook():
    st.header("Page", anchor=False, divider="red")
    pageNumber = st.number_input("Page Number", min_value=1, step=1, key="notebookPageNumber")
    pageId = st.text_input("Id", key="notebookPageId")
    pageIsInteractive = st.selectbox("Is Interactive", ["true", "false"], key="notebookPageIsInteractive")
    pageContent = st.text_area("Content", key="notebookPageContent")
    pageClue = st.text_area("Clue", key="notebookPageClue")
    
    st.header("Content", anchor=False, divider="red")
    content = st.text_area("Content", key="notebookContentContent")
    contentIsInteractive = st.selectbox("Is Interactive", ["true", "false"], key="notebookPageContentIsInteractive")
    contentClue = st.text_area("Clue", key="notebookPageContentClue")
    solution = st.text_area("Solution", key="notebookPageContentSolution")
    
    if st.button("Dodaj stronę", use_container_width=True, type="primary"):
        page = {
        {
            "pageNumber": pageNumber,
            "id": pageId,
            "isInteractive": pageIsInteractive,
            "content": pageContent,
            "clue": pageClue
            },
            {
            "content": content,
            "isInteractive": contentIsInteractive,
            "id": pageId,
            "clue": contentClue,
            "pageNumber": pageNumber,
            "solution": solution
            },
        }
        st.session_state.notebookPages.append(page)
        st.rerun()
    
