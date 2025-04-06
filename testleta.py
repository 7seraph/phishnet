# Testing Letta API client
from letta_client import Letta

client = Letta(token="MDgwNjQxY2YtMTI0NC00NDZmLThiM2YtMTVhNTIzOTJjMDhiOjhkNTg1ZTg1LTk1ODItNGRmYi1iZjY4LTBiOTRmZTAwYmVlNQ==")

try:
    response = client.templates.create_agents(
        project="default-project",
        template_version="cruel-blush-turkey:latest",
    )
    print("Agent created:", response)
except Exception as e:
    print("Error:", str(e))