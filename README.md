# Personalized Dinner Recipe Generator

A Python CLI tool that uses the Groq API (LLaMA-3.3-70B) to generate personalized
dinner recipes based on your allergies and dietary preferences using a structured
prompt engineering approach.

## Project Structure
```
├── main.py               # Entry point — user input, save output
├── prompt_template.py    # f-string prompt (instruction + example + CoT)
├── llm_client.py         # Groq API interaction
├── .env                  # API key (not committed to Git)
└── recipe_output_*.txt   # Auto-generated output files
```

## Setup

1. **Clone the repo and install dependencies**
```bash
   pip install groq python-dotenv
```

2. **Add your Groq API key to `.env`**
```
   GROQ_API_KEY=your_key_here
```
   Get a free key at https://console.groq.com

3. **Run**
```bash
   python main.py
```

## Usage

When prompted, enter your allergies and dietary preferences:
```
Enter your allergies (comma-separated, or Enter for none):
> peanuts, shellfish

Enter your dietary preferences (comma-separated, or Enter for none):
  Examples: vegetarian, vegan, halal, keto, gluten-free, dairy-free
> halal, gluten-free
```

The recipe is printed to the console and saved as `recipe_output_<timestamp>.txt`
in the same folder.

## Prompt Design

The prompt template in `prompt_template.py` combines three techniques:

| Technique | Purpose |
|---|---|
| **Instruction-based** | Defines the chef persona, hard safety rules, and output schema |
| **Example-based** | Embeds a worked sample recipe to anchor format and quality |
| **Chain-of-Thought** | Forces the model to audit ingredients before generating the recipe |
