import streamlit as st
import sys
import os
import base64
from pathlib import Path

# Step 1: Get absolute path to project root
APP_DIR = Path(__file__).parent.resolve()
BASE_DIR = APP_DIR.parent

# Step 2: Add src folder to system path
SRC_PATH = BASE_DIR / 'src'
if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

# Step 3: Import your functions
from content_based_filtering import load_and_prepare_data, recommend_by_genres

# Step 4: Load data
@st.cache_data
def get_data():
    data_path = BASE_DIR / 'data' / 'movies_ratings_merged.csv'
    if not data_path.exists():
        st.error(f"❌ File not found: {data_path}")
        st.stop()
    return load_and_prepare_data(str(data_path))

df_exploded = get_data()

# Step 5: Set background image
def set_background(image_path):
    try:
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
    except Exception as e:
        st.warning(f"⚠️ Background image could not be loaded. Reason: {e}")

set_background(APP_DIR / "background_image.avif")

# Step 6: Streamlit UI
st.title("🎬 Genre-Based Movie Recommender")

# Step 7: Genre Selection
unique_genres = sorted(df_exploded['genres'].unique())
selected_genres = st.multiselect(
    label="",
    options=unique_genres,
    max_selections=3,
    placeholder="🎯 Select up to 3 genres you like",
    key="genre"
)

# Step 8: Show recommendations
if selected_genres:
    st.subheader("🎯 Top Recommendations")
    results = recommend_by_genres(selected_genres, df_exploded)

    for _, row in results.iterrows():
        st.markdown(f"**🎬 {row['title']}**  \n⭐ Average Rating: {round(row['avg_rating'], 2)}")
        st.markdown("---")
else:
    st.info("Please select at least one genre.")
