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

////////////////////////////////////////////////////////////////////////
//
//      RECURSIVIDADE
//      FUNCÕES INTERNAS / ANINHADAS
//
////////////////////////////////////////////////////////////////////////

//
// FACTORIAL

// N! = N x (N-1) x (N-2) x ... x 1
// N! = N x (N-1)!
// 1! = 1
// 0! = 1

function factorialI(n) {
  let res = 1;
  for (let i = n; i > 0; i -= 1) {
    res *= i;
  }
  return res;
}

function factorialR(n) {
  if ([0, 1].includes(n)) {
    return 1;
  }
  return n * factorialR(n - 1);
}

// factorialR(5) = 5 * 24 = 120
// factorialR(4) = 4 * 6 = 24
// factorialR(3) = 3 * 2 = 6
// factorialR(2) = 2 * 1 = 2
// factorialR(1) = 1

//
// FIBONACCI

// Fib(N) = Fib(N-1) + Fib(N-2)
// Fib(1) = 1
// Fib(0) = 0

function fibI(n) {
  if ([0, 1].includes(n)) {
    return n;
  }
  let [x, y] = [0, 1];
  for (let i = 2; i <= n; i += 1) {
    [y, x] = [y + x, y];
  }
  return y;
}

function fibI(n) {
  if ([0, 1].includes(n)) {
    return n;
  }
  let [f2, f1] = [0, 1];
  let fN;
  for (let i = 2; i <= n; i += 1) {
    fN = f1 + f2;
    f2 = f1;
    f1 = fN;
  }
  return fN;
}

function fibR(n) {
  if ([0, 1].includes(n)) {
    return n;
  }
  return fibR(n - 1) + fibR(n - 2);
}

//
// PALINDROMO

// Exemplo: txt = 'AABAA'
//
//     i ->
//     0     1     2     3     4
//     A  |  A  |  B  |  A  |  A
//    -5    -4    -3    -2    -1
//                          <- j

function ePalindromo(txt) {
  let [i, j] = [0, txt.length - 1];
  while (i < j) {
    if (txt[i] != txt[j]) {
      return false;
    }
    i += 1;
    j -= 1;
  }
  return true;
}

function ePalR(txt) {
  if (txt.length <= 1) {
    return true;
  }
  return txt[0] === txt[txt.length - 1] && ePalR(txt.slice(1, -1));
}

//
// FLATTEN

// let nums = [1, 2, [3, [4, 5], 6], 7];

function flatten(arr) {
  if (arr.length === 0) {
    return [];
  }
  let [first, rest] = [arr[0], arr.slice(1)];
  if (Array.isArray(first)) {
    return flatten(first).concat(flatten(rest));
  }
  return [first].concat(flatten(rest));
}

function flatten(arr) {
  function doFlatten(arr, pos, retArr) {
    if (pos === arr.length) {
      return;
    }

    let first = arr[pos];
    if (Array.isArray(first)) {
      doFlatten(first, 0, retArr);
    } else {
      retArr.push(first);
    }
    doFlatten(arr, pos + 1, retArr);
  }

  let retArr = [];
  doFlatten(arr, 0, retArr);
  return retArr;
}

////////////////////////////////////////////////////////////////////////
//
//      CLOSURES E IIFES
//
////////////////////////////////////////////////////////////////////////

// . Contexto da função interna, ou envolvida, inclui o contexto da função
//   externa, ou envolvente
// . Este contexto persiste após a função externa ter terminado
// . Contexto de uma função é o âmbito do bloco dessa função (mais o âmbito
//   global)
// . Âmbito de uma função interna é um âmbito dessa função mais o âmbito da
//   da função externa
//
// NOTA: Termo "contexto" utilizado como sinónimo de "âmbito" ou de
//       "escopo" (scope)
//
// Âmbito de bloco (block scope):
//
//  {
//      let X;
//      {
//          let Y;
//          ... temos acesso a X e Y ...
//      }
//      ... temos acesso a apenas a X ...
//  }
//
// O mesmo aplica-se a funções:
//
//  function verde() {
//      let X;
//      function vermelha() {
//          let Y;
//          ... temos acesso a X e Y ...
//      }
//      ... temos acesso a apenas a X ...
//      return vermelha;    // funcao é um objecto com acesso a X e Y e params de preta
//  }
//
//      ┌─────────────────────────────────┐
//      │              ┌───────────────┐  │
//      │              │               │  │
//      │  VERMELHA    │     VERDE     │  │
//      │              │               │  │
//      │              └───────────────┘  │
//      └─────────────────────────────────┘
//

