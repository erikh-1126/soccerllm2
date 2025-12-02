from llama_cpp import Llama
import os
import textwrap

MODEL_PATH = os.environ.get("MODEL_PATH", "/models/llama3.gguf")

_llama = None
def get_llama():
    global _llama
    if _llama is None:
        _llama = Llama(model_path=MODEL_PATH)
    return _llama

def make_prompt(player_name: str, facts: str) -> str:
    return textwrap.dedent(f"""
    You are a helpful soccer historian. Using only the provided facts, write a concise, factual
    career summary for the player. Do NOT hallucinate facts beyond the provided facts.

    Player: {player_name}

    Facts (from public sources):
    {facts}

    Output JSON with fields:
    - biography: short paragraph summary (1-3 sentences)
    - teams: list of major clubs & years if present in facts
    - achievements: bullet list (short)
    - style_of_play: short phrase/one sentence or "N/A" if not present

    Return ONLY valid JSON.
    """).strip()

def generate_summary(player_name: str, facts: str, max_tokens: int = 512):
    llama = get_llama()
    prompt = make_prompt(player_name, facts)
    # synchronous completion
    resp = llama.create(prompt=prompt, max_tokens=max_tokens, temperature=0.0)
    text = resp.get("choices", [{}])[0].get("text", "").strip()
    return text
