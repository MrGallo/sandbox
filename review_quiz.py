from typing import Dict


def is_potentially_explosive(inventory: Dict) -> bool:
    """Determines if your inventory is potentially explosive.
    
    An inventory is considered potentially explosive if it contains
    even the mention of both "fire" and "propane" in the dictionary's keys.
    The quantities of each element are irrevelant.
    
    Args:
        inventory: A dictionary that may be explosive.
    Returns:
        True if potentially explosive, False otherwise.
    """
    fire_mentioned = "fire" in inventory
    propane_mentioned = "propane" in inventory
    
    return fire_mentioned and propane_mentioned
