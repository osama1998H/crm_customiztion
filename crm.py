lead_score = 0

if doc.source:
    lead_score = lead_score + 10

if doc.industry:
    lead_score = lead_score + 20

if doc.market_segment:
    lead_score = lead_score + 30

# Update the lead score field
doc.lead_score = lead_score
