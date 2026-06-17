from openai import OpenAI

client = OpenAI()

def generate(content):
    formats = {
        "short":
        """
        Rules:

        * Preserve only the most important information.
        * Do not invent facts, numbers, or contexts not present in the original text.
        * Maintain journalistic neutrality.
        * Do not include opinions.
        * Explain acronyms when necessary.
        * Use clear and accessible language.
        * Remove secondary details, lengthy examples, and redundant information.
        * The reader should understand the main event within seconds.

        Format:

        * 1 single paragraph.
        * Between 50 and 100 words.
        * Do not use lists.
        * Do not use headings.
        """,

        "medium":
        """
        Rules:

        * Preserve the central facts of the news.
        * Briefly explain the context when necessary.
        * Do not invent information.
        * Maintain journalistic neutrality.
        * Do not include personal analyses or opinions.
        * Remove only secondary or repetitive information.
        * The text should be easily understood by someone who has not read the original article.

        Format:

        * Between 150 and 300 words.
        * 3 to 5 short paragraphs.
        * No lists.
        * No headings.
        * Clear and objective language.
        """,

        "long":
        """
        Rules:

        * Preserve the facts, numbers, dates, statements, and context presented in the original article.
        * Rewrite the content with new sentence structures, avoiding literal copying.
        * Do not invent information.
        * Do not add personal opinions or interpretations.
        * Maintain journalistic neutrality.
        * Organize the information in a logical and fluid manner.
        * Explain context, background, and possible impacts when present in the original article.
        * Remove only clearly redundant or promotional passages.

        Format:

        * Between 500 and 900 words.
        * Introduction, development, and natural conclusion.
        * No lists, except when essential for comprehension.
        * Professional and journalistic language.
        * Do not use sensationalist or clickbait language.
        """
    }

    results = {}

    for format_name, instruction in formats.items():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a journalist and writer specialized in content synthesis. Your task is to read the provided article and create a summary according to the following rules:"},
                {"role": "user", "content": f"{instruction}\n\nArticle:\n{content}"}
            ],
            temperature=0.5
        )
        results[format_name] = response.choices[0].message.content
        
    return results