import plotly.express as px
import pandas as pd
# Sample Big Data-like Time Series Dataset
data = {
"Year": [2018, 2019, 2020, 2021, 2022]*2,
"Temperature": [30, 32, 33, 31, 34, 28, 29, 31, 30, 33],
"City": ["Chennai"]*5 + ["Delhi"]*5
}
df = pd.DataFrame(data)
# Sort by year to ensure proper animation
df = df.sort_values(by="Year")
fig = px.line(df, x="Year", y="Temperature", color="City",
markers=True, title="Temperature Trends Over Years")
fig.update_layout(
xaxis=dict(dtick=1), # Show every year
yaxis_title="Temperature (°C)",
xaxis_title="Year",
transition={'duration': 500}
)
fig.show()