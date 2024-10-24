# import streamlit as st

# st.set_page_config(
#     page_title="Group assesment"
# )

# st.header("Banking Data Details")
# st.sidebar.write("main page")

# import pandas as pd
# df = pd.read_csv('banking.csv')
# st.dataframe(df)

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('banking.csv')

# Create a multipage structure
st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts"])

if page == "Home":
    st.title("Welcome to the Banking Data App")
    st.write("This app helps you explore banking data interactively.")

    from PIL import Image 
    im = Image.open('bg-image.png')
    st.image(im)

elif page == "Charts":
    st.title("Interactive Charts")

   # Add a dropdown to filter by job type
    job_filter = st.selectbox("Select Job", options=["All"] + list(df['job'].unique()), index=0)

    # Filter the dataframe based on selected job type
    if job_filter != "All":
        filtered_df = df[df['job'] == job_filter]
    else:
        filtered_df = df

    # Create two columns
    col1, col2 = st.columns(2)

    # First chart in the first column
    with col1:
        st.subheader("Chart 1: Distribution of Age")
        fig1 = px.histogram(filtered_df, x='age', title=f"Age Distribution for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig1)

    # Second chart in the second column (using 'duration' instead of 'balance')
    with col2:
        st.subheader("Chart 2: Duration by Job")
        fig2 = px.bar(filtered_df, x='job', y='duration', color="marital", title=f"Duration by Job for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig2)

    # Add interactive control for marital status
    st.subheader("Filter by Marital Status")
    marital_status = st.selectbox("Choose marital status", options=["All"] + list(df['marital'].unique()))

    # Filter the dataframe based on selected marital status
    if marital_status != "All":
        filtered_df = filtered_df[filtered_df['marital'] == marital_status]

    # Show filtered data in chart and table
    st.write(f"Filtered Data by {marital_status} status:" if marital_status != "All" else "Complete Data:")
    st.write(filtered_df)


