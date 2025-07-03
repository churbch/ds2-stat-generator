import os
from dotenv import load_dotenv
import random # For mock questions and judgments
# import requests # Uncomment when making actual Perplexity API calls
# import openai # Uncomment when making actual ChatGPT/Deepseek API calls
# import google.generativeai as genai # Uncomment when making actual Gemini API calls

# Load environment variables from .env file
load_dotenv()

# Define Dark Souls 2 Stats
DS2_STATS = [
    "Vigor", "Endurance", "Vitality", "Attunement", "Strength",
    "Dexterity", "Adaptability", "Intelligence", "Faith"
]

def generate_follow_up_questions_mock(initial_statement: str) -> list[str]:
    """
    Mocks the AI's ability to generate quirky follow-up questions based on an initial statement.
    In a later step, this will be replaced by an actual AI call (e.g., using Gemini).
    """
    print(f"AI (mock): Analyzing your statement: '{initial_statement}' to generate questions...")
    
    # Breadcrumb: This is where an actual AI call would go.
    # For example:
    # gemini_api_key = os.getenv("GEMINI_API_KEY")
    # if gemini_api_key:
    #     genai.configure(api_key=gemini_api_key)
    #     model = genai.GenerativeModel('gemini-pro')
    #     response = model.generate_content(f"Given the user's statement: '{initial_statement}', generate 3 quirky and random follow-up questions that could reveal more about their current 'stats' in a Dark Souls 2-like context. Focus on unusual life events. Format as a list of questions.")
    #     questions = [q.strip() for q in response.text.split('\n') if q.strip().endswith('?')]
    #     return questions if questions else ["Have you found any lost souls recently?", "Did you accidentally aggro a friendly NPC?", "Have you discovered a new shortcut in your daily routine?"]

    mock_questions = [
        "Have you recently stumbled upon a forgotten coin in an old jacket?",
        "Did you accidentally consume something questionable, leading to unexpected side effects?",
        "Has a sudden, inexplicable urge to explore a dark, damp cave overcome you?",
        "Have you encountered a suspiciously helpful stranger offering unsolicited advice?",
        "Did you misplace an important item only to find it in the most illogical place?",
        "Have you been plagued by an unusual, persistent sound that only you can hear?",
        "Did you recently acquire a new, seemingly useless trinket that you can't part with?",
        "Has a small, furry creature attempted to steal your lunch?",
        "Have you found yourself inexplicably drawn to a particular, dimly lit corner of a room?",
        "Did you accidentally walk into a spiderweb this morning?",
    ]
    
    # Select a random subset of questions
    num_questions = random.randint(3, 5)
    return random.sample(mock_questions, min(num_questions, len(mock_questions)))

def fetch_data_with_perplexity_mock(query: str) -> str:
    """
    Mocks fetching data using Perplexity AI.
    This will be replaced by an actual Perplexity API call.
    """
    print(f"\nPerplexity AI (mock): Searching for data related to: '{query}'...")
    # Breadcrumb: This is where the actual Perplexity API call would go.
    # perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
    # if perplexity_api_key:
    #     headers = {"Authorization": f"Bearer {perplexity_api_key}"}
    #     response = requests.post("https://api.perplexity.ai/chat/completions", json={"model": "pplx-7b-online", "messages": [{"role": "user", "content": query}]}, headers=headers)
    #     return response.json()["choices"][0]["message"]["content"]

    mock_data_responses = [
        "Statistical data suggests a correlation between finding money and a temporary boost in mood, often leading to increased productivity for a short period.",
        "Historical records indicate that unexpected encounters with small, furry creatures have occasionally led to new discoveries or unusual alliances.",
        "Psychological studies show that individuals who frequently misplace items often develop enhanced problem-solving skills due to constant searching.",
        "Anecdotal evidence links inexplicable urges to explore dark places with a subconscious desire for novelty and adventure."
    ]
    return random.choice(mock_data_responses)

def get_chatgpt_judgment_mock(context: str) -> dict[str, int]:
    """
    Mocks ChatGPT's judgment on DS2 stats.
    """
    print("ChatGPT (mock): Judging stats...")
    # Breadcrumb: Integrate actual ChatGPT API call here.
    # openai.api_key = os.getenv("CHATGPT_API_KEY")
    # if openai.api_key:
    #     response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #             {"role": "system", "content": "You are an expert at assigning Dark Souls 2 stats based on life events. Assign values between 1 and 99."},
    #             {"role": "user", "content": f"Given the following context: {context}\nAssign Dark Souls 2 stats (Vigor, Endurance, Vitality, Attunement, Strength, Dexterity, Adaptability, Intelligence, Faith) with values from 1 to 99. Return as a JSON object."}
    #         ]
    #     )
    #     # Parse response to dict
    #     return json.loads(response.choices[0].message.content)

    return {stat: random.randint(1, 99) for stat in DS2_STATS}

