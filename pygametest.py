#Michael Cho ENAE 380 - 0202 Final
import numpy as np
import math
import random
fulldeck = []
board = []
hand = []

for i in range(0, 52, 1):
	fulldeck.append(i + 1)

def shuffledeck(fulldeck):
	shuffle = random.shuffle(fulldeck)
	for j in range(0, 5, 1):
		board.append(detcard(fulldeck[j]))
	for k in range(5, 7, 1):
		hand.append(detcard(fulldeck[k]))
	return(board, hand)

def detcard(val):
	num = val % 13
	suit = val // 13
	if num == 0:
		suit -= 1
		num = 13
	elif suit == 4 and num != 0:
		suit = "not"
		num = "valid"

	if suit == 0:
		suit = "DIAMOND"
	elif suit == 1:
		suit = "HEART"
	elif suit == 2:
		suit = "SPADE"
	elif suit == 3:
		suit = "CLUB"
	info = [suit, num, val]
	return info


def bubble_sort(my_list):
    temp1 = 0 #these are value holders
    temp2 = 0
    for j in range(0, 28, 1):  #this is going to run for the required amount of passes when n = 8
        for i in range(0, len(my_list) - 1, 1): #this goes through the list 
            if my_list[i] > my_list[i + 1]: #this checks to see if the first value is larger
                temp1 = my_list[i] #sets temp values
                temp2 = my_list[i + 1]
                my_list.pop(i) #deletes the two spots
                my_list.pop(i)
                my_list.insert(i, temp2) #swaps the values
                my_list.insert(i + 1, temp1)
    return my_list

def checkhand(board, hand):
	count = 0
	countsgreaterthan2 = []
	handstr = 0
	suitlist = []
	vallist = []
	valcount = []
	deckval = []
	for l in range(0, len(board), 1):
		suitlist.append(board[l][0])
		vallist.append(board[l][1])
		deckval.append(board[l][2])
		if board[l][1] == 1:
			vallist.append(14)
	for m in range(0, len(hand), 1):
		suitlist.append(hand[m][0])
		vallist.append(hand[m][1])
		deckval.append(hand[m][2])
		if hand[m][1] == 1:
			vallist.append(14)
	#sort vallist and deckval using bubble sort from lab 2
	sortedvallist = bubble_sort(vallist)
	sorteddeckval = bubble_sort(deckval)
	#Check Royal
	royalcheck = 0
	royalcounter = 0
	royalcardchecklist = [1, 14, 27, 40]
	for y in range(0, len(royalcardchecklist), 1):
		royalcheck = royalcardchecklist[y]
		for x in range(0, len(sorteddeckval), 1):
			if sorteddeckval[x] == royalcheck:# or sorteddeckval[x] == 14 or sorteddeckval[x] == 27 or sorteddeckval == 40:
				if royalcheck % 13 == 1:
					royalcheck += 9
					royalcounter += 1

				elif royalcheck % 13 != 1:
					royalcheck += 1
					royalcounter += 1
	if royalcounter == 5:
		handstr = "RoyalFlush"
		return(handstr)
	#Check Straight Flush
	valchecklist = [] #checks to make sure all same suit
	for s in range(0, 3, 1):
		if sorteddeckval[s + 1] == sorteddeckval[s] + 1 and sorteddeckval[s + 2] == sorteddeckval[s] + 2 and sorteddeckval[s + 3] == sorteddeckval[s] + 3 and sorteddeckval[s + 4] == sorteddeckval[s] + 4:
			highcardSF = s + 4
			for t in range(s + 4, s - 1, -1):
				valchecklist.append(detcard(sorteddeckval[t]))
			for u in range(0, len(valchecklist), 1):
				if valchecklist[0][0] == valchecklist[u][0]:
					handstr = "StraightFlush"
					return(handstr)
	#Finding Counts
	paircount = 0
	tripcount = 0
	for n in range(1, 14, 1):
		for o in range(0, len(sortedvallist), 1):
			if sortedvallist[o] == n:
				count += 1
		valcount.append(count)
		count = 0
	for p in range(0, len(valcount), 1): 
		if valcount[p] >= 2:
			cardval = p + 1
			#print(str(valcount[p]) + " of " + str(cardval)) #THIS SHIT TELLS HOW MANY OF EACH 
			if valcount[p] == 4:
				handstr = "Quads"
				return(handstr)
			elif valcount[p] == 3: 
				handstr = "Trips"
				tripcount += 1
			elif valcount[p] == 2:
				handstr = "Pair"
				paircount += 1
	#Check FullHouse
	if tripcount >= 1 and paircount >= 1:
		handstr = "FullHouse"
		return(handstr)
	#Check Flush
	Dcount = 0
	Hcount = 0
	Scount = 0
	Ccount = 0
	suitcountlist = []
	for q in range(0, len(suitlist), 1):
		if suitlist[q] == "DIAMOND":
			Dcount += 1
		elif suitlist[q] == "HEART":
			Hcount += 1
		elif suitlist[q] == "SPADE":
			Scount += 1
		elif suitlist[q] == "CLUB":
			Ccount += 1
	suitcountlist.append(Dcount)
	suitcountlist.append(Hcount)	
	suitcountlist.append(Scount)	
	suitcountlist.append(Ccount)
	for r in range(0, len(suitcountlist), 1):
		if suitcountlist[r] >= 5:
			handstr = "Flush"
			return(handstr)	
	#Check Straight
	straightvalues = []
	straightcounter = 0
	for z in range(0, len(sortedvallist), 1):
		straightvalues.append(sortedvallist[z])
	for v in range(0, len(straightvalues), 1):
		straightcounter = 0
		straightcheck = straightvalues[v]
		for w in range(0, len(sortedvallist), 1):
			if sortedvallist[w] == straightcheck:
				straightcheck += 1
				straightcounter += 1
			if straightcounter == 5:
				handstr = "Straight"
				return(handstr)
	if paircount >= 2:
		handstr = "TwoPair"
		return(handstr)
	if handstr == 0:
		handstr = "HighCard"
	#print(valcount)
	return(handstr)
	
