#!/usr/bin/env python3

import pathlib
import re
import ipaddress
import email
from email.policy import default as DEFAULT_POLICY
from tqdm import tqdm

# === Directory containing .eml files ===
spam_dir = pathlib.Path(".") / "spam"

# === Step 1: Find all email files ===
all_eml_paths = list(spam_dir.glob("*.eml"))

# === Step 2: Load emails into memory ===
all_eml = []
for path in tqdm(all_eml_paths, desc="Loading emails"):
    with path.open("rb") as f:
        msg = email.message_from_binary_file(f, policy=DEFAULT_POLICY)
        all_eml.append(msg)

# === Step 3: Filter only emails sent to CYFO INC ===
cyfoinc_emails = []
for eml in all_eml:
    # TODO: Extract the "To" field and check if it ends with "[find cyfo inc email]"
    pass

# === Step 4: Count CYFO emails ===
print("Q11: How many emails have been sent to CYFO INC?", "A:", len(cyfoinc_emails))

# === Step 5: Extract public IPs from the last Received header ===
sending_ips = set()
ipv4_re = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for eml in cyfoinc_emails:
    # TODO: Get all "Received" headers
    # TODO: Find the last one that contains a valid IP
    # TODO: Extract public IPs (ignore private ones)
    pass

# === Step 6: Display unique public IPs ===
print("Q13: What servers sent the emails (i.e. the first in the received-chain)?", "A:", sorted(sending_ips))
