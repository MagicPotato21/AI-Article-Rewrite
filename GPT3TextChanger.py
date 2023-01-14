import openai
openai.api_key = "API-KEY"

# Read the text file
with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Break the text into chunks
chunk_size = 100
text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

rewritten_text = ""

# Process each chunk separately
for chunk in text_chunks:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Please check the text for plagiarism and rewrite it if necessary. Original text: {chunk}"),
        temperature=0.5
    )
    rewritten_text += response.choices[0].text

# Save the rewritten text to a new file
with open("rewritten_textfile.txt", "w", encoding="utf-8") as file:
    file.write(rewritten_text)

    time.sleep(120)

print("The text has been checked for plagiarism and rewritten.")
