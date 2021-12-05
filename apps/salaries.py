import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_degreedf
import plotly.graph_objects as go
import re



#We gotta make sure to put the data in the data folder and then import it correctly.

def app():
    #Title and Introduction
    st.title('Salaries')
    st.write("Salaries are something to hopefully expect once you finish you academic career, in this page we will dive into what the job market looks like for certain degree holders and what that will mean for your loan payments in realtion to your income.")

    df = create_degreedf()

    selected_major = st.selectbox('Select your major you wish to view salary information for.', df['Undergraduate Major'])
    major_data = df[df['Undergraduate Major'] == selected_major]


    undergrad_major = str(major_data['Undergraduate Major'].values)
    start_salary = str(major_data['start_med_salary'].values)
    mid_salary = str(major_data['mid_med_salary'].values)
    percent_change = str(major_data['percent_change'].values)
    mid_10 = str(major_data['mid-10'].values)
    mid_25 = str(major_data['mid-25'].values)
    mid_75 = str(major_data['mid-75'].values)
    mid_90 = str(major_data['mid-90'].values)

    for character in '[\'\]':
        undergrad_major = undergrad_major.replace(character, '')
        start_salary = start_salary.replace(character, '')
        mid_salary = mid_salary.replace(character, '')
        percent_change = percent_change.replace(character, '')
        mid_10 = mid_10.replace(character, '')
        mid_25 = mid_25.replace(character, '')
        mid_75 = mid_75.replace(character, '')
        mid_90 = mid_90.replace(character, '')

    


    st.write("Average starting salary for " + undergrad_major + " is approx.: `$" + start_salary + "`")
    st.write("Average Mid-Career salary for  " +  undergrad_major + " is approx.: `$" + mid_salary + "`")
    st.write("Percentage change from starting salary to mid-career for " + undergrad_major + " is approx.: `" + percent_change + "%" + "`")

    # fig = go.Figure(go.Pie(labels=['Mid-Career 10th percentile', 'Mid-Career 25th percentile', 'Mid-Career 75th percentile', 'Mid-Career 90th percentile'],
    #                          values=[mid_10, mid_25, mid_75, mid_90],
                    
    #                         ))
    # fig.update_layout(xaxis_tickangle=35, 
    #                     xaxis_title='Percentile',
    #                     yaxis_title='Percentages per percentile',
    #                     )
    # fig.update_yaxes(automargin=True)
    # fig = go.Figure()
    # fig2 = go.Figure()
    # fig.add_trace(go.Scatter(name='10th Percentile', x=df.loc[:25, 'Undergraduate Major'], y=df.loc[:25, 'mid-10'], mode='lines+markers'))
    # fig.add_trace(go.Scatter(name='25th Percentile', x=df.loc[:25, 'Undergraduate Major'], y=df.loc[:25, 'mid-25'], mode='lines+markers'))
    # fig.add_trace(go.Scatter(name='75th Percentile', x=df.loc[:25, 'Undergraduate Major'], y=df.loc[:25, 'mid-75'], mode='lines+markers'))
    # fig.add_trace(go.Scatter(name='90th Percentile', x=df.loc[:25, 'Undergraduate Major'], y=df.loc[:25, 'mid-90'], mode='lines+markers'))
    # fig2.add_trace(go.Scatter(name='10th Percentile', x=df.loc[26:51, 'Undergraduate Major'], y=df.loc[26:51, 'mid-10'], mode='lines+markers'))
    # fig2.add_trace(go.Scatter(name='25th Percentile', x=df.loc[26:51, 'Undergraduate Major'], y=df.loc[26:51, 'mid-25'], mode='lines+markers'))
    # fig2.add_trace(go.Scatter(name='75th Percentile', x=df.loc[26:51, 'Undergraduate Major'], y=df.loc[26:51, 'mid-75'], mode='lines+markers'))
    # fig2.add_trace(go.Scatter(name='90th Percentile', x=df.loc[26:51, 'Undergraduate Major'], y=df.loc[26:51, 'mid-90'], mode='lines+markers'))
    chosen_majors = st.multiselect('Select Some Majors to Look at', df['Undergraduate Major'])
    
    chosen_majors.sort()
    print(chosen_majors)
    fig = go.Figure()
    for k in chosen_majors:
        print(k)
        major = df[df['Undergraduate Major'] == k]
        print(major)
        fig.add_trace(go.Scatter(
            x=major['Undergraduate Major'], 
            y=major['mid-10'], 
            mode='markers', 
            connectgaps = True,       
            legendgroup='Mid Career 10th Percentile',
            name='Mid Career 10th Percentile',
            marker=dict(
            color='blue',
            size=15,
            line=dict(
                color='DarkSlateGray',
                width=2
            )
        )))
        fig.add_trace(go.Scatter(
            x=major['Undergraduate Major'], 
            y=major['mid-25'], 
            mode='markers', 
            connectgaps = True,
            legendgroup='Mid Career 25th Percentile',
            name='Mid Career 25th Percentile',
            marker=dict(
            color='yellow',
            size=15,
            line=dict(
                color='DarkSlateGray',
                width=2
            )
        )))
        fig.add_trace(go.Scatter(
            x=major['Undergraduate Major'],
            y=major['mid-75'], 
            mode='markers', 
            connectgaps = True,
            legendgroup='Mid Career 75th Percentile',
            name='Mid Career 75th Percentile',
            marker=dict(
            color='red',
            size=15,
            line=dict(
                color='DarkSlateGray',
                width=2
            )
        )))
        fig.add_trace(go.Scatter(
            x=major['Undergraduate Major'], 
            y=major['mid-90'], mode='markers', 
            connectgaps = True,
            legendgroup='Mid Career 90th Percentile',
            name='Mid Career 90th Percentile',
            marker=dict(
            color='green',
            size=15,
            line=dict(
                color='DarkSlateGray',
                width=2
            )
        )))

        fig.update_layout(
            xaxis_tickangle=25,
            xaxis_title='Majors',
            yaxis_title='Salary Amount Per Percentile',
            showlegend = False,
            autosize=False,
            width=800,
            height=500,
        )



    st.plotly_chart(fig)
    st.markdown("🟦 Mid Career 10th Percentile")
    st.markdown("🟨 Mid Career 25th Percentile")
    st.write("🟥 Mid Career 75th Percentile")
    st.write("🟩 Mid Career 90th Percentile")       