def get_deepseek_judgment_mock(context: str) -> dict[str, int]:
    """
    Mocks Deepseek's judgment on DS2 stats.
    """
    print("Deepseek (mock): Judging stats...")
    # Breadcrumb: Integrate actual Deepseek API call here.
    # openai.api_base = "https://api.deepseek.com/v1" # Or similar endpoint
    # openai.api_key = os.getenv("DEEPSEEK_API_KEY")
    # if openai.api_key:
    #     response = openai.ChatCompletion.create(
    #         model="deepseek-chat", # Or appropriate Deepseek model
    #         messages=[
    #             {"role": "system", "content": "You are an expert at assigning Dark Souls 2 stats based on life events. Assign values between 1 and 99."},
    #             {"role": "user", "content": f"Given the following context: {context}\nAssign Dark Souls 2 stats (Vigor, Endurance, Vitality, Attunement, Strength, Dexterity, Adaptability, Intelligence, Faith) with values from 1 to 99. Return as a JSON object."}
    #         ]
    #     )
    #     # Parse response to dict
    #     return json.loads(response.choices[0].message.content)

    return {stat: random.randint(1, 99) for stat in DS2_STATS}

def get_gemini_judgment_mock(context: str) -> dict[str, int]:
    """
    Mocks Gemini's judgment on DS2 stats.
    """
    print("Gemini (mock): Judging stats...")
    # Breadcrumb: Integrate actual Gemini API call here.
    # gemini_api_key = os.getenv("GEMINI_API_KEY")
    # if gemini_api_key:
    #     genai.configure(api_key=gemini_api_key)
    #     model = genai.GenerativeModel('gemini-pro')
    #     response = model.generate_content(f"Given the following context: {context}\nAssign Dark Souls 2 stats (Vigor, Endurance, Vitality, Attunement, Strength, Dexterity, Adaptability, Intelligence, Faith) with values from 1 to 99. Return as a JSON object.")
    #     # Parse response to dict
    #     return json.loads(response.text)

    return {stat: random.randint(1, 99) for stat in DS2_STATS}

def get_perplexity_judgment_mock(context: str) -> dict[str, int]:
    """
    Mocks Perplexity's judgment on DS2 stats (can also act as an expert).
    """
    print("Perplexity (mock): Judging stats...")
    # Breadcrumb: Integrate actual Perplexity API call here.
    # perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
    # if perplexity_api_key:
    #     headers = {"Authorization": f"Bearer {perplexity_api_key}"}
    #     response = requests.post("https://api.perplexity.ai/chat/completions", json={
    #         "model": "pplx-7b-online", # Or another suitable model
    #         "messages": [
    #             {"role": "system", "content": "You are an expert at assigning Dark Souls 2 stats based on life events. Assign values between 1 and 99."},
    #             {"role": "user", "content": f"Given the following context: {context}\nAssign Dark Souls 2 stats (Vigor, Endurance, Vitality, Attunement, Strength, Dexterity, Adaptability, Intelligence, Faith) with values from 1 to 99. Return as a JSON object."}
    #         ]
    #     }, headers=headers)
    #     # Parse response to dict
    #     return json.loads(response.json()["choices"][0]["message"]["content"])

    return {stat: random.randint(1, 99) for stat in DS2_STATS}

def combine_judgments(all_judgments: list[dict[str, int]]) -> dict[str, int]:
    """
    Combines judgments from multiple AI models.
    Currently, this is a simple average. More sophisticated weighting can be added here.
    """
    combined_stats = {stat: 0 for stat in DS2_STATS}
    num_judgments = len(all_judgments)

    if num_judgments == 0:
        return {stat: 0 for stat in DS2_STATS}

    for judgment in all_judgments:
        for stat, value in judgment.items():
            combined_stats[stat] += value
    
    # Average the stats
    for stat in combined_stats:
        combined_stats[stat] = round(combined_stats[stat] / num_judgments)

    return combined_stats

