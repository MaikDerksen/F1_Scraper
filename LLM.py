# LLM.py
import cohere
from tqdm import tqdm  # Add tqdm for progress bar

# Set up your Cohere API key
co = cohere.Client('X0fzsb3dji0CWtTMkYAJxexZ4gkU5eFOVDwSfypO')

def summarize_content_with_cohere(content):
    try:
        # Split content by topics (assuming headers start with "Header:")
        sections = content.split('Header:')
        
        # Initialize the final summary and progress bar
        final_summary = ""
        with tqdm(total=len(sections), desc="Summarizing sections") as pbar:
            for section in sections:
                if not section.strip():  # Skip empty sections
                    pbar.update(1)
                    continue

                # Extract the header (assumed to be the first line of the section)
                lines = section.strip().split('\n')
                header = lines[0].strip()  # The first line is the header
                body = '\n'.join(lines[1:])  # The rest is the body/content

                # Summarize the content
                response = co.generate(
                    model='command-xlarge-nightly',
                    prompt=f"Summarize the following text into key points:\n\n{body}",
                    max_tokens=150,
                    temperature=0.5
                )

                # Extract the summary text
                summary_points = response.generations[0].text.strip()

                # Append the header and summary points to the final summary
                final_summary += f"{header}\n{summary_points}\n\n"

                # Update progress bar
                pbar.update(1)

        return final_summary.strip()
    
    except Exception as e:
        return f"Error during summarization: {e}"
