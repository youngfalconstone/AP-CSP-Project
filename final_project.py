from word2number import w2n

def calculate_subgrades(condition):
    #CSP: use of at least one collection type to represent a collection of data that is stored
    #CSP: at least one procedure that contributes to the program's intended purpose
    if condition["Centering"] >= 0.9:
        centering = 10
    elif condition["Centering"] >= 0.8:
        centering = 9
    elif condition["Centering"] >= 0.7:
        centering = 8
    elif condition["Centering"] >= 0.7:
        centering = 7
    else:
        centering = 6
    subgrades = {
        "Corners": max(1, int(10 - (3 * condition["Major Corner Dings"] + 1 * condition["Minor Corner Dings"]))),
        "Edges": max(1, int(10 - (4 * condition ["Major Edge Dings"] + 0.5 * condition["Minor Surface Dings"]))),
        "Surface": max(1, int(10 - (4 * condition ["Major Surface Dings"] + 0.5 * condition["Minor Surface Dings"]))),
        "Centering": centering
        }
    return subgrades

def calculate_final_grade(subgrades):
    #CSP: an algorithm that includes sequencing, selection, and iteration
    #sequencing
    total = 0
    count = 0
    #iteration
    for grade in subgrades.values():
        #selection
        if grade > 1:
            total += grade
            count += 1
    return total/count

def collect_condition():
    #CSP: instructions for input from the user
    condition = {
        "Minor Corner Dings": w2n.word_to_num(input("Minor Corner Dings: ")),
        "Major Corner Dings": w2n.word_to_num(input("Major Corner Dings: ")),
        "Minor Edge Dings": w2n.word_to_num(input("Minor Edge Dings: ")),
        "Major Edge Dings": w2n.word_to_num(input("Major Edge Dings: ")),
        "Minor Surface Dings": w2n.word_to_num(input("Minor Surface Dings: ")),
        "Major Surface Dings": w2n.word_to_num(input("Major Surface Dings: ")),
        "Centering": float(input("Centering ratio (0.0-1.0): "))
    }
    return condition

def main():
    #CSP: calls to student-developed procedure
    print("\nWelcome to the card grading program.\n")

    condition = collect_condition()

    subgrades = calculate_subgrades(condition)

    print("\nSubgrades:")
    for condition, value in subgrades.items():
        print(f"{condition}: {value}")

    final_grade = calculate_final_grade(subgrades)

    #CSP: output based off input and program functionality
    print(f"\nFinal Grade: {final_grade}")

if __name__ == "__main__":
    main()
