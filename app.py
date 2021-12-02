import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed", page_title='UniSight', page_icon=':goat:')
from multiapp import MultiApp
from apps import home, data_stats, about, loans, salaries # import your app modules here

# hide_footer_style = """
#     <style>
#     .reportview-container .main footer {visibility: hidden;}    
#     """
# st.markdown(hide_footer_style, unsafe_allow_html=True)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("About", about.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Loans", loans.app)
app.add_app("Salaries", salaries.app)

# The main app
app.run()