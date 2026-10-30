name = "pro"
tools = ["python", "linux", "git"]

def show(tool):
    print(f"learning: {tool}")

for tool in tools:
    show(tool)

print(f"total tools: {len(tools)}")
