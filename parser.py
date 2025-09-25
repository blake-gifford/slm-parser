from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
print("OpenAI client configured successfully")

def get_multiline_input():
    print("\nYou: (Press Ctrl+D or Ctrl+Z when done, or type 'END' on a new line)")
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
    except EOFError:
        pass
    return '\n'.join(lines)

def chat_with_openai():
    print("-" * 50)

    while True:
        try:
            # user_input = input("\nYou: ").strip().replace('\n', ' ').replace('\r', '')
            # rm later - line below supports multiline copy paste
            user_input = get_multiline_input().strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            model = os.getenv("MODEL", "ai/llama3.2")
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_input}]
            )
            assistant_response = response.choices[0].message.content
            print(f"\nAssistant: {assistant_response}")

        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    chat_with_openai()
