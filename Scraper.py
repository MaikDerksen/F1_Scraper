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

    # Ensure the 'results' folder exists
    if not os.path.exists('results'):
        os.makedirs('results')

    # Open the file to write the full content
    file_path = f'results/MSM_{date_str}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        
        # Loop through all articles
        for article in articles:
            # Find the first anchor tag (the article link)
            link = article.find("a")
            if link and "href" in link.attrs:
                # Extract the href (URL) and build the full URL if needed
                article_url = link["href"]
                if not article_url.startswith("http"):
                    article_url = "https://www.motorsport-magazin.com" + article_url

                # Fetch the article page
                article_page = requests.get(article_url)
                print(f"Article page request status: {article_page.status_code} - {article_url}")
                
                # Parse the article page
                article_soup = BeautifulSoup(article_page.text, "html.parser")

                # Find the header (h2) and paragraphs (p) in the article
                article_header = article_soup.find("h2").get_text() if article_soup.find("h2") else "No header found"
                article_content = [p.get_text() for p in article_soup.find_all("p")]

                # Combine the article content into a single string
                full_content = article_header + "\n" + "\n".join(article_content)

                # Write the full content to the file
                file.write(f"Header: {article_header}\n")
                file.write("Content:\n")
                file.write(full_content + "\n")
                file.write("\n---\n")

    return file_path