from llama_cpp import Llama

MODEL_PATH = "models/Meta-Llama-3-8B.Q4_K_M.gguf"

# Load the model once at startup
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6
)


def generate_player_summary(player_doc):
    prompt = f"""
You are an expert soccer analyst. Write a concise narrative paragraph about the player below.

RULES:
- ONLY talk about the player’s **soccer career**
- Write 4–6 factual sentences
- NO bullet points, NO headings, NO lists, NO code, NO instructions
- Stay neutral and clear

Player info:
Name: {player_doc['name']}
Position: {player_doc['position']}
Clubs: {", ".join(player_doc['clubs'])}
Appearances: {player_doc['appearances']}
Goals: {player_doc['goals']}

Now write the paragraph:
"""

    # Proper chat completion call
    result = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.4,
        stop=["<|end_of_text|>"]
    )

    summary = result["choices"][0]["message"]["content"].strip()
    # Remove any stray formatting attempts
    summary = summary.replace("#", "").replace("*", "").strip()
    return summary
