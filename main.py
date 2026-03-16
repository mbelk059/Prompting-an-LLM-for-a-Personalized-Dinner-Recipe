import os
import datetime
from prompt_template import build_prompt
from llm_client import query_llm


def get_user_input() -> tuple[list[str], list[str]]:
    print("Welcome to Your Personalized Dinner Recipe Maker!")

    raw_allergies = input(
        "\nEnter your allergies (comma-separated, or Enter for none):\n> "
    ).strip()
    allergy_list = (
        [a.strip() for a in raw_allergies.split(",") if a.strip()]
        if raw_allergies else []
    )

    raw_prefs = input(
        "\nEnter your dietary preferences (comma-separated, or Enter for none):\n"
        "  Examples: vegetarian, vegan, halal, keto, gluten-free, dairy-free\n> "
    ).strip()
    food_preferences = (
        [p.strip() for p in raw_prefs.split(",") if p.strip()]
        if raw_prefs else []
    )

    return allergy_list, food_preferences


def save_output(prompt: str, response: str, allergy_list: list[str],
                food_preferences: list[str]) -> str:
    timestamp  = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename   = f"recipe_output_{timestamp}.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, filename)

    sep = "=" * 70
    content = f"""{sep}
PERSONALIZED DINNER RECIPE GENERATOR
Generated: {datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S")}
{sep}

USER PROFILE
------------
Allergies          : {", ".join(allergy_list) if allergy_list else "none"}
Dietary Preferences: {", ".join(food_preferences) if food_preferences else "none"}

{sep}
PROMPT SENT TO LLM
{sep}

{prompt}

{sep}
LLM RESPONSE
{sep}

{response}

{sep}
END OF FILE
{sep}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path


def main():
    allergy_list, food_preferences = get_user_input()

    prompt = build_prompt(allergy_list, food_preferences)

    print("\nGenerating your personalized recipe! Please wait …\n")

    response = query_llm(prompt)

    print("\n" + "=" * 60)
    print("YOUR PERSONALIZED RECIPE IS READY!")
    print("=" * 60)
    print(response)

    saved_path = save_output(prompt, response, allergy_list, food_preferences)
    print(f"\nSaved to: {saved_path}")


if __name__ == "__main__":
    main()