def add_member():
    members = load_csv(MEMBER_FILE)
    mid = input("Enter Member ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    members.append({"MemberID": mid, "Name": name, "Phone": phone})
    save_csv(MEMBER_FILE, members, ["MemberID", "Name", "Phone"])
    print("Member registered successfully!\n")

def display_members():
    members = load_csv(MEMBER_FILE)
    print("\n--- Member List ---")
    for m in members:
        print(f"{m['MemberID']} | {m['Name']} | {m['Phone']}")
    print()

def issue_book():
    books = load_csv(BOOK_FILE)
    members = load_csv(MEMBER_FILE)
    issues = load_csv(ISSUE_FILE)
    bid = input("Enter Book ID: ")
    mid = input("Enter Member ID: ")
    book = next((b for b in books if b["BookID"] == bid and b["Available"] == "Yes"), None)
    member = next((m for m in members if m["MemberID"] == mid), None)
    if book and member:
        date = input("Enter Issue Date (DD-MM-YYYY): ")
        issues.append({"BookID": bid, "MemberID": mid, "IssueDate": date, "ReturnDate": "", "Fine": "0"})
        book["Available"] = "No"
        save_csv(BOOK_FILE, books, ["BookID", "Title", "Author", "Available"])
        save_csv(ISSUE_FILE, issues, ["BookID", "MemberID", "IssueDate", "ReturnDate", "Fine"])
        print("Book issued successfully!\n")
    else:
        print("Invalid Book ID or Member ID / Book not available.\n")

def return_book():
    issues = load_csv(ISSUE_FILE)
    books = load_csv(BOOK_FILE)
    bid = input("Enter Book ID to return: ")
    mid = input("Enter Member ID: ")
    for i in issues:
        if i["BookID"] == bid and i["MemberID"] == mid and i["ReturnDate"] == "":
            return_date = input("Enter Return Date (DD-MM-YYYY): ")
            fine = input("Enter Fine Amount (if any): ")
            i["ReturnDate"] = return_date
            i["Fine"] = fine
            for b in books:
                if b["BookID"] == bid:
                    b["Available"] = "Yes"
            save_csv(ISSUE_FILE, issues, ["BookID", "MemberID", "IssueDate", "ReturnDate", "Fine"])
            save_csv(BOOK_FILE, books, ["BookID", "Title", "Author", "Available"])
            print("Book returned successfully!\n")
            return
    print("No matching issued book found.\n")
