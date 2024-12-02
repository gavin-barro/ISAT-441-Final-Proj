import matplotlib.pyplot as plt
from ecosystem import Ecosystem
import random
from bees import Bee

"""
    Driver module to be used to run our program.
    TODO: This python module runs the simulation and collections information on it.
    It will run the simulation for a select amount of ticks and every tick the 
    information on the program will outputed. The idea of this simulation is 
    to simulate the introduction of an invasive species and its impact on an exsisting
    ecosystem. 
    
    Invasive flower gives more pollen than the other flowers in the ecosystem
    The bees gravitate towards that flower

    Author: Gavin Barro and Austin Earl
    Version: 10/15/2024
"""


def main() -> None:
    defaults1 = setup_simulation1()
    
    # Baseline simulation where invasive flowers don't dominate
    simulation1 = Ecosystem(defaults1["Bees"], defaults1["Flowers"], defaults1["Hives"], defaults1["Seeds"])
    
    # # Invasive flowers dominate because their nectar rewards are higher
    # simulation2 = Ecosystem()
    
    # # Bees prefer invasive flowers, causing the second bee species to take over
    # simulation3 = Ecosystem()



def setup_simulation1() -> dict[str, list]:
    """
    Sets up base components to our environment

    Returns:
        dict: our default parameters
    """
    
    # # A dictionary is used for scalabilty and reusability
    # defaults = {
    #     "random_generator_seed": 0,
    #     "starting_number_of_bees": 30,
    #     "bee_wait_time": 8,
    #     "bee_vision_length": 7,
    #     "bee_vision_degrees": 45,
    #     "bee_lifetime": 1000,

    #     "Bee1_Pref_WhiteFlower": 100,
    #     "Bee1_Pref_RedFlower": 75,
    #     "Bee1_Pref_BlueFlower": 50,
    #     "Bee1_Pref_GreenFlower": 25,
    #     "Bee1_start_forager_production": 500,
    #     "Bee1_end_forager_production": 3300,
    #     "Bee1_Pref_InvasiveFlower": 63,

    #     "Bee2_Pref_WhiteFlower": 25,
    #     "Bee2_Pref_RedFlower": 50,
    #     "Bee2_Pref_BlueFlower": 75,
    #     "Bee2_Pref_GreenFlower": 100,
    #     "Bee2_start_forager_production": 500,
    #     "Bee2_end_forager_production": 3300,
    #     "Bee2_Pref_InvasiveFlower": 63,

    #     "number_of_WhiteFlower": 100,
    #     "number_of_RedFlower": 100,
    #     "number_of_BlueFlower": 100,
    #     "number_of_GreenFlower": 100,
    #     "number_of_InvasiveFlower": 100,

    #     "WhiteFlower_nectar_regeneration": 0.4,
    #     "RedFlower_nectar_regeneration": 0.4,
    #     "BlueFlower_nectar_regeneration": 0.4,
    #     "GreenFlower_nectar_regeneration": 0.4,
    #     "InvasiveFlower_nectar_regeneration": 0.4,

    #     "lifespan_WhiteFlower": 2000,
    #     "lifespan_RedFlower": 2500,
    #     "lifespan_BlueFlower": 2500,
    #     "lifespan_GreenFlower": 2000,
    #     "lifespan_InvasiveFlower": 2000,

    #     "start_of_bloom_WhiteFlower": 500,
    #     "start_of_bloom_RedFlower": 2000,
    #     "start_of_bloom_BlueFlower": 2000,
    #     "start_of_bloom_GreenFlower": 500,
    #     "start_of_bloom_InvasiveFlower": 500,

    #     "InvasiveFlower": False,
    #     "percent_seed_death": 0.70,
    #     "seeds_fall_radius": 5,
    #     "nectar_per_bee": 1200,
    #     "max_nectar": 25,
    #     "max_slots": 20  # maximum number of seeds a flower can create
    # }

    hives_list = []
    
    seed_list = []
    
    flowers_list = []
    
    bees_list = []
    for i in range(30):
        curr_age = 0
        curr_species = "Bee"
        choosen_flower = None
        previous_flower = None
        home_hive = hives_list[random(0, len(hives_list) - 1)]
        collection_start_time = 0 # most recent time the bee has collected
        count_carry_nectar = 0
        pollen = 0
        bee = Bee(curr_age, curr_species, choosen_flower, previous_flower, home_hive, 
                      collection_start_time, count_carry_nectar, pollen)
        bees_list.append(bee)
    
    return {"Bees": bees_list, "Flowers": flowers_list, "Hives": hives_list, "Seeds": seed_list}


if __name__ == "__main__":
    main()