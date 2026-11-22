import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Умный и прикольный редактор фото!",
                   page_icon="🤩",
                   layout="wide")

st.title("📸классный фоторедактор")
st.write("отдавай все свои фото")

st.sidebar.header("настройки фото")
uploaded_file = st.sidebar.file_uploader("выбрать картинку...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("орех фото")
        st.image(img_array, use_container_width=True)

    filter_option = st.sidebar.selectbox("Choose Filter pls:",
                                         ["оригинал", "монохром", "блюр", "яркость", "контраст", "инверсия"])

    processed_img = img_array.copy()

    if filter_option == "монохром":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    elif filter_option == "блюр":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)
    elif filter_option == "яркость":
        processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)
    elif filter_option == "контраст":
        processed_img = cv2.convertScaleAbs(img_array, alpha=1.7, beta=0)
    elif filter_option == "инверсия":
        processed_img = 225 - img_array

    with col2:
        st.subheader("готово")
        st.image(processed_img, width="stretch")