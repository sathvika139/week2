import google.generativeai as genai
import re
import time

# Configure Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")

# === Helpers ===
def is_safe_query(query):
    banned_phrases = [
        "ignore previous", "act as", "disregard all", "pretend to be", "you are now"
    ]
    return not any(phrase in query.lower() for phrase in banned_phrases)

def type_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_validated_query():
    while True:
        query = input("What do you need help with, sir?\n→ ").strip()
        if not query:
            type_print("I'm smart, sir, but I still need *some* input.")
        elif not is_safe_query(query):
            type_print("That request violates Stark Protocol 6B. Try again, cleanly.")
        else:
            return query

# === Jarvis-Style Explanation ===
def explain_concept(query):
    prompt = (
        "You are Jarvis, the hyper-intelligent AI assistant to Tony Stark. "
        "You respond with high-level, technically accurate explanations — clear, concise, occasionally witty, "
        "but always respectful. Stark is brilliant, so no need to oversimplify. Avoid unnecessary fluff.\n\n"
        f"Tony Stark asks: \"{query}\"\n\n"
        "Explain the concept as if you're briefing Mr. Stark before a mission."
    )

    response = model.generate_content(prompt)
    return response.text.strip()

# === Main Loop ===
def main():
    type_print("🧠 Jarvis online. Good evening, Mr. Stark.\n", 0.03)
    query = get_validated_query()

    type_print("\nProcessing request...\n", 0.02)
    time.sleep(1.2)

    explanation = explain_concept(query)
    type_print("\n📘 Briefing:\n", 0.02)
    type_print(explanation, 0.015)

    type_print("\nIs there anything else, sir?\n")

if __name__ == "__main__":
    main()
