def pit_stops(year: int, race_round: int, stop_number: int = 0, fastest: bool = False):
    args = {}
    args['year'] = year
    args['race_round'] = race_round
    args['stop_number'] = stop_number
    args['fastest'] = fastest

    return args

def pit_stopsA(year: int, race_round: int, driver_id: str=None, stop_number: int = 0, fastest: bool = False):
    args = {}
    args['year'] = year
    args['race_round'] = race_round
    args['stop_number'] = stop_number
    args['fastest'] = fastest

    return args

def pit_stopsB(year: int, race_round: int, stop_number: int = 0, fastest: bool = False, driver_id: str=None):
    args = {}
    args['year'] = year
    args['race_round'] = race_round
    args['stop_number'] = stop_number
    args['fastest'] = fastest

    return args

def pit_stopsC(year: int, race_round: int, *, stop_number: int = 0, fastest: bool = False, driver_id: str=None):
    args = {}
    args['year'] = year
    args['race_round'] = race_round
    args['stop_number'] = stop_number
    args['fastest'] = fastest

    return args
