class TestPitStops:
    import f1pystats.f1pystats as fp

    def test_pit_stops_race(self):
        args = self.fp.pit_stops(2023, 24)
        assert args['year'] == 2023
        assert args['race_round'] == 24
        assert args['stop_number'] == 0
        assert args['fastest'] == False
