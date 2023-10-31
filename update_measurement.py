def update_measurement_result(measurement_result):
    measurement_weight = {
    "身高": 1.0,
    "头围": 1.0,
    "颈围": 0.95,
    "肩宽": 1.02,
    "胸围": 0.91,
    "腰围": 0.8769,
    "臀围": 1.0,
    "左大臂围": 1.0,
    "右大臂围": 1.0,
    "左大臂长": 1.0026,
    "右大臂长": 1.0,
    "左小臂长": 1.0455,
    "右小臂长": 1.0,
    "左大腿围": 0.98,
    "右大腿围": 0.98,
    "左大腿长": 0.9575,
    "右大腿长": 0.95,
    "左小腿长": 1.1,
    "右小腿长": 1.1,
    "左臂长":[1,1],
    "右臂长":[1,1],
    "左腿长": [1,1.1], # [大腿，小腿]
    "右腿长": [1,1.1], # [大腿，小腿]
    }
    # Define the new keys and their related component measurements
    composite_measurements = {
        "左臂长": ["左小臂长", "左大臂长"],
        "右臂长": ["右小臂长", "右大臂长"],
        "左腿长": ["左大腿长", "左小腿长"],
        "右腿长": ["右大腿长", "右小腿长"]
    }

    # Iterate through the keys and compute their values if they don't exist
    for key, components in composite_measurements.items():
        if key not in measurement_result:
            left_multiplier, right_multiplier = measurement_weight[key]
            measurement_result[key] = (measurement_result[components[0]] * left_multiplier +
                                    measurement_result[components[1]] * right_multiplier)
        else:
            left_multiplier, right_multiplier = measurement_weight[key]
            measurement_result[key] = (measurement_result[components[0]] * left_multiplier +
                                    measurement_result[components[1]] * right_multiplier)
    # Continue with the original loop for the other measurements
    for key, value in measurement_result.items():
        if type(measurement_weight[key]) is int:  # Single multiplier
            measurement_result[key] = value * measurement_weight[key]
    return measurement_result

if __name__ == '__main__':
    measurement_result = {
    "身高": 174.24,
    "头围": 55.52,
    "颈围": 38.33,
    "肩宽": 38.28,
    "胸围": 98.63,
    "腰围": 88.93,
    "臀围": 98.53,
    "左大臂围": 29.89,
    "右大臂围": 29.53,
    "左大臂长": 29.31,
    "右大臂长": 29.36,
    "左小臂长": 23.18,
    "右小臂长": 23.85,
    "左大腿围": 57.64,
    "右大腿围": 57.25,
    "左大腿长": 43.58,
    "右大腿长": 43.45,
    "左小腿长": 37.69,
    "右小腿长": 37.69,  	
       "左臂长":45.29,
    "右臂长":46.81,
    "左腿长":70.96,
    "右腿长":71.04, 	
    }
    measurement_result = update_measurement_result(measurement_result)
    print(measurement_result)
        