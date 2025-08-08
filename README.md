## Master AI Agentic Engineering -  build autonomous AI Agents

### 6 week journey to code and deploy AI Agents with OpenAI Agents SDK, CrewAI, LangGraph, AutoGen and MCP

![Autonomous Agent](assets/autonomy.png)

_If you're looking at this in Cursor, please right click on the filename in the Explorer on the left, and select "Open preview", to view the formatted version._

I couldn't be more excited to welcome you! This is the start of your 6 week adventure into the powerful, astonishing and often surreal world of Agentic AI.

### Before you begin

I'm here to help you be most successful! Please do reach out if I can help, either in the platform or by emailing me direct (ed@edwarddonner.com). It's always great to connect with people on LinkedIn to build up the community - you'll find me here:  
https://www.linkedin.com/in/eddonner/  
And this is new to me, but I'm also trying out X/Twitter at [@edwarddonner](https://x.com/edwarddonner) - if you're on X, please show me how it's done 😂  

### The not-so-dreaded setup instructions

Perhaps famous last words: but I really, truly hope that I've put together an environment that will be not too horrific to set up!

- Windows people, your instructions are [here](setup/SETUP-PC.md)
- Mac people, yours are [here](setup/SETUP-mac.md)
- Linux people, yours are [here](setup/SETUP-linux.md)

Any problems, please do contact me.

### Important notes for CrewAI week (Week 3)

Windows PC users: you will need to have checked the "gotcha #4" at the top of the [SETUP-PC](setup/SETUP-PC.md) instructions -- installing Microsoft Build Tools.  
If you don't do this, then CrewAI will fail with an obscure error involving Chroma..


Then, you will need to run this command in a Cursor Terminal in the project root directory in order to run the Crew commands:  
`uv tool install crewai`   
And in case you've used Crew before, it might be worth doing this to make sure you have the latest:  
`uv tool upgrade crewai`  

Then please keep in mind for Crew:

1. There are two ways that you can work on the CrewAI project in week 3. Either review the code for each project while I build it, and then do `crewai run` to see it in action. Or if you prefer to be more hands-on, then create your own Crew project from scratch to mirror mine; for example, create `my_debate` to go alongside `debate`, and write the code alongside me. Either approach works!  
2. Windows users: there's a new issue that was recently introduced by one of Crew's libraries. Until this is fixed, you might get a "unicode" error when you try to run `crewai create crew`.  If that happens, please try running this command in the Terminal first: `$env:PYTHONUTF8 = "1"`  
3. Gemini users: in addition to a key in your `.env` file for `GOOGLE_API_KEY`, you will need an identical key for `GEMINI_API_KEY`

### Super useful resources

- The course [resources](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/) with videos
- Many essential guides in the [guides](guides/01_intro.ipynb) section
- The [troubleshooting](setup/troubleshooting.ipynb) notebook

### API costs - please read me!

This course does involve making calls to OpenAI and other frontier models, requiring an API key and a small spend, which we set up in the SETUP instructions. If you'd prefer not to spend on API calls, there are cheaper alternatives like DeepSeek and free alternatives like using Ollama!

Details are [here](guides/09_ai_apis_and_ollama.ipynb).

Be sure to monitor your API costs to ensure you are totally happy with any spend. For OpenAI, the dashboard is [here](https://platform.openai.com/usage).

### ABOVE ALL ELSE -

Be sure to have fun with the course! You could not have picked a better time to be learning about Agentic AI. I hope you enjoy every single minute! And if you get stuck at any point - [contact me](https://www.linkedin.com/in/eddonner/).

### Run guides by subfolder

Below are concise instructions to run each subproject from the repository root. Prefer using `uv` for consistent, isolated runs.

Prerequisites
- Install uv: `pip install uv`
- Create a `.env` in the repo root (or in the specific subfolder you run) with relevant keys:

```
OPENAI_API_KEY=sk-...
# Optional, used where push notifications are enabled
PUSHOVER_USER=...
PUSHOVER_TOKEN=...
# Optional for some projects
GOOGLE_API_KEY=...
GEMINI_API_KEY=...
```

If you prefer pip instead of uv, install from the provided requirements files in each folder.

#### 1_foundations (Gradio personal assistant)
- Change directory: `cd 1_foundations`
- Dependencies: `uv run python -V` (resolves via root `pyproject.toml`) or `pip install -r requirements.txt`
- Run: `uv run python app.py` (or `python app.py` if using pip)
- Notes: requires `OPENAI_API_KEY`. Push notifications use `PUSHOVER_USER` and `PUSHOVER_TOKEN` (optional). Reads `me/linkedin.pdf` and `me/summary.txt`.

#### 2_openai/deep_research (OpenAI Agents SDK + Gradio)
- Change directory: `cd 2_openai/deep_research`
- Run: `uv run python deep_research.py`
- Notes: requires `OPENAI_API_KEY`. Optional push notifications use `PUSHOVER_*`.

#### 3_crew (CrewAI projects)
For each project below:
1) Change directory into the project folder
2) Ensure CrewAI CLI is installed: `uv tool install crewai` (update with `uv tool upgrade crewai`)
3) Run: `crewai run`

- coder: `cd 3_crew/coder && crewai run`
- debate: `cd 3_crew/debate && crewai run`
- engineering_team: `cd 3_crew/engineering_team && crewai run`
- financial_researcher: `cd 3_crew/financial_researcher && crewai run`
- stock_picker: `cd 3_crew/stock_picker && crewai run`

Notes
- Requires `OPENAI_API_KEY`. Some features may also use `GOOGLE_API_KEY` and `GEMINI_API_KEY`.
- Windows users: see the CrewAI notes above in this README (Build Tools and UTF-8 env var) before running.

#### 4_langgraph (Sidekick + LangGraph)
- Change directory: `cd 4_langgraph`
- First-time browser tooling: `uv run playwright install --with-deps chromium`
- Run Sidekick UI: `uv run python sidekick.py`
- Alternatively run the simple app: `uv run python app.py`
- Notes: requires `OPENAI_API_KEY`. Uses a local SQLite checkpoint in `memory.db`.

#### 5_autogen (AutoGen multi-agent)
- Change directory: `cd 5_autogen`
- Run: `uv run python world.py`
- Notes: requires `OPENAI_API_KEY`. Spawns multiple agents, may create `idea*.md` files.

#### 6_mcp (Model Context Protocol demos + Traders UI)
- Change directory: `cd 6_mcp`
- Start the UI: `uv run python app.py`
- Optional MCP servers (each in its own terminal):
  - Accounts: `uv run python accounts_server.py`
  - Market: `uv run python market_server.py`
  - Push: `uv run python push_server.py` (requires `PUSHOVER_*`)
- Programmatic client examples are in `accounts_client.py`.

### Notebooks
- Many labs live under each numbered folder. Launch with your preferred environment, e.g.:
  - `uv run jupyter notebook` and open the relevant `*.ipynb` files.