import re
import glob
import os

file_paths = glob.glob(os.getenv("USERPROFILE") + r'\.vscode\extensions\github.copilot-*\dist\extension.js')
if file_paths == list():
    print("no copilot extension found")
    exit()

pattern = re.compile(r'\.maxPromptCompletionTokens\(([a-zA-Z0-9_]+),([0-9]+)\)')
replacement = r'.maxPromptCompletionTokens(\1,2048)'

for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    
    new_content = pattern.sub(replacement, content)
    if new_content == content:
        print("no match found in " + file_path)
        continue
    else:
        print("replaced " + file_path)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("replace finish")