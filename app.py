import streamlit as st

# Data: Major operation budgets for USA, UK, India, and Pakistan
operation_budgets = {
    "USA": {
        "Heart Surgery": 60000,
        "Knee Replacement": 35000,
        "Appendix Removal": 15000,
        "Organ Transplant": 120000,
        "Cancer Treatment": 90000,
        "Brain Surgery": 80000,
        "Spinal Surgery": 50000,
    },
    "UK": {
        "Heart Surgery": 40000,
        "Knee Replacement": 25000,
        "Appendix Removal": 12000,
        "Organ Transplant": 100000,
        "Cancer Treatment": 75000,
        "Brain Surgery": 60000,
        "Spinal Surgery": 35000,
    },
    "India": {
        "Heart Surgery": 8000,
        "Knee Replacement": 6000
