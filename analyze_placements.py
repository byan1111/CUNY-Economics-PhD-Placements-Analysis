from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

DATA_FILE = Path("data/cuny_graduate_center_economics_phd_placements.csv")


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def main() -> None:
    rows = load_rows(DATA_FILE)

    if not rows:
        print("No placement rows found yet.")
        return

    year_counts = Counter(row["graduation_year"] for row in rows if row.get("graduation_year"))
    placement_counts = Counter(row["placement_institution"] for row in rows if row.get("placement_institution"))

    print("Institution: CUNY Graduate Center")
    print("Program: Economics PhD")
    print(f"Total candidates: {len(rows)}")

    print("\nPlacements by graduation year:")
    for year, count in sorted(year_counts.items()):
        print(f"- {year}: {count}")

    print("\nTop placement institutions:")
    for placement, count in placement_counts.most_common(10):
        print(f"- {placement}: {count}")

    print("\nCandidate job market papers:")
    for row in sorted(rows, key=lambda r: (r.get("graduation_year", ""), r.get("candidate_name", ""))):
        print(
            f"- {row.get('graduation_year', '')} | {row.get('candidate_name', '')} | "
            f"{row.get('placement_institution', '')} | {row.get('job_market_paper_title', '')}"
        )


if __name__ == "__main__":
    main()
