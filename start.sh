#!/bin/bash

# Start FastAPI backend in the background
echo "Starting FastAPI backend..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
echo "Starting Streamlit frontend..."
streamlit run app.py --server.port 7860 --server.address 0.0.0.0
