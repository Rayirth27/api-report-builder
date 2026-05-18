# API Report Builder

Python tool that authenticates to REST APIs, parses JSON responses, and writes structured CSV reports.

## What it does
- Calls NASA APOD API with API key authentication
- Simulates Bearer token auth
- Parses JSON response
- Writes vertical CSV report automatically

## How to run
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Copy .env.example to .env and add your keys
4. Run: python main.py
5. Optional date: python main.py 2026-01-01

## Environment Variables
NASA_API_KEY — from api.nasa.gov