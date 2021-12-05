import streamlit as st
import openpyxl as opx
from data.create_data import create_table, create_degreedf

level = ''

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

    st.header('Contributors')
    c = st.container()
    with c :
        st.write("Thomas Cowie -- Co Project Manager")
        st.write("Casey Oates -- Co Project Managers")
        st.write("Eric Betties -- Resource Mangers")
        st.write("Symon Burchill -- Business Analyst")

    #Sources
    st.header('Sources')
    st.markdown("""<a href="https://educationdata.org/average-student-loan-debt">Average Student Loans</a>""", unsafe_allow_html=True)
    st.markdown("""<a href="https://educationdata.org/average-student-loan-interest-rate#:~:text=5.8%25%20is%20the%20average%20student%20loan%20interest%20rate%20among%20all,rates%20fell%20an%20average%2031.24%25.">Average Student Loan Interest Rates </a>""", unsafe_allow_html=True)
    
    st.header('Data Set Used for College Stats')
    college_path = './data/cc_institution_details.xlsx'
    with open(college_path, 'rb') as my_file:
        if st.download_button(label = 'Download', 
            data = my_file, 
            file_name = 'cc_institution_details.xlsx', 
            mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):      
            st.success('Download Successful!')
            st.balloons()
    st.header("Data Set Used for Salary by Major")

    degree_path = './data/degrees-that-pay-back.xlsx'
    with open(degree_path, 'rb') as my_file:
        if st.download_button(label = 'Download', 
            data = my_file, 
            file_name = 'degrees-that-pay-back.xlsx', 
            mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):      
            st.success('Download Successful!')
            st.balloons()
        