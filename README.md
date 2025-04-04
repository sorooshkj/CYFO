# Email Processing Instructions

## Stage 1: Load Email Files
1. Navigate to the folder `./spam/` that contains all `.eml` email files.
2. Loop through all `.eml` files and read them using the `email` module.

---

## Stage 2: Filter for CYFO INC Recipients
For each email:
1. Retrieve the `To:` address.
2. Check if the address ends with `@find the cyfo inc email`.
   - If it does, keep the email.
   
At the end of this stage, you will have a list of emails sent to CYFO INC employees.

---

## Stage 3: Extract the First Server from Headers
For each CYFO INC email:
1. Collect all `Received:` headers (there are usually many).
2. Identify the first sending server:
   - The first sending server is found in the **last** `Received:` header (email headers are reverse chronological).
   - If the last headers don’t contain IPs (e.g., spam filters), keep popping the last header until you find one with an IPv4 address.

---

## Stage 4: Extract Public IPs
From the valid `Received:` header:
1. Use a regex to find all IPv4 addresses (e.g., `192.168.1.1`, `34.71.206.167`).
2. For each IP:
   - Use `ipaddress.ip_address()` to validate it.
   - Skip it if it's a private IP (e.g., `10.x.x.x`, `192.168.x.x`, etc.).
   - If it’s public, add it to a set of unique IPs.

---

## Stage 5: Display Results
1. Sort the list of unique public IPs.
2. Print the results.
