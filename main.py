"""
main.py

This file defines. the FastAPI web server and API routes.
-Starts backend
-Configures CORS for frontend to fetch
-Loads dataset one time at startup
-Defines endpoints for data retrieval
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_processing import build_master_table, get_top_countries, get_country

app = FastAPI()

#Enable Cors for Frontend to fetch
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache data at startup
master_df = build_master_table()


@app.get("/")
def root():
    return {"message": "DSL Backend Running"}


@app.get("/data")
def get_all_data():
    return master_df.to_dict(orient="records")

#Returns top 10 countries by funding
@app.get("/top")
def get_top():
    top_df = get_top_countries(master_df, 10)
    return top_df.to_dict(orient="records")

#Returns data for a specific country using is ISO3 code.
@app.get("/country/{iso3}")
def get_single_country(iso3: str):
    result = get_country(master_df, iso3)
    return result.to_dict(orient="records")


@app.get("/refresh")
def refresh_data():
    global master_df
    master_df = build_master_table()
    return {"status": "Data refreshed"}