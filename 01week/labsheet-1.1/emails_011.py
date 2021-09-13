#!/usr/bin/env python3

import sys

for email in sys.stdin:
  email = email.strip()
  dcu_email = "@mail.dcu.ie"
  if dcu_email in email:
    email = email.replace(dcu_email, "")
    email = "".join([i for i in email if not i.isdigit()])
    email = email.split(".")
    name = email[0] + " " + email[1]
    print (name.title())
