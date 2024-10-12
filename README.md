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
  
### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MaikDerksen/F1_Scraper.git
   cd F1_Scraper

# Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate      # For Windows

# Install the dependencies:
pip install -r requirements.txt

# Set up environment variables:
COHERE_API_KEY=your_cohere_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+your_phone_number