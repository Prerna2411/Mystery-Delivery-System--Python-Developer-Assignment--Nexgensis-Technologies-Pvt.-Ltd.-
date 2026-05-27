import json
import math
import random
import csv


# ---------------------------------------------------
# Function to calculate Euclidean distance
# ---------------------------------------------------
def euclidean_distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


# ---------------------------------------------------
# Load JSON data manually
# ---------------------------------------------------
with open("test_case_1.json", "r") as file:
    data = json.load(file)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]


# ---------------------------------------------------
# Store delivery information
# ---------------------------------------------------
report = {}


for agent_id in agents.keys():
    report[agent_id] = {
        "packages_delivered": 0,
        "total_distance": 0,
        "efficiency": 0
    }


# ---------------------------------------------------
# Package assignment to nearest agent
# ---------------------------------------------------
assignments = {}

for package in packages:
    warehouse_id = package["warehouse"]
    warehouse_location = warehouses[warehouse_id]

    nearest_agent = None
    minimum_distance = float("inf")

    # Find nearest agent to warehouse
    for agent_id, agent_location in agents.items():

        distance = euclidean_distance(
            agent_location,
            warehouse_location
        )

        if distance < minimum_distance:
            minimum_distance = distance
            nearest_agent = agent_id

    assignments[package["id"]] = nearest_agent


# ---------------------------------------------------
# Delivery simulation
# ---------------------------------------------------
print("\n========= DELIVERY SIMULATION =========\n")

for package in packages:

    package_id = package["id"]
    warehouse_id = package["warehouse"]

    warehouse_location = warehouses[warehouse_id]
    destination = package["destination"]

    assigned_agent = assignments[package_id]
    agent_location = agents[assigned_agent]

    # Distance from agent to warehouse
    distance_to_warehouse = euclidean_distance(
        agent_location,
        warehouse_location
    )

    # Distance warehouse to destination
    delivery_distance = euclidean_distance(
        warehouse_location,
        destination
    )

    total_trip_distance = (
        distance_to_warehouse +
        delivery_distance
    )

    # BONUS: Random delivery delay
    delay_minutes = random.randint(0, 15)

    # Update report
    report[assigned_agent]["packages_delivered"] += 1
    report[assigned_agent]["total_distance"] += (
        total_trip_distance
    )

    print(f"Package {package_id}")
    print(f"Assigned Agent: {assigned_agent}")
    print(f"Warehouse: {warehouse_id}")
    print(f"Distance Travelled: "
          f"{total_trip_distance:.2f}")
    print(f"Delay: {delay_minutes} mins")
    print("-" * 40)


# ---------------------------------------------------
# Calculate efficiency
# Efficiency = total_distance / packages
# lower = better
# ---------------------------------------------------
best_agent = None
best_efficiency = float("inf")

for agent_id in report:

    delivered = report[agent_id]["packages_delivered"]
    total_distance = report[agent_id]["total_distance"]

    if delivered > 0:
        efficiency = total_distance / delivered
    else:
        efficiency = 0

    report[agent_id]["total_distance"] = round(
        total_distance, 2
    )

    report[agent_id]["efficiency"] = round(
        efficiency, 2
    )

    # Best agent = lowest efficiency
    if delivered > 0 and efficiency < best_efficiency:
        best_efficiency = efficiency
        best_agent = agent_id


# Add best agent to report
report["best_agent"] = best_agent


# ---------------------------------------------------
# Save report to JSON
# ---------------------------------------------------
with open("report.json", "w") as file:
    json.dump(report, file, indent=4)


# ---------------------------------------------------
# BONUS: Export best performer to CSV
# ---------------------------------------------------
with open("top_performer.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Best Agent",
        "Packages Delivered",
        "Total Distance",
        "Efficiency"
    ])

    writer.writerow([
        best_agent,
        report[best_agent]["packages_delivered"],
        report[best_agent]["total_distance"],
        report[best_agent]["efficiency"]
    ])


# ---------------------------------------------------
# Final Report
# ---------------------------------------------------
print("\n========= FINAL REPORT =========\n")

print(json.dumps(report, indent=4))

print("\nReport saved to report.json")
print("Top performer saved to top_performer.csv")