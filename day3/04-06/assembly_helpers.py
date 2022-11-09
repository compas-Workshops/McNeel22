from collections import deque


def traverse(assembly, k):
    tovisit = deque([k])
    visited = set([k])
    ordering = [k]
    while tovisit:
        node = tovisit.popleft()
        for nbr in assembly.graph.neighbors_in(node):
            if nbr not in visited:
                tovisit.append(nbr)
                visited.add(nbr)
                ordering.append(nbr)
    return ordering


def draw_connections(assembly):
    import compas_ghpython

    node_point = {}
    for node in assembly.graph.nodes():
        block = assembly.graph.node_attribute(node, "block")
        point = block.center()
        node_point[node] = point

    lines = []

    for u, v in assembly.graph.edges():
        a = node_point[u]
        b = node_point[v]
        lines.append(
            {
                "start": list(a),
                "end": list(b),
            }
        )
    return compas_ghpython.draw_lines(lines)


def get_assembly_sequence(assembly, top_course=None):
    sequence = []
    sequence_set = set(sequence)

    if not top_course:
        top_course = [node for node in assembly.graph.nodes() if assembly.graph.degree_out(node) == 0]

    blocks = top_course

    for c in blocks:
        parts = traverse(assembly, c)

        for part in reversed(parts):
            if part in sequence_set:
                continue
            sequence.append(part)
            sequence_set.add(part)

    return sequence
