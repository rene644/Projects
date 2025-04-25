import os

json_path = r"C:\Users\renem\Documentos\Python with AI\python_projects\python_projects\weather_projects\ivr_simulator_RT.json"

print("Checking path:", json_path)
if os.path.exists(json_path):
    print("✅ JSON file found at:", json_path)
else:
    print("❌ JSON file not found!")
