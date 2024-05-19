import streamlit as st
import os

st.markdown(
    """
    <style>
    .stButton button {
        background-color: #007bff; 
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .stButton button:hover {
        background-color: #0069d9; 
    }

    .stTextArea textarea {
        font-family: monospace; 
        width: 100%;
        height: 200px;
    }

    .total-items {
        font-size: 24px;
        color: green;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True,
)



if st.button('Crawl data'):
    os.system('cd laptopCrawler && python aps_crawl.py')

# Read and display crawl status
status_log_path = './database/crawl_status_log.txt'
total_items = 0
crawl_success = False
total_duration = "0:00:00.000000"

# Update parse_items_scraped to also check for success status
def parse_items_scraped(line):
    global crawl_success  # Declare crawl_success as global
    try:
        if "Crawl success" in line:
            crawl_success = True
            return 0  # We don't need to extract numbers from this line
        else:
            # Split the line and get the second-to-last element which should be the number
            parts = line.split()
            num_items = int(parts[-3])
            return num_items
    except (IndexError, ValueError) as e:
        print(f"Error parsing line: {line} - {e}")
        return 0

# Update the duration parsing logic
def parse_duration(line):
    global total_duration
    if "Total duration:" in line:
        total_duration = line.split(":")[-1].strip()
    else:
        return None

if os.path.exists(status_log_path):
    with open(status_log_path, 'r') as f:
        status_log = f.readlines()

    for line in status_log:
        items_scraped = parse_items_scraped(line)
        print(f"Parsed items: {items_scraped} from line: {line}")
        total_items += items_scraped
        parse_duration(line)

    st.text_area('Status Log', "".join(status_log))
    st.markdown(f'<p class="total-items">Total Items Scraped: {total_items}</p>', unsafe_allow_html=True)

    if crawl_success:
        st.success("Crawl Success!")
        st.markdown(f'<p class="total-items">Total Duration: {total_duration} (s)</p>', unsafe_allow_html=True)

else:
    st.write("No crawl status available.")

if st.button('Preprocess filename'):
    os.system('cd database && python process_filename.py')
    st.success("Preprocess filename Success!")

if st.button('Preprocess data'):
    os.system('cd preprocessing && python preprocessing.py')
    st.success("Preprocess data Success!")


