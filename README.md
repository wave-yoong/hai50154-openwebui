# HAI-5014 Open WebUI demo

Repo for the Open WebUI demo in class HAI5014

## Supabase

- Create new project in Supabase called `openwebui` [https://supabase.com/dashboard/](https://supabase.com/dashboard/)
- Copy `Session pooled (Shared Pooler)` connection string
- Save this connection string as `DATABASE_URL` and `PGVECTOR_DB_URL` environment variable (In Codespace settings, secrets & variables)

## Google Gemini API key
- Get your Google gemini API key [https://aistudio.google.com/app/apikeys](https://aistudio.google.com/app/apikeys)
- Save this API key as `OPENAI_API_KEY` environment variable (In Codespace settings, secrets & variables)

## Codespace
- Open repo in Codespaces (or Docker)
- Check if the environment variables are set correctly by running `echo $DATABASE_URL` and `echo $PGVECTOR_DB_URL`
- Run OpenWebUI with the command `dotenv run open-webui serve`

A pop-up should indicate that a webserver has launched. If not, click the "ports" tab in the terminal window, and open the website.

Walk trough the Open WebUI *get started* wizzard and create an admin account. Make sure to remember your password :)

### Additional settings

#### Standard model:
In the Open WebUI **admin panel**, go to Settings -> Models
- Click the gear icon on the upper right
- Scroll down to 'Default Models' and select a model (e.g. `gemini-2.5-flash-preview`)  

#### Embeddings model
In the Open WebUI **admin panel**, go to Settings -> Documents -> Embedding and change the following
- Embedding Model Engine: `https://generativelanguage.googleapis.com/v1beta/openai`
- API Key: your Google API key
- Embedding Model: `text-embedding-004`

