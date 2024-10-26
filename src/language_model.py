import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from tqdm import tqdm  # For progress display

# Load API key from environment variables
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Initialize the client with the API key
client = InferenceClient(api_key=HF_API_KEY)

def summarize_content_by_header(content: str):

    # Split the content into sections by the "Header" keyword
    sections = content.split("Header:")

    # Initialize the final summary
    final_summary = ""

    # Progress bar for section processing
    with tqdm(total=len(sections), desc="Summarizing sections") as pbar:
        for section in sections:
            if not section.strip():  # Skip empty sections
                pbar.update(1)
                continue

            # Extract the header and body from the section
            lines = section.strip().split('\n')
            header = lines[0].strip() if lines else "No Header"
            body = '\n'.join(lines[1:])

            # Create the message for summarization
            messages = [
                {
                "role": "user", 
                "content": f"Please summarize the following section using the exact format:\n\n"
                    f"{{Header}}\n"
                    f"- Key point 1...\n"
                    f"- Key point 2...\n"
                    f"- Key point 3...\n\n"
                    f"Only include the header and key points without any extra text or explanation.\n\n"
                    f"Text to summarize:\n\n{body}"
                }
            ]




            # Stream the summarization response
            stream = client.chat.completions.create(
                model="meta-llama/Meta-Llama-3-8B-Instruct",
                messages=messages,
                max_tokens=150,
                stream=True
            )

            # Collect the streamed output
            summary_points = ""
            for chunk in stream:
                summary_points += chunk.choices[0].delta.content

            # Append the header and summary to the final output
            final_summary += f"Header: {header}\n{summary_points.strip()}\n\n"

            # Update the progress bar
            pbar.update(1)

    return final_summary.strip()
