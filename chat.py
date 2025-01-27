from gradio_client import Client

client = Client("Blandskron/ChatBots")
result = client.predict(
		message="Hola hablame de la historia de la humanidad",
		api_name="/chat"
)
print(result)
