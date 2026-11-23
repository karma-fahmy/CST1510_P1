"""
RECORD CHECK  -  my version
===========================

Name  : Karmah Abdelrahman Mohamed Lotfy Abdellatif fahmy
Lane  : Cyber
Date  : 11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    fields = {}
    for p in raw_line.strip().split(","):
        key, value = p.split("=")
        fields[key.strip().lower()] = value.strip().lower()

    return {"src": fields["src"], "attempts": int(fields["attempts"]), "result": fields["result"]}
    
def status_of(record):
     if record["result"] == "failed" and record["attempts"] >= 10:
        return "FLAGGED"
     return "OK"

# ====================================================================== INPUT

raw_records = []

with open("mp_messy.txt") as f:
    for raw_line in f:
        if raw_line.strip():
            raw_records.append(raw_line)

# =============================================================== PROCESS + OUTPUT

flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    if status == "FLAGGED":
        flagged_count += 1

    print(record, ':', status)

print(f'\n{len(raw_records)} records printed, {flagged_count} of which are flagged')

