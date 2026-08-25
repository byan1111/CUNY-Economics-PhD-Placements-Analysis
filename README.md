# CUNY-Economics-PhD-Placements-Analysis

This repository is used to analyze past candidates' placement records and job market papers.

## Current scope (stage 1)
- Institution: **CUNY Graduate Center**
- Program: **Economics PhD**

## Data file
Use the scoped dataset at:

`/home/runner/work/CUNY-Economics-PhD-Placements-Analysis/CUNY-Economics-PhD-Placements-Analysis/data/cuny_graduate_center_economics_phd_placements.csv`

Columns:
- `candidate_name`
- `graduation_year`
- `placement_institution`
- `placement_type`
- `job_market_paper_title`
- `job_market_paper_link`
- `source_link`

## Run the analysis
From the repository root:

```bash
python analyze_placements.py
```

The script summarizes:
- candidate count
- placements by graduation year
- top placement institutions
- candidate/job-market-paper listing
