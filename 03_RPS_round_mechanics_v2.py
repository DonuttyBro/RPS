#Function used to check input is valid


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


#Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

#Ask user for # of rounds, <eneter> for infinite mode
rounds = check_rounds()

mode = ""

if rounds == "":
    mode = "infinite"
    rounds = 10

end_game = "no"
while end_game == "no":

    rounds_played += 1

    # incresase rounds so infinite mode is actually infinite
    if mode == "infinite":
        rounds += 1

    #Start of Game Play Loop

    #Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played)
    else:
        heading = "Round {} of {}".format(rounds_played, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    #End game if exit code is typed
    if choose == "xxx" or rounds_played >= rounds:
        break

# **** rest of loop / game ****