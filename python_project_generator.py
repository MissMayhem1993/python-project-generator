import os

project_name = input("Enter project name: ")

os.mkdir(project_name)

with open(f"{project_name}/main.py", "w") as f:
    f.write('print("Hello from your new project!")\n')

print(f"Project '{project_name}' created successfully.")
