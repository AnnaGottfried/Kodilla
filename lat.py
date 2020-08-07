import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":

    if len(sys.argv)<2:
        exit(1)
    age = int(sys.argv[1])
    print_maturity(age)