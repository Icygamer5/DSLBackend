""" config.py 
This file centralizes configuration settings for the backend. 
If any files are moved or paths are changed update it 
here instead of editing multiple files
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Data", "final_country_funding_population.csv")