# ==========================
# PART 1 : ARCHITECTURE
# ==========================

from src.architecture.dual_domain_architecture import DualDomainArchitecture
from src.architecture.risk_mapping import RiskMapper

print("\n" + "=" * 50)
print("MATRISK AI - PART 1")
print("=" * 50)

architecture = DualDomainArchitecture()
architecture.display_architecture()

mapper = RiskMapper()

print("\n=== RISK MAPPING ===")

for material_event, financial_event in mapper.map_material_to_finance().items():
    print(f"{material_event} --> {financial_event}")


# ==========================
# PART 2 : CRYSTAL STRUCTURE
# ==========================

from src.crystal_structure_model.crystal_encoder import CrystalEncoder
from src.crystal_structure_model.feature_builder import FeatureBuilder
from src.crystal_structure_model.property_prediction_model import (
    PropertyPredictionModel
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 2")
print("=" * 50)

# Sample Material
material = "Steel Alloy A"

# Step 1: Encode Material
encoder = CrystalEncoder()
material_data = encoder.encode(material)

print("\nMaterial Selected:")
print(material)

print("\nEncoded Material Properties:")
for key, value in material_data.items():
    print(f"{key}: {value}")

# Step 2: Build Features
builder = FeatureBuilder()
features = builder.build(material_data)

print("\nFeature Vector:")
print(features)

# Step 3: Load Model and Predict
model = PropertyPredictionModel()

predicted_strength = model.predict_strength(features)

print("\n=== PROPERTY PREDICTION RESULT ===")
print(f"Predicted Strength: {predicted_strength} MPa")

print("\nPart 2 completed successfully.")
# ==========================
# PART 3 : FAILURE MODEL
# ==========================

from src.degradation_failure_model.degradation_simulator import (
    DegradationSimulator
)

from src.degradation_failure_model.stress_strain_engine import (
    StressStrainEngine
)

from src.degradation_failure_model.failure_prediction_model import (
    FailurePredictionModel
)

from src.degradation_failure_model.risk_quantification import (
    RiskQuantification
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 3")
print("=" * 50)

simulator = DegradationSimulator()

strength_curve = simulator.simulate(
    predicted_strength,
    years=10
)

print("\nStrength Degradation Over 10 Years:")

for year, strength in enumerate(
    strength_curve,
    start=1
):
    print(
        f"Year {year}: {strength} MPa"
    )

current_strength = strength_curve[-1]

stress_engine = StressStrainEngine()

utilization = stress_engine.utilization_ratio(
    current_strength,
    applied_stress=200
)

failure_model = FailurePredictionModel()

failure_probability = failure_model.predict(
    utilization
)

risk_engine = RiskQuantification()

risk_level = risk_engine.classify(
    failure_probability
)

print("\n=== FAILURE ANALYSIS ===")

print(
    f"Current Strength: "
    f"{current_strength} MPa"
)

print(
    f"Utilization Ratio: "
    f"{utilization}"
)

print(
    f"Failure Probability: "
    f"{failure_probability}"
)

print(
    f"Risk Level: "
    f"{risk_level}"
)
# ==========================
# PART 4 : FINANCIAL RISK
# ==========================

from src.financial_risk_integration.commodity_trading_desk import (
    CommodityTradingDesk
)

from src.financial_risk_integration.price_shock_simulator import (
    PriceShockSimulator
)

from src.financial_risk_integration.infrastructure_finance import (
    InfrastructureFinance
)

from src.financial_risk_integration.capex_risk import (
    CapexRisk
)

from src.financial_risk_integration.opex_risk import (
    OpexRisk
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 4")
print("=" * 50)

commodity = CommodityTradingDesk()

commodity_risk = commodity.evaluate(
    failure_probability
)

print(
    f"\nCommodity Risk: "
    f"{commodity_risk}"
)

shock_engine = PriceShockSimulator()

new_price = shock_engine.simulate(
    base_price=100,
    risk_level=commodity_risk
)

print(
    f"Commodity Price After Shock: "
    f"${new_price}"
)

finance = InfrastructureFinance()

project_loss = finance.estimate_loss(
    project_value=10_000_000,
    failure_probability=failure_probability
)

print(
    f"Estimated Project Loss: "
    f"${project_loss:,.2f}"
)

capex = CapexRisk()

capex_loss = capex.calculate(
    10_000_000,
    failure_probability
)

print(
    f"CAPEX Risk: "
    f"${capex_loss:,.2f}"
)

opex = OpexRisk()

opex_loss = opex.calculate(
    10_000_000,
    failure_probability
)

print(
    f"OPEX Risk: "
    f"${opex_loss:,.2f}"
)
# ==========================
# PART 5 : INSURANCE & ESG
# ==========================

from src.insurance_esg.catastrophe_pricing import (
    CatastrophePricing
)

from src.insurance_esg.insurance_risk_model import (
    InsuranceRiskModel
)

from src.insurance_esg.esg_scoring_engine import (
    ESGScoringEngine
)

from src.insurance_esg.portfolio_analytics import (
    PortfolioAnalytics
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 5")
print("=" * 50)

insurance = InsuranceRiskModel()

insurance_risk = insurance.classify(
    failure_probability
)

print(
    f"\nInsurance Risk: "
    f"{insurance_risk}"
)

catastrophe = CatastrophePricing()

premium = catastrophe.calculate_premium(
    asset_value=10_000_000,
    failure_probability=failure_probability
)

print(
    f"Catastrophe Premium: "
    f"${premium:,.2f}"
)

esg_engine = ESGScoringEngine()

esg_score = esg_engine.calculate(
    failure_probability
)

print(
    f"ESG Score: "
    f"{esg_score}"
)

portfolio = PortfolioAnalytics()

portfolio_rating = portfolio.evaluate(
    esg_score
)

print(
    f"Portfolio Rating: "
    f"{portfolio_rating}"
)
# ==========================
# PART 6 : MATRISK LAB
# ==========================

from src.matrisk_lab.lab_engine import (
    MatRiskLab
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 6")
print("=" * 50)

lab = MatRiskLab()

simulation = lab.execute()

print("\nSimulation Result")

print(
    f"Event: "
    f"{simulation['event']}"
)

print(
    f"Severity: "
    f"{simulation['severity']}"
)

print(
    f"Resilience Score: "
    f"{simulation['resilience_score']}"
)
# ==========================
# PART 7 : VALIDATION
# ==========================

from src.validation.commodity_validation import (
    CommodityValidation
)

from src.validation.infrastructure_validation import (
    InfrastructureValidation
)

from src.validation.insurance_validation import (
    InsuranceValidation
)

from src.validation.metrics import (
    Metrics
)

from src.validation.benchmark_tests import (
    BenchmarkTests
)

print("\n" + "=" * 50)
print("MATRISK AI - PART 7")
print("=" * 50)

commodity_test = CommodityValidation().run()

infrastructure_test = (
    InfrastructureValidation().run()
)

insurance_test = (
    InsuranceValidation().run()
)

metrics = Metrics().calculate()

benchmarks = BenchmarkTests().run()

print("\nCommodity Validation")
print(commodity_test)

print("\nInfrastructure Validation")
print(infrastructure_test)

print("\nInsurance Validation")
print(insurance_test)

print("\nPerformance Metrics")
print(metrics)

print("\nBenchmark Results")
print(benchmarks)