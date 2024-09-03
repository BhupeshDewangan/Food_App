import google.generativeai as genai
import os

import streamlit as st
# from prompt import *

API_KEY = "AIzaSyDzXN0UKvKj19CLHj-oi8FmjBSes_PUo54"
genai.configure(api_key=API_KEY)


def health_analysis(product_name, nutrition_label):
    prompt = f"Analyze {product_name} for nutritional value, processing level, and {nutrition_label}. Check for compliance with specific diets and its suitability for diabetes and allergens. Review brand claims for accuracy. Provide a summary with recommendations and highlight any health concerns with {product_name} and {nutrition_label}. If input box does not have Foot Item then Say 'PLEASE PROVIDE ME FOOD ITEM'"
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


def get_user_input():
    product_name = st.text_input("Product Name")
    nutrition_label = st.text_area("Nutrition Label")
    return product_name, nutrition_label

def main():
    st.title("Health Analysis of Products")
    
    product_name, nutrition_label = get_user_input()
    
    if st.button("Analyze"):
        with st.spinner("Getting Data"):
            if nutrition_label and product_name:
                health_ana = health_analysis(product_name, nutrition_label)
                st.write(health_ana)

            else:
                st.error("Please provide a nutrition label.")
    
if __name__ == "__main__":
    main()
