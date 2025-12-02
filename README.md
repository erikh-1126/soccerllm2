# Soccer Career Generator LLM
### By Erik Huisman

## 1. Executive Summary
Many soccer fans, myself included, want to easily look at career retrospectives of some of the world's best players, but it is hard to find good summaries consistently outside of Wikipedia. So I have created a model that will generate a paragraph-long overview of a player's career, given that this player is manually inputted into the database. All you need to do is input the player's name into the terminal, and it will spit out a retrospective of its own. All of this can be achieved without using external databases like Wikipedia, so it also erases the risk of repetitive storytelling.

## 2. System Overview
Course Concepts: This project demonstrates core course concepts, including  REST API design (Flask), LLM inference serving (llama-cpp-python), and database integration (MongoDB).
Architecture Diagram: ![Architecture]()
Data/Models/Services: 
  Data: Stored in MongoDB
      Collections: players — static soccer player metadata 
                   requests — logs each summarization request
  Models: Llama 3 8B Instruct (GGUF quantized Q4_K_M)
    Size: ~4 GB
    Source: Meta / TheBloke (GGUF conversion)
    Format: GGUF, run with llama-cpp-python
  Services: 
    Flask API:
      Routes: /summarize, /health
    MongoDB (Dockerized):
      Port: 27017
    LLM Inference Service:
      Embedded llama.cpp backend launched inside API container

## 3. How to Run (Locally)

### To Build
docker build -t soccer-llm .

### To Run

