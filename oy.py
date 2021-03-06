import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
z_link = [[False for i in range(zone_count)] for j in range(zone_count)]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    z_link[zone_1][zone_2] = True


def moves(x):
	aval = []
	for i in range(x-20,x+20):
	    if (z_link[x][i]):
	        if (True):
	            aval.append(i)
	return aval

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    z_vis = []                  # list visible zone
    to_move = []
    z_pods = []
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        if visible:
            z_vis.append(z_id)
        if pods_p0 > 1:
            to_move.append(z_id)
            z_pods.append(pods_p0)
            
        
                

    # Write an action using print
    # To debug: 
    #print(owner_id, file=sys.stderr)

    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    for i in range(len(to_move)):
        can_move=moves(to_move[i])
        print(z_pods[i]-1, to_move[i], can_move[random.randint(0,len(can_move)))])
    print("WAIT")