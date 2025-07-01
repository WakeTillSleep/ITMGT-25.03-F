def relationship_status(from_member, to_member, social_graph):
    from_follows_to = to_member in social_graph[from_member]["following"]
    to_follows_from = from_member in social_graph[to_member]["following"]

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    size = len(board)

    # Check rows
    for row in board:
        if row.count(row[0]) == size and row[0] != "":
            return row[0]

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != "":
            return column[0]

    # Check diagonals
    diag1 = [board[i][i] for i in range(size)]
    if diag1.count(diag1[0]) == size and diag1[0] != "":
        return diag1[0]

    diag2 = [board[i][size - 1 - i] for i in range(size)]
    if diag2.count(diag2[0]) == size and diag2[0] != "":
        return diag2[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), info in route_map.items():
            if start == current_stop:
                total_time += info["travel_time_mins"]
                current_stop = end
                break

    return total_time