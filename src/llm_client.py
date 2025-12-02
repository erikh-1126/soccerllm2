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
You are a soccer historian. Write a concise, factual career summary.

Name: {player_doc['name']}
Position: {player_doc['position']}
Clubs: {", ".join(player_doc['clubs'])}
Appearances: {player_doc['appearances']}
Goals: {player_doc['goals']}

Write 4–6 sentences.
"""

    response = llm(prompt, max_tokens=200)
    return response["choices"][0]["text"].strip()
