import pandas as pd
import streamlit as st
import polyline


# Page configuration for wider sidebar
st.set_page_config(layout="wide", page_title="Polyline Plotter", page_icon="🗺️")

# Streamlit app title
st.title("Polyline Plotter")
st.subheader("Plot Google Polyline on Map")

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 400px;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .sidebar .sidebar-content input {
        color: black;
    }
    .sidebar .sidebar-content .stFileUploader {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: #2e7bcf;
        color: white;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Polyline String")

polyline_string = st.sidebar.text_area("Enter the encoded polyline string", placeholder="u`ulFe|ynU?jjqAa`lQ?gb_BkbqD?xxTx_P_}hQbpvDu}mF?jubKo{lF?xgpI_{cE?|loAoxuK?apw@scxH?_~xDf~V?~f@{}@?}_Jwko@?")


if st.sidebar.button("Plot on Map"):
    pings = polyline.decode(polyline_string, geojson=True)

    df = pd.DataFrame(pings, columns=["lat", "lon"])
    st.map(df)
