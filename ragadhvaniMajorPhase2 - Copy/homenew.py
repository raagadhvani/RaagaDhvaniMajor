import streamlit as st

# CSS styles
st.markdown(
    """
    <style>
    .title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #333333;
    }
    .content {
        font-size: 18px;
        margin-bottom: 20px;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">Raagadhvani: A Deep Learning Approach to Music Generation</p>', unsafe_allow_html=True)

# Introduction to Carnatic music
st.markdown('<p class="content">Carnatic music is one of the oldest forms of classical music in India, primarily practiced in the Southern states. It has a rich tradition rooted in devotional music, with intricate melodies and rhythmic patterns.</p>', unsafe_allow_html=True)

# Ragas involved in Carnatic music
st.markdown('<p class="content">Ragas play a central role in Carnatic music, each with its unique melodic structure, mood, and associations. They provide a framework for improvisation and composition.</p>', unsafe_allow_html=True)

# Major Ragas and their characteristics
st.markdown('<p class="content"><strong>Major Ragas and their Characteristics:</strong></p>', unsafe_allow_html=True)
st.markdown('<ul class="content"><li>Mohana: Evokes a peaceful and devotional mood, with emphasis on shuddha swaras (pure notes).</li><li>Bhairavi: Associated with themes of love, devotion, and compassion, with a melancholic feel.</li><li>Kalyani: Known for its uplifting and majestic character, often used in compositions expressing joy and celebration.</li><li>Shankarabharanam: Represents grandeur and solemnity, with a strong emphasis on the madhyama (fourth note).</li><li>Todi: Elicits a somber and introspective mood, characterized by complex melodic phrases and gamakas (ornamentations).</li><li>Kambhoji: Radiates a playful and lively atmosphere, with an emphasis on swara patterns and rhythmic variations.</li><li>Yaman: Originating from Hindustani music, Yaman is adapted into Carnatic music, known for its serene and romantic appeal, with a focus on smooth melodic movements.</li></ul>', unsafe_allow_html=True)