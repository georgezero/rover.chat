""" ChatGPT Example

```bash
# First create python virtual environment 
python -m venv venv
source venv/bin/activate
pip install openai

# Set Open API key 
export OPENAI_API_KEY="[key]"
```

# API example from docs
## https://platform.openai.com/docs/api-reference/completions/create
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="What's the best way to treat a runny nose and sore throat?",
  max_tokens=500,
  temperature=0
)

print(response)
