import re
import pandas as pd
def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s*[apAP][mM]\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({"User_messages": messages, "message_date": dates})
    df["message_date"] = pd.to_datetime(df["message_date"], format='%d/%m/%Y, %I:%M %p - ')
    df.rename(columns={"message_date": "date"}, inplace=True)

    users = []
    messages = []

    for message in df["User_messages"]:
        entry = re.split(r"([\w\s]+?):\s", message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append("group_notification")
            messages.append(entry[0])

    df["users"] = users
    df["message"] = messages
    df.drop(["User_messages"], axis=1, inplace=True)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute
    df["timline"] = df["date"].dt.date
    df["day_name"] = df["date"].dt.day_name()
    df = df.drop(columns=["date"])

    return df