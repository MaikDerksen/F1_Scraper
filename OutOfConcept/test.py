from mail_sender import send_email
import time   
import os
gmail_user = os.getenv('GMAIL')
gmail_password = os.getenv('GMAIL_APP')
to_email = os.getenv('GMAIL')

print(f"GMAIL_USER: {gmail_user}")
print(f"GMAIL_APP: {gmail_password}")
print(f"TO_EMAIL: {to_email}")


print(f"Step 5: Sending summary via Gmail...")
start_time = time.time()  # Start timing
send_email("results\MSM_17_10_2024.txt")
end_time = time.time()  # End timing
print(f"Step 5 completed in {end_time - start_time:.2f} seconds.")