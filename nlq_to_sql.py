def nlq_to_sql(nlq):
    nlq = nlq.lower()

    # Marks sorting
    if "marks" in nlq:
        if "desc" in nlq or "descending" in nlq:
            return "SELECT * FROM students ORDER BY marks DESC;"
        elif "asc" in nlq or "ascending" in nlq:
            return "SELECT * FROM students ORDER BY marks ASC;"

    # Name sorting
    if "name" in nlq:
        if "desc" in nlq or "reverse" in nlq:
            return "SELECT * FROM students ORDER BY name DESC;"
        else:
            return "SELECT * FROM students ORDER BY name ASC;"

    # Age sorting
    if "age" in nlq:
        if "youngest" in nlq or "asc" in nlq or "ascending" in nlq:
            return "SELECT * FROM students ORDER BY age ASC;"
        elif "oldest" in nlq or "desc" in nlq or "descending" in nlq:
            return "SELECT * FROM students ORDER BY age DESC;"

    # For Multiple columns and different commands
    if "column1" in nlq and "column2" in nlq:
        if "column1 in desc" in nlq or "column1 in descending" in nlq:
            col1_order = "DESC"
        else:
            col1_order = "ASC"

        if "column2 in desc" in nlq or "column2 in descending" in nlq:
            col2_order = "DESC"
        else:
            col2_order = "ASC"

        return f"SELECT * FROM students ORDER BY column1 {col1_order}, column2 {col2_order};"

    return "Wrong query"
myinput= input("Enter your query in plain English: ")
print("SQL:", nlq_to_sql(myinput))


