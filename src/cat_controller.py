class CatController:
    CONFIG = {
        "Give water.": [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19],
        "Open cat cage.": [7],
        "Close cat cage.": [20],
        "Feed": [8, 12, 17],
        "1 mouse": [8],
        "1 hamster": [12],
        "1 chicken": [17],
    }

    def hourly_run(self, hour):
        log = []
        for action, hours in self.CONFIG.items():
            if hour in hours:
                log.append(action)
        return '\n'.join(log)
