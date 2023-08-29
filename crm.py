# This code works on server script inside the frappe framework
# event => before_save
# doctype => lead

lead_score = 0

if doc.source:
    lead_score += 10

if doc.industry:
    lead_score += 20

if doc.market_segment:
    lead_score += 30

# Update the lead score field
doc.lead_score = lead_score
