import os
import json
import requests
import openai
import google.generativeai as genai
from typing import Dict, List, Optional

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

def get_openai_response(prompt: str, system_message: str = "", temperature: float = 0.7) -> Optional[str]:
    """
    Get response from OpenAI GPT API
    """
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("OpenAI API key not found")
            return None
            
        client = openai.OpenAI(api_key=api_key)
        
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=temperature
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return None

def get_deepseek_response(prompt: str, system_message: str = "", temperature: float = 0.7) -> Optional[str]:
    """
    Get response from Deepseek API
    """
    try:
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            print("Deepseek API key not found")
            return None
            
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=temperature
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Deepseek API error: {e}")
        return None

def get_gemini_response(prompt: str, system_message: str = "", temperature: float = 0.7) -> Optional[str]:
    """
    Get response from Google Gemini API
    """
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("Google API key not found")
            return None
            
        genai.configure(api_key=api_key)
        generation_config = genai.types.GenerationConfig(temperature=temperature)
        model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)
        
        full_prompt = f"{system_message}\n\n{prompt}" if system_message else prompt
        response = model.generate_content(full_prompt)
        
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None

def get_perplexity_response(prompt: str, system_message: str = "", temperature: float = 0.7) -> Optional[str]:
    """
    Get response from Perplexity API
    """
    try:
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            print("Perplexity API key not found")
            return None
            
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Tye": "application/json"
        }
        
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": messages,
            "temperature": temperature
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Perplexity API error: {e}")
        return None

def generate_quirky_questions(initial_statement: str, num_questions: int = 5) -> List[str]:
    """
    Generate quirky, seemingly irrelevant questions using AI
    """
    prompt = f"""Generate {num_questions} quirky, fun, and seemingly irrelevant questions for the Bearer of the Curse. 

The questions should be unexpected and playful, like:
- "Do you have a cat?"
- "When did you last eat pickles?"
- "Have you ever talked to a houseplant?"
- "Do you prefer stairs or elevators?"
- "How much is too much when buying underwear?"
- "When did you last find money on the floor?"

Make them answerable in 1-2 sentences. Return only the questions, one per line."""

    # Try different APIs for question generation
    for api_func in [get_gemini_response, get_openai_response, get_deepseek_response]:
        response = api_func(prompt, temperature=0.9)
        if response:
            questions = [q.strip() for q in response.split('\n') if q.strip() and '?' in q]
            if questions:
                return questions[:num_questions]
    
    # Fallback questions if all APIs fail
    return [
        "Do you have a cat?",
        "When did you last eat pickles?",
        "Have you ever talked to a houseplant?",
        "Do you prefer stairs or elevators?",
        "What's your favorite type of cheese?",
        "How much is too much when buying underwear?",
        "When did you last find money on the floor?"
    ]

def judge_stats_from_answer(question: str, answer: str, api_name: str) -> Optional[Dict[str, int]]:
    """
    Get stat judgment from a specific AI API based on question/answer pair
    """
    system_message = "You are an expert at assigning Dark Souls 2 stats based on personality insights. Address the user as 'Bearer of the Curse'."
    
    prompt = f"""Bearer of the Curse answered: "{answer}" to the question: "{question}"

Based on this response, assign Dark Souls 2 stats with values between 1-99. Consider what this reveals about their character, personality, and life approach.

Stats to assign:
- Vigor (health/vitality)
- Endurance (stamina/persistence) 
- Vitality (equipment load/burden capacity)
- Attunement (magic slots/spiritual awareness)
- Strength (physical power)
- Dexterity (agility/finesse)
- Adaptability (flexibility/learning)
- Intelligence (analytical thinking)
- Faith (belief/trust)

Return ONLY a JSON object in this exact format:
{{"Vigor": 25, "Endurance": 30, "Vitality": 20, "Attunement": 15, "Strength": 35, "Dexterity": 40, "Adaptability": 25, "Intelligence": 45, "Faith": 30}}"""

    api_functions = {
        "openai": get_openai_response,
        "deepseek": get_deepseek_response,
        "gemini": get_gemini_response,
        "perplexity": get_perplexity_response
    }
    
    api_func = api_functions.get(api_name.lower())
    if not api_func:
        return None
        
    response = api_func(prompt, system_message)
    if not response:
        return None
        
    try:
        # Extract JSON from response
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start != -1 and json_end != -1:
            json_str = response[json_start:json_end]
            stats = json.loads(json_str)
            
            # Validate all required stats are present
            required_stats = ["Vigor", "Endurance", "Vitality", "Attunement", "Strength", "Dexterity", "Adaptability", "Intelligence", "Faith"]
            if all(stat in stats for stat in required_stats):
                return stats
    except json.JSONDecodeError:
        pass
    
    return None

