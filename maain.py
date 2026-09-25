import random
subjects = [
    "Pranjal",
    "Zeny",
    "Yojan",
    "Sharad",
    "Hulku"
    "Liza"
]

actions =[
    "playing",
    "danching",
    "creating",
    "paintiing",
    "shoting",
    "reading",
    "declares war on"
]

places_or_things = [
    "the park",
    "bedroom",
    "highway",
    "picture",
    "book",
    "the world"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f" Breaking News: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("Do you want to generate another headline? (y/n): ").strip().lower()
    if user_input == "no":
        break

    print("\nThanks for using the fake news headline generator!")
