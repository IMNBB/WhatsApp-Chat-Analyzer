from wordcloud import WordCloud
def status(selected_user, df):
    if selected_user != "group_analysis":
        df = df[df["users"] == selected_user]
    num_messages = df.shape[0]
    #Number of words
    words = []
    for message in df["message"]:
        words.extend(str(message).split())  # Ensure message is converted to string
    # # Count media messages
    media = df[df["message"] == "<Media omitted>\n"].shape[0]
    return num_messages, len(words) , media


def create_wordCloud(selected_user, df):
    if selected_user != "group_analysis":
        df = df[df["users"] == selected_user]
    wc: WordCloud = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    df_wc = wc.generate(df["message"].str.cat(sep=" "))
    return df_wc
#
#
def monthly_Messages(selected_user, df):
    if selected_user != "group_analysis":
        df = df[df["users"] == selected_user]
    timeline = df.groupby(["year", "month"]).count()["message"].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i] + "-" + str(timeline["year"][i]))
    timeline["time"] = time
    return timeline
def daily_timeline(selected_user , df):
    if(selected_user != "group_analysis"):
        df = df[df["users"] == selected_user]
    daily_Timeline = df.groupby("timline").count()["message"].reset_index()
    return daily_Timeline
def weekly_timeline(selected_user , df):
    if(selected_user != "group_analysis"):
        df = df[df["users"] == selected_user]
    daily_Timeline = df.groupby("day_name").count()["message"].reset_index()
    return daily_Timeline
def busy_timeline(selected_user , df):
    if(selected_user != "group_analysis"):
        df = df[df["users"] == selected_user]
    busy_timeline = df["day_name"]
    return busy_timeline.value_counts()