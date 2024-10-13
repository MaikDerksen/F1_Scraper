# F1 News Scraper and Summarizer

## Overview
This project is a Python-based scraper that collects the latest Formula 1 news articles from [Motorsport Magazin](https://www.motorsport-magazin.com/formel1/news.html), summarizes the content using the Cohere language model, and sends the summarized text via WhatsApp using Twilio.

### Key Features
- **Web scraping**: Collects F1 articles from the web.
- **Text Summarization**: Uses Cohere's LLM to generate summaries of the scraped content.
- **WhatsApp Notifications**: Sends the summary via WhatsApp using Twilio's API.
- **Modular structure**: Components for scraping, summarization, and message delivery are separated for easy customization.

---

## Installation

### Prerequisites
- Python 3.8+
- A virtual environment (optional but recommended)
- A Cohere account and API key
- A Twilio account and credentials (with WhatsApp sandbox enabled)
  
# Setup

**Clone the repository**:
   ```bash
   git clone https://github.com/MaikDerksen/F1_Scraper.git
   cd F1_Scraper
   ```

# Create and activate a virtual environment:
```bash
python -m venv venv

source venv/bin/activate  # For Linux/Mac

venv\Scripts\activate      # For Windows
```
# Dependencies
- Cohere for language model API (cohere-py)
- Twilio for WhatsApp message delivery (twilio)
- BeautifulSoup for scraping (beautifulsoup4)
- Requests for HTTP requests (requests)
- python-dotenv for environment variables management (python-dotenv)
- tqdm for displaying progress bars (tqdm)
Install all dependencies using:

# Install the dependencies:
```bash
pip install -r requirements.txt
```

# Set up environment variables:
Create a `.env` file 
```
COHERE_API_KEY=your_cohere_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+your_phone_number
```

# Usage
Run Locally
Run the scraper and summarizer: The main script scrapes the latest F1 articles, summarizes them, and sends the summary via WhatsApp.

```bash
python main.py
```
Track progress: The script provides step-by-step progress messages and uses a progress bar to show the LLM summarization progress.

# Output:

Summaries are saved in the summaries/ folder.
Summaries are sent to your WhatsApp using the Twilio API.
Docker Setup
You can run the entire project using Docker to avoid dealing with dependencies manually.

# Build the Docker image:

```bash
docker build -t f1_scraper .
```
Run the Docker container: After the image is built, run the container using the following command:

```bash
docker run --env-file .env f1_scraper
```
Run in Detached Mode (optional): To run the container in detached mode (in the background), use:

```bash
docker run -d --env-file .env f1_scraper
```
Docker Tips
If you update the code or dependencies, you need to rebuild the image:

```bash
docker build -t f1_scraper .
```
If you want to stop the running Docker container:

```bash
docker ps  # Find the container ID
docker stop <container_id>
Project Structure
```

```bash
F1_Scraper/
│
├── LLM.py                  # Handles text summarization using Cohere
├── Scraper.py              # Scrapes articles from the website
├── message.py              # Sends summaries via Twilio's WhatsApp API
├── Summarize.py            # Handles file reading and finding the latest article
├── main.py                 # Orchestrates the whole process
├── requirements.txt        # List of dependencies
├── Dockerfile              # Docker configuration file
├── .dockerignore           # Files to ignore when building Docker image
├── .env                    # Environment variables (excluded from Git)
└── README.md               # Project documentation
```

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact
For questions, reach out to the project creator:

Maik Derksen
GitHub: MaikDerksen

