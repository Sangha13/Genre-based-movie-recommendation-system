# 🎬 Genre-Based Movie Recommender

A clean, aesthetic, and minimalistic **Streamlit-based web app** that recommends movies purely based on the genres you enjoy. It uses **content-based filtering** to suggest top-rated movies, even if no user history is available — making it perfect for first-time users or casual viewers!

Whether you're in the mood for action-packed thrillers, light-hearted comedies, or heartwarming dramas, this app will guide you to top-rated picks based on your favorite genres.

---

## 📌 Features

- 🎯 Select up to **3 genres** using an intuitive dropdown
- ⭐ Instantly view **top-rated movies** in those genres (based on average rating)
- 🧹 Uses a **cleaned and pre-merged dataset** of movies and ratings
- 🌿 Visually soothing with a **nature-themed background** and dark overlay
- 💻 Fully responsive design — works seamlessly on desktop, tablet, or mobile
- ⚡ Fast performance with `@st.cache_data` for efficient data loading

---

## 🚀 Live App

👉 [Click here to try the live app](https://YOUR-STREAMLIT-LINK-HERE)  
_(Replace with your Streamlit Share or other hosted URL)_

---

## ⚙️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Data Handling**: `pandas`
- **Visualization**: `matplotlib`, `seaborn`
- **Language**: Python 3.8+

---

## 🧠 How It Works

1. Loads a merged dataset of movies and user ratings
2. Users choose their preferred genres (up to 3)
3. The app filters movies belonging to those genres
4. It then calculates the average rating for each and displays the top-rated ones

No machine learning or user profiles needed — just pure content-based logic!

---

