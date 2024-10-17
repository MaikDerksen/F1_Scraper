import os
import time
from scraper import scrape_articles
from summarize import read_latest_file
from language_model import summarize_content_with_tinyllama
from mail_sender import send_email

def summarize_latest_file():
    # Step 1: Scraping the latest articles and saving in 'results' folder
    print("Step 1: Scraping the latest articles...")
    start_time = time.time()  # Start timing
    latest_file = scrape_articles()  # The file will be saved in the 'results' folder in the root project directory
    end_time = time.time()  # End timing
    print(f"Step 1 completed in {end_time - start_time:.2f} seconds.")

    # Step 2: Reading the content from the latest file in 'results' folder
    print(f"Step 2: Reading the content from {latest_file}...")
    start_time = time.time()  # Start timing
    content = read_latest_file(latest_file)
    end_time = time.time()  # End timing
    print(f"Step 2 completed in {end_time - start_time:.2f} seconds.")

    # Step 3: Generating a summary using TinyLlama
    print("Step 3: Generating a summary using TinyLlama...")
    start_time = time.time()  # Start timing
    summary = summarize_content_with_tinyllama(content)
    end_time = time.time()  # End timing
    print(f"Step 3 completed in {end_time - start_time:.2f} seconds.")

    # Define the directory for the summaries (root directory 'summaries/')
    summary_dir = 'summaries'

    # Step 4: Ensure the 'summaries' directory exists
    print(f"Step 4: Saving the summary to a file in {summary_dir}...")
    start_time = time.time()  # Start timing
    os.makedirs(summary_dir, exist_ok=True)

    # Construct a new filename for the summary without any reference to 'results'
    base_filename = os.path.basename(latest_file)  # Get the base filename like 'MSM_13_10_2024.txt'
    summary_filename = os.path.join(summary_dir, base_filename.replace("MSM_", "summary_MSM_"))  # Change prefix to 'summary_MSM_'

    # Write the summary to the 'summaries' folder
    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write(summary)
    end_time = time.time()  # End timing
    print(f"Step 4 completed in {end_time - start_time:.2f} seconds.")

    # Step 5: Sending the summary via Gmail
    print(f"Step 5: Sending summary via Gmail...")
    start_time = time.time()  # Start timing
    send_email(summary_filename)
    end_time = time.time()  # End timing
    print(f"Step 5 completed in {end_time - start_time:.2f} seconds.")

    print(f"Summary saved to: {summary_filename}")

# Run the summarize process
if __name__ == "__main__":
    summarize_latest_file()
