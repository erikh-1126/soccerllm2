import os
from llama_cpp import Llama

MODEL_PATH = os.getenv("MODEL_PATH")

llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_summary(player_doc):
    prompt = f"""
    You are a soccer historian. Write a factual, concise career overview.

    Name: {player_doc['name']}
    Position: {player_doc['position']}
    Clubs: {", ".join(player_doc['clubs'])}
    Appearances: {player_doc['appearances']}
    Goals: {player_doc['goals']}

    Write 5–7 sentences.
    """

    output = llm(prompt, max_tokens=300, stop=["###"])
    return output["choices"][0]["text"].strip()
