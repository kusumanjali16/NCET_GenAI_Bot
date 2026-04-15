import streamlit as st
from groq import Groq

st.set_page_config("SugnyanAI Context Generator",layout="wide")
st.title("SugnyanAI-Context Generator")
st.image("ncet logo.png")

client=Groq(api_key=st.secrets["GROQ_API_KEY"])
product=st.text_input("product")
audience.st.text_input("Audience")
#BUTTOM TO Generate Content 
if st.button("Generate Content"):
  prompt=f"write marketing content for {product} targeting {audience}."
  response = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=[{"role":"user","content":prompt}]
  )
  st.session_state.text = response.choices[0].message.content
  text =response.choices[0].message.content
  st.write(text)

if "text" in st.session_state:
  content = st.text_area("Genearted Content", st.session_state.text,height=300)
  st.download_button(
            label="Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
  )
else:
  st.info("Generate content first")
