import streamlit as st
from data.create_data import create_table, create_degreedf

level = ''

def app():
    st.markdown("<h1>Home</h1>", unsafe_allow_html=True)

    st.markdown("""
    <section>
    At <b><strong>UniSight</strong></b>, we want to provide accessible, easy-to-read data and 
    visuals to help potential and current students make informed decisions 
    on college degrees and the careers they lead to. Guiding individuals through 
    major college and career decisions, with up-to-date information, is our 
    objective.</section>""", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'> Contributors </h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
        <p>Thomas Cowie -- Co Project Manager</p>
        <p>Casey Oates -- Co Project Managers</p>
        <p>Eric Betties -- Resource Manager</p>
        <p>Symon Burchill -- Business Analyst</p>
        </div>
    """, unsafe_allow_html=True)

    # st.write("Thomas Cowie -- Co Project Manager")
    # st.write("Casey Oates -- Co Project Managers")
    # st.write("Eric Betties -- Resource Mangers")
    # st.write("Symon Burchill -- Business Analyst")

    #Sources
    st.markdown("<h3 style='text-align: center;'> Sources </h3>", unsafe_allow_html=True)
    #st.markdown("""<a href="https://educationdata.org/average-student-loan-debt">Average Student Loans</a>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center';>
    <a href="https://educationdata.org/average-student-loan-debt">Average Student Loans</a>
    <p></p>
    <a href="https://educationdata.org/average-student-loan-interest-rate#:~:text=5.8%25%20is%20the%20average%20student%20loan%20interest%20rate%20among%20all,rates%20fell%20an%20average%2031.24%25.">Average Student Loan Interest Rates </a>
    </div>""", unsafe_allow_html=True)
    
    st.write("------------------------------------------------------------------------------")


    st.header('Data Set Used for College Stats')
    college_path = './data/cc_institution_details.xlsx'
    col1, col2 = st.columns([1,3])

    with open(college_path, 'rb') as my_file:
        with col1:
            if st.download_button(label = 'Download', 
                data = my_file, 
                file_name = 'cc_institution_details.xlsx', 
                mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):      
                st.success('Download Successful!')
                st.balloons()
        with col2:
            st.markdown("""<a href="https://www.kaggle.com/cdelany7/exploration-of-college-salaries-by-major/data">Average Student Loan Interest Rates </a>""", unsafe_allow_html=True)

    st.header("Data Set Used for Salary by Major")

    col3, col4 = st.columns([1,3])
    degree_path = './data/degrees-that-pay-back.xlsx'

    with open(degree_path, 'rb') as my_file:
        with col3:
            if st.download_button(label = 'Download', 
                data = my_file, 
                file_name = 'degrees-that-pay-back.xlsx', 
                mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'): 
                st.success('Download Successful!')
                st.balloons()
        with col4:
            st.markdown("""<a href="https://www.kaggle.com/cdelany7/exploration-of-college-salaries-by-major/data">Average Student Loan Interest Rates </a>""", unsafe_allow_html=True)     
               
    st.header("Clone the multi-page source repository:")           
    st.code("""
$ git clone git@github.com:upraneelnihar/streamlit-multiapps
$ cd streamlit-multiapps
""", language="markdown")