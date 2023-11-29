def main():
    print("Email slicer ")
    print("")

    email_input= input("Input your email address: ")


    (username, domain) = email_input.split("@")
    (domain, extenstion) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extenstion)

main()