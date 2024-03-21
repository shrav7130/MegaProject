import streamlit as st


def app():
    page_bg_img="""

        <style>
        [data-testid="stAppViewContainer"]
           {
                background-image: url('https://www.kurseongmunicipality.org/images/Cloudburst1.jpg');
                background-size: cover;
            }
        </style>
        """
    st.markdown(page_bg_img,unsafe_allow_html=True)
    st.header("What is Cloud burst")
    st.subheader('A cloud burst is a sudden, intense rainfall that happens over a short period, causing rapid flooding and other related disasters.These events, often associated with thunderstorms or convective clouds, can cause rapid flooding, landslides, and other disasters. Cloud bursts exhibit extreme intensity, varying durations, and highly localized impacts. They are typically caused by convective activity and topographical factors such as mountainous terrain.')
    st.subheader('Cloud burst prediction is the scientific process of forecasting sudden, intense rainfall events using weather data and computer models to help communities prepare for and respond to potential flooding and related disasters.')
    