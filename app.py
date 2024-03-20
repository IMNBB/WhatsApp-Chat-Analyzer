import streamlit as st
import re
import pandas as pd
import preprosessing
import helper
import stats
import matplotlib.pyplot as plt

st.sidebar.title("Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Upload your file here...")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprosessing.preprocess(data)
    st.title("Here is the data")
    st.dataframe(df)

    user_list = df["users"].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "group_analysis")
    selected_users = st.sidebar.selectbox("Select the person", user_list)
    if (st.sidebar.button("Show Analysis")):
        col1, col2, col3, col4 = st.columns(4)
        num_messages,words,media= helper.status(selected_users, df) #words, media#
        with col1:
            st.header("Total message")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Medial Links")
            st.title(media)

        #group level
        if (selected_users == "group_analysis"):
            st.header("Most Busy user")
            active, perCent = stats.mosT_active(df)

            fig, ax = plt.subplots()
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("Visualization")
                ax.bar(active.index, active.values)
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.header("Percentage")
                st.dataframe(perCent)
            # Worldcloud
            st.header("WORD CLOUD")
            df_wc = helper.create_wordCloud(selected_users, df)
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)
        # stats area
        st.header("Monthly Timeline")
        col1 ,col2 = st.columns(2)
        with col1:
            timeLine = helper.monthly_Messages(selected_users, df)
            fig, ax = plt.subplots()
            ax.plot(timeLine["time"], timeLine["message"])
            plt.xticks(rotation="vertical")
            st.pyplot()
        #Daily Timeline
        with col2:
            st.header("Monthly Timeline")
            dailytimeLine = helper.daily_timeline(selected_users, df)
            fig, ax = plt.subplots()
            ax.plot(dailytimeLine["timline"], dailytimeLine["message"])
            plt.xticks(rotation="vertical")
            st.pyplot()

        #Weekly Timeline
        st.header("Weekly Timeline")
        weeklytimLine = helper.weekly_timeline(selected_users, df)
        fig, ax = plt.subplots()
        ax.plot(weeklytimLine["day_name"], weeklytimLine["message"])
        plt.xticks(rotation="vertical")
        st.pyplot()

        # Weekly Timeline
        st.header("Busy Day")
        weeklytimLine = helper.busy_timeline(selected_users, df)
        fig, ax = plt.subplots()
        ax.bar(weeklytimLine.index, weeklytimLine.values)
        st.pyplot(fig)

