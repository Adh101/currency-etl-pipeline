# 💱 Currency ETL Pipeline

A fully automated ETL (Extract, Transform, Load) pipeline for fetching, transforming, and loading real-time currency exchange rate data into a PostgreSQL database. Designed with production-readiness in mind using Python, pandas, SQLAlchemy, GitHub Actions, and launchd for scheduling.

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
│
├── extract.py              # Script to extract currency data from API
├── transform.py            # Cleans and reshapes the extracted data
├── load.py                 # Loads transformed data into PostgreSQL
├── config.py               # Loads environment variables and DB URI
├── run_pipeline.py         # Orchestrates the ETL pipeline
├── requirements.txt        # Python package dependencies
├── .env                    # Local environment variables (excluded from Git)
├── .gitignore              # Files/folders to ignore in Git
│
├── launchd/
│   └── com.currency.etl.plist     # macOS LaunchAgent for local scheduling
│
├── .github/
│   └── workflows/
│       └── etl_pipeline.yml       # GitHub Actions CI workflow
│
└── README.md              # Documentation for the project
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




