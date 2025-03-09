from openai import OpenAI
from app.config import OPENAI_API_KEY



def summarize_reviews(reviews: list, name: str) -> str:
    text = get_prompt(reviews, name)
    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{text}"
            }]
    )
    return response["choices"][0]["message"]["content"]


def get_prompt(reviews: list, name: str) -> str:
    text = " ".join([f"Rating: {r['rating']}, Comentario: {r['text']['text']};" for r in reviews])
    return f"""
                Por favor, resume las siguientes reseñas en un resumen conciso pero detallado.
                El resumen no debe ser ni muy largo ni muy escueto y debe incluir la información más relevante,
                abarcando aspectos positivos y negativos, temas clave y el sentimiento general 
                expresado por los usuarios. Utiliza un lenguaje claro y preciso.
                
                Nombre del lugar: {name}
    
                ----REVIEWS START----
                {text}
                ----REVIEWS END----
            """
