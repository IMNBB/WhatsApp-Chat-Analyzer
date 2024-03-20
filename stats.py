def mosT_active(df):
    acTive = df["users"].value_counts().head()
    perCentage = round((df["users"].value_counts()/ df.shape[0]) * 100 ,2).reset_index().rename(columns = {"index":"name" ,"users":"percent"})
    return acTive , perCentage

