# tempat mengerjakan coin change dengan greedy
himpunankandidat = [5,4,3,1];
coin = 7
solusi = [];
while(coin is not 0):
	while(himpunankandidat):
		nuker = max(himpunankandidat)
		if (coin-nuker < 0):
			himpunankandidat.pop()
		else:
			coin = coin-nuker;
			solusi.append(nuker)
			break
print(solusi)