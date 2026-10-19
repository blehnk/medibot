"""Copy the explicit supplied dataset allowlist into ignored local data/."""

import argparse
from pathlib import Path
from zipfile import ZipFile

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILES = (
    "billing/billing_codes.pdf",
    "billing/claim_submission_guide.md",
    "clinical/diagnostic_reference.pdf",
    "clinical/drug_formulary.pdf",
    "clinical/treatment_protocols.pdf",
    "equipment/equipment_manual.pdf",
    "general/code_of_conduct.pdf",
    "general/general_faqs.pdf",
    "general/leave_policy.pdf",
    "general/staff_handbook.pdf",
    "nursing/icu_nursing_procedures.pdf",
    "nursing/infection_control.pdf",
    "db/mediassist.db",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Path to the supplied mediassist_data.zip")
    args = parser.parse_args()
    destination = PROJECT_ROOT / "data" / "mediassist_data"
    with ZipFile(args.archive) as archive:
        # Validate every required entry and existing file before writing anything.
        payloads = {}
        for name in DATA_FILES:
            payload = archive.read("mediassist_data/" + name)
            target = destination / name
            if target.exists() and target.read_bytes() != payload:
                raise SystemExit(f"Refusing to overwrite differing local file: {target}")
            payloads[target] = payload
        for target, payload in payloads.items():
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(payload)
    print(f"Prepared {len(DATA_FILES)} allowlisted local files in {destination}")
    print("Dataset files are excluded from Git; original resources are unchanged.")


if __name__ == "__main__":
    main()
