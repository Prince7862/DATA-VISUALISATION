import pandas as pd
import plotly.express as px

df = pd.read_csv("scatterdata.csv")
fig = px.scatter(df, x="Date", y="Cases", size="Cases", color="Country", size_max=20)
fig.show()