def pit_stops(year: int, race_round: int, stop_number: int = 0, fastest: bool = False):
    args = {}
    args['year'] = year
    args['race_round'] = race_round
    args['stop_number'] = stop_number
    args['fastest'] = fastest

    return args
