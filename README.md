# Task 1: Maximum Flow Application for Goods Logistics

## Description

This project models a network for delivering goods from terminals to stores via warehouses. The Edmonds-Karp maximum flow algorithm is used to find the optimal distribution of goods.

## Network Graph

| From        | To           | Capacity (units) |
|-------------|--------------|------------------|
| Terminal 1  | Warehouse 1  | 25               |
| Terminal 1  | Warehouse 2  | 20               |
| Terminal 1  | Warehouse 3  | 15               |
| Terminal 2  | Warehouse 3  | 15               |
| Terminal 2  | Warehouse 4  | 30               |
| Terminal 2  | Warehouse 2  | 10               |
| Warehouse 1 | Store 1      | 15               |
| Warehouse 1 | Store 2      | 10               |
| Warehouse 1 | Store 3      | 20               |
| Warehouse 2 | Store 4      | 15               |
| Warehouse 2 | Store 5      | 10               |
| Warehouse 2 | Store 6      | 25               |
| Warehouse 3 | Store 7      | 20               |
| Warehouse 3 | Store 8      | 15               |
| Warehouse 3 | Store 9      | 10               |
| Warehouse 4 | Store 10     | 20               |
| Warehouse 4 | Store 11     | 10               |
| Warehouse 4 | Store 12     | 15               |
| Warehouse 4 | Store 13     | 5                |
| Warehouse 4 | Store 14     | 10               |

## Technologies

- Python  
- NetworkX (maximum flow algorithm)  
- Matplotlib (visualization)  
- Tabulate (table formatting)  

## Running the Program

```bash
pip install networkx matplotlib tabulate
cd maximum_flow
python maximum_flow.py
```
## Result

![Logistics Network Graph](maximum_flow/graph/visualize_graph.jpg)


---

