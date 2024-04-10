function fruits(type, weight, price){
    let sum = (weight / 1000) * price;

    console.log(`I need $${sum.toFixed(2)} to buy ${(weight/1000).toFixed(2)} kilograms ${type}.`);
}

fruits('orange', 2500, 1.80)
fruits('apple', 1563, 2.35)