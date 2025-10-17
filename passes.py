# passes.py

def calculate_passes(initial_width, initial_height, initial_length, target_thicknesses, passes_count, reduction_percent):
    """
    Calculate passes dynamically.
    initial_width, initial_height, initial_length in mm
    target_thicknesses: list of final thicknesses to be reached (mm)
    passes_count: total number of passes (int)
    reduction_percent: % reduction per pass (approximate)
    
    Returns:
    List of dicts with each pass details.
    """
    passes = []
    volume = initial_width * initial_height * initial_length  # volume constant (mm^3)

    current_thickness = max(initial_width, initial_height)  # Assume square billet, thickness = max side initially
    current_length = initial_length

    for stage in range(1, passes_count + 1):
        # Calculate reduction for this pass
        reduction = reduction_percent
        
        # Reduce thickness by reduction%
        new_thickness = current_thickness * (1 - reduction / 100)
        if new_thickness < min(target_thicknesses):
            new_thickness = min(target_thicknesses)

        # Calculate new length to keep volume constant: volume = thickness^2 * length (approximation for square/round)
        # length = volume / (thickness^2)
        new_length = volume / (new_thickness ** 2)

        # Pressure estimation: assume linear relation with reduction (example)
        pressure = reduction * 10  # Just an example scale factor

        # Shape selection based on stage (example logic)
        if stage % 3 == 1:
            shape = 'round'
        elif stage % 3 == 2:
            shape = 'oval'
        else:
            shape = 'square'

        pass_info = {
            "stage": stage,
            "name": f"Pass {stage}",
            "desc": f"Thickness: {new_thickness:.1f} mm, Length: {new_length:.0f} mm",
            "shape": shape,
            "diameter": new_thickness,
            "length": new_length,
            "reduction": reduction,
            "pressure": pressure
        }

        passes.append(pass_info)

        # Update for next iteration
        current_thickness = new_thickness
        current_length = new_length

        # Stop if reached minimum target thickness
        if new_thickness <= min(target_thicknesses):
            break

    return passes
