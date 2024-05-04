import streamlit as st

# Theme configuration
theme = """
    <style>
        .stApp {
            background-color: #FFFFFF;
            color: #262730;
            font-family: sans-serif;
        }
        .css-2trqyj {
            color: #262730;
        }
        .st-bu {
            background-color: #FFD3E0; /* Lighter shade of pink */
        }
        .st-cg {
            background-color: #F0F2F6;
        }
        img {
            max-width: 50%;
            height: auto;
        }
    </style>
"""
st.markdown(theme, unsafe_allow_html=True)

# Title
st.title("🎶 Raagadhvani: A Deep Learning Approach For Music Generation")

# Introduction to Indian Classical Music and Carnatic Music
st.subheader("Indian Classical Music and Carnatic Music")
st.write("Indian classical music is one of the oldest musical traditions in the world, with a rich history and cultural significance. Carnatic music is a form of Indian classical music that is primarily practiced in the southern states of India.")
st.write("Carnatic music is known for its intricate melodies, rhythmic patterns, and improvisational aspects. It has a vast repertoire of compositions spanning various genres and themes, including devotional, romantic, and philosophical themes.")

# Swaras and their representation
st.subheader("🎵 Swaras and their Representation")
st.image("swaras.PNG", caption="Swaras in Carnatic Music")
st.write("Swaras are the seven basic musical notes in Indian classical music. They are: Sa, Ri, Ga, Ma, Pa, Dha, Ni, corresponding to Do, Re, Mi, Fa, So, La, Ti in Western music.")
st.write("In Carnatic music, each swara is associated with a specific frequency and is denoted by a unique symbol. These swaras form the foundation of melodies in Carnatic music and are used to create intricate melodic structures known as ragas.")

# Characteristics of major ragas
st.subheader("🎶 Major Ragas and their Characteristics")
st.image("ragachart.png", caption="Carnatic Raagas")
ragas_characteristics = {
    "Hanumathodi": {
        "Characteristics": "Hanumathodi is a morning raga that evokes a feeling of devotion and peace. It is known for its gentle and melodious phrases, with a focus on the lower notes (mandra sthayi).",
        "Famous Compositions": "Sri Subramanyaaya Namastestu, Raghuvamsha Sudha",
        "Image": "Hanumatodi_scale.gif"
    },
    "Bhairavi": {
        "Characteristics": "Bhairavi is a late-night raga that conveys a sense of longing and devotion. It is characterized by its use of komal (flat) Ni and Dha, and its complex melodic phrases.",
        "Famous Compositions": "Sri Chakra Raja, Bhavayami Raghuramam",
        "Image": "Natabhairavi_scale.gif"
    },
    "Kambhoji": {
        "Characteristics": "Kambhoji is a popular raga that is often used for lighter compositions. It is known for its playful and cheerful nature, with a focus on the middle notes (madhya sthayi).",
        "Famous Compositions": "Evari Bodhana, Nannu Vidachi",
        "Image": "Harikambhoji_scale.gif"
    },
    "Shankarabharanam": {
        "Characteristics": "Shankarabharanam is a classic raga that is often used for elaborate compositions. It is known for its grand and majestic phrases, with a focus on the upper notes (tara sthayi).",
        "Famous Compositions": "Swagatham Krishna, Devi Neeye Thunai",
        "Image": "Sankarabharanam_scale.gif"
    },
    "Kalyani": {
        "Characteristics": "Kalyani is a morning raga that is often used for auspicious occasions. It is known for its uplifting and joyful nature, with a focus on the upper notes (tara sthayi).",
        "Famous Compositions": "Brova Bharama, Evarunnarayya",
        "Image": "Kalyani_scale.gif"
    }
}

# Display characteristics of major ragas in expandable sections
for raga, info in ragas_characteristics.items():
    with st.expander(f"{raga.capitalize()}"):
        st.image(info["Image"], caption=f"{raga.capitalize()} Raga")
        st.write(f"**Characteristics**: {info['Characteristics']}")
        st.write(f"**Famous Compositions**: {info['Famous Compositions']}")

# Closing note
st.markdown("---")
st.write("Start exploring the world of Indian classical music with Raagadhvani!")
