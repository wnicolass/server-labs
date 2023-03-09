"use strict";

////////////////////////////////////////////////
//
//      CONCAT & SPLICE
//
///////////////////////////////////////////////

// 1st version
function concat(items) {
  const itemsTxt = [];
  for (let item of items) {
    itemsTxt.push("" + item);
  }
  return itemsTxt.join("");
}

// 2nd version
function concatII(...items) {
  const itemsTxt = [];
  for (let item of items) {
    itemsTxt.push("" + item);
  }
  return itemsTxt.join("");
}

// 3rd version
function concatIII(items, sep = "", end = "") {
  const itemsTxt = [];
  for (let item of items) {
    itemsTxt.push("" + item);
  }
  itemsTxt.push(end);
  return itemsTxt.join(sep);
}

// 4th version
function concatIV(items, namedArgs) {
  let { sep, end } = namedArgs;
  sep = sep || "";
  end = end || "";
  const itemsTxt = [];
  for (let item of items) {
    itemsTxt.push("" + item);
  }
  itemsTxt.push(end);
  return itemsTxt.join(sep);
}

// 5th version
function concatV(items, { sep = "", end = "" } = {}) {
  const itemsTxt = [];
  for (let item of items) {
    itemsTxt.push("" + item);
  }
  itemsTxt.push(end);
  return itemsTxt.join(sep);
}

// console.log(concatV([1, 2, "alberto", "antunes", [0, 1]], { end: "theend" }));

// splice
// array.splice(start[, deleteCount[, item1[, item2[, ...]]]])

function splice(items, spliceOptions) {
  let { start, deleteCount, newItems } = spliceOptions;
  let result =
    deleteCount && newItems
      ? items.splice(start, deleteCount, ...newItems)
      : deleteCount
      ? items.splice(start, deleteCount)
      : newItems
      ? items.splice(start, 0, ...newItems)
      : items.splice(start);
  return result;
}

// let nums = [14, 7, 7, 0, 1];
// splice(nums, { start: 1, deleteCount: 2, newItems: [8, 8, 8] });
// console.log(nums);

///////////////////////////////////////////////////////
//
//   LAMBDAS, ARROW FUNCTIONS & HIGH-ORDER FUNCTIONS
//
//////////////////////////////////////////////////////

const nums = [100, 15, -2, -1, 59, 44, 12, 10, 46, 77, 15, 90, 15];
const names = ["alberto", "bruno", "armando", "josé", "albertina", "amanda"];

// high-order function
function filter(items, criteria) {
  const selected = [];
  for (let item of items) {
    if (criteria(item)) {
      selected.push(item);
    }
  }
  return selected;
}

function ePar(num) {
  return num % 2 === 0;
}

function ePositivo(num) {
  return num >= 0;
}

function terminadoEmOh(texto) {
  return texto[texto.length - 1] === "o";
}

function temPeloMenosTresAs(texto) {
  let quantos = 0;
  for (let ch of [...texto]) {
    if (ch === "a") {
      quantos += 1;
    }
  }
  return quantos >= 3;
}

console.log(filter(nums, ePar));
console.log(
  filter(nums, function (num) {
    return num % 2 === 0;
  })
);
console.log(filter(nums, ePositivo));
console.log(
  filter(nums, function (num) {
    return num >= 0;
  })
);
console.log(filter(names, terminadoEmOh));
console.log(
  filter(names, function (name) {
    return name[name.length - 1] === "o";
  })
);
console.log(filter(names, temPeloMenosTresAs));
console.log(
  filter(names, function atLeastThreeA(txt) {
    let quantos = 0;
    for (let ch of [...txt]) {
      if (ch === "a") {
        quantos += 1;
      }
    }
    return quantos >= 3;
  })
);

function between(a, b) {
  return (num) => num >= a && num <= b;
}

function notBetween(a, b) {
  return (num) => num < a || num > b;
}

function lengthEquals(a) {
  return (obj) => obj.length === a;
}

// with arrow functions
console.log(filter(nums, (num) => num % 2 === 0));
console.log(filter(nums, (num) => num >= 0));
console.log(filter(names, (name) => name[name.length - 1] === "o"));

console.log(filter(nums, between(10, 20)));
console.log(filter(nums, notBetween(10, 20)));
console.log(filter(nums, (num) => num === 15));
console.log(filter(names, (name) => name.length === 7));
console.log(filter(names, lengthEquals(7)));

////////////////////////////////////////////////////////////////////////
//
//      FILTER, MAP, FOR-EACH, REDUCE, EVERY, SOME
//
////////////////////////////////////////////////////////////////////////

console.log(nums.filter((num) => num >= 15));
console.log(nums.map((num) => num * 2));
names.forEach((name) => console.log(name));
names.forEach(console.log);
names.forEach((name, i) => console.log(`${i} -> ${name}`));

console.log(nums.reduce((acc, num) => acc + num, 0));
console.log(names.reduce((acc, name) => acc + name + "/", ""));

let allPositive = true;
allPositive = nums.every((num) => num >= 0);
let atLeastOnePositive = nums.some((num) => num >= 0);
console.log(allPositive, atLeastOnePositive);
