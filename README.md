# 💱 Fully Automated Currency ETL Pipeline Project

A fully automated ETL (Extract, Transform, Load) pipeline for fetching, transforming, and loading real-time currency exchange rate data into a PostgreSQL database. Designed with production-readiness in mind using Python, pandas, SQLAlchemy, GitHub Actions for automated scheduling to Supasbase PostgreSQL database, and launchd for manual local scheduling. 

---

## 📌 Features

- ✅ Fetches daily currency exchange rates from a public API
- ✅ Transforms raw JSON into structured tabular format using `pandas`
- ✅ Loads cleaned data into a PostgreSQL database via `SQLAlchemy` and automated scheduling to Supabase Database using `GitHub Actions`.
- ✅ Supports both local (macOS `launchd`) and cloud automation (`GitHub Actions`)
- ✅ Uses `.env` and GitHub Secrets for secure credential management

---

## 🛠 Tech Stack

| Layer        | Tools/Libraries                 |
|--------------|----------------------------------|
| Language     | Python, SQL                      |
| Data Wrangling | `pandas`, `requests`           |
| Database     | PostgreSQL,Supabase, `SQLAlchemy`, `psycopg2` |
| Automation   | GitHub Actions, macOS `launchd` |
| Secrets Mgmt | `.env`, `python-dotenv`         |

---

## 📂 Project Structure
<pre> 
currency-etl-pipeline/
├── .github/                    # GitHub Actions workflows
│   └── workflows/
│       └── etl_pipeline.yml    # CI pipeline for daily ETL runs
│
├── pipeline/                   # ETL components
│   ├── fetch_api.py            # Extracts data from currency API
│   ├── transform_data.py       # Transforms raw JSON into structured format
│   ├── validate_data.py        # Validates and filters data
│   └── load_to_db.py           # Loads cleaned data into PostgreSQL
│
├── run_pipeline.py             # Main entry point to run the ETL job
├── run_pipeline_cron.sh        # Shell script for local cron scheduling
│
├── test_fetch.py               # Unit test for fetch_api.py
├── test_validate.py            # Unit test for validate_data.py
├── test_pipeline.py            # End-to-end pipeline test
│
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore .env, bytecode, logs, etc.
└── README.md                   # Project documentation

 </pre>


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Adh101/currency-etl-pipeline.git
cd currency-etl-pipeline
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Configure .env
```bash
API_KEY=your_api_key_here
API_URL=https://api.exchangerate-api.com/v4/latest/USD
DB_URI=postgresql+psycopg2://user:password@localhost:5432/yourdb
```
### 4. Run the pipeline
```bash
python run_pipeline.py
```
## 🗓️ Schedule the Pipeline
### Option A: GitHub Actions (Cloud)
- Set up the PostgresSQL database at Supabase.
- CI/CD pipeline runs daily at 6 AM UTC.
- Secrets like API_KEY and DB_URI are stored in GitHub Secrets.
Note: See .github/workflows/etl_pipeline.yml

### Option B: Local Setup via `launchd` (macOS Scheduler)
- Copy the com.currency.etl.plist to ~/Library/LaunchAgents/
- Load the job:
 ```bash
launchctl load ~/Library/LaunchAgents/com.currency.etl.plist
```
- Confirm it’s scheduled:
 ```bash
launchctl list | grep currency
```

## 🧪 Example Output
The pipeline loads data into a PostgreSQL table such as:

| date       | base\_currency | target\_currency | exchange\_rate |
| ---------- | -------------- | ---------------- | -------------- |
| 2025-07-13 | USD            | EUR              | 0.922          |
| 2025-07-13 | USD            | JPY              | 138.24         |

## 📖 Blog
Read the full tutorial on Medium:
[📚 Learning ETL with APIs – A Hands-on Journey into Data Engineering](https://medium.com/@atish.dhamala/learning-etl-with-apis-a-hands-on-journey-into-data-engineering-b11ef5fbde16)




