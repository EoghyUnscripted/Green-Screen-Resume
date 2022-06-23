from .data import data_compiler as compiler, typewriter as typer, snooze


def profile():
    """ Function used to get profile information. """

    data = compiler()
    profile = data[0]["profile"]

    typer(f'Name: {profile["name"]}\n'
          + f'Title: {profile["title"]}\n'
          + f'Pronouns: {profile["pronouns"]}\n'
          + f'Profile: {profile["profile"]}')


def contact():
    """ Function used to get contact information. """

    data = compiler()

    contact = data[0]["contact"]

    typer(f'Email: {contact["email"]}\n'
          + f'Hacker Rank: {contact["hacker rank"]}\n'
          + f'Replit: {contact["replit"]}\n'
          + f'LinkedIn: {contact["linkedin"]}\n'
          + f'Location: {contact["location"]}')


def about():
    """ Function used to get personal profile information. """

    data = compiler()
    about = data[0]["about me"]

    nickname_string = ""
    keyword_string = ""
    phrases_string = ""

    nicknames = [i for i in about["nicknames"]]
    keywords = [i for i in about["keywords"]]
    phrases = [i for i in about["common phrases"]]

    for i in nicknames:
        nickname_string += i + "\n"

    for i in keywords:
        keyword_string += i + "\n"

    for i in phrases:
        phrases_string += i + "\n"

    typer(f'My name is Eoghan,'
          + f' but others have also called me:\n{nickname_string}')

    snooze()

    typer(f'I have been described as:\n{keyword_string}')

    snooze()

    typer(f'Some of my common phrases are:\n{phrases_string}')

    snooze()

    typer(f'If I had a theme song, it would probably be: {about["theme song"]}\n'
          + f'I didn\'t choose it, it chose me.')

    snooze()

    typer(f'My last exotic trip was to... {about["last trip"]}.')

    snooze()


def fun_facts():
    """ Function used to get fun facts information. """

    data = compiler()

    fun_facts_string = ""

    fun_facts = [i for i in data[0]["fun facts"]]

    for i in fun_facts:
        fun_facts_string += (f"- {i}\n")

    typer(f'Some fun facts:\n\n{fun_facts_string}')


def education():
    """ Function to get educational information. """

    data = compiler()

    academic = data[0]["education"]["academic"]
    independent = data[0]["education"]["independent"]

    academic_string = ""

    for i in academic:

        academic_string += (f"ACADEMIC:\n"
                            + f"\n[{i['year']}]\n"
                            + f"\n{i['degree']}\n"
                            + f"{str(i['name']).upper()} - {i['city']}\n"
                            + f"\nGPA: {i['gpa']}\n"
                            + f"\n- {i['description'][0]}\n")

    for i in independent:

        academic_string += (f"\n\nINDEPENDENT LEARNING:\n"
                            + f"\n[{i['years']}]\n"
                            + f"\n{str(i['name']).upper()}\n")

        for j in i['description']:

            academic_string += (f"\n- {j}\n")

    typer(academic_string)

    snooze(10)


def experience():
    """ Function to get educational information. """

    data = compiler()

    relevant = data[0]["experience"]["relevant"]
    other = data[0]["experience"]["other"]

    experience_string = (f"RELEVANT EXPERIENCE:\n")

    for i in relevant:

        experience_string += (f"\n\n[{i['duration']}]\n"
                              + f"\n{i['title']}\n"
                              + f"{str(i['name']).upper()} - {i['city']}\n")

        for j in i['description']:

            experience_string += (f"\n{' ' * 2}- {j}\n")

    experience_string += (f"\n\nOTHER EXPERIENCE:\n")

    for i in other:

        experience_string += (f"\n\n[{i['duration']}]\n"
                              + f"\n{i['title']}\n"
                              + f"{str(i['name']).upper()} - {i['city']}\n")

        for j in i['description']:

            if len(i['description']) > 1:
                experience_string += (f"- {j}\n")

    typer(experience_string)

    snooze(15)


def qualifications():
    """ Function to get educational information. """

    data = compiler()

    qualifications = data[0]["qualifications"]

    qualifications_string = (f"QUALIFICATIONS:\n\n")

    for i in qualifications:

        qualifications_string += (f"- {i}\n")

    typer(qualifications_string)

    snooze()


def skills():
    """ Function to get educational information. """

    data = compiler()

    skills = data[0]["skills"][0]

    skills_string = (f"SKILLS:\n")

    for i in skills:

        skills_string += (f"\n{str(i).capitalize()}\n\n")

        for j in skills[i]:

            skills_string += (f" [{j}] ")

    typer(skills_string)

    snooze()


def get_function(index):
    """ Function used to call another function for main. """

    index = int(index)

    functions = [
        profile,
        about,
        qualifications,
        contact,
        education,
        experience,
        skills,
        fun_facts
    ]

    try:

        functions[index]()
        snooze(10)

    except:

        print(index)
        print(f"\nSorry, that section does not exist. Try another option!")
        response = input()

        if response.lower() == "quit":
            typer("Exiting... Goodbye!")
            quit()

        else:
            get_function(response)
