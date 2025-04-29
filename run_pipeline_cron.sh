#!/bin/bash

# Debugging start
echo "=== CRON JOB START ===" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt
echo "Current Time: $(date)" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt
echo "Current User: $(whoami)" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt
echo "Current Directory: $(pwd)" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt
echo "PATH: $PATH" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt

# Step 1: Go to project directory
cd /Users/atishdhamala/currency_pipeline_project
echo "Changed to project directory." >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt

# Step 2: Activate virtual environment
source currency_enc/bin/activate
echo "Activated virtual environment." >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt

# Step 3: Print python version
python3 --version >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt

# Step 4: Run the ETL pipeline
/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 run_pipeline.py >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt 2>&1

echo "=== CRON JOB END ===" >> /Users/atishdhamala/currency_pipeline_project/logs/cron_debug_log.txt
