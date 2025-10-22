print("Recovery AI ready!")
# Test imports
import gspread, pandas, openai, langchain, streamlit, flask
print("All libraries loaded successful.")
import pandas as pd
df=pd.read_csv ('recovery_data.csv')
print("Mock data loaded:")
avg_mood=df['mood'].mean()
print(f"Average mood:{avg_mood:.2f}")