from llama_cpp import Llama

MODEL_PATH = "models/Meta-Llama-3-8B.Q4_K_M.gguf"

# Load model once at startup
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_player_summary(player_doc):
    """
    player_doc is a dict from MongoDB:
    {
        "name": "Lionel Messi",
        "position": "Forward",
        "clubs": ["Barcelona", "PSG", "Inter Miami"],
        "appearances": 900,
        "goals": 700
    }
    """
    prompt = f"""
def generate_player_summary(player_doc):
    prompt = f"""
You are an expert soccer analyst. Your task is to write a concise and factual career summary for the player provided.
Follow ALL rules below:

- ONLY write about the player's soccer career.
- Do NOT include any sections, chapters, academic content, essay structure, citations, or unrelated information.
- Write 4–6 sentences in paragraph form.
- Do NOT add headings or bullet points.
- Stay factual, neutral, and concise.

Player Information:
Name: {player_doc['name']}
Position: {player_doc['position']}
Clubs: {", ".join(player_doc['clubs'])}
Appearances: {player_doc['appearances']}
Goals: {player_doc['goals']}

Write the summary now:
""".strip()

    response = llm(prompt, max_tokens=200)
    return response["choices"][0]["text"].strip()
