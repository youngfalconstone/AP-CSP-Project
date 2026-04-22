def calculate_subgrades(condition):
    if condition["Centering"] >= 0.9:
        centering = 10
    elif condition["Centering"] >= 0.8:
        centering = 9
    elif condition["Centering"] >= 0.7:
        centering = 8
    elif condition["Centering"] >= 0.6:
        centering = 7
    else:
        centering = 6

    subgrades = {
        "Corners": max(1, int(10 - (3 * condition["Major Corner Dings"] + 1 * condition["Minor Corner Dings"]))),
        "Edges": max(1, int(10 - (4 * condition["Major Edge Dings"] + 0.5 * condition["Minor Edge Dings"]))),
        "Surface": max(1, int(10 - (4 * condition["Major Surface Dings"] + 0.5 * condition["Minor Surface Dings"]))),
        "Centering": centering
    }
    return subgrades


def calculate_final_grade(subgrades):
    total = 0
    count = 0
    for grade in subgrades.values():
        if grade > 1:
            total += grade
            count += 1
    return round((total / count) * 2) / 2


def collect_condition():
    condition = {
        "Minor Corner Dings": int(input("Minor Corner Dings: ")),
        "Major Corner Dings": int(input("Major Corner Dings: ")),
        "Minor Edge Dings": int(input("Minor Edge Dings: ")),
        "Major Edge Dings": int(input("Major Edge Dings: ")),
        "Minor Surface Dings": int(input("Minor Surface Dings: ")),
        "Major Surface Dings": int(input("Major Surface Dings: ")),
        "Centering": float(input("Centering ratio (0.0-1.0): "))
    }
    return condition


def main():
    print("\nWelcome to the card grading program.\n")

    condition = collect_condition()
    subgrades = calculate_subgrades(condition)

    print("\nSubgrades:")
    for category, value in subgrades.items():
        print(f"{category}: {value}")

    final_grade = calculate_final_grade(subgrades)
    print(f"\nFinal Grade: {final_grade}")


if __name__ == "__main__":
    main()
