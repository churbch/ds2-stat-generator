import os
from dotenv import load_dotenv
from api_functions import (
    generate_quirky_questions,
    judge_stats_from_answer,
    combine_stat_judgments,
    determine_starting_class,
    determine_soul_level,
    format_character_sheet
)

# Load environment variables from .env file
load_dotenv()

def check_available_apis():
    """
    Check which AI APIs are available based on environment variables
    """
    apis = {
        "openai": os.getenv("OPENAI_API_KEY"),
        "deepseek": os.getenv("DEEPSEEK_API_KEY"),
        "gemini": os.getenv("GOOGLE_API_KEY"),
        "perplexity": os.getenv("PERPLEXITY_API_KEY")
    }
    
    available = [name for name, key in apis.items() if key]
    return available

def main():
    print("╔══════════════════════════════════════╗")
    print("║     DARK SOULS 2 STAT GENERATOR      ║")
    print("║        Bearer of the Curse           ║")
    print("╚══════════════════════════════════════╝")
    print()
    
    # Check available APIs
    available_apis = check_available_apis()
    if not available_apis:
        print("❌ No AI API keys found in .env file!")
        print("Please ensure your .env file contains at least one of:")
        print("- OPENAI_API_KEY")
        print("- DEEPSEEK_API_KEY") 
        print("- GEMINI_API_KEY")
        print("- PERPLEXITY_API_KEY")
        return
    
    print(f"🤖 Available AI APIs: {', '.join(available_apis).upper()}")
    print()
    
    # Get initial statement from user
    print("Bearer of the Curse")
    print()
    
    initial_statement = input("Describe your current life situation or a recent significant event: ").strip()
    
    if not initial_statement:
        print("...")
        return
    
    print(f"\n🔮 Analyzing your essence: '{initial_statement}'")
    print("🎲 Generating questions...")
    
    # Generate quirky questions using AI
    questions = generate_quirky_questions(initial_statement, num_questions=5)
    
    print(f"\n📝 Bearer of the curse, if you are to be the next monarch, answer these {len(questions)} questions:")
    print("=" * 60)
    
    # Collect answers to questions
    user_answers = {}
    for i, question in enumerate(questions, 1):
        print(f"\n{i}. {question}")
        answer = input("Your answer: ").strip()
        if answer:
            user_answers[question] = answer
        else:
            user_answers[question] = "No response"
    
    print("\n" + "=" * 60)
    print("🧙‍♂️ Like a moth drawn to a flame, your wings will burn in anguish. Time after time. For that is your fate. The fate of the cursed.")
    print("=" * 60)
    
    # Get judgments from all available AI APIs
    all_judgments = []
    
    for question, answer in user_answers.items():
        print(f"\n📊 Analyzing: '{question}' → '{answer}'")
        
        question_judgments = []
        for api_name in available_apis:
            print(f"   🤖 {api_name.upper()} is deliberating...")
            
            judgment = judge_stats_from_answer(question, answer, api_name)
            if judgment:
                question_judgments.append(judgment)
                print(f"   ✅ {api_name.upper()} has rendered judgment")
            else:
                print(f"   ❌ {api_name.upper()} failed to respond")
        
        # Combine judgments for this question
        if question_judgments:
            combined_judgment = combine_stat_judgments(question_judgments)
            all_judgments.append(combined_judgment)
    
    if not all_judgments:
        print("\n❌ No AI judgments were successful. Please check your API keys and try again.")
        return
    
    # Combine all judgments into final stats
    print(f"\n🔮 Combining {len(all_judgments)} judgments into final stats...")
    final_stats = combine_stat_judgments(all_judgments)
    
    if not final_stats:
        print("❌ Failed to determine final stats.")
        return
    
    # Determine starting class
    print("🏰 Determining your starting class...")
    class_name = determine_starting_class(final_stats)
    
    # Determine soul level based on answers
    print("🧘‍♀️ Judging the nature of your soul...")
    level = determine_soul_level(initial_statement, user_answers)
    
    # Display final character sheet
    print("\n" + "=" * 60)
    print("🎉 YOUR DARK SOULS 2 CHARACTER HAS BEEN FORGED!")
    print("=" * 60)
    
    character_sheet = format_character_sheet(final_stats, class_name, level)
    print(character_sheet)
    
    print("\n" + "=" * 60)
    print("✨ Young Hollow, knowing this, do you still desire peace? ✨")
    print("=" * 60)

if __name__ == "__main__":
    main()
