import streamlit as st
import functions

titles=functions.readfile()
def add_title():
    title = st.session_state["new_title"] +"\n"
    titles.append(title)
    functions.writefile(titles)


st.title("My watch list")
st.write("Cuz you have so much shit to watch but such little time")

for tno, title in enumerate(titles):
    checkbox = st.checkbox(title,key=title)
    if checkbox:
        titles.pop(tno)
        functions.writefile(titles)
        del st.session_state[title]
        st.rerun()


st.text_input(label=" ",placeholder="Ender a new title....",on_change=add_title, key='new_title')