def combine_stat_judgments(all_judgments: List[Dict[str, int]]) -> Dict[str, int]:
    """
    Combine multiple AI stat judgments into final stats
    """
    if not all_judgments:
        return {}
    
    stats = ["Vigor", "Endurance", "Vitality", "Attunement", "Strength", "Dexterity", "Adaptability", "Intelligence", "Faith"]
    combined_stats = {stat: 0 for stat in stats}
    
    for judgment in all_judgments:
        for stat in stats:
            if stat in judgment:
                combined_stats[stat] += judgment[stat]
    
    # Average the stats
    num_judgments = len(all_judgments)
    for stat in combined_stats:
        combined_stats[stat] = round(combined_stats[stat] / num_judgments)
    
    return combined_stats

def load_class_stats() -> Dict[str, Dict]:
    """
    Load starting class stats from class_stats.csv
    """
    import csv
    
    class_stats = {}
    try:
        with open('class_stats.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                class_name = row['Class']
                class_stats[class_name] = {
                    'Level': int(row['Level']),
                    'Vigor': int(row['Vigor']),
                    'Endurance': int(row['Endurance']),
                    'Vitality': int(row['Vitality']),
                    'Attunement': int(row['Attunement']),
                    'Strength': int(row['Strength']),
                    'Dexterity': int(row['Dexterity']),
                    'Adaptability': int(row['Adaptability']),
                    'Intelligence': int(row['Intelligence']),
                    'Faith': int(row['Faith'])
                }
    except FileNotFoundError:
        print("class_stats.csv not found!")
        return {}
    
    return class_stats

def determine_starting_class(user_stats: Dict[str, int]) -> str:
    """
    Determine starting class based on user's stats
    Returns: class_name
    """
    class_stats = load_class_stats()
    if not class_stats:
        return "Deprived"
    
    # Get user's 3 highest stats
    sorted_user_stats = sorted(user_stats.items(), key=lambda x: x[1], reverse=True)
    user_top_3 = [stat[0] for stat in sorted_user_stats[:3]]
    
    best_match = None
    best_score = -1
    
    # Compare against each starting class
    for class_name, stats in class_stats.items():
        # Get class's 3 highest stats (excluding Level)
        class_stat_values = {k: v for k, v in stats.items() if k != 'Level'}
        sorted_class_stats = sorted(class_stat_values.items(), key=lambda x: x[1], reverse=True)
        class_top_3 = [stat[0] for stat in sorted_class_stats[:3]]
        
        # Calculate match score (how many of top 3 stats match)
        match_score = len(set(user_top_3) & set(class_top_3))
        
        if match_score > best_score:
            best_score = match_score
            best_match = class_name
    
    if not best_match:
        best_match = "Deprived"
        
    return best_match

def determine_soul_level(initial_statement: str, user_answers: Dict[str, str]) -> int:
    """
    Determine the user's soul level based on the overall sentiment and strength of their answers.
    """
    context = f"Initial Statement: {initial_statement}\n\n"
    for q, a in user_answers.items():
        context += f"Q: {q}\nA: {a}\n\n"
        
    prompt = f"""You are a wise, ancient being judging the soul of the Bearer of the Curse.
Based on the following life summary, determine their Soul Level.

Consider these factors:
- Happiness and well-being: Happier, more content individuals should have a higher level.
- Strength and resilience: Answers showing strength or overcoming adversity should result in a higher level.
- Weakness and sadness: Answers that seem weak, sad, or resigned should result in a lower level.
- Apathy or lack of detail: Non-answers or very short answers might indicate a lower level of engagement with life.

The level should be between 1 and 100. A completely average person might be level 20-30. A truly exceptional and self-actualized person might be level 70+. Someone struggling deeply might be level 5-10.

Life Summary:
---
{context}
---

Based on this, what is their Soul Level? Return ONLY the integer number. For example: 25"""

    # Use a strong reasoning model for this task
    for api_func in [get_gemini_response, get_openai_response]:
        response = api_func(prompt, temperature=0.5)
        if response:
            try:
                # Find the first integer in the response
                import re
                match = re.search(r'\d+', response)
                if match:
                    level = int(match.group(0))
                    return max(1, min(level, 100)) # Clamp level between 1 and 100
            except (ValueError, TypeError):
                continue
    
    # Fallback level
    return 15

def format_character_sheet(user_stats: Dict[str, int], class_name: str, level: int) -> str:
    """
    Format the final character sheet for display
    """
    class_stats = load_class_stats()
    base_stats = class_stats.get(class_name, {})
    
    sheet = f"""
╔══════════════════════════════════════╗
║        BEARER OF THE CURSE           ║
╠══════════════════════════════════════╣
║ Starting Class: {class_name:<19} ║
║ Level: {level:<29} ║
╠══════════════════════════════════════╣
║              STATS                   ║
╠══════════════════════════════════════╣"""
    
    stat_names = ["Vigor", "Endurance", "Vitality", "Attunement", "Strength", "Dexterity", "Adaptability", "Intelligence", "Faith"]
    
    for stat in stat_names:
        value = user_stats.get(stat, 0)
        base_value = base_stats.get(stat, 0)
        bonus = value - base_value if base_value else 0
        bonus_str = f" (+{bonus})" if bonus > 0 else ""
        sheet += f"\n║ {stat:<12}: {value:>2}{bonus_str:<10} ║"
    
    sheet += "\n╚══════════════════════════════════════╝"
    
    return sheet
