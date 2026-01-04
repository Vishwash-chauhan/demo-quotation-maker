# Quotation Maker

Small n8n workflow + Python code to render event quotations as HTML/PDF.

## What this repo contains
- `workflow.example.json` — **sanitized** n8n workflow (credential ids replaced with `REDACTED`). Use this as a template to import into your n8n instance.
- `code.py` — Python code used in the n8n Code node to build the HTML quotation.
- `input.json` — sample input used for testing locally.
- `Untitled-1.html` — example generated HTML output.

## Safety & Secrets
- The checked-in example workflow has had credential ids and names replaced with `REDACTED`.
- Do NOT commit real credentials (API keys, client secrets, tokens) to this repository.
- This repo is safe to make public if you DO NOT add any files containing secrets. The `.gitignore` already excludes `workflow.json` and common secret files.

## Quick start
1. Import `workflow.example.json` into your n8n instance.
2. Recreate the credentials referenced by name in n8n (Google Sheets, PDF Noodle, etc.).
3. Run the workflow or use n8n's manual trigger.

## Public form
A static public form is included at `form.html`. It:
- Fetches the live **Master Menu** sheet from your Google Sheet (no API key required if the sheet is public)
- Provides a searchable checkbox list to select multiple items
- Builds an editable table where you enter `Pcs`; `Amount` is auto-calculated and the `Total` is shown
- Posts the final payload to an n8n Webhook (set the webhook URL in the form before submit)

To use the form:
1. Ensure the sheet "Master Menu" is published or shared publicly.
2. Edit `form.html` and set the `webhookUrl` field or paste your n8n webhook in the form UI.
3. Import `workflow.form.example.json` into n8n and update the Google Sheets credential and sheet id (values are REDACTED in the example).

## Git / Remote
To initialize locally and make the first commit (already done if you used the `Initialize` step in this repo):

```bash
cd "Quotation Maker"
# (optional) set user.name/user.email if git rejects commits
git config user.name "Your Name"
git config user.email "you@example.com"

# add a remote and push (example)
git remote add origin git@github.com:your-user/quotation-maker.git
git branch -M main
git push -u origin main
```

## Notes
- Use secret scanning tools (git-secrets, detect-secrets) before pushing public.
- If you ever accidentally commit secrets, rotate the credentials immediately.

---

If you want, I can initialize the repo locally and make the initial commit, or push it to a remote if you provide the remote URL/token.
