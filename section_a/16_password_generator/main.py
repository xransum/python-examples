"""Password Generator.

Write a password generator in Python. Be
creative with how you generate passwords -
strong passwords have a mix of lowercase
letters, uppercase letters, numbers, and
symbols. The passwords should be random,
generating a new password every time the
user asks for a new password. Include your
run-time code in a main method.

Extra:
    - Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
from random import choices, shuffle

words = "angle, ant, apple, arch, arm, army, baby, bag, ball, band, basin, basket, bath, bed, bee, bell, berry, bird, blade, board, boat, bone, book, boot, bottle, box, boy, brain, brake, branch, brick, bridge, brush, bucket, bulb, button, cake, camera, card, cart, carriage, cat, chain, cheese, chest, chin, church, circle, clock, cloud, coat, collar, comb, cord, cow, cup, curtain, cushion, dog, door, drain, drawer, dress, drop, ear, egg, engine, eye, face, farm, feather, finger, fish, flag, floor, fly, foot, fork, fowl, frame, garden, girl, glove, goat, gun, hair, hammer, hand, hat, head, heart, hook, horn, horse, hospital, house, island, jewel, kettle, key, knee, knife, knot, leaf, leg, library, line, lip, lock, map, match, monkey, moon, mouth, muscle, nail, neck, needle, nerve, net, nose, nut, office, orange, oven, parcel, pen, pencil, picture, pig, pin, pipe, plane, plate, plough, pocket, pot, potato, prison, pump, rail, rat, receipt, ring, rod, roof, root, sail, school, scissors, screw, seed, sheep, shelf, ship, shirt, shoe, skin, skirt, snake, sock, spade, sponge, spoon, spring, square, stamp, star, station, stem, stick, stocking, stomach, store, street, sun, table, tail, thread, throat, thumb, ticket, toe, tongue, tooth, town, train, tray, tree, trousers, umbrella, wall, watch, wheel, whip, whistle, window, wing, wire, worm".split(", ")
shuffle(words)
alpha_lower = list("abcdefghijklmnopqrstuvwxyz")
alpha_upper = [c.upper() for c in alpha_lower]
numeric = list("0123456789")
special = list("!@#$%^&*()_+=[]{}|;:<>.?/")

def generate_password(segs, total_segs):
    """Generate a password of N elements from a given list of values."""
    shuffle(segs)
    values = choices(segs, k=total_segs)
    return "".join(values)


strengths = ["weak", "medium", "strong"]

def main():
    """Main function."""
    print("Password Generator -")
    for s in range(len(strengths)):
        strength = strengths[s]
        print(f"{s + 1}. {strength}")

    opt = int(input("Select a Password Strength: ")) - 1
    if 0 > opt <= len(strengths):
        print("Invalid option selected.")

    option = strengths[opt]
    password = ""
    if option == "strong":
        password = generate_password([*alpha_lower, *alpha_upper, *numeric, *special], 21)
    elif option == "medium":
        password = generate_password([*words[0:10], *numeric], 8)
    else:
        password = generate_password(words, 2)

    print(password)

if __name__ == "__main__":
    main()