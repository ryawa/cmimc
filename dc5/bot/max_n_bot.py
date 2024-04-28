import math

def strategy(current_board, player_id):
    max_depth = 3
    potential_moves = generate_moves(current_board)
    
    best_move = None
    best_score = float('inf')
    
    for move in potential_moves:
        new_board = current_board.copy()
        new_board[move] = player_id
        score = maxn_search(new_board, player_id, max_depth, float('-inf'), float('inf'), False)
        
        if score < best_score:
            best_score = score
            best_move = move
    
    return best_move

def generate_moves(current_board):
    potential_moves = []
    for coord in current_board:
        for neighbor in get_neighbors(coord):
            if neighbor not in current_board:
                potential_moves.append(neighbor)
    return potential_moves

def get_neighbors(coord):
    x, y, z = coord
    neighbors = [
        (x+1, y-1, z), (x+1, y, z-1), (x, y+1, z-1),
        (x-1, y+1, z), (x-1, y, z+1), (x, y-1, z+1)
    ]
    return neighbors

def maxn_search(board, player_id, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board, player_id)
    
    if maximizing_player:
        max_score = float('-inf')
        for move in generate_moves(board):
            new_board = board.copy()
            new_board[move] = player_id
            score = maxn_search(new_board, player_id, depth - 1, alpha, beta, False)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float('inf')
        for move in generate_moves(board):
            new_board = board.copy()
            new_board[move] = (player_id + 1) % 3
            score = maxn_search(new_board, player_id, depth - 1, alpha, beta, True)
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

def evaluate_board(board, player_id):
    score = 0
    for coord in board:
        if board[coord] == player_id:
            score += calculate_component_score(board, coord)
    return score

def calculate_component_score(board, start_coord):
    visited = set()
    queue = [start_coord]
    player_id = board[start_coord]
    score = 0
    
    while queue:
        current = queue.pop(0)
        visited.add(current)
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            if neighbor in board and board[neighbor] == player_id and neighbor not in visited:
                queue.append(neighbor)
    
    diameter = 0
    for coord in visited:
        neighbors = get_neighbors(coord)
        connected = False
        for neighbor in neighbors:
            if neighbor in visited and board[neighbor] == player_id:
                connected = True
                break
        if not connected:
            diameter = max(diameter, calculate_diameter(board, player_id, coord))
    
    if diameter < 3:
        score = 0
    elif diameter == 3:
        score = 1
    elif diameter == 4:
        score = 3
    return score

def calculate_diameter(board, player_id, start_coord):
    visited = set()
    queue = [(start_coord, 0)]
    player_id = board[start_coord]
    max_distance = 0
    
    while queue:
        current, distance = queue.pop(0)
        visited.add(current)
        max_distance = max(max_distance, distance)
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            if neighbor in board and board[neighbor] == player_id and neighbor not in visited:
                queue.append((neighbor, distance + 1))
    
    return max_distance

