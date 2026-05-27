import json
import math
import random
import csv


# =====================================================
# Function: Calculate Euclidean Distance
# =====================================================
def euclidean_distance(point1, point2):
    """
    Calculate Euclidean distance
    between two coordinates.
    """
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


# =====================================================
# BONUS: ASCII Route Visualization
# =====================================================
def visualize_route(
    agent_id,
    agent_location,
    warehouse_id,
    warehouse_location,
    destination
):
    """
    Visualize delivery route in ASCII.
    """

    print("\nASCII ROUTE VISUALIZATION")
    print("-" * 40)

    print(
        f"{agent_id} "
        f"{agent_location}"
    )

    print("      |")
    print("      v")

    print(
        f"{warehouse_id} "
        f"{warehouse_location}"
    )

    print("      |")
    print("      v")

    print(
        f"Destination "
        f"{destination}"
    )

    print("-" * 40)


# =====================================================
# Function: Find Nearest Agent
# =====================================================
def find_nearest_agent(
    warehouse_location,
    agents
):
    """
    Find nearest agent
    using Euclidean distance.

    Tie-breaking:
    lexicographically smaller
    agent ID wins.
    """

    nearest_agent = None
    minimum_distance = float("inf")

    for (
        agent_id,
        agent_location
    ) in agents.items():

        distance = euclidean_distance(
            agent_location,
            warehouse_location
        )

        if distance < minimum_distance:
            minimum_distance = distance
            nearest_agent = agent_id

        elif distance == minimum_distance:
            nearest_agent = min(
                nearest_agent,
                agent_id
            )

    return nearest_agent


# =====================================================
# Load and Parse JSON File Manually
# =====================================================
try:
    with open(
        "test_case_1.json",
        "r"
    ) as file:

        json_content = file.read()

    data = json.loads(
        json_content
    )

except FileNotFoundError:
    print(
        "Error: JSON file not found."
    )
    exit()

except json.JSONDecodeError:
    print(
        "Error: Invalid JSON format."
    )
    exit()


# =====================================================
# Extract Data
# =====================================================
warehouses = data.get(
    "warehouses",
    {}
)

agents = data.get(
    "agents",
    {}
)

packages = data.get(
    "packages",
    []
)


# =====================================================
# Initialize Report
# =====================================================
report = {}

for agent_id in agents:

    report[agent_id] = {
        "packages_delivered": 0,
        "total_distance": 0,
        "efficiency": 0
    }


# =====================================================
# Dynamic Agent Joining Setup
# =====================================================
new_agent_added = False

mid_point = len(
    packages
) // 2


# =====================================================
# Delivery Simulation
# =====================================================
print(
    "\n========== DELIVERY SIMULATION ==========\n"
)

"""
ASSUMPTION:
Each package delivery
is treated as an
independent trip.

Agent starts from
original location
for every package.
"""

for index, package in enumerate(
    packages
):

    # ==========================================
    # BONUS:
    # Dynamic Agent Joining
    # ==========================================
    if (
        not new_agent_added
        and index == mid_point
    ):

        print(
            "\nNEW AGENT JOINED MID-DAY!"
        )

        print(
            "Agent A5 joined "
            "at [50, 50]\n"
        )

        agents["A5"] = [
            50,
            50
        ]

        report["A5"] = {
            "packages_delivered": 0,
            "total_distance": 0,
            "efficiency": 0
        }

        new_agent_added = True

    package_id = package["id"]

    warehouse_id = package[
        "warehouse"
    ]

    warehouse_location = (
        warehouses[
            warehouse_id
        ]
    )

    destination = package[
        "destination"
    ]

    # ==========================================
    # Dynamic nearest agent assignment
    # ==========================================
    assigned_agent = (
        find_nearest_agent(
            warehouse_location,
            agents
        )
    )

    agent_location = agents[
        assigned_agent
    ]

    # ==========================================
    # Distance Calculation
    # ==========================================
    distance_to_warehouse = (
        euclidean_distance(
            agent_location,
            warehouse_location
        )
    )

    delivery_distance = (
        euclidean_distance(
            warehouse_location,
            destination
        )
    )

    total_trip_distance = (
        distance_to_warehouse
        + delivery_distance
    )

    # ==========================================
    # BONUS:
    # Random delivery delay
    # ==========================================
    delay_minutes = (
        random.randint(
            0,
            15
        )
    )

    # ==========================================
    # Update Report
    # ==========================================
    report[
        assigned_agent
    ][
        "packages_delivered"
    ] += 1

    report[
        assigned_agent
    ][
        "total_distance"
    ] += (
        total_trip_distance
    )

    # ==========================================
    # Print Simulation Details
    # ==========================================
    print(
        f"Package ID       : "
        f"{package_id}"
    )

    print(
        f"Assigned Agent   : "
        f"{assigned_agent}"
    )

    print(
        f"Warehouse        : "
        f"{warehouse_id}"
    )

    print(
        f"Distance Travelled: "
        f"{total_trip_distance:.2f}"
    )

    print(
        f"Delivery Delay   : "
        f"{delay_minutes} mins"
    )

    # ==========================================
    # BONUS:
    # ASCII Route Visualization
    # ==========================================
    visualize_route(
        assigned_agent,
        agent_location,
        warehouse_id,
        warehouse_location,
        destination
    )


# =====================================================
# Calculate Efficiency
# =====================================================
best_agent = None
best_efficiency = (
    float("inf")
)

for agent_id in report:

    delivered = report[
        agent_id
    ][
        "packages_delivered"
    ]

    total_distance = report[
        agent_id
    ][
        "total_distance"
    ]

    if delivered > 0:

        efficiency = (
            total_distance
            / delivered
        )

    else:
        efficiency = 0

    report[
        agent_id
    ][
        "total_distance"
    ] = round(
        total_distance,
        2
    )

    report[
        agent_id
    ][
        "efficiency"
    ] = round(
        efficiency,
        2
    )

    if (
        delivered > 0
        and efficiency
        < best_efficiency
    ):

        best_efficiency = (
            efficiency
        )

        best_agent = (
            agent_id
        )


report[
    "best_agent"
] = best_agent


# =====================================================
# Validate Package Count
# =====================================================
total_delivered = sum(
    report[agent][
        "packages_delivered"
    ]
    for agent in report
    if isinstance(
        report[agent],
        dict
    )
)

if (
    total_delivered
    != len(packages)
):

    print(
        "\nWARNING: "
        "Package count mismatch!"
    )

else:
    print(
        "\nAll packages "
        "delivered successfully."
    )


# =====================================================
# Save JSON Report
# =====================================================
with open(
    "report.json",
    "w"
) as file:

    json.dump(
        report,
        file,
        indent=4
    )

print(
    "\nreport.json generated."
)


# =====================================================
# BONUS:
# Export Best Performer
# =====================================================
with open(
    "top_performer.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(
        file
    )

    writer.writerow([
        "Best Agent",
        "Packages Delivered",
        "Total Distance",
        "Efficiency"
    ])

    writer.writerow([
        best_agent,
        report[
            best_agent
        ][
            "packages_delivered"
        ],
        report[
            best_agent
        ][
            "total_distance"
        ],
        report[
            best_agent
        ][
            "efficiency"
        ]
    ])

print(
    "top_performer.csv "
    "generated."
)


# =====================================================
# Final Report
# =====================================================
print(
    "\n========== FINAL REPORT ==========\n"
)

print(
    json.dumps(
        report,
        indent=4
    )
)