def main():
    print("Welcome to the DS2 Stat Generator!")
    print("Loading AI API keys...")

    # Retrieve API keys
    perplexity_api_key = os.getenv("PERPLEXITY_API_KEY")
    chatgpt_api_key = os.getenv("CHATGPT_API_KEY")
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Basic check to see if keys are loaded (they might be None if not in .env)
    # This will be used to determine which AIs are 'available' for the MoE
    available_ais = {
        "Perplexity": perplexity_api_key,
        "ChatGPT": chatgpt_api_key,
        "Deepseek": deepseek_api_key,
        "Gemini": gemini_api_key
    }

    if not any(available_ais.values()):
        print("Warning: No AI API keys found. Please ensure your .env file is correctly configured.")
    else:
        print("API keys loaded (or attempted to load). Available AIs:")
        for ai, key_present in available_ais.items():
            print(f"- {ai}: {'Available' if key_present else 'Not Available'}")

    print("\n--- Your Initial Statement ---")
    initial_statement = input("Please describe your current life situation or a recent significant event: ")
    
    if not initial_statement.strip():
        print("No statement provided. Exiting.")
        return

    print("\n--- AI Generating Questions ---")
    # Use Gemini for question generation if available, otherwise mock
    # Breadcrumb: Replace with actual Gemini call if API key is present
    follow_up_questions = generate_follow_up_questions_mock(initial_statement)

    print("\n--- Follow-up Questions for You ---")
    user_answers = {}
    for i, question in enumerate(follow_up_questions):
        answer = input(f"{i+1}. {question} (Your answer): ")
        user_answers[question] = answer

    print("\n--- Your Answers ---")
    for question, answer in user_answers.items():
        print(f"Q: {question}\nA: {answer}")

    # --- Perplexity AI Data Fetching ---
    # Combine initial statement and answers for a comprehensive query
    perplexity_query = f"Given the user's initial statement: '{initial_statement}' and their answers to follow-up questions: {user_answers}. Find relevant statistical data or anecdotal evidence that links these life events to potential changes in personal attributes or 'stats'."
    
    fetched_data = fetch_data_with_perplexity_mock(perplexity_query)
    print(f"\n--- Data Fetched by Perplexity AI (Mock) ---")
    print(fetched_data)

    # --- Mixture of Experts (MoE) ---
    print("\n--- Mixture of Experts: Judging Your Stats ---")
    all_judgments = []
    context_for_ais = f"Initial Statement: {initial_statement}\nUser Answers: {user_answers}\nFetched Data: {fetched_data}"

    # Call each AI that has an API key available
    if available_ais["ChatGPT"]:
        all_judgments.append(get_chatgpt_judgment_mock(context_for_ais))
    if available_ais["Deepseek"]:
        all_judgments.append(get_deepseek_judgment_mock(context_for_ais))
    if available_ais["Gemini"]:
        all_judgments.append(get_gemini_judgment_mock(context_for_ais))
    # Perplexity can also act as an expert for judgment, not just data fetching
    if available_ais["Perplexity"]:
        all_judgments.append(get_perplexity_judgment_mock(context_for_ais))

    final_stats = combine_judgments(all_judgments)

    print("\n--- Your Dark Souls 2 Stats (Combined Judgment) ---")
    for stat, value in final_stats.items():
        print(f"{stat}: {value}")

    print("\n--- Next Steps for You ---")
    print("1. **Install AI Client Libraries**: Make sure you have `openai` and `google-generativeai` installed. You can do this by running `pip install -r requirements.txt` after activating your Conda environment.")
    print("2. **Populate .env**: Ensure your `.env` file contains your actual API keys for Perplexity, ChatGPT, Deepseek, and Gemini.")
    print("3. **Uncomment and Implement API Calls**: In `app.py`, uncomment the `import` statements for `requests`, `openai`, and `google.generativeai`. Then, within each `get_xxx_judgment_mock` function (and `generate_follow_up_questions_mock`, `fetch_data_with_perplexity_mock`), uncomment the actual API call logic and replace the mock return with the real API response parsing.")
    print("4. **Refine Judgment Logic**: The `combine_judgments` function currently uses a simple average. You might want to implement a more sophisticated weighting system or a different aggregation method based on your preferences or the perceived reliability of each AI.")
    print("5. **Error Handling**: Add robust error handling for API calls (e.g., try-except blocks for network issues, invalid API keys, rate limits).")
    print("6. **User Experience**: Consider how to present the final stats more engagingly (e.g., a simple text-based character sheet, or even a basic web interface if you want to expand).")

if __name__ == "__main__":
    main()