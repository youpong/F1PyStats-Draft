class TestPitStops:
    import f1pystats.f1pystats as fp

    def test_pit_stops(self):
        args = self.fp.pit_stops(2023, 24, 1)
        assert args['year'] == 2023
        assert args['race_round'] == 24
        assert args['stop_number'] == 1
        assert args['fastest'] == False

    def test_pit_stopsA(self):
        args = self.fp.pit_stopsA(2023, 24, 1)
        assert args['year'] == 2023
        assert args['race_round'] == 24
        assert args['stop_number'] == 1 # fail here
        assert args['fastest'] == False

    def test_pit_stopsB(self):
        args = self.fp.pit_stopsB(2023, 24, 1)
        assert args['year'] == 2023
        assert args['race_round'] == 24
        assert args['stop_number'] == 1
        assert args['fastest'] == False

    def test_pit_stopsC(self):
        args = self.fp.pit_stopsC(2023, 24, 1) # fail here
        assert args['year'] == 2023
        assert args['race_round'] == 24
        assert args['stop_number'] == 1
        assert args['fastest'] == False
