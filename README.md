# Faceless Video Automation
Generates daily motivational videos and posts to YouTube, Facebook, Instagram. Uploads to Dropbox and prints a shareable link.
## Setup
1) Create `.env` from `.env.example` and fill credentials.
2) Install dependencies:
   ```bash
   pip install -r requirements.txt
Run once:
bash
python -m src.main --run-now
Scheduling (daily at 12:00 PM Pakistan)
Use Windows Task Scheduler to run:

bash
python -m src.main --run-now
Notes
TikTok is excluded for now (manual upload).
Dropbox link is generated after each run.
---
