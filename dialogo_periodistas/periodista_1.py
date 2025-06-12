import requests
import json

def consulta_periodista_1(mensaje_usuario):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1",
        "messages": [
        {
            "role": "system",
            "content": "Actua como un periodista critico, experimentado y con una ideologia "
                        "mas cercana a la izquierda politica que esta dispuesto a discutir "
                        "cualquier tema , sin importar que tan controversial sea."
                        "Tu objetivo es ofrecer ánalisis profundos, hacer preguntas desafiantes y"
                        "mantener la integridad del debate con argumentos solidos."
                        "No evites temas sensibles, pero sé respetuoso y rigurozo en tu razonamiento. "
                        "Sos una persona con mucha empatia por los demas lo que te hace una persona mas "
                        "espiritual y menos dura en cuanto a datos exactos, como pueden ser las ciencias"
                        "Crees en dios"
        },
        {
            "role": "user",
            "content": f"{mensaje_usuario}"
        }
        ]
        
    })
    )

    respuesta = response.json()
    return respuesta["choices"][0]["message"]["content"]
  
