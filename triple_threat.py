"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Yu - November 2025
"""

import random

def main():
    cost_to_play: int = 3
    base_prize: int = 10
    min_plays:int = 1000
    max_plays:int = 5000
    mega_prize:int = 10
    min_day:int = 1
    max_day:int = 7
    day_run = random.randint(min_day, max_day)
    total_collected:int = 0
    total_payout:int = 0
    total_profit:int = 0
    games_played:int = 0
    for i in range (day_run):
        num_play = random.randint(min_plays,max_plays)
        games_played:int = games_played + num_play
        for i in range(num_play):
            roll_1: int = random.randint(1, 6)
            roll_2: int = random.randint(1, 6)
            roll_3: int = random.randint(1, 6)
            if roll_1 == roll_2 == roll_3:
                if roll_1 == 6:
                    pay_out =  base_prize * mega_prize
                    total_payout = total_payout + pay_out
                else:
                    pay_out:int = base_prize * roll_1
                    total_payout = total_payout + pay_out
                    total_collected = total_collected + cost_to_play
            else:
                total_collected = total_collected + cost_to_play
    total_profit = total_collected - total_payout 
    
    print("Days played, Games played, Total Collected, Total pay out, Total profit")
    print(f"{day_run}, {games_played}, {total_collected}, {total_payout}, {total_profit}")
        
if __name__ == "__main__":
    main()