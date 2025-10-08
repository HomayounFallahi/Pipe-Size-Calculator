# This Python script calculates the Outer Diameter (OD), Inner Diameter (ID),
# and Wall Thickness of pipes based on their nominal size and schedule.
# The data used for lookup is provided in the problem description.

def get_pipe_dimensions(pipe_size_input, schedule_input):
    """
    Retrieves the OD, ID, and Wall Thickness for a given pipe nominal size and schedule.

    Args:
        pipe_size_input (str): The nominal pipe size (e.g., "1/8", "1", "2 1/2").
                                The input can include '"' (e.g., "1/8\"") but it will be removed.
        schedule_input (str): The pipe schedule (e.g., "40", "STD", "XS", "160").

    Returns:
        dict or str: A dictionary containing 'OD', 'ID', and 'Wall' if a match is found,
                     otherwise a string indicating that the data was not found.
    """

    # Normalize the input pipe size by removing quotes and standardizing spaces
    # This helps in matching user input with the data structure
    normalized_pipe_size = pipe_size_input.replace('"', '').strip()
    normalized_schedule = schedule_input.upper().strip() # Convert schedule to uppercase for consistent matching

    # Data structure containing pipe dimensions based on nominal size and schedule.
    # This dictionary is structured for efficient lookup:
    # {
    #   "Pipe Size": {
    #     "OD": <Outer Diameter>,
    #     "schedules": {
    #       ("Schedule1", "Schedule2"): {"ID": <Inner Diameter>, "Wall": <Wall Thickness>},
    #       ...
    #     }
    #   },
    #   ...
    # }
    pipe_data = {
        "1/8": {
            "OD": 0.405,
            "schedules": {
                ("10", "10S"): {"ID": 0.307, "Wall": 0.049},
                ("40", "STD", "40S"): {"ID": 0.269, "Wall": 0.068},
                ("80", "XS", "80S"): {"ID": 0.215, "Wall": 0.095}
            }
        },
        "1/4": {
            "OD": 0.54,
            "schedules": {
                ("10", "10S"): {"ID": 0.41, "Wall": 0.065},
                ("40", "STD", "40S"): {"ID": 0.364, "Wall": 0.088},
                ("80", "XS", "80S"): {"ID": 0.302, "Wall": 0.119}
            }
        },
        "3/8": {
            "OD": 0.675,
            "schedules": {
                ("10", "10S"): {"ID": 0.545, "Wall": 0.065},
                ("40", "STD", "40S"): {"ID": 0.493, "Wall": 0.091},
                ("80", "XS", "80S"): {"ID": 0.423, "Wall": 0.126}
            }
        },
        "1/2": {
            "OD": 0.84,
            "schedules": {
                ("5", "5S"): {"ID": 0.71, "Wall": 0.065},
                ("10", "10S"): {"ID": 0.674, "Wall": 0.083},
                ("40", "STD", "40S"): {"ID": 0.622, "Wall": 0.109},
                ("80", "XS", "80S"): {"ID": 0.546, "Wall": 0.147},
                ("160",): {"ID": 0.466, "Wall": 0.187},
                ("XX",): {"ID": 0.252, "Wall": 0.294}
            }
        },
        "3/4": {
            "OD": 1.05,
            "schedules": {
                ("5", "5S"): {"ID": 0.92, "Wall": 0.065},
                ("10", "10S"): {"ID": 0.884, "Wall": 0.083},
                ("40", "STD", "40S"): {"ID": 0.824, "Wall": 0.113},
                ("80", "XS", "80S"): {"ID": 0.742, "Wall": 0.154},
                ("160",): {"ID": 0.614, "Wall": 0.218},
                ("XX",): {"ID": 0.434, "Wall": 0.308}
            }
        },
        "1": {
            "OD": 1.315,
            "schedules": {
                ("5", "5S"): {"ID": 1.185, "Wall": 0.065},
                ("10", "10S"): {"ID": 1.097, "Wall": 0.109},
                ("40", "STD", "40S"): {"ID": 1.049, "Wall": 0.133},
                ("80", "XS", "80S"): {"ID": 0.957, "Wall": 0.179},
                ("160",): {"ID": 0.815, "Wall": 0.25},
                ("XX",): {"ID": 0.599, "Wall": 0.358}
            }
        },
        "1 1/4": {
            "OD": 1.66,
            "schedules": {
                ("5", "5S"): {"ID": 1.53, "Wall": 0.065},
                ("10", "10S"): {"ID": 1.442, "Wall": 0.109},
                ("40", "STD", "40S"): {"ID": 1.38, "Wall": 0.14},
                ("80", "XS", "80S"): {"ID": 1.278, "Wall": 0.191},
                ("160",): {"ID": 1.16, "Wall": 0.25},
                ("XX",): {"ID": 0.896, "Wall": 0.382}
            }
        },
        "1 1/2": {
            "OD": 1.9,
            "schedules": {
                ("5", "5S"): {"ID": 1.77, "Wall": 0.065},
                ("10", "10S"): {"ID": 1.682, "Wall": 0.109},
                ("40", "STD", "40S"): {"ID": 1.61, "Wall": 0.145},
                ("80", "XS", "80S"): {"ID": 1.5, "Wall": 0.2},
                ("160",): {"ID": 1.337, "Wall": 0.281},
                ("XX",): {"ID": 1.1, "Wall": 0.4}
            }
        },
        "2": {
            "OD": 2.375,
            "schedules": {
                ("5", "5S"): {"ID": 2.225, "Wall": 0.065},
                ("10", "10S"): {"ID": 2.157, "Wall": 0.109},
                ("40", "STD", "40S"): {"ID": 2.067, "Wall": 0.154},
                ("80", "XS", "80S"): {"ID": 1.939, "Wall": 0.218},
                ("160",): {"ID": 1.687, "Wall": 0.344},
                ("XX",): {"ID": 1.503, "Wall": 0.436}
            }
        },
        "2 1/2": {
            "OD": 2.875,
            "schedules": {
                ("5", "5S"): {"ID": 2.709, "Wall": 0.083},
                ("10", "10S"): {"ID": 2.635, "Wall": 0.12},
                ("40", "STD", "40S"): {"ID": 2.469, "Wall": 0.203},
                ("80", "XS", "80S"): {"ID": 2.323, "Wall": 0.276},
                ("160",): {"ID": 2.125, "Wall": 0.375},
                ("XX",): {"ID": 1.771, "Wall": 0.552}
            }
        },
        "3": {
            "OD": 3.5,
            "schedules": {
                ("5", "5S"): {"ID": 3.334, "Wall": 0.083},
                ("10", "10S"): {"ID": 3.26, "Wall": 0.12},
                ("40", "STD", "40S"): {"ID": 3.068, "Wall": 0.216},
                ("80", "XS", "80S"): {"ID": 2.9, "Wall": 0.3},
                ("160",): {"ID": 2.624, "Wall": 0.438},
                ("XX",): {"ID": 2.3, "Wall": 0.6}
            }
        },
        "3 1/2": {
            "OD": 4.0,
            "schedules": {
                ("5", "5S"): {"ID": 3.834, "Wall": 0.083},
                ("10", "10S"): {"ID": 3.76, "Wall": 0.12},
                ("40", "STD", "40S"): {"ID": 3.548, "Wall": 0.226},
                ("80", "XS", "80S"): {"ID": 3.364, "Wall": 0.318},
                ("XX",): {"ID": 2.728, "Wall": 0.636}
            }
        },
        "4": {
            "OD": 4.5,
            "schedules": {
                ("5", "5S"): {"ID": 4.334, "Wall": 0.083},
                ("10", "10S"): {"ID": 4.26, "Wall": 0.12},
                ("40", "STD", "40S"): {"ID": 4.026, "Wall": 0.237},
                ("80", "XS", "80S"): {"ID": 3.826, "Wall": 0.337},
                ("120",): {"ID": 3.624, "Wall": 0.438},
                ("160",): {"ID": 3.438, "Wall": 0.531},
                ("XX",): {"ID": 3.152, "Wall": 0.674}
            }
        },
        "4 1/2": {
            "OD": 5.0,
            "schedules": {
                ("10", "10S"): {"ID": 4.506, "Wall": 0.247},
                ("STD", "40S"): {"ID": 4.506, "Wall": 0.247},
                ("XS", "80S"): {"ID": 4.29, "Wall": 0.355}
            }
        },
        "5": {
            "OD": 5.563,
            "schedules": {
                ("5", "5S"): {"ID": 5.345, "Wall": 0.109},
                ("10", "10S"): {"ID": 5.295, "Wall": 0.134},
                ("40", "STD", "40S"): {"ID": 5.047, "Wall": 0.258},
                ("80", "XS", "80S"): {"ID": 4.813, "Wall": 0.375},
                ("120",): {"ID": 4.563, "Wall": 0.5},
                ("160",): {"ID": 4.313, "Wall": 0.625},
                ("XX",): {"ID": 4.063, "Wall": 0.75}
            }
        },
        "6": {
            "OD": 6.625,
            "schedules": {
                ("5", "5S"): {"ID": 6.407, "Wall": 0.109},
                ("10", "10S"): {"ID": 6.357, "Wall": 0.134},
                ("40", "STD", "40S"): {"ID": 6.065, "Wall": 0.28},
                ("80", "XS", "80S"): {"ID": 5.761, "Wall": 0.432},
                ("120",): {"ID": 5.501, "Wall": 0.562},
                ("160",): {"ID": 5.189, "Wall": 0.719},
                ("XX",): {"ID": 4.897, "Wall": 0.864}
            }
        },
        "7": {
            "OD": 7.625,
            "schedules": {
                ("STD", "40", "40S"): {"ID": 7.005, "Wall": 0.31},
                ("XS", "80", "80S"): {"ID": 6.625, "Wall": 0.5},
                ("XX",): {"ID": 5.875, "Wall": 0.875}
            }    
        },
        "8": {
            "OD": 8.625,
            "schedules": {
                ("5S",): {"ID": 8.407, "Wall": 0.109},
                ("10", "10S"): {"ID": 8.329, "Wall": 0.148},
                ("20",): {"ID": 8.125, "Wall": 0.25},
                ("30",): {"ID": 8.071, "Wall": 0.277},
                ("40", "STD", "40S"): {"ID": 7.981, "Wall": 0.322},
                ("60",): {"ID": 7.813, "Wall": 0.406},
                ("80", "XS", "80S"): {"ID": 7.625, "Wall": 0.5},
                ("100",): {"ID": 7.439, "Wall": 0.594},
                ("120",): {"ID": 7.189, "Wall": 0.719},
                ("140",): {"ID": 7.001, "Wall": 0.812},
                ("160",): {"ID": 6.813, "Wall": 0.906},
                ("XX",): {"ID": 6.875, "Wall": 0.875}
            }
        },
        "9": {
            "OD": 9.625,
            "schedules": {
                ("STD", "40", "40S"): {"ID": 8.941, "Wall": 0.342},
                ("XS", "80", "80S"): {"ID": 8.625, "Wall": 0.5},
                ("XX",): {"ID": 7.875, "Wall": 0.875}
            }
        },
        "10": {
            "OD": 10.75,
            "schedules": {
                ("5S",): {"ID": 10.482, "Wall": 0.134},
                ("10", "10S"): {"ID": 10.42, "Wall": 0.165},
                ("20",): {"ID": 10.25, "Wall": 0.25},
                ("30",): {"ID": 10.136, "Wall": 0.307},
                ("40", "STD", "40S"): {"ID": 10.02, "Wall": 0.365},
                ("60", "XS", "80S"): {"ID": 9.75, "Wall": 0.5},
                ("80",): {"ID": 9.564, "Wall": 0.594},
                ("100",): {"ID": 9.314, "Wall": 0.719},
                ("120",): {"ID": 9.064, "Wall": 0.844},
                ("140", "XX"): {"ID": 8.75, "Wall": 1.0},
                ("160",): {"ID": 8.5, "Wall": 1.125}
            }
        },    
        "11": {
            "OD": 11.75,
            "schedules": {
                ("STD", "40", "40S"): {"ID": 11.0, "Wall": 0.375},
                ("XS", "80", "80S"): {"ID": 10.75, "Wall": 0.5},
                ("XX",): {"ID": 10.0, "Wall": 0.875}
            }
        },
        "12": {
            "OD": 12.75,
            "schedules": {
                ("5S",): {"ID": 12.438, "Wall": 0.156},
                ("10", "10S"): {"ID": 12.39, "Wall": 0.18},
                ("20",): {"ID": 12.25, "Wall": 0.25},
                ("30",): {"ID": 12.09, "Wall": 0.33},
                ("STD", "40S"): {"ID": 12.0, "Wall": 0.375},
                ("40",): {"ID": 11.938, "Wall": 0.406},
                ("XS", "80S"): {"ID": 11.75, "Wall": 0.5},
                ("60",): {"ID": 11.626, "Wall": 0.562},
                ("80",): {"ID": 11.376, "Wall": 0.688},
                ("100",): {"ID": 11.064, "Wall": 0.844},
                ("120", "XX"): {"ID": 10.75, "Wall": 1.0},
                ("140",): {"ID": 10.5, "Wall": 1.125},
                ("160",): {"ID": 10.126, "Wall": 1.312}
            }
        },
        "14": {
            "OD": 14.0,
            "schedules": {
                ("10S",): {"ID": 13.624, "Wall": 0.188},
                ("10",): {"ID": 13.5, "Wall": 0.25},
                ("20",): {"ID": 13.375, "Wall": 0.312},
                ("30", "STD", "40S"): {"ID": 13.25, "Wall": 0.375},
                ("40",): {"ID": 13.124, "Wall": 0.438},
                ("XS", "80S"): {"ID": 13.0, "Wall": 0.5},
                ("60",): {"ID": 12.814, "Wall": 0.594},
                ("80",): {"ID": 12.5, "Wall": 0.75},
                ("100",): {"ID": 12.124, "Wall": 0.938},
                ("120",): {"ID": 11.814, "Wall": 1.09},
                ("140",): {"ID": 11.5, "Wall": 1.25},
                ("160",): {"ID": 11.188, "Wall": 1.406}
            }
        },
        "16": {
            "OD": 16.0,
            "schedules": {
                ("10S",): {"ID": 15.624, "Wall": 0.188},
                ("10",): {"ID": 15.5, "Wall": 0.25},
                ("20",): {"ID": 15.375, "Wall": 0.312},
                ("30", "STD", "40S"): {"ID": 15.25, "Wall": 0.375},
                ("40", "XS", "80S"): {"ID": 15.0, "Wall": 0.5},
                ("60",): {"ID": 14.688, "Wall": 0.656},
                ("80",): {"ID": 14.314, "Wall": 0.844},
                ("100",): {"ID": 13.938, "Wall": 1.031},
                ("120",): {"ID": 13.564, "Wall": 1.22},
                ("140",): {"ID": 13.124, "Wall": 1.438},
                ("160",): {"ID": 12.814, "Wall": 1.594}
            }
        },
        "18": {
            "OD": 18.0,
            "schedules": {
                ("10S",): {"ID": 17.624, "Wall": 0.188},
                ("10",): {"ID": 17.5, "Wall": 0.25},
                ("20",): {"ID": 17.375, "Wall": 0.312},
                ("STD", "40S"): {"ID": 17.25, "Wall": 0.375},
                ("30",): {"ID": 17.124, "Wall": 0.438},
                ("XS", "80S"): {"ID": 17.0, "Wall": 0.5},
                ("40",): {"ID": 16.876, "Wall": 0.562},
                ("60",): {"ID": 16.5, "Wall": 0.75},
                ("80",): {"ID": 16.126, "Wall": 0.938},
                ("100",): {"ID": 15.688, "Wall": 1.156},
                ("120",): {"ID": 15.25, "Wall": 1.38},
                ("140",): {"ID": 14.876, "Wall": 1.562},
                ("160",): {"ID": 14.438, "Wall": 1.781}
            }
        },
        "20": {
            "OD": 20.0,
            "schedules": {
                ("10S",): {"ID": 19.564, "Wall": 0.218},
                ("10",): {"ID": 19.5, "Wall": 0.25},
                ("20", "STD", "40S"): {"ID": 19.25, "Wall": 0.375},
                ("30", "XS", "80S"): {"ID": 19.0, "Wall": 0.5},
                ("40",): {"ID": 18.812, "Wall": 0.594},
                ("60",): {"ID": 18.376, "Wall": 0.812},
                ("80",): {"ID": 17.938, "Wall": 1.031},
                ("100",): {"ID": 17.438, "Wall": 1.281},
                ("120",): {"ID": 17.0, "Wall": 1.5},
                ("140",): {"ID": 16.5, "Wall": 1.75},
                ("160",): {"ID": 16.064, "Wall": 1.969}
            }
            },
        "22": {
            "OD": 22.0,
            "schedules": {
                ("10", "10S"): {"ID": 21.5, "Wall": 0.25},
                ("STD", "20", "40S"): {"ID": 21.25, "Wall": 0.375},
                ("XS", "30", "80S"): {"ID": 21.0, "Wall": 0.5},
                ("60",): {"ID": 20.25, "Wall": 0.875},
                ("80",): {"ID": 19.75, "Wall": 1.125},
                ("100",): {"ID": 19.25, "Wall": 1.375},
                ("120",): {"ID": 18.749, "Wall": 1.626},
                ("140",): {"ID": 18.25, "Wall": 1.875},
                ("160",): {"ID": 17.75, "Wall": 2.125}
            }
        },
        "24": {
            "OD": 24.0,
            "schedules": {
                ("10", "10S"): {"ID": 23.5, "Wall": 0.25},
                ("20", "STD", "40S"): {"ID": 23.25, "Wall": 0.375},
                ("XS", "80S"): {"ID": 23.0, "Wall": 0.5},
                ("30",): {"ID": 22.876, "Wall": 0.562},
                ("40",): {"ID": 22.626, "Wall": 0.688},
                ("60",): {"ID": 22.064, "Wall": 0.969},
                ("80",): {"ID": 21.564, "Wall": 1.219},
                ("100",): {"ID": 20.938, "Wall": 1.531},
                ("120",): {"ID": 20.376, "Wall": 1.812},
                ("140",): {"ID": 19.876, "Wall": 2.062},
                ("160",): {"ID": 19.314, "Wall": 2.344}
            }
        },
        "26": {
            "OD": 26.0,
            "schedules": {
                ("10",): {"ID": 25.376, "Wall": 0.312},
                ("STD", "40S"): {"ID": 25.25, "Wall": 0.375},
                ("XS", "80S"): {"ID": 25.0, "Wall": 0.5}
            }
        },
        "28": {
            "OD": 28.0,
            "schedules": {
                ("10",): {"ID": 27.376, "Wall": 0.312},
                ("STD", "40S"): {"ID": 27.25, "Wall": 0.375},
                ("XS", "20", "80S"): {"ID": 27.0, "Wall": 0.5},
                ("30",): {"ID": 26.75, "Wall": 0.625}
            }
        },
        "30": {
            "OD": 30.0,
            "schedules": {
                ("10", "10S"): {"ID": 29.376, "Wall": 0.312},
                ("STD", "40S"): {"ID": 29.25, "Wall": 0.375},
                ("20", "XS", "80S"): {"ID": 29.0, "Wall": 0.5},
                ("30",): {"ID": 28.75, "Wall": 0.625}
            }
        },
        "32": {
            "OD": 32.0,
            "schedules": {
                ("10",): {"ID": 31.376, "Wall": 0.312},
                ("20",): {"ID": 31.25, "Wall": 0.375},
                ("STD",): {"ID": 31.0, "Wall": 0.5}, 
                ("30",): {"ID": 30.75, "Wall": 0.625},
                ("40",): {"ID": 30.624, "Wall": 0.688}
            }
        },
        "34": {
            "OD": 34.0,
            "schedules": {
                ("10",): {"ID": 33.376, "Wall": 0.312},
                ("STD",): {"ID": 33.25, "Wall": 0.375},
                ("20",): {"ID": 33.0, "Wall": 0.5},
                ("30",): {"ID": 32.75, "Wall": 0.625},
                ("40",): {"ID": 32.624, "Wall": 0.688}
            }
        },
        "36": {
            "OD": 36.0,
            "schedules": {
                ("10",): {"ID": 35.376, "Wall": 0.312},
                ("STD", "40S"): {"ID": 35.25, "Wall": 0.375},
                ("XS", "80S"): {"ID": 35.0, "Wall": 0.5},
                ("30",): {"ID": 34.75, "Wall": 0.625}
            }
        },
        "42": {
            "OD": 42.0,
            "schedules": {
                ("STD", "40S"): {"ID": 41.25, "Wall": 0.375},
                ("XS", "80S"): {"ID": 41.0, "Wall": 0.5},
                ("30",): {"ID": 40.75, "Wall": 0.625},
                ("40",): {"ID": 40.5, "Wall": 0.75}
            }
        },
        "48": {
            "OD": 48.0,
            "schedules": {
                ("STD", "40S"): {"ID": 47.25, "Wall": 0.375},
                ("XS", "80S"): {"ID": 47.0, "Wall": 0.5}
            }
        },
        "54": {
            "OD": 54.0,
            "schedules": {
                ("STD",): {"ID": 53.25, "Wall": 0.375},
                ("XH",): {"ID": 53.0, "Wall": 0.5}
            }
        },
        "60": {
            "OD": 60.0,
            "schedules": {
                ("STD",): {"ID": 59.25, "Wall": 0.375},
                ("XH",): {"ID": 59.0, "Wall": 0.5}
        }
    }
}

    # Check if the normalized pipe size exists in the data
    if normalized_pipe_size in pipe_data:
        pipe_size_info = pipe_data[normalized_pipe_size]
        od = pipe_size_info["OD"]
        schedules_for_size = pipe_size_info["schedules"]

        # Iterate through the schedules for the given pipe size to find a match
        for schedule_keys, dimensions in schedules_for_size.items():
            if normalized_schedule in schedule_keys:
                return {
                    "OD": od,
                    "ID": dimensions["ID"],
                    "Wall Thickness": dimensions["Wall"]
                }
    
    # If no match is found after checking all entries
    return f"No data found for Pipe Size: '{pipe_size_input}' and Schedule: '{schedule_input}'."

