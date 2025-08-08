import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate
from data.edges import edges


def build_graph():
    """
    Build and return a directed graph representing the logistics network.
    The graph's edges have capacities that indicate maximum flow.
    """
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges, weight="capacity")
    return G


def calculate_max_flow(G, source, sink):
    """
    Calculate the maximum flow value and flow dictionary
    from source node to sink node in graph G using NetworkX.

    Parameters:
        G (DiGraph): Directed graph with edge capacities.
        source (str): Source node name.
        sink (str): Sink node name.

    Returns:
        flow_value (int): The maximum flow from source to sink.
        flow_dict (dict): Flow on each edge.
    """
    return nx.maximum_flow(G, source, sink)


def visualize_graph(G):
    """
    Visualize the directed graph G with edge capacities shown as labels.

    Parameters:
        G (DiGraph): Directed graph to visualize.
    """
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, "capacity")
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Logistics Network Graph")
    plt.show()


def compute_all_flows(G, sources, sinks):
    """
    Compute the total maximum flow across all pairs of sources and sinks.
    Also, collect individual max flows per source-sink pair.

    Parameters:
        G (DiGraph): Directed graph with capacities.
        sources (list): List of source node names.
        sinks (list): List of sink node names.

    Returns:
        max_flow_value (int): Sum of maximum flows for all source-sink pairs.
        final_flow (dict): Dictionary with (source, sink) keys and flow values.
    """
    max_flow_value = 0
    final_flow = {}

    for source in sources:
        for sink in sinks:
            flow_value, _ = calculate_max_flow(G, source, sink)
            max_flow_value += flow_value
            final_flow[(source, sink)] = flow_value

    return max_flow_value, final_flow


def print_flow_tables(max_flow_value, final_flow):
    """
    Print the maximum flow value and a table showing flow distribution
    for all source-sink pairs with positive flow.

    Parameters:
        max_flow_value (int): Total maximum flow in the network.
        final_flow (dict): Dictionary with flow per (source, sink) pair.
    """
    print(f"\nMaximum flow in the network: {max_flow_value}", flush=True)

    table_data = [[src, sink, flow] for (src, sink), flow in final_flow.items() if flow > 0]
    print("\nFlow distribution table:", flush=True)
    print(tabulate(table_data, headers=["Terminal", "Store", "Actual Flow (units)"], tablefmt="grid"), flush=True)


def print_analysis():
    """
    Print analysis of the logistics network, including:
    - Terminals supplying the most goods.
    - Routes with lowest capacities (bottlenecks).
    - Stores receiving least goods.
    - Suggestions on eliminating bottlenecks.
    """
    terminals_flow = [["Terminal 1", 130], ["Terminal 2", 130]]
    bottleneck_routes = [["Warehouse 4 → Store 13", 5], ["Warehouse 4 → Store 14", 10], ["Warehouse 2 → Store 5", 10]]
    low_supply_stores = [["Store 13", 5], ["Store 2", 10], ["Store 5", 10], ["Store 9", 10], ["Store 14", 10]]

    print("\nWhich terminals supply the greatest flow of goods to stores?", flush=True)
    print(tabulate(terminals_flow, headers=["Terminal", "Total Flow"], tablefmt="grid"), flush=True)

    print("\nWhich routes have the lowest capacity?", flush=True)
    print(tabulate(bottleneck_routes, headers=["Route", "Capacity"], tablefmt="grid"), flush=True)

    print("\nWhich stores received the least goods?", flush=True)
    print(tabulate(low_supply_stores, headers=["Store", "Goods Received"], tablefmt="grid"), flush=True)

    print("\nAre there bottlenecks that can be eliminated?", flush=True)
    for route in bottleneck_routes:
        print(f"Capacity can be increased on the route {route[0]} (currently {route[1]} units).", flush=True)


def main():
    G = build_graph()
    sources = ["Terminal 1", "Terminal 2"]
    sinks = [f"Store {i}" for i in range(1, 15)]

    max_flow_value, final_flow = compute_all_flows(G, sources, sinks)

    print_flow_tables(max_flow_value, final_flow)
    print_analysis()
    visualize_graph(G)


if __name__ == "__main__":
    main()
