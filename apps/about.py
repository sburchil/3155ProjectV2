import streamlit as st




def app():
    st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)

    st.markdown("""
    At UniSight, we want to provide accessible, easy-to-read data and 
    visuals to help potential and current students make informed decisions 
    on college degrees and the careers they lead to. Guiding individuals through 
    major college and career decisions, with up-to-date information, is our 
    objective.""")

    # st.write("At UniSight, we want to provide accessible, easy-to-read data and visuals to help potential and current students make informed decisions on college degrees and the careers they lead to.")
    # st.write("Guiding individuals through major college and career decisions, with up-to-date information, is our objective.")

    st.markdown('### Contributors')
    c = st.container()
    with c :
        st.write("Thomas Cowie -- Co Project Manager")
        st.write("Casey Oates -- Co Project Managers")
        st.write("Eric Betties -- Resource Mangers")
        st.write("Symon Burchill -- Business Analyst")