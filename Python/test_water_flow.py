from pytest import approx
import pytest

from water_flow import water_column_height
from water_flow import pressure_gain_from_water_height
from water_flow import pressure_loss_from_pipe

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)
    
def test_pressure_gain_from_water_height():
    # Test case 1: Height of 0.0 meters
    # The expected pressure should be 0.0 kPa
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)

    # Test case 2: Height of 30.2 meters
    # Calculate the expected pressure using the formula P = (ρ * g * h) / 1000
    expected_pressure_30_2 = (998.2 * 9.80665 * 30.2) / 1000  # Expected pressure in kPa
    assert pressure_gain_from_water_height(30.2) == approx(expected_pressure_30_2, abs=0.001)

    # Test case 3: Height of 50.0 meters
    # Calculate the expected pressure using the same formula
    expected_pressure_50_0 = (998.2 * 9.80665 * 50.0) / 1000  # Expected pressure in kPa
    assert pressure_gain_from_water_height(50.0) == approx(expected_pressure_50_0, abs=0.001)

def test_pressure_loss_from_pipe():
    # Test case 1
    result = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75)
    assert abs(result - 0.000) < 0.001, f"Test failed for case 1: {result}"

    # Test case 2
    result = pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75)
    assert abs(result - 0.000) < 0.001, f"Test failed for case 2: {result}"

    # Test case 3
    result = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00)
    assert abs(result - 0.000) < 0.001, f"Test failed for case 3: {result}"

    # Test case 4
    result = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75)
    assert abs(result + 113.008) < 0.001, f"Test failed for case 4: {result}"

    # Test case 5
    result = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65)
    assert abs(result + 100.462) < 0.001, f"Test failed for case 5: {result}"

    # Test case 6
    result = pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65)
    assert abs(result + 61.576) < 0.001, f"Test failed for case 6: {result}"

    # Test case 7
    result = pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65)
    assert abs(result + 110.884) < 0.001, f"Test failed for case 7: {result}"



pytest.main(["-v", "--tb=line", "-rN", __file__])