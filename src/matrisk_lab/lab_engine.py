from src.matrisk_lab.shock_generator import ShockGenerator
from src.matrisk_lab.scenario_manager import ScenarioManager
from src.matrisk_lab.score_tracker import ScoreTracker
from src.matrisk_lab.gamified_simulation import (
    GamifiedSimulation
)

class MatRiskLab:

    def execute(self):

        shock = ShockGenerator()

        event = shock.generate()

        manager = ScenarioManager()

        severity = manager.severity(event)

        tracker = ScoreTracker()

        score = tracker.calculate_score(
            severity
        )

        game = GamifiedSimulation()

        return game.run(
            event,
            severity,
            score
        )