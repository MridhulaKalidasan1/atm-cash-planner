import streamlit as st
import heapq
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="ATM Cash Planner", layout="wide")
st.title("🖨️ Smart Cash Distribution Planner")

# 2. The Algorithm Core
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]: continue
        for v, weight in graph[u].items():
            dist = curr_dist + weight
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    return distances

# 3. Sidebar UI Controls
st.sidebar.header("Logistics Configuration")
start_hub = st.sidebar.selectbox("Select Cash Depot Hub", ["Central Depot A", "North Hub B"])
truck_capacity = st.sidebar.slider("Cash Truck Capacity ($)", 50000, 500000, 200000)

# 4. Mock Map Data (Streamlit natively supports maps!)
# Create fake coordinates for your ATMs
map_data = pd.DataFrame({
    'lat': [13.0827, 13.0900, 13.0700],
    'lon': [80.2707, 80.2800, 80.2600],
    'name': ['ATM 1 - Main St', 'ATM 2 - Sector 5', 'ATM 3 - Airport Rd']
})

st.subheader("ATM Network Locations")
st.map(map_data) # This will automatically render an interactive map!

# 5. Trigger optimization
if st.button("Calculate Optimal Routes"):
    # Define a simple graph for testing
    graph = {
        "Central Depot A": {"ATM 1 - Main St": 5, "ATM 2 - Sector 5": 10},
        "North Hub B": {"ATM 1 - Main St": 8, "ATM 2 - Sector 5": 7},
        "ATM 1 - Main St": {"ATM 3 - Airport Rd": 3},
        "ATM 2 - Sector 5": {"ATM 3 - Airport Rd": 1},
        "ATM 3 - Airport Rd": {}
    }
    
    results = dijkstra(graph, start_hub)
    
    st.success("Optimization Complete!")
    st.write("Shortest Distances from Hub:", results)