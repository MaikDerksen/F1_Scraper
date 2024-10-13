# main.py
import os
import time
from scraper import scrape_articles
from language_model import summarize_content_with_cohere
from summarize import read_latest_file
from send_message import send_whatsapp_messageT

def summarize_latest_file():
    # Step 1: Scraping the latest articles
    print("Step 1: Scraping the latest articles...")
    start_time = time.time()  # Start timing
    latest_file = scrape_articles()
    end_time = time.time()  # End timing
    print(f"Step 1 completed in {end_time - start_time:.2f} seconds.")

    # Step 2: Reading the content from the latest file
    print(f"Step 2: Reading the content from {latest_file}...")
    start_time = time.time()  # Start timing
    content = read_latest_file(latest_file)
    end_time = time.time()  # End timing
    print(f"Step 2 completed in {end_time - start_time:.2f} seconds.")

    # Step 3: Generating a summary using Cohere API
    print("Step 3: Generating a summary using Cohere API...")
    start_time = time.time()  # Start timing
    summary = summarize_content_with_cohere(content)
    end_time = time.time()  # End timing
    print(f"Step 3 completed in {end_time - start_time:.2f} seconds.")

    # Define the directory for the summaries
    summary_dir = 'summaries'

    # Step 4: Saving the summary to a file
    print(f"Step 4: Saving the summary to a file in {summary_dir}...")
    start_time = time.time()  # Start timing
    os.makedirs(summary_dir, exist_ok=True)
    summary_filename = os.path.join(summary_dir, latest_file.replace("MSM_", "summary_MSM_"))

    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write(summary)
    end_time = time.time()  # End timing
    print(f"Step 4 completed in {end_time - start_time:.2f} seconds.")

    # Step 5: Sending summary via WhatsApp
    print(f"Step 5: Sending summary via WhatsApp...")
    start_time = time.time()  # Start timing
    send_whatsapp_messageT(summary_filename)
    end_time = time.time()  # End timing
    print(f"Step 5 completed in {end_time - start_time:.2f} seconds.")

    print(f"Summary saved to: {summary_filename}")

# Run the summarize process
if __name__ == "__main__":
    summarize_latest_file()
