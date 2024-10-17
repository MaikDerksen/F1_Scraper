# LLM.py
import torch
from transformers import pipeline
from tqdm import tqdm  # Progress bar for sections
#max tokens 2048
# Initialize the TinyLlama model pipeline
pipe = pipeline("text-generation", 
                model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
                torch_dtype=torch.bfloat16, 
                device_map="auto")

def summarize_content_with_tinyllama(content):
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

                # Prepare the prompt using the chat template
                messages = [
                    {"role": "system", "content": "You are a helpful summarization bot."},
                    {"role": "user", "content": f"Summarize the following text into key points:\n\n{body}"}
                ]
                prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

                # Generate summary using TinyLlama
                outputs = pipe(prompt, max_new_tokens=150, do_sample=True, temperature=0.5)
                summary_points = outputs[0]["generated_text"].strip()

                # Append the header and summary points to the final summary
                final_summary += f"{header}\n{summary_points}\n\n"

                # Update progress bar
                pbar.update(1)

        return final_summary.strip()
    
    except Exception as e:
        return f"Error during summarization: {e}"