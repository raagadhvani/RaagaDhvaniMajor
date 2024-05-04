import streamlit as st
import numpy as np
import wave
import struct
# Some Useful Variables
window_size = 2205    # Size of window to be used for detecting silence
beta = 1   # Silence detection parameter
max_notes = 10000    # Maximum number of notes in file, for efficiency
sampling_freq = 44100   # Sampling frequency of audio signal
threshold = 1600
# Reference notes
reference_notes = [
    'S_4', 'R2_4',  'G3_4', 'M1_4', 'P_4', 
    'D2_4',  'N3_4',  'R1_4',  'G2_4',  'M2_4', 
    'D1_4',  'N2_4'
]
def filter_notes(input_array, reference_notes):
    reference_set = set(reference_notes)
    filtered_notes = [note for note in input_array if note in reference_set]
    return filtered_notes
notes = [
    'S_0', 'R1_0', 'R2_0', 'G2_0', 'G3_0', 'M1_0', 'M2_0', 'P_0', 'D1_0', 'D2_0', 'N2_0', 'N3_0',
    'S_1', 'R1_1', 'R2_1', 'G2_1', 'G3_1', 'M1_1', 'M2_1', 'P_1', 'D1_1', 'D2_1', 'N2_1', 'N3_1',
    'S_2', 'R1_2', 'R2_2', 'G2_2', 'G3_2', 'M1_2', 'M2_2', 'P_2', 'D1_2', 'D2_2', 'N2_2', 'N3_2',
    'S_3', 'R1_3', 'R2_3', 'G2_3', 'G3_3', 'M1_3', 'M2_3', 'P_3', 'D1_3', 'D2_3', 'N2_3', 'N3_3',
    'S_4', 'R1_4', 'R2_4', 'G2_4', 'G3_4', 'M1_4', 'M2_4', 'P_4', 'D1_4', 'D2_4', 'N2_4', 'N3_4',
    'S_5', 'R1_5', 'R2_5', 'G2_5', 'G3_5', 'M1_5', 'M2_5', 'P_5', 'D1_5', 'D2_5', 'N2_5', 'N3_5',
    'S_6', 'R1_6', 'R2_6', 'G2_6', 'G3_6', 'M1_6', 'M2_6', 'P_6', 'D1_6', 'D2_6', 'N2_6', 'N3_6',
    'S_7', 'R1_7', 'R2_7', 'G2_7', 'G3_7', 'M1_7', 'M2_7', 'P_7', 'D1_7', 'D2_7', 'N2_7', 'N3_7',
    'S_8', 'R1_8', 'R2_8', 'G2_8', 'G3_8', 'M1_8', 'M2_8', 'P_8', 'D1_8', 'D2_8', 'N2_8', 'N3_8'
]

# Array for corresponding frequencies in Hertz
array = [
    16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87,
    32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74,
    65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47,
    130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94,
    261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88,
    523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61, 880.00, 932.33, 987.77,
    1046.50, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98, 1567.98, 1661.22, 1760.00, 1864.66, 1975.53,
    2093.00, 2217.46, 2349.32, 2489.02, 2637.02, 2793.83, 2959.96, 3135.96, 3322.44, 3520.00, 3729.31, 3951.07,
    4186.01, 4434.92, 4698.63, 4978.03, 5274.04, 5587.65, 5919.91, 6271.93, 6644.88, 7040.00, 7458.62, 7902.13
]

def identify_notes(sound):
    Identified_Notes = []
    sound_square = np.square(sound)
    frequency = []
    dft = []
    i = 0
    j = 0
    k = 0

    while(i<=len(sound_square)-window_size):
        s = 0.0
        j = 0
        while j <= window_size and (i + j) < len(sound_square): 
            s = s + sound_square[i+j]
            j = j + 1	

        if s < threshold:
            if(i-k>window_size*4):
                dft = np.array(dft)
                dft = np.fft.fft(sound[k:i])
                dft=np.argsort(dft)

                if(dft[0]>dft[-1] and dft[1]>dft[-1]):
                    i_max = dft[-1]
                elif(dft[1]>dft[0] and dft[-1]>dft[0]):
                    i_max = dft[0]
                else :	
                    i_max = dft[1]

                frequency.append((i_max*sampling_freq)/(i-k))
                dft = []
                k = i+1
        i = i + window_size

    for i in frequency :
        idx = (np.abs(array-i)).argmin()
        Identified_Notes.append(notes[idx])

    return Identified_Notes

# Define a function to check if the identified notes match the expected sequence
def check_match(identified_notes, expected_sequence):
    matched_notes = 0
    for i in range(len(expected_sequence)):
        if i < len(identified_notes) and identified_notes[i] == expected_sequence[i]:
            matched_notes += 1
    return matched_notes

