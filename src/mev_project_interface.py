import sys
import os
import argparse
import json
from matplotlib import pyplot as plt

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from classes import order, venue, market, agent

def load_data(file_path):
    """
    Load data from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The loaded data from the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file_path}.")
        sys.exit(1)

def create_orders(data):
    """
    Create a list of Order instances from the loaded JSON data.

    Parameters:
    data (dict): The loaded JSON data.

    Returns:
    list: A list of Order instances.
    """
    Orders = []
    for index in data['orders']:
        Order = order.from_json(index, data['orders'][index])
        Orders.append(Order)
        #Order.print_info()
    return Orders

def create_venues(data):
    """
    Create a list of Venue instances from the loaded JSON data.

    Parameters:
    data (dict): The loaded JSON data.

    Returns:
    list: A list of Venue instances.
    """
    Venues = []
    for venue_name, venue_info in data['venues'].items():
        Venue = venue.from_json(venue_name, venue_info['reserves'])
        #Venue.print_info()
        Venues.append(Venue)
    return Venues

def main(file_path):
    """
    Main function to process the JSON file and create the market graph.

    Parameters:
    file_path (str): The path to the JSON file.
    """
    # Load data from JSON file
    data = load_data(file_path)

    # Create Orders and Venues from JSON data
    Orders = create_orders(data)
    Venues = create_venues(data)

    # Initialize the market graph from the list of venues
    Market = market(Venues)
    #Market.plot_market()

    # Initialize Agent and read the first order
    Agent = agent()
    Agent.read_order(Orders[0])

    # Read market data and optimize strategy
    Agent.read_market(Market)
    optimal_values, optimal_b_values, optimal_b_sum = Agent.optimize_strategy()
