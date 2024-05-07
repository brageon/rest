#!/bin/bash
DL="https://o66rembza0myxeg.lambda-url.eu-north-1.on.aws/"
message="Your message content was awesome here"
curl -X POST -H "Content-Type: text/plain" -d "$message" "$DL"
curl https://ddarwin.s3.eu-north-1.amazonaws.com/dove.txt
# Run this on Termux after rooting Android. Not working in Redmi.
# This setup is ETL. Learn more in repo debt. Mighty repo oak as SaaS.