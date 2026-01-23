import gradio as gr
import sqlite3
import pandas as pd

def fetch_teams():
    conn = sqlite3.connect('playoffs.db')
    cursor = conn.cursor()
    query = """
    SELECT * 
    FROM teams;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns=['id', 'City', 'Name'])
    return records_df

iface = gr.Interface(fn = fetch_teams, inputs = [], outputs = gr.Dataframe(headers = ['id', 'City', 'Name']))
iface.launch()
