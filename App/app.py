import streamlit as st
import sys
import os
import base64

# Step 1: Get absolute path of the root directory (M_R_S)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Step 2: Add src folder to system path
SRC_PATH = os.path.join(BASE_DIR, 'src')
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# Step 3: Import your functions
from content_based_filtering import load_and_prepare_data, recommend_by_genres

# Step 4: Debug File Path Issue (TEMPORARY)
try:
    data_folder_path = os.path.join(BASE_DIR, 'data')
    st.write("🔍 BASE_DIR:", BASE_DIR)
    st.write("🔍 Looking for file at:", data_folder_path)
    st.write("📂 Files in data/ folder:", os.listdir(data_folder_path))
except Exception as e:
    st.error(f"⚠️ Could not read data folder: {e}")

# Step 5: Load data
@st.cache_data
def get_data():
    data_path = os.path.join(BASE_DIR, 'data', 'movies_ratings_merged.csv')
    return load_and_prepare_data(data_path)

df_exploded = get_data()

# Step 6: Set background with soft overlay and custom text styling
def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    [data-testid="stApp"] {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                          url("data:image/avif;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}

    .stMarkdown, .stTextInput, .stSelectbox, .stMultiselect, .stDataFrame {{
        color: white !important;
    }}

    label[for^="genre"] {{
        color: black !important;
        font-weight: bold;
    }}

    .stAlert p {{
        color: black !important;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image
set_background(os.path.join(os.path.dirname(__file__), "background_image.avif"))

# Step 7: App Title
st.title("🎬 Genre-Based Movie Recommender")

# Step 8: Genre Multiselect with placeholder inside (no label)
unique_genres = sorted(df_exploded['genres'].unique())
selected_genres = st.multiselect(
    label="",
    options=unique_genres,
    max_selections=3,
    placeholder="🎯 Select up to 3 genres you like",
    key="genre"
)

# Step 9: Show Recommendations
if selected_genres:
    st.subheader("🎯 Top Recommendations")

    results = recommend_by_genres(selected_genres, df_exploded)

    for _, row in results.iterrows():
        st.markdown(f"**🎬 {row['title']}**  \n⭐ Average Rating: {round(row['avg_rating'], 2)}")
        st.markdown("---")
else:
    st.info("Please select at least one genre.")
