import sys
import os
import argparse
import json
from matplotlib import pyplot as plt

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import mev_project_interface as interface

json_file = 'data.json'
    
# URL of the GeckoTerminal pools page
url = "https://www.geckoterminal.com/solana/pools/32D4zRxNc1EssbJieVHfPhZM3rH6CzfUPrWUuWxD9prG"

# Token variables
token1 = "USDC"
token2 = "USDT"

interface.add_venue_to_json(url, token1, token2, json_file)
interface.main(json_file)


