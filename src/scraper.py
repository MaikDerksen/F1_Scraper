import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_articles():
    # URL of the news page
    url = "https://www.motorsport-magazin.com/formel1/news.html"

    # Request the main page
    page = requests.get(url)
    print(f"Main page request status: {page.status_code}")

    # Parse the page
    soup = BeautifulSoup(page.text, "html.parser")

    # Find all articles
    articles = soup.find_all("article")

    # Get the current date for file naming
    now = datetime.now()
    date_str = now.strftime("%d_%m_%Y")

    # Ensure the 'results' and 'websites' folders exist
    os.makedirs('results', exist_ok=True)
    os.makedirs('websites', exist_ok=True)

    # Open the file to write the full content
    file_path = f'results/MSM_{date_str}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        # Open the log file for the websites
        log_path = f'websites/log_{date_str}.txt'
        with open(log_path, 'w', encoding='utf-8') as log_file:
            # Loop through all articles
            for article in articles:
                # Find the first anchor tag (the article link)
                link = article.find("a")
                if link and "href" in link.attrs:
                    # Extract the href (URL) and build the full URL if needed
                    article_url = link["href"]
                    if "bilder" in article_url:
                        continue
                    if "video" in article_url:
                        continue
                    if not article_url.startswith("http"):
                        article_url = "https://www.motorsport-magazin.com" + article_url

                    # Fetch the article page
                    article_page = requests.get(article_url)
                    status_code = article_page.status_code  # Save the status code

                    # Log the URL and status code to the log file
                    log_file.write(f"Status: {status_code} - {article_url}\n")

                    print(f"Article page request status: {status_code} - {article_url}")

                    # Parse the article page
                    article_soup = BeautifulSoup(article_page.text, "html.parser")

                    # Remove the "Kommentare" section and any other unwanted sections
                    if article_soup.find("section", class_="additionals"):
                        article_soup.find("section", class_="additionals").decompose()  # Remove the comments section

                    # Remove the "Newsletter" section (and any other content in the footer)
                    if article_soup.find("footer"):
                        article_soup.find("footer").decompose()  # Remove the entire footer

                    # Check if the page has a header and extract it, otherwise handle missing header
                    article_header = article_soup.find("h1") or article_soup.find("h2")
                    if article_header:
                        article_header_text = article_header.get_text().strip()
                    else:
                        article_header_text = "No header found"

                    # Extract content paragraphs and remove unwanted ones like "Newsletter"
                    article_content = [p.get_text().strip() for p in article_soup.find_all("p") if "Newsletter" not in p.get_text()]

                    # Combine the article content into a single string
                    full_content = article_header_text + "\n" + "\n".join(article_content)

                    # Remove any unwanted footer text
                    unwanted_footer_markers = [
                        "© Motorsport-Magazin",
                        "AnmeldenRegistrierenJetzt Plus-Vorteile"
                    ]

                    # Remove any part of the content after an unwanted footer marker is found
                    for marker in unwanted_footer_markers:
                        if marker in full_content:
                            full_content = full_content.split(marker)[0]

                    # Write the filtered content to the file
                    file.write(f"Header: {article_header_text}\n")
                    file.write("Content:\n")
                    file.write(full_content.strip() + "\n")
                    file.write("\n---\n")

    return file_path