def compare_flight_routes(our_routes, competitor_routes):
    common_destinations = our_routes.intersection(competitor_routes)
    
    unique_to_us = our_routes.difference(competitor_routes)
    
    unique_to_competitor = competitor_routes.difference(our_routes)
    neither_share = our_routes.symmetric_difference(competitor_routes) - common_destinations
    
    print("Destinations both airlines fly to:")
    print(common_destinations)
    print("\nDestinations unique to our airline:")
    print(unique_to_us)
    print("\nDestinations unique to the competitor:")
    print(unique_to_competitor)
    print("\nDestinations that neither airline shares:")
    print(neither_share)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

compare_flight_routes(our_routes, competitor_routes)