# --- Main execution block for user interaction ---
if __name__ == "__main__":
    print("Welcome to the Pipe Dimension Calculator!")
    print("Enter the nominal pipe size and schedule to get its OD, ID, and Wall Thickness.")
    print("Example Pipe Sizes: 1/2, 2, 3 1/2, 10, 1/8\"")
    print("Example Schedules: 40, STD, XS, 160, 10S")

    while True:
        try:
            user_pipe_size = input("\nEnter Pipe Nominal Size (e.g., 1/2, 2, 1 1/4): ")
            user_schedule = input("Enter Schedule (e.g., 40, STD, XS): ")

            dimensions = get_pipe_dimensions(user_pipe_size, user_schedule)

            if isinstance(dimensions, dict):
                print("\n--- Pipe Dimensions Found ---")
                print(f"Nominal Pipe Size: {user_pipe_size}")
                print(f"Schedule: {user_schedule}")
                print(f"Outer Diameter (OD): {dimensions['OD']}")
                print(f"Inner Diameter (ID): {dimensions['ID']}")
                print(f"Wall Thickness: {dimensions['Wall Thickness']}")
                print("-----------------------------")
            else:
                print(f"\nError: {dimensions}")

            another_lookup = input("\nDo you want to look up another pipe? (yes/no): ").lower()
            if another_lookup != 'yes':
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    print("Thank you for using the Pipe Dimension Calculator!")
