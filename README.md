
# 🚀 AI-Powered SEO Automation Workflow

## 👨‍💻 Created by Shivendra

---

## 📌 Overview

This project implements an **end-to-end AI-powered SEO automation workflow** built using n8n.

The system automatically:

* Collects real SEO-related data for YouTube
* Processes and analyzes ranking data
* Generates AI-driven insights using Google Gemini
* Stores historical results in Google Sheets
* Sends a formatted SEO report via Gmail

The workflow runs with minimal manual input and demonstrates **real-world SEO automation and AI-powered insight generation**.

---


## 📊 Generated Insight Report

(Attached separately in project submission)

---

## 🔎 Data Configuration

**Data Source:**
Google Search Console API

**Target Query:**

```
site:https://www.youtube.com/
```

**Automation Platform:**
n8n

**AI Model Used:**
Google Gemini

**Execution Date:**
Auto-generated per run

---

## 🗂 Historical Data Storage

### 📊 Google Sheets (Tracking)

Each workflow execution appends a new row including:

* Search query
* Total indexed results
* Average ranking position
* Top-ranking pages
* Extracted keywords
* Execution timestamp

---

## ⚙️ Workflow Architecture (Step-by-Step)

### 1️⃣ Trigger

* Manual trigger OR scheduled trigger
* Starts the workflow

---

### 2️⃣ Fetch SEO Data (API Request)

* Sends request to fetch SEO data
* Retrieves real-time ranking metrics

**Metrics Collected:**

* Search query
* Total indexed results
* Average ranking position
* Top ranking pages
* Keywords from snippets
* Timestamp

---

### 3️⃣ Data Processing & Transformation

* Converts API data into structured format

**Extracts:**

* Page URLs
* Ranking positions
* Snippets

**Performs:**

* Average ranking calculation
* Top pages identification
* Keyword frequency analysis
* Trend detection

---

### 4️⃣ AI Insights Generation (Gemini)

* Data is sent to Gemini AI

**AI generates:**

* Executive summary
* SEO performance analysis
* Actionable recommendations
* Ranking patterns
* Keyword insights

---

### 5️⃣ Data Storage (Google Sheets)

* Appends results to Google Sheets
* Enables historical tracking

---

### 6️⃣ Email Report (Gmail)

* Sends automated SEO report to:

📩 **[pr.shivendra.1747@gmail.com](mailto:pr.shivendra.1747@gmail.com)**

**Email includes:**

* Executive summary
* AI insights
* Top pages
* Keyword analysis
* Recommendations
* Timestamp

---

## 📈 Output Example

Each report contains:

* Query summary
* Total results
* Average ranking position
* AI analysis
* Top YouTube pages
* Keyword insights
* Recommendations
* Timestamp

---

## 🛠 Tools & Technologies Used

* Automation: n8n
* SEO Data: Google Search Console API
* Processing: JavaScript (inside n8n)
* AI: Google Gemini
* Storage: Google Sheets
* Email: Gmail

---

## ▶️ How to Run

1. Import `workflow.json` into n8n
2. Configure credentials:

   * Google APIs
   * Gmail
   * Gemini API key
3. Connect Google Sheets
4. Run workflow
5. Verify:

   * Data added to Google Sheets
   * Email received

---

## ⭐ Key Features

* Uses real SEO data
* Fully automated workflow
* AI-powered insights
* Historical tracking
* Minimal manual effort

---

## 📧 Contact

**Shivendra**
📩 [pr.shivendra.1747@gmail.com](mailto:pr.shivendra.1747@gmail.com)

---
