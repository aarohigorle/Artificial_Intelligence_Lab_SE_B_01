def career(interests):
    interests = [interest.capitalize() for interest in interests]
    if 'Maths' in interests and 'Physics' in interests:
        print("Suggested Career Path: Mechanical Engineering")
    elif 'Programming' in interests and 'Maths' in interests:
        print("Suggested Career Path: Computer Engineering")
    elif 'Biology' in interests and 'Chemistry' in interests:
        print("Suggested Career Path: Biotechnology")
    elif 'Circuits' in interests and 'Maths' in interests:
        print("Suggested Career Path: Electronics Engineering")
    else:
        print("No clear suggestion based on current interests. Try more specific or different combinations.")

def main():
    print("Welcome to the Career Path Expert System!")
    user_input = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests = user_input.split(',')
    career(interests)

if __name__ == "__main__":
    main()

          
