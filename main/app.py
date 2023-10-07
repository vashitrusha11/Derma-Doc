import streamlit as st
from pages import login, select_option, dermadoc, telemedicine

if __name__ == '__main__':
    # Check the session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = ""

    if not st.session_state.logged_in:
        login()
    else:
        if st.session_state.page == "":
            select_option()
        elif st.session_state.page == "DermaDoc":
            dermadoc()
        elif st.session_state.page == "Telemedicine":
            telemedicine()
