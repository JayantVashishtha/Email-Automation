import smtplib
import pandas as pd
from email.message import EmailMessage
import time
import os

# 1. Load emails from Excel
df = pd.read_excel("/content/Nikunj list.xlsx")
email_list = df['Email'].dropna().tolist()[450:900]  # Limit to 450 emails

# 2. Load previous log if exists to skip already sent emails
log_path = "email_log.csv"
if os.path.exists(log_path):
    log_df = pd.read_csv(log_path)
    sent_emails = log_df[log_df['status'] == 'Sent']['email'].tolist()
else:
    log_df = pd.DataFrame(columns=["email", "status", "error_message"])
    sent_emails = []

# 3. Email body
email_body = f"""
Dear Hiring Team,

I am Jayant Vashishtha, a final-year B.Tech student in Computer Science and Engineering at Hindustan College of Science and Technology, Agra. I am writing to express my keen interest in internship or full-time opportunities in the field of Artificial Intelligence, Machine Learning, and Deep Learning.

Highlights of my AI/ML/DL background include:

Research Internship at C-DAC: Worked on enhancing water body detection from satellite imagery using the YOLO object detection model. This project involved hands-on experience with QGIS and remote sensing data, combining geospatial analysis with deep learning techniques.

Technical Proficiency: Proficient in Python, Deep Learning frameworks (TensorFlow, Keras, PyTorch), and foundational ML concepts including supervised and unsupervised learning, CNNs, and object detection.

Applied Experience: My project focuses on the Detection and Classification of Degenerative Lumbar Spine Conditions using MRI images with CNN and YOLO models, demonstrating real-world application of deep learning in the medical domain.

I am passionate about solving challenging problems using data-driven approaches and eager to contribute to impactful AI/ML projects. I would welcome the opportunity to bring my technical and research skills to your team.

Thank you for considering my application. I look forward to the opportunity to contribute and grow within your organization.

Best regards,
Jayant Vashishtha
Phone: +91 9084999456
email: jayantvashishtha.work@gmail.com
LinkDIn: https://www.linkedin.com/in/jayantvashishtha/
"""

# 4. Resume path
resume_path = "/content/Resume.pdf"

# 5. Gmail credentials
EMAIL_ADDRESS = 'jayantvashishtha.work@gmail.com'
EMAIL_PASSWORD = 'roslftofjtosidyk'  # App-specific password

# 6. Function to send email
def send_email(to_email):
    msg = EmailMessage()
    msg['Subject'] = 'Internship/Full-Time Application –AI/ML/DL Roles'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(email_body)

    # Attach resume
    with open(resume_path, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename="Resume.pdf")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# 7. Sending loop with log
for email in email_list:
    if email in sent_emails:
        print(f"⏭️ Skipped (already sent): {email}")
        continue

    try:
        send_email(email)
        print(f"✅ Email sent to {email}")
        log_df = pd.concat([log_df, pd.DataFrame([{
            'email': email, 'status': 'Sent', 'error_message': ''
        }])], ignore_index=True)
    except Exception as e:
        print(f"❌ Failed to send to {email}. Error: {e}")
        log_df = pd.concat([log_df, pd.DataFrame([{
            'email': email, 'status': 'Failed', 'error_message': str(e)
        }])], ignore_index=True)

    # Save log after each attempt to prevent loss in case of interruption
    log_df.to_csv(log_path, index=False)
    time.sleep(5)  # Delay to avoid spam detection
