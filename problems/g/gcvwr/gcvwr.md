# GCVWR

You are looking to buy a new camper, but you are a bit concerned that your truck might not be able to safely pull the camper you are currently interested in purchasing. So you do some calculations.

First, you look up your truck’s Gross Combined Vehicle Weight Rating (GCVWR); the maximum total weight it can haul including the weight of the truck itself. You also have a list of items you would want to bring on a camping trip.

But wait! You want a bit of wiggle room too in case you want to bring any extra items with you. So you want to reserve a bit of towing capacity, after factoring in the weight of the vehicle. That is, the total weight of the trailer and goods you want to bring should not exceed 90%
of the towing capacity remaining after factoring in the truck.

## Input

The first line of input contains three integers G (5000≤G≤25000), T (3000≤T≤12000), and N (1≤N≤100). Here, G is the GCVWR in lbs, T is the weight of your truck in lbs, and N is the number of items you want to bring camping. You are guaranteed both G and T are multiples of 10.

The second line contains N space-separated integers w1,…,wN. For each 1≤i≤N, wi (1≤wi≤500) is the weight (in lbs) of the i'th item you want to bring on the trip.

You are further guaranteed T≤G−2000 and that the total weight of all items is at most 90% of the towing capacity that remains after subtracting the weight of the truck from the GCVWR.

## Output

Output a single line containing a single integer that is the maximum possible weight of a trailer you can pull subject to the restrictions described above.

## Explanation of First Sample

The remaining towing capacity after subtracting out the weight of the truck is G−T=9000 lbs, so the weight of the items plus the weight of the trailer you want to purchase should not exceed 90% of this, namely 8100 lbs.

The total weight of items you want to bring is 1205, so the weight of the trailer you want to purchase should not exceed 6895 lbs.

## Info

- Problem ID: gcvwr
- CPU Time limit: 1 second
- Memory limit: 1024 MB
- Difficulty: 1.3
- Author: Zachary Friggstad
- Source: Alberta Collegiate Programming Contest 2021
