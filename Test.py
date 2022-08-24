def leap_year(year) :
    
    defa = 2021

    if year%4==0 and year %100==0 and year%400==0 : 
        print("Year " + str(year) + " was a leap year")
    else:
        print("Year " + str(year) + " was not a leap year")

leap_year(1)
leap_year(100)
leap_year(2000)
leap_year(2019)
leap_year(2040)
leap_year(2100)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)