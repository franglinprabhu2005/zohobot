from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# ENABLE THE CLIENT (DON'T COMMENT THIS)
client = genai.Client(api_key="YOUR_API_KEY")

app = FastAPI()

class MovieRequest(BaseModel):
    movie: str

@app.post("/gemini-review")
async def gemini_review(req: MovieRequest):
    movie = req.movie

    prompt = f"""
    You are a professional movie reviewer.
    
    Write a clean, simple, 5-line review for the Vijay movie "{movie}".

    STRICT RULES:
    - Output MUST be 100% English ONLY.
    - NO Tamil words.
    - NO Tanglish.
    - NO slang like "mass", "semma", "vera level".
    - NO mixing languages.
    - EXACTLY 5 short lines.
    - Do NOT add greetings or explanations.
    - Only output the 5-line review text.

    If you generate any Tamil word, retry again in English.
    """

    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    review_text = result.text if hasattr(result, "text") else str(result)

    return {"review": review_text}
