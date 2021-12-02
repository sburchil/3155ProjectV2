import pandas as pd
import numpy as np
degree_data = pd.read_excel('degrees-that-pay-back.xlsx')


def create_table(level):
    data = pd.read_excel('cc_institution_details.xlsx')
    

    if (level == '2-year'):
        df = pd.DataFrame(data, 
            columns=['chronname', 'state', 'level', 'student_count', 'grad_100_value', 'grad_150_value' ])
        df = pd.DataFrame(df[df['level']==level])
    elif (level == '4-year'):
        df = pd.DataFrame(data, 
            columns=['chronname', 'state', 'level', 'student_count', 'grad_100_value', 'grad_150_value' ])
        df = pd.DataFrame(df[df['level']==level])
    else:
        df = pd.DataFrame(data, 
            columns=['chronname', 'state', 'level', 'student_count', 'grad_100_value', 'grad_150_value' ])

    

    return df

def create_degreedf():
    degree_df = pd.DataFrame(degree_data, 
        columns=['Undergraduate Major', 'start_med_salary', 'mid_med_salary', 'percent_change', 'mid-10', 'mid-25', 'mid-75', 'mid-90'])

    return degree_df




    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
