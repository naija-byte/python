def report_books_issued():
    issues = load_csv(ISSUE_FILE)
    print("\nBooks currently issued:")
    for i in issues:
        if i["ReturnDate"] == "":
            print(f"BookID: {i['BookID']} issued to MemberID: {i['MemberID']} on {i['IssueDate']}")
    print()

def report_by_date():
    issues = load_csv(ISSUE_FILE)
    date = input("Enter Issue Date (DD-MM-YYYY): ")
    print(f"\nMembers who issued books on {date}:")
    for i in issues:
        if i["IssueDate"] == date:
            print(f"MemberID: {i['MemberID']} | BookID: {i['BookID']}")
    print()

def report_pending_returns():
    issues = load_csv(ISSUE_FILE)
    print("\nMembers with pending returns:")
    for i in issues:
        if i["ReturnDate"] == "":
            print(f"MemberID: {i['MemberID']} has not returned BookID: {i['BookID']}")
    print()

def main_menu():
    while True:
        print("""
===== Library Management System =====
1. Add Book
2. Display Books
3. Delete Book
4. Register Member
5. Display Members
6. Issue Book
7. Return Book
8. Report: Books currently issued
9. Report: Members who issued on specific date
10. Report: Pending returns
0. Exit
""")
        ch = input("Enter your choice: ")
        if ch == "1": add_book()
        elif ch == "2": display_books()
        elif ch == "3": delete_book()
        elif ch == "4": add_member()
        elif ch == "5": display_members()
        elif ch == "6": issue_book()
        elif ch == "7": return_book()
        elif ch == "8": report_books_issued()
        elif ch == "9": report_by_date()
        elif ch == "10": report_pending_returns()
        elif ch == "0":
            print("Thank you for using Library System!")
            break
        else:
            print("Invalid choice!\n")

main_menu()