// EXEMPLO 1: SOMADOR
function somador(n) {
  function soma(x) {
    return x + n;
  }
  return soma;
}

somaA = somador(10);
somaA(1); // 11
somaA(10); // 20

// Ou, de forma mais sucinta, utilizando uma lambda:

function somador(n) {
  return function (x) {
    return x + n;
  };
}

// "Arrow functions", que também são lambdas, tornam o código ainda
// mais sucinto:

function somador(n) {
  return (x) => x + n;
}

function counter() {
  let count = 0;
  return () => (count += 1);
}

function range(start, end, step = 1) {
  let count = start;
  return function () {
    let value =
      (step > 0 && count < end) || (step < 0 && count > end)
        ? count
        : undefined;
    count = count + (value !== undefined) * step;
    return value;
  };
}

r1 = range(0, 3);
console.log(r1()); // 0
console.log(r1()); // 1
console.log(r1()); // 2
console.log(r1()); // undefined

r2 = range(0, 10, 2);
console.log(r2()); // 0
console.log(r2()); // 2
console.log(r2()); // 4
console.log(r2()); // 6
console.log(r2()); // 8
console.log(r2()); // undefined

r3 = range(20, 14, -2);
console.log(r3()); // 20
console.log(r3()); // 18
console.log(r3()); // 16
console.log(r3()); // undefined

function makeToMonthName() {
  let months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  return function (monthNum) {
    return months[monthNum - 1];
  };
}

toMonthName = makeToMonthName();

const toMonthName = (function () {
  let months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  return function toMonthName(monthNum) {
    return months[monthNum - 1];
  };
})(); // IIFE : Immediately Invoked Function Expression

function isValidDate(date) {
  const YEAR = "(19[0-9][0-9]|20[0-4][0-9]|2050)";
  const DD_MM_31 = "(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])";
  const DD_MM_30 = "(0[1-9]|[12][0-9]|30)/(0[469]|11)";
  const DD_FEB = "(0[1-9]|1[0-9]|2[0-8])/02";
  const LEAP_YEARS =
    "(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944" +
    "|1948|1952|1956|1960|1964|1968|1972|1976|1980" +
    "|1984|1988|1992|1996|2000|2004|2008|2012|2016" +
    "|2020|2024|2028|2032|2036|2040|2044|2048)";
  const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
  const dateRegExp = new RegExp(
    `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
  );
  return dateRegExp.test(date.trim());
}

const isValidDate = (function () {
  const YEAR = "(19[0-9][0-9]|20[0-4][0-9]|2050)";
  const DD_MM_31 = "(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])";
  const DD_MM_30 = "(0[1-9]|[12][0-9]|30)/(0[469]|11)";
  const DD_FEB = "(0[1-9]|1[0-9]|2[0-8])/02";
  const LEAP_YEARS =
    "(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944" +
    "|1948|1952|1956|1960|1964|1968|1972|1976|1980" +
    "|1984|1988|1992|1996|2000|2004|2008|2012|2016" +
    "|2020|2024|2028|2032|2036|2040|2044|2048)";
  const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
  const dateRegExp = new RegExp(
    `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
  );
  return function isValidDate(date) {
    return dateRegExp.test(date.trim());
  };
})();

function timedRun(fun, count = 10_000_000) {
  const start = Date.now();
  for (let i = 0; i < count; i += 1) {
    fun();
  }
  return (Date.now() - start) / 1000;
}
