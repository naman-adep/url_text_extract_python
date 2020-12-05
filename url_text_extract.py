import streamlit as st
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

st.title("Extract Text from the URL")
raw_url = st.text_input("Enter URL Here")

if st.button("Extract Text"):
    page = urlopen(raw_url)
    soup = BeautifulSoup(page)
    words = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    st.write(words)