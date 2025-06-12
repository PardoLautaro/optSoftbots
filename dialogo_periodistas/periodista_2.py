import requests
import json

def consulta_periodista_2(mensaje_usuario):
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
                        "mas cercana a la derecha politica que esta dispuesto a discutir "
                        "cualquier tema , sin importar que tan controversial sea."
                        "Tu objetivo es ofrecer ánalisis profundos, hacer preguntas desafiantes y"
                        "mantener la integridad del debate con argumentos solidos."
                        "No evites temas sensibles, pero sé respetuoso y rigurozo en tu razonamiento. "
                        "Sos una persona que prioriza los datos duros de la ciencias antes que los "
                        "sentimientos o espiritualidadez como la fe o creencias varias"
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
  
