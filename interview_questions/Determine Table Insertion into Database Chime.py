"""
Problem Statement:

We have a bunch of raw SQL inserts which have been separated by table that need to be injected into our database. 
Unfortunately because the tables have foreign key constraints we can't run the statements indiscriminately. 
Given a list of table names which are present in a database. Write a function which determines the proper table insertion order into that database considering foreign key constraints. 

Assuming that you have access to the following two helper functions:
- tables_with_constraints_on: Takes a list of tables names and returns a list of table names that must be INSERTED AFTER the input tables. I.E the output tables have a foreign key constraint on one or more of the input tables.

- tables_constrained_by: Takes a list of tables names and returns a list of table names that must be INSERTED BEFORE the input tables. I.E the returned tables have a foreign key constraint on one or more of the input tables.

Consider a database has the tables A, B, C, D, E, F, G, H

- Table B has a fk on A and is self referencing
B -> A
B -> B
- Table C has a fk on A and B
C -> A
D -> B
- Table E has a fk on G
E -> G
- Table F has a fk on E
F -> E
- Table G has a fk on F
G -> F
- Table H has a fk on G
H -> G

- tables_with_constraints_on(['D']) -> []
- tables_constrained_by(['D']) -> ['B', 'A'] since D -> B -> A
- tables_with_constraints_on(['B']) -> ['C', 'D', 'B'] since C -> B and D -> B and B-> B
- tables_constrained_by(['B']) -> ['A', 'B'] since B -> A and B -> B
- tables_with_constraints_on(['G']) -> ['E', 'F', 'G'] since G -> F -> E -> G
- tables_constrained_by(['G']) -> ['E', 'F', 'G', 'H'] since G -> F -> E -> G and H ->G

"""

"""
BFS+Topological Sort Using Kahn's Algorithm

This problem is a classic application of Topological Sorting. In a database context, we treat tables as nodes and foreign key constraints as directed edges.

To determine the insertion order, we need to find a sequence where every table is placed after the tables it depends on. However, your data presents two specific challenges: self-references (Table B) and circular dependencies (Tables E, F, and G).

The Logic:

- Dependency Tracking: For each table, we check which tables must be inserted "before" it using tables_constrained_by.

- Self-Reference Handling: A table that references itself (like B) will always appear in its own "before" list. We must ignore the table itself during the check to allow it to be cleared for insertion.

- Iterative Selection: We repeatedly look for tables whose dependencies are already satisfied (i.e., they are already in our ordered_list).

- Cycle Detection: If we still have tables to insert but none of them have their dependencies satisfied, we have hit a circular dependency (like E → G → F → E). In a real-world scenario, you would have to temporarily disable constraints to break the cycle.
"""

def get_insertion_order(all_tables):
    order = []
    # 1. Count how many things each table is waiting for (In-degree)
    # We use tables_constrained_by here
    dependency_counts = {}
    for table in all_tables:
        deps = set(tables_constrained_by([table]))
        # We subtract 1 if the table is self-referencing (B -> B)
        count = len(deps - {table})
        dependency_counts[table] = count

    # 2. Find tables with 0 dependencies to start
    ready_queue = [t for t in all_tables if dependency_counts[t] == 0]

    while ready_queue:
        current = ready_queue.pop(0)
        order.append(current)

        # 3. Use tables_with_constraints_on to find who was waiting for 'current'
        children = tables_with_constraints_on([current])
        for child in children:
            if child == current or child not in dependency_counts:
                continue
            
            # Reduce the count for the child
            dependency_counts[child] -= 1
            
            # If the child has no more blockers, it's ready!
            if dependency_counts[child] == 0:
                ready_queue.append(child)

    # Check for cycles (tables left over that never hit 0)
    if len(order) < len(all_tables):
        remaining = set(all_tables) - set(order)
        print(f"Cycle detected in: {remaining}")
        order.extend(list(remaining)) # Force them in to finish

    return order


"""
Input = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Expected Output: ['A', 'B', 'C', 'D', ...] followed by a warning about the E-F-G cycle, ending with H.
"""

"""
How this processes your example:

    A is added first (no dependencies).

    B is added next (it depends on A; its self-reference is ignored).

    C and D are added (they depend on A and B, which are now finished).

    E, F, G form a cycle. The function will detect that none of these can "go first." It will trigger the warning and add them (likely in alphabetical order) to finish the list.

    H depends on G. In a standard DAG, it would wait for G. In a cycle scenario, it is often swept up in the cycle resolution.

Final Calculated Order

Given your constraints, the valid order (ignoring the cycle conflict) would look like this:
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    Note: For the cycle E → G → F → E, you cannot insert these using standard raw SQL without first executing SET FOREIGN_KEY_CHECKS = 0; or making the foreign key columns nullable, inserting them as null, and then updating the IDs.
"""