def analyze_audio(expected_sequence, aarohanam_file):
    if aarohanam_file is not None:
        sound_file = wave.open(aarohanam_file, 'r')
        file_length = sound_file.getnframes()
        sound = np.zeros(file_length)

        for i in range(file_length):
            data = sound_file.readframes(1)
            data = struct.unpack("hh", data)
            sound[i] = int(data[0])

        sound = np.divide(sound, float(2**15))   # Normalize data in range -1 to 1
        identified_notes = identify_notes(sound)  # Assuming identify_notes is defined elsewhere
        output_string = ', '.join(identified_notes)
        #st.write(output_string)

        # Filter notes not present in 4th and 5th octaves
        filtered_identified_notes = filter_notes(identified_notes, reference_notes)  # Assuming filter_notes is defined elsewhere
        filtered_output_string = ', '.join(filtered_identified_notes)
        #st.write(filtered_output_string)
        unique_notes = [filtered_identified_notes[0]]  # Start with the first note

        for i in range(1, len(filtered_identified_notes)):
            if filtered_identified_notes[i] != filtered_identified_notes[i - 1]:  # Compare with the previous note
                unique_notes.append(filtered_identified_notes[i])

        filtered_unique_notes = ', '.join(unique_notes)
        st.write("IDENTIFIED NOTES:")
        st.write(filtered_unique_notes)

        matching_notes = []
        total_notes = len(expected_sequence)
        matching_count = 0

        for i, note in enumerate(expected_sequence):
            played_note = unique_notes[i] if i < len(unique_notes) else ""
            #st.write(played_note)
            if note == played_note:
                matching_count += 1
            matching_notes.append((note, played_note))

        # Display results
        col1, col2 = st.columns(2)
        all_matched = True

        for i, (expected_note, played_note) in enumerate(matching_notes):
            column = col1 if i < 4 else col2

            if expected_note == played_note:
                column.success(f"Expected: {expected_note}, Played: {played_note} ✔️")
            else:
                all_matched = False
                column.error(f"Expected: {expected_note}, Played: {played_note} ❌")

        progress_percentage = (matching_count / total_notes)
        st.write(f"Progress: {progress_percentage * 100:.2f}%")
        st.progress(progress_percentage)

        if all_matched:
            st.success("Congratulations! All notes matched correctly.")
        else:
            st.error("Keep practicing! Some notes are not matched.")





# List of expected sequences
sarali_sequences = [
    ['S_4', 'R2_4', 'S_4', 'R2_4', 'S_4', 'R2_4', 'G3_4', 'M1_4'],
    ['G3_4', 'M1_4', 'P_4', 'D2_4', 'N3_4', 'D2_4', 'P_4', 'M1_4']]
    

dhatu_sequences = [
    ['S_4', 'M1_4', 'G3_4', 'M1_4', 'R2_4', 'G3_4', 'S_4', 'R2_4'],
    ['G3_4', 'D2_4', 'P_4', 'D2_4', 'M1_4', 'P_4', 'G3_4', 'M1_4'],
    ['D2_4', 'G3_4', 'M1_4', 'G3_4', 'P_4', 'M1_4', 'D2_4', 'P_4'],
    ['N3_4', 'M1_4', 'P_4', 'D2_4', 'N3_4', 'D2_4', 'P_4', 'M1_4'],
    ['G3_4', 'M1_4', 'G3_4', 'P_4', 'M1_4', 'P_4', 'M1_4', 'D2_4'],
    ['R2_4', 'P_4', 'M1_4', 'P_4', 'G3_4', 'M1_4', 'R2_4', 'G3_4'],
]


# # Streamlit UI
# st.title("Carnatic Music Tutor")

# # Sarali Swaras Section
# st.title("Sarali Swaras")
# for i, sequence in enumerate(sarali_sequences, start=1):
#     st.subheader(f"Please play {sequence}")
#     audio_file = st.file_uploader(f"Upload audio file for Sequence {i}", key=f"sarali_audio_{i}", type=["wav"])
#     if audio_file is not None:
#         analyze_audio(sequence, audio_file)

# # Dhatu Swaras Section
# st.title("Dhatu Swaras")
# for i, sequence in enumerate(dhatu_sequences, start=1):
#     st.subheader(f"Please play {sequence}")
#     audio_file = st.file_uploader(f"Upload audio file for Sequence {i}", key=f"dhatu_audio_{i}", type=["wav"])
#     if audio_file is not None:
#         analyze_audio(sequence, audio_file)


# Streamlit UI
st.set_page_config(page_title="Carnatic Music Tutor🎵", page_icon="🎵")
st.title("Carnatic Music Tutor")
st.markdown(
    """<style>
    .main-title {
        color: #ff5733;
        text-align: center;
        font-size: 36px;
        margin-bottom: 30px;
    }
    .sub-header {
        color: #4CAF50;
        font-size: 24px;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .upload-section {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>""",
    unsafe_allow_html=True
)

# Sarali Swaras Section
st.title("Sarali Swaras🎵")
for i, sequence in enumerate(sarali_sequences, start=1):
    st.subheader(f"{sequence}")
    with st.container():
        st.info(f"Please listen to the guide audio and then play {sequence}")
        st.audio("pages\sarali{i}.wav", format="audio/wav")
        audio_file = st.file_uploader(f"Upload audio file", key=f"sarali_audio_{i}", type=["wav"])
        
        if audio_file is not None:
            analyze_audio(sequence, audio_file)
    st.text("")
# Dhatu Swaras Section
st.title("Dhatu Swaras🎵")
for i, sequence in enumerate(dhatu_sequences, start=1):
    st.subheader(f"{sequence}")
    with st.container():
        st.info(f"Please listen to the guide audio and then play {sequence}")
        st.audio("pages\srsrsrgm.wav", format="audio/wav")
        audio_file = st.file_uploader(f"Upload audio file", key=f"dhatu_audio_{i}", type=["wav"])
        if audio_file is not None:
            analyze_audio(sequence, audio_file)