def badge_maker(name):
   return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages_list= []
    for name in names:
        badge_message=f"Hello, my name is {name}."
        badge_messages_list.append(badge_message)
    

    return badge_messages_list

def assign_rooms(names):
    room_assignments = []
    i=1
    while i <= len(names):
        name = names[i-1]
        room_message = f"Hello, {name}! You'll be assigned to room {i}!"
        room_assignments.append(room_message)
        i += 1
    return room_assignments

def printer(names):
    for message in batch_badge_creator(names):
        print(message)
    
    for room_assignment in assign_rooms(names):
        print(room_assignment)
    return None
