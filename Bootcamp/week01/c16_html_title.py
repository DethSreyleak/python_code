user_input = input("Enter a title: ")
result = user_input.title()
if user_input == "":
    print("Nothing to display.")
else:
    print("<h1>"+ result +"</h1>")
    