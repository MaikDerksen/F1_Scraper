# main.py
import os
from Scraper import scrape_articles
from LLM import summarize_content_with_cohere
from Summarize import find_latest_file, read_latest_file
from send_message import send_whatsapp_messageT

def summarize_latest_file():
    print("Step 1: Scraping the latest articles...")
    latest_file = scrape_articles()

    print(f"Step 2: Reading the content from {latest_file}...")
    content = read_latest_file(latest_file)

    print("Step 3: Generating a summary using Cohere API...")
    summary = summarize_content_with_cohere(content)

    # Define the directory for the summaries
    summary_dir = 'summaries'

    print(f"Step 4: Saving the summary to a file in {summary_dir}...")
    os.makedirs(summary_dir, exist_ok=True)
    summary_filename = os.path.join(summary_dir, latest_file.replace("MSM_", "summary_MSM_"))

    with open(summary_filename, 'w', encoding='utf-8') as summary_file:
        summary_file.write(summary)

    print(f"Step 5: Sending summary via WhatsApp...")
    send_whatsapp_messageT(summary_filename)

    print(f"Summary saved to: {summary_filename}")

# Run the summarize process
if __name__ == "__main__":
    summarize_latest_file()
