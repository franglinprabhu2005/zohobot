from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# USE NEW SAFE KEY HERE
#client = genai.Client(api_key="AIzaSyC3k9rdwJgQf53UwqJKwFTv_JXaHD8CrFQ")

app = FastAPI()

class MovieRequest(BaseModel):
    movie: str

@app.post("/gemini-review")
async def gemini_review(req: MovieRequest):
    movie = req.movie

    prompt = f"""
    You are a movie reviewer.
    Give a short, friendly, 5-line review for the Vijay movie "{movie}".
    IMPORTANT RULES:
    - Write only in English.
    - Do NOT use Tamil words.
    - Keep the tone simple and casual.
    - Output exactly 5 short lines.
    """

    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    review_text = result.text if hasattr(result, "text") else str(result)

    return {"review": review_text}