def bestpossiblehand(board):
	vallist = []
	deckval = []
	for l in range(0, len(board), 1):
		vallist.append(board[l][1])
		deckval.append(board[l][2])
		if board[l][1] == 1:
			vallist.append(14)
	sortedvallist = bubble_sort(vallist)
	sorteddeckval = bubble_sort(deckval)
	#Check RoyalFlush
	Dcount = 0
	Hcount = 0
	Scount = 0
	Ccount = 0	
	suitcountlist = []
	for i in range(0, len(board), 1):
		if board[i][0] == "DIAMOND":
			Dcount += 1
		elif board[i][0]== "HEART":
			Hcount += 1
		elif board[i][0] == "SPADE":
			Scount += 1
		elif board[i][0] == "CLUB":
			Ccount += 1
	suitcountlist.append(Dcount)
	suitcountlist.append(Hcount)	
	suitcountlist.append(Scount)	
	suitcountlist.append(Ccount)
	royalcounter = 0
	suit = 0
	for m in range(0, len(suitcountlist), 1):
		if suitcountlist[m] >= 3:
			if m == 0:
				suit = "DIAMOND"
			elif m == 1:
				suit = "HEART"
			elif m == 2:
				suit = "SPADE"
			elif m == 3:
				suit = "CLUB"
			for n in range(0, len(board), 1):
				if board[n][0] == suit:
					if board[n][1] == 13 or board[n][1] == 12 or board[n][1] == 11 or board[n][1] == 10 or board[n][1] == 1:
						royalcounter += 1
	if royalcounter >= 3:
		possiblehand = "RoyalFlush"
		return(possiblehand)
 	#Check StraightFlush
	for l in range(0, len(sorteddeckval) - 2, 1):
		test1 = detcard(sorteddeckval[l])
		test2 = detcard(sorteddeckval[l + 2])
		if (sorteddeckval[l + 2] - sorteddeckval[l]) <= 4 and test1[0] == test2[0]:
			possiblehand = "StraightFlush"
			return(possiblehand)
	#Check Count
	valcount = []
	count = 0
	for n in range(1, 14, 1):
		for o in range(0, len(board), 1):
			if board[o][1] == n:
				count += 1
				valcount.append(count)
		count = 0
	for p in range(0, len(valcount), 1): 
		if valcount[p] >= 2:
			possiblehand = "Quads"
			return(possiblehand)			
	#Check Flush
	for r in range(0, len(suitcountlist), 1):
		if suitcountlist[r] >= 3:
			possiblehand = "Flush"
			return(possiblehand)
	#Check Straight
	singlevallist = [sortedvallist[0]]
	for j in range(1, len(sortedvallist), 1): #eliminates duplicate vals
	  	if sortedvallist[j] != singlevallist[j - 1]:
	  		singlevallist.append(vallist[j])
	for k in range(0, len(singlevallist)- 2, 1):
		if (singlevallist[k + 2] - singlevallist[k]) <= 4:
			possiblehand = "Straight"
			return(possiblehand)
	return("Trips")

playing = 1
while playing == 1:
	start = input("Would you like to test your Poker knowledge? (Y to play and N to quit) ")
	if start == "N":
		playing = 0
	elif start == "Y":
		board = []
		hand = []
		shuffledeck(fulldeck)
		# board = [['SPADE', 2, 28], ['DIAMOND', 1, 1], ['DIAMOND', 9, 9], ['DIAMOND', 2, 2], ['HEART', 1, 14]]
		# hand = [['CLUB', 12, 51], ['SPADE',5,18]]
		check = (checkhand(board, hand))
		best = (bestpossiblehand(board))
		# print(check + "  " + best)
		print("The Board is:")
		for z in range(0, len(board), 1):
			if board[z][1] == 10:
				print("T " + str(board[z][0]))
			elif board[z][1] == 11:
				print("J " + str(board[z][0]))
			elif board[z][1] == 12:
				print("Q " + str(board[z][0]))
			elif board[z][1] == 13:
				print("K " + str(board[z][0]))
			elif board[z][1] == 1:
				print("A " + str(board[z][0]))
			else:
				print(str(board[z][1]) + " " + str(board[z][0]))
		print("Your Hand is:")
		for y in range(0, len(hand), 1):
			if hand[y][1] == 10:
				print("T " + str(hand[y][0]))
			elif hand[y][1] == 11:
				print("J " + str(hand[y][0]))
			elif hand[y][1] == 12:
				print("Q " + str(hand[y][0]))
			elif hand[y][1] == 13:
				print("K " + str(hand[y][0]))
			elif hand[y][1] == 1:
				print("A " + str(hand[y][0]))
			else:
				print(str(hand[y][1]) + " " + str(hand[y][0]))
		askhand = input("What is your current hand strength? (HighCard, Pair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush, RoyalFlush, N to quit) ")
		if askhand == "N":
			playing = 0
			continue
		elif askhand == check:
			print("You are correct!")
		else:
			print("Incorrect. The correct answer was " + check)
		askbesthand = input("What is the best possible hand that can be created on this board? (HighCard, Pair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush, RoyalFlush, N to quit) ")
		if askbesthand == "N":
			playing = 0
		elif askbesthand == best:
			print("You are correct!")
		else:
			print("Incorrect. The correct answer was " + best)
	else:
		print("Not Valid, Try Again")
print("Goodbye!")