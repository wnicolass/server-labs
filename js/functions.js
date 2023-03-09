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

let nums = [14, 7, 7, 0, 1];
splice(nums, { start: 1, deleteCount: 2, newItems: [8, 8, 8] });
console.log(nums);
