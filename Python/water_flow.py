#Calculates and returns the height of a column of wather from a tower and tank wall height.

def water_column_height(tower_height, tank_height):
    h = tower_height + ( 3 * tank_height) / 4
    return h

#Calculates and returns the pressure caused by Earth's gravity

def pressure_gain_from_water_height(height):
    p = 998.2
    g = 9.80665

    P = ( p * g * height) / 1000
    return P


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Given constant for the density of water in kg/m^3
    water_density = 998.2  # kg/m^3
    
    # Calculate the pressure loss using the provided formula
    pressure_loss = (-friction_factor * pipe_length * water_density * fluid_velocity**2) / (2000 * pipe_diameter)
    
    # Return the pressure loss value
    return pressure_loss