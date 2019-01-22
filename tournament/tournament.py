def tally(input_string):
    results = dict()
    teams = []
    if input_string:
        lines = input_string.split("\n")
        for line in lines:
            team1, team2, result = line.split(";")
            if team1 not in results:
                results.update({team1: {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}})
            if team2 not in results:
                results.update({team2: {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}})
            if result == 'win':
                results[team1]['W'] += 1
                results[team1]['P'] += 3
                results[team2]['L'] += 1
            elif result == 'draw':
                results[team1]['D'] += 1
                results[team1]['P'] += 1
                results[team2]['D'] += 1
                results[team2]['P'] += 1
            else:
                results[team1]['L'] += 1
                results[team2]['W'] += 1
                results[team2]['P'] += 3
            results[team1]['MP'] += 1
            results[team2]['MP'] += 1
        teams = sorted(sorted(results), key=lambda x: results[x]['P'], reverse=True)
    return "Team                           | MP |  W |  D |  L |  P" + \
           "".join(("\n" + team.ljust(31) + "|" + str(results[team]['MP']).rjust(3) + " |" +
                    str(results[team]['W']).rjust(3) + " |" + str(results[team]['D']).rjust(3) + " |" +
                    str(results[team]['L']).rjust(3) + " |" + str(results[team]['P']).rjust(3) for team in teams))
