class GamifiedSimulation:

    def run(
        self,
        event,
        severity,
        score
    ):

        return {

            "event": event,
            "severity": severity,
            "resilience_score": score
        }