def main():
    
    # Asking user for a year
    year = input("Give me a year: ")
    year = int(year)

    # Testing if the 'year' is a leap year
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False

    # Testing 'leap' to create a message
    if leap:
        message = "is a leap year."
    else:
        message = "is not a leap year."

    print(year, message)


if __name__ == '__main__':
    main()