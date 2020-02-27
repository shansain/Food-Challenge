def challenge_list(request):
    challenge_list = [
        "Chinese food challenge",
        "Vegan Instant",
        "Food Diggers",
        "Indian food challenge",
        "Special challenge for a limited time",
        "Jerusalem Challenge",
        "The Shawarma Challenge",
    ]
    return {'challenge_list': challenge_list}
