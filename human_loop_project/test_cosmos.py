from tools.cosmos_tool import CosmosTool

tool = CosmosTool()

print("=" * 40)
print("ALL EMPLOYEES")
print("=" * 40)

employees = tool.get_all_employees()

for emp in employees:
    print(emp)