"""
Builds the personalized recipe prompt using three techniques:
  - Instruction-based : role, rules, and output schema
  - Example-based     : a worked sample recipe
  - Chain-of-Thought  : step-by-step reasoning scaffold
"""

def build_prompt(allergy_list: list[str], food_preferences: list[str]) -> str:
    allergies_str   = ", ".join(allergy_list)     if allergy_list     else "none"
    preferences_str = ", ".join(food_preferences) if food_preferences else "none"

    prompt = f"""
You are an expert chef and nutritionist. Your task is to generate ONE personalized
dinner recipe that is completely safe and suitable for the user described below.

USER PROFILE
- Allergies: {allergies_str}
- Dietary preferences: {preferences_str}

STRICT RULES  (instruction-based)
1. NEVER include any ingredient the user is allergic to, even in trace amounts.
2. Every ingredient MUST align with the user's dietary preferences.
3. If halal is listed: use only halal-certified meat, no pork or pork by-products,
   no alcohol or alcohol-derived ingredients (wine, beer, vanilla extract, etc.).
4. Provide exact quantities (e.g., "2 cups", "1 tsp") for every ingredient.
5. Step-by-step instructions must be clear enough for a home cook with no
   professional training.
6. End with a short "Chef's Tip" that highlights one technique or substitution.

WORKED EXAMPLE  (example-based)
Below is a sample output for a DIFFERENT user (vegan, allergic to soy) so you
understand the required format. Do NOT copy this recipe — generate a new one
for the user profile above.

--- EXAMPLE START ---
Recipe Name: Moroccan Chickpea Stew

Ingredients:
• 2 cans (400 g each) chickpeas, drained and rinsed
• 1 large onion, diced
• 3 garlic cloves, minced
• 1 can (400 g) crushed tomatoes
• 1 cup vegetable broth (soy-free)
• 1 tsp cumin
• 1 tsp smoked paprika
• ½ tsp cinnamon
• Salt and pepper to taste
• 2 tbsp olive oil
• Fresh cilantro for garnish

Instructions:
Step 1 – Heat olive oil in a large pot over medium heat. Add the diced onion
         and sauté for 5 minutes until translucent.
Step 2 – Stir in garlic, cumin, paprika, and cinnamon; cook for 1 minute
         until fragrant.
Step 3 – Add chickpeas, crushed tomatoes, and broth. Stir to combine.
Step 4 – Simmer on low heat for 20 minutes, stirring occasionally.
Step 5 – Adjust seasoning with salt and pepper. Serve hot, garnished
         with fresh cilantro.

Chef's Tip: For extra depth, toast the whole spices in a dry pan for
30 seconds before grinding them.
--- EXAMPLE END ---

CHAIN-OF-THOUGHT REASONING  (CoT)
Before writing the recipe, think through these steps inside a <reasoning> block:

<reasoning>
Step A – Identify forbidden ingredients: list every ingredient family
         that must be excluded due to the user's allergies.
Step B – Identify required constraints: list the rules imposed by the
         user's dietary preferences (e.g., no animal products for vegan,
         no gluten-containing grains for gluten-free, halal rules).
Step C – Brainstorm 3 candidate dinner ideas that satisfy Steps A and B.
Step D – Choose the best candidate and explain why (nutrition balance,
         accessibility of ingredients, ease of preparation).
Step E – Draft the ingredients list, checking each item against Steps A–B.
Step F – Draft the step-by-step instructions.
</reasoning>

After the </reasoning> block, output ONLY the final recipe in this exact format:

Recipe Name: <name>

Ingredients:
• <quantity> <ingredient>
...

Instructions:
Step 1 – <instruction>
Step 2 – <instruction>
...

Chef's Tip: <tip>
"""
    return prompt