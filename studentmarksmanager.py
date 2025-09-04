def show_menu():
    print("\n--- Student Marks Manager ---")
    print("1. Add Mark")
    print("2. View Marks")
    print("3. Average Marks")
    print("4. Highest & Lowest Mark")
    print("5. Search a Mark")
    print("0. Exit")

marks = []

while True:
    show_menu()
    choice = int(input("Enter choice: "))

    if choice == 0:
        print("Exiting...")
        break

    elif choice == 1:
        m = int(input("Enter mark: "))
        marks.append(m)
        print("Mark added!")

    elif choice == 2:
        print("Marks:", marks)

    elif choice == 3:
        if marks:
            avg = sum(marks) / len(marks)
            print("Average Marks:", avg)
        else:
            print("No marks available!")

    elif choice == 4:
        if marks:
            print("Highest:", max(marks))
            print("Lowest:", min(marks))
        else:
            print("No marks available!")

    elif choice == 5:
        s = int(input("Enter mark to search: "))
        if s in marks:
            print(f"{s} found at index {marks.index(s)}")
        else:
            print("Mark not found!")

    else:
        print("Invalid choice! Try again.")

