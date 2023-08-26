#your app starts now
import streamlit as st

st.set_page_config(page_title="Lil Love Bug")

st.header("Nom Nom :blue[Saahil]!")
st.write("Why so lovely? :ladybug:")

lovey = st.text_input("How much do I love you?")

if lovey == "So much":
  st.write("Mhmm! So much! x 3000")
  st.write("Soo much")
  st.write("Sooo much")
  st.write("Soooo much")
  st.write("Sooooo much")
  st.write("Soooooo much")
else:
  st.write("Nuh uh! WRONG!")
  st.write("I love you so much")
  st.write("Soo much")
  st.write("Sooo much")
  st.write("Soooo much")
  st.write("Sooooo much")
  st.write("Soooooo much")
