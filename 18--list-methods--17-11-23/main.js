suits = ["♥", "♦", "♣", "♠"];
deck = [];

sVals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']

for (var i = 1; i < suits.length; i++) {
    console.log(suits[i]);
    for (var j = 1; j < sVals.length; j++) {
        deck.push(`${suits[i]}${sVals[j]}`)
    };
};

console.log(deck)
