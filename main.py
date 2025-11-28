from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# USE NEW SAFE KEY HERE
client = genai.Client(api_key="AIzaSyBOF0u5i_x-naxmZoFmrKtnhcSnklZsYTg")

app = FastAPI()

class MovieRequest(BaseModel):
    movie: str

@app.post("/gemini-review")
async def gemini_review(req: MovieRequest):
    movie = req.movie

    prompt = f"""
    You are a Tamil movie reviewer.
    Give a short, friendly, 5-line review for the Vijay movie "{movie}".
    Language: simple Tamil + little English.
    """

    result = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    review_text = result.text if hasattr(result, "text") else str(result)

    return {"review": review_text}
