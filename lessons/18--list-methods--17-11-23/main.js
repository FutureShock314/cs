suits = ["♥", "♦", "♣", "♠"];
deck = [];

sVals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for (var i = 0; i < suits.length; i++) {
    console.log(suits[i]);
    for (var j = 0; j < sVals.length; j++) {
        deck.push(`${suits[i]}${sVals[j]}`)
    };
};

console.log(deck)
