import json
import os
import asyncio
from dotenv import load_dotenv
from multi_agents.agents.master import MasterAgent

# Load environment variables from the .env file
load_dotenv()

# Define the relative path to the task.json file
current_directory = os.path.dirname(__file__)
task_json_path = os.path.join(current_directory, 'task.json')

# Verify the path and load the task configuration
if not os.path.exists(task_json_path):
    raise FileNotFoundError(f"Task configuration file not found: {task_json_path}")

with open(task_json_path, 'r') as file:
    task_config = json.load(file)

# Initialize the MasterAgent with the task configuration
master_agent = MasterAgent(task=task_config)

# Run the task asynchronously
async def run_task():
    result = await master_agent.run()
    print("Task completed with result:", result)

# Execute the task
asyncio.run(run_task())
