# Clean Code


- [Clean Code](#clean-code)
  - [Introduction 简介](#introduction-简介)
  - [**Variables 变量**](#variables-变量)
    - [Use meaningful and pronounceable variable names 使用有意义的变量名](#use-meaningful-and-pronounceable-variable-names-使用有意义的变量名)
    - [Use the same vocabulary for the same type of variable 合并功能一致的变量](#use-the-same-vocabulary-for-the-same-type-of-variable-合并功能一致的变量)
    - [Use searchable names 便于搜索的名字](#use-searchable-names-便于搜索的名字)
    - [Use explanatory variables 使用自解释的变量名](#use-explanatory-variables-使用自解释的变量名)
    - [Avoid Mental Mapping 避免思维映射](#avoid-mental-mapping-避免思维映射)
    - [Don't add unneeded context 不添加无用的上下文](#dont-add-unneeded-context-不添加无用的上下文)
    - [Use default parameters instead of short circuiting or conditionals 使用默认参数，而非短路或条件判断](#use-default-parameters-instead-of-short-circuiting-or-conditionals-使用默认参数而非短路或条件判断)
  - [**Functions 函数**](#functions-函数)
    - [Function arguments (2 or fewer ideally) 参数越少越好 (理想情况不超过2个)](#function-arguments-2-or-fewer-ideally-参数越少越好-理想情况不超过2个)
    - [Functions should do one thing 函数只做一件事](#functions-should-do-one-thing-函数只做一件事)
    - [Function names should say what they do 函数名应明确表明其功能](#function-names-should-say-what-they-do-函数名应明确表明其功能)
    - [Functions should only be one level of abstraction 函数应该只做一层抽象](#functions-should-only-be-one-level-of-abstraction-函数应该只做一层抽象)
    - [Remove duplicate code 移除重复的代码](#remove-duplicate-code-移除重复的代码)
    - [Set default objects with Object.assign 使用 Object.assign 设置默认对象](#set-default-objects-with-objectassign-使用-objectassign-设置默认对象)
    - [Don't use flags as function parameters 不要使用标记(Flag)作为函数参数](#dont-use-flags-as-function-parameters-不要使用标记flag作为函数参数)
    - [Avoid Side Effects (part 1) 避免副作用](#avoid-side-effects-part-1-避免副作用)
    - [Avoid Side Effects (part 2)](#avoid-side-effects-part-2)
    - [Don't write to global functions 不要写全局函数](#dont-write-to-global-functions-不要写全局函数)
    - [Favor functional programming over imperative programming 采用函数式编程而不是命令式编程](#favor-functional-programming-over-imperative-programming-采用函数式编程而不是命令式编程)
    - [Encapsulate conditionals 封装判断条件](#encapsulate-conditionals-封装判断条件)
    - [Avoid negative conditionals 避免“否定情况”的判断](#avoid-negative-conditionals-避免否定情况的判断)
    - [Avoid conditionals 避免条件判断](#avoid-conditionals-避免条件判断)
    - [Avoid type-checking (part 1) 避免类型判断(part 1)](#avoid-type-checking-part-1-避免类型判断part-1)
    - [Avoid type-checking (part 2) 避免类型判断(part 2)](#avoid-type-checking-part-2-避免类型判断part-2)
    - [Don't over-optimize 避免过度优化](#dont-over-optimize-避免过度优化)
    - [Remove dead code 删除无效的代码](#remove-dead-code-删除无效的代码)
  - [**Objects and Data Structures 对象和数据结构**](#objects-and-data-structures-对象和数据结构)
    - [Use getters and setters 使用 getters 和 setters](#use-getters-and-setters-使用-getters-和-setters)
    - [Make objects have private members 让对象拥有私有成员](#make-objects-have-private-members-让对象拥有私有成员)
  - [**Classes 类**](#classes-类)
    - [Prefer ES2015/ES6 classes over ES5 plain functions 使用 ES6 的 classes 而不是 ES5 的 Function](#prefer-es2015es6-classes-over-es5-plain-functions-使用-es6-的-classes-而不是-es5-的-function)
    - [Use method chaining 使用方法链](#use-method-chaining-使用方法链)
    - [Prefer composition over inheritance 优先使用组合模式而非继承](#prefer-composition-over-inheritance-优先使用组合模式而非继承)
  - [**SOLID**](#solid)
    - [Single Responsibility Principle (SRP) 单一职责原则 (SRP)](#single-responsibility-principle-srp-单一职责原则-srp)
    - [Open/Closed Principle (OCP)](#openclosed-principle-ocp)
    - [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
    - [Interface Segregation Principle (ISP)](#interface-segregation-principle-isp)
    - [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)
  - [**Testing**](#testing)
    - [Single concept per test](#single-concept-per-test)
  - [**Concurrency**](#concurrency)
    - [Use Promises, not callbacks](#use-promises-not-callbacks)
    - [Async/Await are even cleaner than Promises](#asyncawait-are-even-cleaner-than-promises)
  - [**Error Handling**](#error-handling)
    - [Don't ignore caught errors](#dont-ignore-caught-errors)
    - [Don't ignore rejected promises](#dont-ignore-rejected-promises)
  - [**Formatting**](#formatting)
    - [Use consistent capitalization](#use-consistent-capitalization)
    - [Function callers and callees should be close](#function-callers-and-callees-should-be-close)
  - [**Comments**](#comments)
    - [Only comment things that have business logic complexity.](#only-comment-things-that-have-business-logic-complexity)
    - [Don't leave commented out code in your codebase](#dont-leave-commented-out-code-in-your-codebase)
    - [Don't have journal comments](#dont-have-journal-comments)
    - [Avoid positional markers](#avoid-positional-markers)
    - [SOLID](#solid-1)
      - [Single responsibility](#single-responsibility)
      - [Open closed](#open-closed)
      - [Liskov substitution](#liskov-substitution)
      - [Interface segregation](#interface-segregation)
      - [Dependency Inversion](#dependency-inversion)
    - [Don't repeat yourself (DRY)](#dont-repeat-yourself-dry)
    - [Keep it Short and Simple (KISS Principle)](#keep-it-short-and-simple-kiss-principle)
  

## Introduction 简介

![Humorous image of software quality estimation as a count of how many expletives
you shout when reading code](https://www.osnews.com/images/comics/wtfm.jpg)

Software engineering principles, from Robert C. Martin's book
[_Clean Code_](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882),
adapted for JavaScript. This is not a style guide. It's a guide to producing
[readable, reusable, and refactorable](https://github.com/ryanmcdermott/3rs-of-software-architecture) software in JavaScript.

Not every principle herein has to be strictly followed, and even fewer will be
universally agreed upon. These are guidelines and nothing more, but they are
ones codified over many years of collective experience by the authors of
_Clean Code_.

Our craft of software engineering is just a bit over 50 years old, and we are
still learning a lot. When software architecture is as old as architecture
itself, maybe then we will have harder rules to follow. For now, let these
guidelines serve as a touchstone by which to assess the quality of the
JavaScript code that you and your team produce.

One more thing: knowing these won't immediately make you a better software
developer, and working with them for many years doesn't mean you won't make
mistakes. Every piece of code starts as a first draft, like wet clay getting
shaped into its final form. Finally, we chisel away the imperfections when
we review it with our peers. Don't beat yourself up for first drafts that need
improvement. Beat up the code instead!

这不是一份 TypeScript 编码风格规范，而是将 Robert C. Martin 的软件工程著作 [《Clean Code》](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) 适用到 TypeScript，引导读者使用 TypeScript 编写[易读、复用和可扩展](https://github.com/ryanmcdermott/3rs-of-software-architecture)的软件。

实际上，并不是每一个原则都要严格遵守，能被广泛认同的原则就更少了。这看起来虽然只是一份指导原则，但却是 *Clean Code* 作者对多年编程经验的凝练。

软件工程技术已有50多年的历史了，我们仍然要学习很多的东西。当软件架构和架构本身一样古老的时候，也许我们需要遵守更严格的规则。但是现在，让这些指导原则作为评估您和您的团队代码质量的试金石。

最后你需要知道的是，这些东西不会让你立刻变成一个优秀的工程师，长期奉行他们也并不意味着你能够高枕无忧不再犯错。千里之行，始于足下。我们需要时常和同行们进行代码评审，不断优化自己的代码。不要惧怕改善代码质量所需付出的努力，加油。

## **Variables 变量**

>计算机科学只存在两个难题：缓存失效和命名。—— Phil KarIton

### Use meaningful and pronounceable variable names 使用有意义的变量名

**:-1: Bad:**

```javascript
function between<T>(a1: T, a2: T, a3: T) {
  return a2 <= a1 && a1 <= a3;
}
```

**:+1: Good:**

```javascript
function between<T>(value: T, left: T, right: T) {
  return left <= value && value <= right;
}
```

**[⬆ back to top](#table-of-contents)**

### Use the same vocabulary for the same type of variable 合并功能一致的变量

**:-1: Bad:**

```javascript
getUserInfo();
getClientData();
getCustomerRecord();
```

**:+1: Good:**

```javascript
getUser();
```

**[⬆ back to top](#table-of-contents)**

### Use searchable names 便于搜索的名字

We will read more code than we will ever write. It's important that the code we
do write is readable and searchable. By _not_ naming variables that end up
being meaningful for understanding our program, we hurt our readers.
Make your names searchable. Tools like
[buddy.js](https://github.com/danielstjules/buddy.js) and
[ESLint](https://github.com/eslint/eslint/blob/660e0918933e6e7fede26bc675a0763a6b357c94/docs/rules/no-magic-numbers.md)
can help identify unnamed constants.

往往我们读代码要比写的多，所以易读性和可搜索非常重要。如果不抽取并命名有意义的变量名，那就坑了读代码的人。代码一定要便于搜索，[TSLint](https://palantir.github.io/tslint/rules/no-magic-numbers/) 就可以帮助识别未命名的常量。


**:-1: Bad:**

```javascript
// What the heck is 86400000 for?
setTimeout(blastOff, 86400000);
```

**:+1: Good:**

```javascript
// Declare them as capitalized named constants.
const MILLISECONDS_PER_DAY = 60 * 60 * 24 * 1000; //86400000;

setTimeout(blastOff, MILLISECONDS_PER_DAY);
```

**[⬆ back to top](#table-of-contents)**

### Use explanatory variables 使用自解释的变量名

**:-1: Bad:**

```javascript
declare const users:Map<string, User>;

for (const keyValue of users) {
  // ...
}
```

**:+1: Good:**

```javascript
declare const users:Map<string, User>;

for (const [id, user] of users) {
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid Mental Mapping 避免思维映射

Explicit is better than implicit. (不要让人去猜测或想象变量的含义) *明确是王道。*

**:-1: Bad:**

```javascript
const locations = ["Austin", "New York", "San Francisco"];
locations.forEach(l => {
  doStuff();
  // Wait, what is `l` for again?
  dispatch(l);
});
```

**:+1: Good:**

```javascript
const locations = ["Austin", "New York", "San Francisco"];
locations.forEach(location => {
  doStuff();
  dispatch(location);
});
```

**[⬆ back to top](#table-of-contents)**

### Don't add unneeded context 不添加无用的上下文

If your class/object name tells you something, don't repeat that in your
variable name. 如果类名或对象名已经表达了某些信息，在内部变量名中不要再重复表达。

**:-1: Bad:**

```javascript
const Car = {
  carMake: "Honda",
  carModel: "Accord",
  carColor: "Blue"
};

function paintCar(car, color) {
  car.carColor = color;
}
```

**:+1: Good:**

```javascript
const Car = {
  make: "Honda",
  model: "Accord",
  color: "Blue"
};

function paintCar(car, color) {
  car.color = color;
}
```

**[⬆ back to top](#table-of-contents)**

### Use default parameters instead of short circuiting or conditionals 使用默认参数，而非短路或条件判断

Default parameters are often cleaner than short circuiting. Be aware that if you
use them, your function will only provide default values for `undefined`
arguments. Other "falsy" values such as `''`, `""`, `false`, `null`, `0`, and
`NaN`, will not be replaced by a default value.

**:-1: Bad:**

```javascript
function createMicrobrewery(name) {
  const breweryName = name || "Hipster Brew Co.";
  // ...
}
```

**:+1: Good:**

```javascript
function createMicrobrewery(name = "Hipster Brew Co.") {
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

## **Functions 函数**

### Function arguments (2 or fewer ideally) 参数越少越好 (理想情况不超过2个)

Limiting the amount of function parameters is incredibly important because it
makes testing your function easier. Having more than three leads to a
combinatorial explosion where you have to test tons of different cases with
each separate argument.

One or two arguments is the ideal case, and three should be avoided if possible.
Anything more than that should be consolidated. Usually, if you have
more than two arguments then your function is trying to do too much. In cases
where it's not, most of the time a higher-level object will suffice as an
argument.

Since JavaScript allows you to make objects on the fly, without a lot of class
boilerplate, you can use an object if you are finding yourself needing a
lot of arguments.

To make it obvious what properties the function expects, you can use the ES2015/ES6
destructuring syntax. This has a few advantages:

1. When someone looks at the function signature, it's immediately clear what
   properties are being used.
2. It can be used to simulate named parameters.
3. Destructuring also clones the specified primitive values of the argument
   object passed into the function. This can help prevent side effects. Note:
   objects and arrays that are destructured from the argument object are NOT
   cloned.
4. Linters can warn you about unused properties, which would be impossible
   without destructuring.

限制参数个数，这样函数测试会更容易。超过三个参数会导致测试复杂度激增，需要测试众多不同参数的组合场景。
理想情况，只有一两个参数。如果有两个以上的参数，那么您的函数可能就太过复杂了。

如果需要很多参数，请您考虑使用对象。为了使函数的属性更清晰，可以使用[解构](https://basarat.gitbooks.io/typescript/docs/destructuring.html)，它有以下优点：

1. 当有人查看函数签名时，会立即清楚使用了哪些属性。
2. 可以用来当作命名的参数
3. 解构对传递给函数的参数对象做深拷贝，这可预防副作用。(注意：**不会克隆**从参数对象中解构的对象和数组)
4. linters会对未使用的属性显示警告。

**:-1: Bad:**

```javascript
function createMenu(title, body, buttonText, cancellable) {
  // ...
}

createMenu("Foo", "Bar", "Baz", true);
```

**:+1: Good:**

```javascript
function createMenu({ title, body, buttonText, cancellable }) {
  // ...
}

createMenu({
  title: "Foo",
  body: "Bar",
  buttonText: "Baz",
  cancellable: true
});
```

**[⬆ back to top](#table-of-contents)**

### Functions should do one thing 函数只做一件事

This is by far the most important rule in software engineering. When functions
do more than one thing, they are harder to compose, test, and reason about.
When you can isolate a function to just one action, it can be refactored
easily and your code will read much cleaner. If you take nothing else away from
this guide other than this, you'll be ahead of many developers.

这是软件功能中最重要的原则之一。

功能不单一的函数将导致难以重构、测试和理解。功能单一的函数易于重构，并使代码更加干净。

**:-1: Bad:**

```javascript
function emailClients(clients) {
  clients.forEach(client => {
    const clientRecord = database.lookup(client);
    if (clientRecord.isActive()) {
      email(client);
    }
  });
}
```

**:+1: Good:**

```javascript
function emailActiveClients(clients) {
  clients.filter(isActiveClient).forEach(email);
}

function isActiveClient(client) {
  const clientRecord = database.lookup(client);
  return clientRecord.isActive();
}
```

**[⬆ back to top](#table-of-contents)**

### Function names should say what they do 函数名应明确表明其功能

**:-1: Bad:**

```javascript
function addToDate(date, month) {
  // ...
}

const date = new Date();

// It's hard to tell from the function name what is added
addToDate(date, 1);
```

**:+1: Good:**

```javascript
function addMonthToDate(month, date) {
  // ...
}

const date = new Date();
addMonthToDate(1, date);
```

**[⬆ back to top](#table-of-contents)**

### Functions should only be one level of abstraction 函数应该只做一层抽象

When you have more than one level of abstraction your function is usually
doing too much. Splitting up functions leads to reusability and easier
testing.

当函数的需要的抽象多于一层时通常意味着函数功能过于复杂，需将其进行分解以提高其可重用性和可测试性。

**:-1: Bad:**

```javascript
function parseBetterJSAlternative(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(" ");
  const tokens = [];
  REGEXES.forEach(REGEX => {
    statements.forEach(statement => {
      // ...
    });
  });

  const ast = [];
  tokens.forEach(token => {
    // lex...
  });

  ast.forEach(node => {
    // parse...
  });
}
```

**:+1: Good:**

```javascript
function parseBetterJSAlternative(code) {
  const tokens = tokenize(code);
  const syntaxTree = parse(tokens); // take it out to be a seperate func
  syntaxTree.forEach(node => {
    // parse...
  });
}

function tokenize(code) {
  const REGEXES = [
    // ...
  ];

  const statements = code.split(" ");
  const tokens = [];
  REGEXES.forEach(REGEX => {
    statements.forEach(statement => {
      tokens.push(/* ... */);
    });
  });

  return tokens;
}

function parse(tokens) {
  const syntaxTree = [];
  tokens.forEach(token => {
    syntaxTree.push(/* ... */);
  });

  return syntaxTree;
}
```

**[⬆ back to top](#table-of-contents)**

### Remove duplicate code 移除重复的代码

Do your absolute best to avoid duplicate code. Duplicate code is bad because it
means that there's more than one place to alter something if you need to change
some logic.

Imagine if you run a restaurant and you keep track of your inventory: all your
tomatoes, onions, garlic, spices, etc. If you have multiple lists that
you keep this on, then all have to be updated when you serve a dish with
tomatoes in them. If you only have one list, there's only one place to update!

Oftentimes you have duplicate code because you have two or more slightly
different things, that share a lot in common, but their differences force you
to have two or more separate functions that do much of the same things. Removing
duplicate code means creating an abstraction that can handle this set of
different things with just one function/module/class.

Getting the abstraction right is critical, that's why you should follow the
SOLID principles laid out in the _Classes_ section. Bad abstractions can be
worse than duplicate code, so be careful! Having said this, if you can make
a good abstraction, do it! Don't repeat yourself, otherwise you'll find yourself
updating multiple places anytime you want to change one thing.

永远、永远、永远不要在任何循环下有重复的代码。

这种做法毫无意义且潜在危险极大。重复的代码意味着逻辑变化时需要对不止一处进行修改。JS 弱类型的特点使得函数拥有更强的普适性。好好利用这一优点吧。

**:-1: Bad:**

```javascript
function showDeveloperList(developers) {
  developers.forEach(developer => {
    const expectedSalary = developer.calculateExpectedSalary();
    const experience = developer.getExperience();
    const githubLink = developer.getGithubLink();
    const data = {
      expectedSalary,
      experience,
      githubLink
    };

    render(data);
  });
}

function showManagerList(managers) { // pretty much the same
  managers.forEach(manager => {
    const expectedSalary = manager.calculateExpectedSalary();
    const experience = manager.getExperience();
    const portfolio = manager.getMBAProjects();
    const data = {
      expectedSalary,
      experience,
      portfolio
    };

    render(data);
  });
}
```

**:+1: Good:**

```javascript
function showEmployeeList(employees) {
  employees.forEach(employee => {
    const expectedSalary = employee.calculateExpectedSalary();
    const experience = employee.getExperience();

    const data = {
      expectedSalary,
      experience
    };

    switch (employee.type) {
      case "manager":
        data.portfolio = employee.getMBAProjects();
        break;
      case "developer":
        data.githubLink = employee.getGithubLink();
        break;
    }

    render(data);
  });
}
```

**[⬆ back to top](#table-of-contents)**

### Set default objects with Object.assign 使用 Object.assign 设置默认对象

**:-1: Bad:**

```javascript
const menuConfig = {
  title: null,
  body: "Bar",
  buttonText: null,
  cancellable: true
};

function createMenu(config) {
  config.title = config.title || "Foo";
  config.body = config.body || "Bar";
  config.buttonText = config.buttonText || "Baz";
  config.cancellable =
    config.cancellable !== undefined ? config.cancellable : true;
}

createMenu(menuConfig);
```

**:+1: Good:**

```javascript
const menuConfig = {
  title: "Order",
  // User did not include 'body' key
  buttonText: "Send",
  cancellable: true
};

function createMenu(config) {
  let finalConfig = Object.assign(
    {
      title: "Foo",
      body: "Bar",
      buttonText: "Baz",
      cancellable: true
    },
    config
  );
  return finalConfig
  // config now equals: {title: "Order", body: "Bar", buttonText: "Send", cancellable: true}
  // ...
}

createMenu(menuConfig);
```

**[⬆ back to top](#table-of-contents)**

### Don't use flags as function parameters 不要使用标记(Flag)作为函数参数

Flags tell your user that this function does more than one thing. Functions should do one thing. Split out your functions if they are following different code paths based on a boolean.

这通常意味着函数的功能的单一性已经被破坏。此时应考虑对函数进行再次划分。

**:-1: Bad:**

```javascript
function createFile(name, temp) {
  if (temp) {
    fs.create(`./temp/${name}`);
  } else {
    fs.create(name);
  }
}
```

**:+1: Good:**

```javascript
function createFile(name) {
  fs.create(name);
}

function createTempFile(name) {
  createFile(`./temp/${name}`);
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid Side Effects (part 1) 避免副作用

A function produces a side effect if it does anything other than take a value in
and return another value or values. A side effect could be writing to a file,
modifying some global variable, or accidentally wiring all your money to a
stranger.

Now, you do need to have side effects in a program on occasion. Like the previous
example, you might need to write to a file. What you want to do is to
centralize where you are doing this. Don't have several functions and classes
that write to a particular file. Have one service that does it. One and only one.

The main point is to avoid common pitfalls like sharing state between objects
without any structure, using mutable data types that can be written to by anything,
and not centralizing where your side effects occur. If you can do this, you will
be happier than the vast majority of other programmers.

当函数产生了除了“接受一个值并返回一个结果”之外的行为时，称该函数产生了副作用。比如写文件、修改全局变量或将你的钱全转给了一个陌生人等。

程序在某些情况下确实需要副作用这一行为，如先前例子中的写文件。这时应该将这些功能集中在一起，不要用多个函数/类修改某个文件。用且只用一个 service 完成这一需求。

**:-1: Bad:**

```javascript
// Global variable referenced by following function.
// If we had another function that used this name, now it'd be an array and it could break it.
let name = "Ryan McDermott";

function splitIntoFirstAndLastName() {
  name = name.split(" ");
}

splitIntoFirstAndLastName();

console.log(name); // ['Ryan', 'McDermott'];
```

**:+1: Good:**

```javascript
function splitIntoFirstAndLastName(name) {
  return name.split(" ");
}

const name = "Ryan McDermott";
const newName = splitIntoFirstAndLastName(name);

console.log(name); // 'Ryan McDermott';
console.log(newName); // ['Ryan', 'McDermott'];
```

**[⬆ back to top](#table-of-contents)**

### Avoid Side Effects (part 2)

In JavaScript, some values are unchangeable (immutable) and some are changeable 
(mutable). Objects and arrays are two kinds of mutable values so it's important 
to handle them carefully when they're passed as parameters to a function. A 
JavaScript function can change an object's properties or alter the contents of 
an array which could easily cause bugs elsewhere.

Suppose there's a function that accepts an array parameter representing a 
shopping cart. If the function makes a change in that shopping cart array - 
by adding an item to purchase, for example - then any other function that 
uses that same `cart` array will be affected by this addition. That may be 
great, however it could also be bad. Let's imagine a bad situation:

The user clicks the "Purchase" button which calls a `purchase` function that
spawns a network request and sends the `cart` array to the server. Because
of a bad network connection, the `purchase` function has to keep retrying the
request. Now, what if in the meantime the user accidentally clicks an "Add to Cart"
button on an item they don't actually want before the network request begins?
If that happens and the network request begins, then that purchase function
will send the accidentally added item because the `cart` array was modified.

A great solution would be for the `addItemToCart` function to always clone the 
`cart`, edit it, and return the clone. This would ensure that functions that are still
using the old shopping cart wouldn't be affected by the changes.

Two caveats to mention to this approach:

1. There might be cases where you actually want to modify the input object,
   but when you adopt this programming practice you will find that those cases
   are pretty rare. Most things can be refactored to have no side effects!

2. Cloning big objects can be very expensive in terms of performance. Luckily,
   this isn't a big issue in practice because there are
   [great libraries](https://facebook.github.io/immutable-js/) that allow
   this kind of programming approach to be fast and not as memory intensive as
   it would be for you to manually clone objects and arrays.



在 JavaScript 中，原类型是值传递，对象、数组是引用传递。

有这样一种情况，如果您的函数修改了购物车数组，用来添加购买的商品，那么其他使用该`cart`数组的函数都将受此添加操作的影响。想象一个糟糕的情况:

用户点击“购买”按钮，该按钮调用`purchase`函数，函数请求网络并将`cart`数组发送到服务器。由于网络连接不好，购买功能必须不断重试请求。恰巧在网络请求开始前，用户不小心点击了某个不想要的项目上的“Add to Cart”按钮，该怎么办？而此时网络请求开始，那么`purchase`函数将发送意外添加的项，因为它引用了一个购物车数组，`addItemToCart`函数修改了该数组，添加了不需要的项。

一个很好的解决方案是`addItemToCart`总是克隆`cart`，编辑它，并返回克隆。这确保引用购物车的其他函数不会受到任何更改的影响。

注意两点:

1. 在某些情况下，可能确实想要修改输入对象，这种情况非常少见。且大多数可以重构，确保没副作用！(见[纯函数](https://en.wikipedia.org/wiki/Pure_function))

2. 性能方面，克隆大对象代价确实比较大。还好有一些很好的库，它提供了一些高效快速的方法，且不像手动克隆对象和数组那样占用大量内存。


**:-1: Bad:**

```javascript
const addItemToCart = (cart, item) => {
  cart.push({ item, date: Date.now() });
};
```

**:+1: Good:**

```javascript
const addItemToCart = (cart, item) => {
  return [...cart, { item, date: Date.now() }];
};
```

**[⬆ back to top](#table-of-contents)**

### Don't write to global functions 不要写全局函数

Polluting globals is a bad practice in JavaScript because you could clash with another
library and the user of your API would be none-the-wiser until they get an
exception in production. Let's think about an example: what if you wanted to
extend JavaScript's native Array method to have a `diff` method that could
show the difference between two arrays? You could write your new function
to the `Array.prototype`, but it could clash with another library that tried
to do the same thing. What if that other library was just using `diff` to find
the difference between the first and last elements of an array? This is why it
would be much better to just use ES2015/ES6 classes and simply extend the `Array` global.

在 JS 中污染全局是一个非常不好的实践，这么做可能和其他库起冲突，且调用你的 API 的用户在实际环境中得到一个 exception 前对这一情况是一无所知的。

想象以下例子：如果你想扩展 JS 中的 Array，为其添加一个 `diff` 函数显示两个数组间的差异，此时应如何去做？你可以将 diff 写入 `Array.prototype`，但这么做会和其他有类似需求的库造成冲突。如果另一个库对 diff 的需求为比较一个数组中首尾元素间的差异呢？

使用 ES6 中的 class 对全局的 Array 做简单的扩展显然是一个更棒的选择。

**:-1: Bad:**

```javascript
Array.prototype.diff = function diff(comparisonArray) {
  const hash = new Set(comparisonArray);
  return this.filter(elem => !hash.has(elem));
};
```

**:+1: Good:**

```javascript
class SuperArray extends Array {
  diff(comparisonArray) {
    const hash = new Set(comparisonArray);
    return this.filter(elem => !hash.has(elem));
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Favor functional programming over imperative programming 采用函数式编程而不是命令式编程

JavaScript isn't a functional language in the way that Haskell is, but it has
a functional flavor to it. Functional languages can be cleaner and easier to test.
Favor this style of programming when you can.

函数式的编程具有更干净且便于测试的特点。尽可能的使用这种风格吧。

**:-1: Bad:**

```javascript
const programmerOutput = [
  {
    name: "Uncle Bobby",
    linesOfCode: 500
  },
  {
    name: "Suzie Q",
    linesOfCode: 1500
  },
  {
    name: "Jimmy Gosling",
    linesOfCode: 150
  },
  {
    name: "Gracie Hopper",
    linesOfCode: 1000
  }
];

let totalOutput = 0;

for (let i = 0; i < programmerOutput.length; i++) {
  totalOutput += programmerOutput[i].linesOfCode;
}
```

**:+1: Good:**

```javascript
const programmerOutput = [
  {
    name: "Uncle Bobby",
    linesOfCode: 500
  },
  {
    name: "Suzie Q",
    linesOfCode: 1500
  },
  {
    name: "Jimmy Gosling",
    linesOfCode: 150
  },
  {
    name: "Gracie Hopper",
    linesOfCode: 1000
  }
];

const totalOutput = programmerOutput.reduce(
  (totalLines, output) => totalLines + output.linesOfCode,
  0
);
```

**[⬆ back to top](#table-of-contents)**

### Encapsulate conditionals 封装判断条件

**:-1: Bad:**

```javascript
if (fsm.state === "fetching" && isEmpty(listNode)) {
  // ...
}
```

**:+1: Good:**

```javascript
function shouldShowSpinner(fsm, listNode) {
  return fsm.state === "fetching" && isEmpty(listNode);
}

if (shouldShowSpinner(fsmInstance, listNodeInstance)) {
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid negative conditionals 避免“否定情况”的判断

**:-1: Bad:**

```javascript
function isDOMNodeNotPresent(node) {
  // ...
}

if (!isDOMNodeNotPresent(node)) {
  // ...
}
```

**:+1: Good:**

```javascript
function isDOMNodePresent(node) {
  // ...
}

if (isDOMNodePresent(node)) {
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid conditionals 避免条件判断

This seems like an impossible task. Upon first hearing this, most people say,
"how am I supposed to do anything without an `if` statement?" The answer is that
you can use polymorphism to achieve the same task in many cases. The second
question is usually, "well that's great but why would I want to do that?" The
answer is a previous clean code concept we learned: a function should only do
one thing. When you have classes and functions that have `if` statements, you
are telling your user that your function does more than one thing. Remember,
just do one thing.

这看起来似乎不太可能。

大多人听到这的第一反应是：“怎么可能不用 if 完成其他功能呢？”许多情况下通过使用多态(polymorphism)可以达到同样的目的。

第二个问题在于采用这种方式的原因是什么。答案是我们之前提到过的：保持函数功能的单一性。

**:-1: Bad:**

```javascript
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case "777":
        return this.getMaxAltitude() - this.getPassengerCount();
      case "Air Force One":
        return this.getMaxAltitude();
      case "Cessna":
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}
```

**:+1: Good:**

```javascript
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid type-checking (part 1) 避免类型判断(part 1)

JavaScript is untyped, which means your functions can take any type of argument.
Sometimes you are bitten by this freedom and it becomes tempting to do
type-checking in your functions. There are many ways to avoid having to do this.
The first thing to consider is consistent APIs.

JS 是弱类型语言，这意味着函数可接受任意类型的参数。

有时这会对你带来麻烦，你会对参数做一些类型判断。有许多方法可以避免这些情况。

**:-1: Bad:**

```javascript
function travelToTexas(vehicle) {
  if (vehicle instanceof Bicycle) {
    vehicle.pedal(this.currentLocation, new Location("texas"));
  } else if (vehicle instanceof Car) {
    vehicle.drive(this.currentLocation, new Location("texas"));
  }
}
```

**:+1: Good:**

```javascript
function travelToTexas(vehicle) {
  vehicle.move(this.currentLocation, new Location("texas"));
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid type-checking (part 2) 避免类型判断(part 2)

If you are working with basic primitive values like strings and integers,
and you can't use polymorphism but you still feel the need to type-check,
you should consider using TypeScript. It is an excellent alternative to normal
JavaScript, as it provides you with static typing on top of standard JavaScript
syntax. The problem with manually type-checking normal JavaScript is that
doing it well requires so much extra verbiage that the faux "type-safety" you get
doesn't make up for the lost readability. Keep your JavaScript clean, write
good tests, and have good code reviews. Otherwise, do all of that but with
TypeScript (which, like I said, is a great alternative!).

如果需处理的数据为字符串，整型，数组等类型，无法使用多态并仍有必要对其进行类型检测时，可以考虑使用 TypeScript。

**:-1: Bad:**

```javascript
function combine(val1, val2) {
  if (
    (typeof val1 === "number" && typeof val2 === "number") ||
    (typeof val1 === "string" && typeof val2 === "string")
  ) {
    return val1 + val2;
  }

  throw new Error("Must be of type String or Number");
}
```

**:+1: Good:**

```javascript
function combine(val1, val2) {
  return val1 + val2;
}
```

**[⬆ back to top](#table-of-contents)**

### Don't over-optimize 避免过度优化

Modern browsers do a lot of optimization under-the-hood at runtime. A lot of
times, if you are optimizing then you are just wasting your time. [There are good
resources](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers)
for seeing where optimization is lacking. Target those in the meantime, until
they are fixed if they can be.

现代的浏览器在运行时会对代码自动进行优化。有时人为对代码进行优化可能是在浪费时间。

[这里可以找到许多真正需要优化的地方](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers)

**:-1: Bad:**

```javascript
// On old browsers, each iteration with uncached `list.length` would be costly
// because of `list.length` recomputation. In modern browsers, this is optimized.
for (let i = 0, len = list.length; i < len; i++) {
  // ...
}
```

**:+1: Good:**

```javascript
for (let i = 0; i < list.length; i++) {
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

### Remove dead code 删除无效的代码

Dead code is just as bad as duplicate code. There's no reason to keep it in
your codebase. If it's not being called, get rid of it! It will still be safe
in your version history if you still need it.

不再被调用的代码应及时删除。

**:-1: Bad:**

```javascript
function oldRequestModule(url) {
  // ...
}

function newRequestModule(url) {
  // ...
}

const req = newRequestModule;
inventoryTracker("apples", req, "www.inventory-awesome.io");
```

**:+1: Good:**

```javascript
function newRequestModule(url) {
  // ...
}

const req = newRequestModule;
inventoryTracker("apples", req, "www.inventory-awesome.io");
```

**[⬆ back to top](#table-of-contents)**

## **Objects and Data Structures 对象和数据结构**

### Use getters and setters 使用 getters 和 setters

Using getters and setters to access data on objects could be better than simply
looking for a property on an object. "Why?" you might ask. Well, here's an
unorganized list of reasons why:

- When you want to do more beyond getting an object property, you don't have
  to look up and change every accessor in your codebase.
- Makes adding validation simple when doing a `set`.
- Encapsulates the internal representation.
- Easy to add logging and error handling when getting and setting.
- You can lazy load your object's properties, let's say getting it from a
  server.

JS 没有接口或类型，因此实现这一模式是很困难的，因为我们并没有类似 `public` 和 `private` 的关键词。

然而，使用 getters 和 setters 获取对象的数据远比直接使用点操作符具有优势。为什么呢？

1. 当需要对获取的对象属性执行额外操作时。
2. 执行 `set` 时可以增加规则对要变量的合法性进行判断。
3. 封装了内部逻辑。
4. 在存取时可以方便的增加日志和错误处理。
5. 继承该类时可以重载默认行为。
6. 从服务器获取数据时可以进行懒加载。

**:-1: Bad:**

```javascript
function makeBankAccount() {
  // ...

  return {
    balance: 0
    // ...
  };
}

const account = makeBankAccount();
account.balance = 100;
```

**:+1: Good:**

```javascript
function makeBankAccount() {
  // this one is private
  let balance = 0;

  // a "getter", made public via the returned object below
  function getBalance() {
    return balance;
  }

  // a "setter", made public via the returned object below
  function setBalance(amount) {
    // ... validate before updating the balance
    balance = amount;
  }

  return {
    // ...
    getBalance,
    setBalance
  };
}

const account = makeBankAccount();
account.setBalance(100);
```

**[⬆ back to top](#table-of-contents)**

### Make objects have private members 让对象拥有私有成员

This can be accomplished through closures (for ES5 and below). 可以通过闭包完成

**:-1: Bad:**

```javascript
const Employee = function(name) {
  this.name = name;
};

Employee.prototype.getName = function getName() {
  return this.name;
};

const employee = new Employee("John Doe");
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
delete employee.name;
console.log(`Employee name: ${employee.getName()}`); // Employee name: undefined
```

**:+1: Good:**

```javascript
function makeEmployee(name) {
  return {
    getName() {
      return name;
    }
  };
}

const employee = makeEmployee("John Doe");
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
delete employee.name;
console.log(`Employee name: ${employee.getName()}`); // Employee name: John Doe
```

**[⬆ back to top](#table-of-contents)**

## **Classes 类**

### Prefer ES2015/ES6 classes over ES5 plain functions 使用 ES6 的 classes 而不是 ES5 的 Function

It's very difficult to get readable class inheritance, construction, and method
definitions for classical ES5 classes. If you need inheritance (and be aware
that you might not), then prefer ES2015/ES6 classes. However, prefer small functions over
classes until you find yourself needing larger and more complex objects.

典型的 ES5 的类(function)在继承、构造和方法定义方面可读性较差。

当需要继承时，优先选用 classes。

但是，当在需要更大更复杂的对象时，最好优先选择更小的 function 而非 classes。

**:-1: Bad:**

```javascript
const Animal = function(age) {
  if (!(this instanceof Animal)) {
    throw new Error("Instantiate Animal with `new`");
  }

  this.age = age;
};

Animal.prototype.move = function move() {};

const Mammal = function(age, furColor) {
  if (!(this instanceof Mammal)) {
    throw new Error("Instantiate Mammal with `new`");
  }

  Animal.call(this, age);
  this.furColor = furColor;
};

Mammal.prototype = Object.create(Animal.prototype);
Mammal.prototype.constructor = Mammal;
Mammal.prototype.liveBirth = function liveBirth() {};

const Human = function(age, furColor, languageSpoken) {
  if (!(this instanceof Human)) {
    throw new Error("Instantiate Human with `new`");
  }

  Mammal.call(this, age, furColor);
  this.languageSpoken = languageSpoken;
};

Human.prototype = Object.create(Mammal.prototype);
Human.prototype.constructor = Human;
Human.prototype.speak = function speak() {};
```

**:+1: Good:**

```javascript
class Animal {
  constructor(age) {
    this.age = age;
  }

  move() {
    /* ... */
  }
}

class Mammal extends Animal {
  constructor(age, furColor) {
    super(age);
    this.furColor = furColor;
  }

  liveBirth() {
    /* ... */
  }
}

class Human extends Mammal {
  constructor(age, furColor, languageSpoken) {
    super(age, furColor);
    this.languageSpoken = languageSpoken;
  }

  speak() {
    /* ... */
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Use method chaining 使用方法链

This pattern is very useful in JavaScript and you see it in many libraries such
as jQuery and Lodash. It allows your code to be expressive, and less verbose.
For that reason, I say, use method chaining and take a look at how clean your code
will be. In your class functions, simply return `this` at the end of every function,
and you can chain further class methods onto it.

这里我们的理解与《代码整洁之道》的建议有些不同。

有争论说方法链不够干净且违反了[德米特法则](https://en.wikipedia.org/wiki/Law_of_Demeter)，也许这是对的，但这种方法在 JS 及许多库(如 JQuery)中显得非常实用。

因此，我认为在 JS 中使用方法链是非常合适的。在 class 的函数中返回 this，能够方便的将类需要执行的多个方法链接起来。

**:-1: Bad:**

```javascript
class Car {
  constructor() {
    this.make = 'Honda';
    this.model = 'Accord';
    this.color = 'white';
  }

  setMake(make) {
    this.name = name;
  }

  setModel(model) {
    this.model = model;
  }

  setColor(color) {
    this.color = color;
  }

  save() {
    console.log(this.make, this.model, this.color);
  }
}

let car = new Car();
car.setColor('pink');
car.setMake('Ford');
car.setModel('F-150')
car.save();
```

**:+1: Good:**

```javascript
class Car {
  constructor() {
    this.make = 'Honda';
    this.model = 'Accord';
    this.color = 'white';
  }

  setMake(make) {
    this.name = name;
    // NOTE: Returning this for chaining
    return this;
  }

  setModel(model) {
    this.model = model;
    // NOTE: Returning this for chaining
    return this;
  }

  setColor(color) {
    this.color = color;
    // NOTE: Returning this for chaining
    return this;
  }

  save() {
    console.log(this.make, this.model, this.color);
  }
}

let car = new Car()
  .setColor('pink')
  .setMake('Ford')
  .setModel('F-150')
  .save();
```

**[⬆ back to top](#table-of-contents)**

### Prefer composition over inheritance 优先使用组合模式而非继承

As stated famously in [_Design Patterns_](https://en.wikipedia.org/wiki/Design_Patterns) by the Gang of Four,
you should prefer composition over inheritance where you can. There are lots of
good reasons to use inheritance and lots of good reasons to use composition.
The main point for this maxim is that if your mind instinctively goes for
inheritance, try to think if composition could model your problem better. In some
cases it can.

You might be wondering then, "when should I use inheritance?" It
depends on your problem at hand, but this is a decent list of when inheritance
makes more sense than composition:

1. Your inheritance represents an "is-a" relationship and not a "has-a"
   relationship (Human->Animal vs. User->UserDetails).
2. You can reuse code from the base classes (Humans can move like all animals).
3. You want to make global changes to derived classes by changing a base class.
   (Change the caloric expenditure of all animals when they move).

在著名的[设计模式](https://en.wikipedia.org/wiki/Design_Patterns)一书中提到，应多使用组合模式而非继承。

这么做有许多优点，在想要使用继承前，多想想能否通过组合模式满足需求吧。

那么，在什么时候继承具有更大的优势呢？这取决于你的具体需求，但大多情况下，可以遵守以下三点：

1. 继承关系表现为"是一个"而非"有一个"(如动物->人 和 用户->用户细节)
2. 可以复用基类的代码("Human"可以看成是"All animal"的一种)
3. 希望当基类改变时所有派生类都受到影响(如修改"all animals"移动时的卡路里消耗量)

**:-1: Bad:**

```javascript
class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // ...
}

// Bad because Employees "have" tax data. EmployeeTaxData is not a type of Employee
class EmployeeTaxData extends Employee {
  constructor(ssn, salary) {
    super();
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}
```

**:+1: Good:**

```javascript
class EmployeeTaxData {
  constructor(ssn, salary) {
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}

class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  setTaxData(ssn, salary) {
    this.taxData = new EmployeeTaxData(ssn, salary);
  }
  // ...
}
```

**[⬆ back to top](#table-of-contents)**

## **SOLID**

### Single Responsibility Principle (SRP) 单一职责原则 (SRP)

As stated in Clean Code, "There should never be more than one reason for a class
to change". It's tempting to jam-pack a class with a lot of functionality, like
when you can only take one suitcase on your flight. The issue with this is
that your class won't be conceptually cohesive and it will give it many reasons
to change. Minimizing the amount of times you need to change a class is important.
It's important because if too much functionality is in one class and you modify
a piece of it, it can be difficult to understand how that will affect other
dependent modules in your codebase.

如《代码整洁之道》一书中所述，“修改一个类的理由不应该超过一个”。

将多个功能塞进一个类的想法很诱人，但这将导致你的类无法达到概念上的内聚，并经常不得不进行修改。

最小化对一个类需要修改的次数是非常有必要的。如果一个类具有太多太杂的功能，当你对其中一小部分进行修改时，将很难想象到这一修够对代码库中依赖该类的其他模块会带来什么样的影响。

**:-1: Bad:**

```javascript
class UserSettings {
  constructor(user) {
    this.user = user;
  }

  changeSettings(settings) {
    if (this.verifyCredentials()) {
      // ...
    }
  }

  verifyCredentials() {
    // ...
  }
}
```

**:+1: Good:**

```javascript
class UserAuth {
  constructor(user) {
    this.user = user;
  }

  verifyCredentials() {
    // ...
  }
}

class UserSettings {
  constructor(user) {
    this.user = user;
    this.auth = new UserAuth(user);
  }

  changeSettings(settings) {
    if (this.auth.verifyCredentials()) {
      // ...
    }
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Open/Closed Principle (OCP)

As stated by Bertrand Meyer, "software entities (classes, modules, functions,
etc.) should be open for extension, but closed for modification." What does that
mean though? This principle basically states that you should allow users to
add new functionalities without changing existing code.

**:-1: Bad:**

```javascript
class AjaxAdapter extends Adapter {
  constructor() {
    super();
    this.name = "ajaxAdapter";
  }
}

class NodeAdapter extends Adapter {
  constructor() {
    super();
    this.name = "nodeAdapter";
  }
}

class HttpRequester {
  constructor(adapter) {
    this.adapter = adapter;
  }

  fetch(url) {
    if (this.adapter.name === "ajaxAdapter") {
      return makeAjaxCall(url).then(response => {
        // transform response and return
      });
    } else if (this.adapter.name === "nodeAdapter") {
      return makeHttpCall(url).then(response => {
        // transform response and return
      });
    }
  }
}

function makeAjaxCall(url) {
  // request and return promise
}

function makeHttpCall(url) {
  // request and return promise
}
```

**:+1: Good:**

```javascript
class AjaxAdapter extends Adapter {
  constructor() {
    super();
    this.name = "ajaxAdapter";
  }

  request(url) {
    // request and return promise
  }
}

class NodeAdapter extends Adapter {
  constructor() {
    super();
    this.name = "nodeAdapter";
  }

  request(url) {
    // request and return promise
  }
}

class HttpRequester {
  constructor(adapter) {
    this.adapter = adapter;
  }

  fetch(url) {
    return this.adapter.request(url).then(response => {
      // transform response and return
    });
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Liskov Substitution Principle (LSP)

This is a scary term for a very simple concept. It's formally defined as "If S
is a subtype of T, then objects of type T may be replaced with objects of type S
(i.e., objects of type S may substitute objects of type T) without altering any
of the desirable properties of that program (correctness, task performed,
etc.)." That's an even scarier definition.

The best explanation for this is if you have a parent class and a child class,
then the base class and child class can be used interchangeably without getting
incorrect results. This might still be confusing, so let's take a look at the
classic Square-Rectangle example. Mathematically, a square is a rectangle, but
if you model it using the "is-a" relationship via inheritance, you quickly
get into trouble.

**:-1: Bad:**

```javascript
class Rectangle {
  constructor() {
    this.width = 0;
    this.height = 0;
  }

  setColor(color) {
    // ...
  }

  render(area) {
    // ...
  }

  setWidth(width) {
    this.width = width;
  }

  setHeight(height) {
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  setWidth(width) {
    this.width = width;
    this.height = width;
  }

  setHeight(height) {
    this.width = height;
    this.height = height;
  }
}

function renderLargeRectangles(rectangles) {
  rectangles.forEach(rectangle => {
    rectangle.setWidth(4);
    rectangle.setHeight(5);
    const area = rectangle.getArea(); // BAD: Returns 25 for Square. Should be 20.
    rectangle.render(area);
  });
}

const rectangles = [new Rectangle(), new Rectangle(), new Square()];
renderLargeRectangles(rectangles);
```

**:+1: Good:**

```javascript
class Shape {
  setColor(color) {
    // ...
  }

  render(area) {
    // ...
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }
}

class Square extends Shape {
  constructor(length) {
    super();
    this.length = length;
  }

  getArea() {
    return this.length * this.length;
  }
}

function renderLargeShapes(shapes) {
  shapes.forEach(shape => {
    const area = shape.getArea();
    shape.render(area);
  });
}

const shapes = [new Rectangle(4, 5), new Rectangle(4, 5), new Square(5)];
renderLargeShapes(shapes);
```

**[⬆ back to top](#table-of-contents)**

### Interface Segregation Principle (ISP)

JavaScript doesn't have interfaces so this principle doesn't apply as strictly
as others. However, it's important and relevant even with JavaScript's lack of
type system.

ISP states that "Clients should not be forced to depend upon interfaces that
they do not use." Interfaces are implicit contracts in JavaScript because of
duck typing.

A good example to look at that demonstrates this principle in JavaScript is for
classes that require large settings objects. Not requiring clients to setup
huge amounts of options is beneficial, because most of the time they won't need
all of the settings. Making them optional helps prevent having a
"fat interface".

**:-1: Bad:**

```javascript
class DOMTraverser {
  constructor(settings) {
    this.settings = settings;
    this.setup();
  }

  setup() {
    this.rootNode = this.settings.rootNode;
    this.settings.animationModule.setup();
  }

  traverse() {
    // ...
  }
}

const $ = new DOMTraverser({
  rootNode: document.getElementsByTagName("body"),
  animationModule() {} // Most of the time, we won't need to animate when traversing.
  // ...
});
```

**:+1: Good:**

```javascript
class DOMTraverser {
  constructor(settings) {
    this.settings = settings;
    this.options = settings.options;
    this.setup();
  }

  setup() {
    this.rootNode = this.settings.rootNode;
    this.setupOptions();
  }

  setupOptions() {
    if (this.options.animationModule) {
      // ...
    }
  }

  traverse() {
    // ...
  }
}

const $ = new DOMTraverser({
  rootNode: document.getElementsByTagName("body"),
  options: {
    animationModule() {}
  }
});
```

**[⬆ back to top](#table-of-contents)**

### Dependency Inversion Principle (DIP)

This principle states two essential things:

1. High-level modules should not depend on low-level modules. Both should
   depend on abstractions.
2. Abstractions should not depend upon details. Details should depend on
   abstractions.

This can be hard to understand at first, but if you've worked with AngularJS,
you've seen an implementation of this principle in the form of Dependency
Injection (DI). While they are not identical concepts, DIP keeps high-level
modules from knowing the details of its low-level modules and setting them up.
It can accomplish this through DI. A huge benefit of this is that it reduces
the coupling between modules. Coupling is a very bad development pattern because
it makes your code hard to refactor.

As stated previously, JavaScript doesn't have interfaces so the abstractions
that are depended upon are implicit contracts. That is to say, the methods
and properties that an object/class exposes to another object/class. In the
example below, the implicit contract is that any Request module for an
`InventoryTracker` will have a `requestItems` method.

**:-1: Bad:**

```javascript
class InventoryRequester {
  constructor() {
    this.REQ_METHODS = ["HTTP"];
  }

  requestItem(item) {
    // ...
  }
}

class InventoryTracker {
  constructor(items) {
    this.items = items;

    // BAD: We have created a dependency on a specific request implementation.
    // We should just have requestItems depend on a request method: `request`
    this.requester = new InventoryRequester();
  }

  requestItems() {
    this.items.forEach(item => {
      this.requester.requestItem(item);
    });
  }
}

const inventoryTracker = new InventoryTracker(["apples", "bananas"]);
inventoryTracker.requestItems();
```

**:+1: Good:**

```javascript
class InventoryTracker {
  constructor(items, requester) {
    this.items = items;
    this.requester = requester;
  }

  requestItems() {
    this.items.forEach(item => {
      this.requester.requestItem(item);
    });
  }
}

class InventoryRequesterV1 {
  constructor() {
    this.REQ_METHODS = ["HTTP"];
  }

  requestItem(item) {
    // ...
  }
}

class InventoryRequesterV2 {
  constructor() {
    this.REQ_METHODS = ["WS"];
  }

  requestItem(item) {
    // ...
  }
}

// By constructing our dependencies externally and injecting them, we can easily
// substitute our request module for a fancy new one that uses WebSockets.
const inventoryTracker = new InventoryTracker(
  ["apples", "bananas"],
  new InventoryRequesterV2()
);
inventoryTracker.requestItems();
```

**[⬆ back to top](#table-of-contents)**

## **Testing**

Testing is more important than shipping. If you have no tests or an
inadequate amount, then every time you ship code you won't be sure that you
didn't break anything. Deciding on what constitutes an adequate amount is up
to your team, but having 100% coverage (all statements and branches) is how
you achieve very high confidence and developer peace of mind. This means that
in addition to having a great testing framework, you also need to use a
[good coverage tool](https://gotwarlost.github.io/istanbul/).

There's no excuse to not write tests. There are [plenty of good JS test frameworks](https://jstherightway.org/#testing-tools), so find one that your team prefers.
When you find one that works for your team, then aim to always write tests
for every new feature/module you introduce. If your preferred method is
Test Driven Development (TDD), that is great, but the main point is to just
make sure you are reaching your coverage goals before launching any feature,
or refactoring an existing one.

### Single concept per test

**:-1: Bad:**

```javascript
import assert from "assert";

describe("MomentJS", () => {
  it("handles date boundaries", () => {
    let date;

    date = new MomentJS("1/1/2015");
    date.addDays(30);
    assert.equal("1/31/2015", date);

    date = new MomentJS("2/1/2016");
    date.addDays(28);
    assert.equal("02/29/2016", date);

    date = new MomentJS("2/1/2015");
    date.addDays(28);
    assert.equal("03/01/2015", date);
  });
});
```

**:+1: Good:**

```javascript
import assert from "assert";

describe("MomentJS", () => {
  it("handles 30-day months", () => {
    const date = new MomentJS("1/1/2015");
    date.addDays(30);
    assert.equal("1/31/2015", date);
  });

  it("handles leap year", () => {
    const date = new MomentJS("2/1/2016");
    date.addDays(28);
    assert.equal("02/29/2016", date);
  });

  it("handles non-leap year", () => {
    const date = new MomentJS("2/1/2015");
    date.addDays(28);
    assert.equal("03/01/2015", date);
  });
});
```

**[⬆ back to top](#table-of-contents)**

## **Concurrency**

### Use Promises, not callbacks

Callbacks aren't clean, and they cause excessive amounts of nesting. With ES2015/ES6,
Promises are a built-in global type. Use them!

**:-1: Bad:**

```javascript
import { get } from "request";
import { writeFile } from "fs";

get(
  "https://en.wikipedia.org/wiki/Robert_Cecil_Martin",
  (requestErr, response, body) => {
    if (requestErr) {
      console.error(requestErr);
    } else {
      writeFile("article.html", body, writeErr => {
        if (writeErr) {
          console.error(writeErr);
        } else {
          console.log("File written");
        }
      });
    }
  }
);
```

**:+1: Good:**

```javascript
import { get } from "request-promise";
import { writeFile } from "fs-extra";

get("https://en.wikipedia.org/wiki/Robert_Cecil_Martin")
  .then(body => {
    return writeFile("article.html", body);
  })
  .then(() => {
    console.log("File written");
  })
  .catch(err => {
    console.error(err);
  });
```

**[⬆ back to top](#table-of-contents)**

### Async/Await are even cleaner than Promises

Promises are a very clean alternative to callbacks, but ES2017/ES8 brings async and await
which offer an even cleaner solution. All you need is a function that is prefixed
in an `async` keyword, and then you can write your logic imperatively without
a `then` chain of functions. Use this if you can take advantage of ES2017/ES8 features
today!

**:-1: Bad:**

```javascript
import { get } from "request-promise";
import { writeFile } from "fs-extra";

get("https://en.wikipedia.org/wiki/Robert_Cecil_Martin")
  .then(body => {
    return writeFile("article.html", body);
  })
  .then(() => {
    console.log("File written");
  })
  .catch(err => {
    console.error(err);
  });
```

**:+1: Good:**

```javascript
import { get } from "request-promise";
import { writeFile } from "fs-extra";

async function getCleanCodeArticle() {
  try {
    const body = await get(
      "https://en.wikipedia.org/wiki/Robert_Cecil_Martin"
    );
    await writeFile("article.html", body);
    console.log("File written");
  } catch (err) {
    console.error(err);
  }
}

getCleanCodeArticle()
```

**[⬆ back to top](#table-of-contents)**

## **Error Handling**

Thrown errors are a good thing! They mean the runtime has successfully
identified when something in your program has gone wrong and it's letting
you know by stopping function execution on the current stack, killing the
process (in Node), and notifying you in the console with a stack trace.

### Don't ignore caught errors

Doing nothing with a caught error doesn't give you the ability to ever fix
or react to said error. Logging the error to the console (`console.log`)
isn't much better as often times it can get lost in a sea of things printed
to the console. If you wrap any bit of code in a `try/catch` it means you
think an error may occur there and therefore you should have a plan,
or create a code path, for when it occurs.

**:-1: Bad:**

```javascript
try {
  functionThatMightThrow();
} catch (error) {
  console.log(error);
}
```

**:+1: Good:**

```javascript
try {
  functionThatMightThrow();
} catch (error) {
  // One option (more noisy than console.log):
  console.error(error);
  // Another option:
  notifyUserOfError(error);
  // Another option:
  reportErrorToService(error);
  // OR do all three!
}
```

### Don't ignore rejected promises

For the same reason you shouldn't ignore caught errors
from `try/catch`.

**:-1: Bad:**

```javascript
getdata()
  .then(data => {
    functionThatMightThrow(data);
  })
  .catch(error => {
    console.log(error);
  });
```

**:+1: Good:**

```javascript
getdata()
  .then(data => {
    functionThatMightThrow(data);
  })
  .catch(error => {
    // One option (more noisy than console.log):
    console.error(error);
    // Another option:
    notifyUserOfError(error);
    // Another option:
    reportErrorToService(error);
    // OR do all three!
  });
```

**[⬆ back to top](#table-of-contents)**

## **Formatting**

Formatting is subjective. Like many rules herein, there is no hard and fast
rule that you must follow. The main point is DO NOT ARGUE over formatting.
There are [tons of tools](https://standardjs.com/rules.html) to automate this.
Use one! It's a waste of time and money for engineers to argue over formatting.

For things that don't fall under the purview of automatic formatting
(indentation, tabs vs. spaces, double vs. single quotes, etc.) look here
for some guidance.

### Use consistent capitalization

JavaScript is untyped, so capitalization tells you a lot about your variables,
functions, etc. These rules are subjective, so your team can choose whatever
they want. The point is, no matter what you all choose, just be consistent.

**:-1: Bad:**

```javascript
const DAYS_IN_WEEK = 7;
const daysInMonth = 30;

const songs = ["Back In Black", "Stairway to Heaven", "Hey Jude"];
const Artists = ["ACDC", "Led Zeppelin", "The Beatles"];

function eraseDatabase() {}
function restore_database() {}

class animal {}
class Alpaca {}
```

**:+1: Good:**

```javascript
const DAYS_IN_WEEK = 7;
const DAYS_IN_MONTH = 30;

const SONGS = ["Back In Black", "Stairway to Heaven", "Hey Jude"];
const ARTISTS = ["ACDC", "Led Zeppelin", "The Beatles"];

function eraseDatabase() {}
function restoreDatabase() {}

class Animal {}
class Alpaca {}
```

**[⬆ back to top](#table-of-contents)**

### Function callers and callees should be close

If a function calls another, keep those functions vertically close in the source
file. Ideally, keep the caller right above the callee. We tend to read code from
top-to-bottom, like a newspaper. Because of this, make your code read that way.

**:-1: Bad:**

```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  lookupPeers() {
    return db.lookup(this.employee, "peers");
  }

  lookupManager() {
    return db.lookup(this.employee, "manager");
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```

**:+1: Good:**

```javascript
class PerformanceReview {
  constructor(employee) {
    this.employee = employee;
  }

  perfReview() {
    this.getPeerReviews();
    this.getManagerReview();
    this.getSelfReview();
  }

  getPeerReviews() {
    const peers = this.lookupPeers();
    // ...
  }

  lookupPeers() {
    return db.lookup(this.employee, "peers");
  }

  getManagerReview() {
    const manager = this.lookupManager();
  }

  lookupManager() {
    return db.lookup(this.employee, "manager");
  }

  getSelfReview() {
    // ...
  }
}

const review = new PerformanceReview(employee);
review.perfReview();
```

**[⬆ back to top](#table-of-contents)**

## **Comments**

### Only comment things that have business logic complexity.

Comments are an apology, not a requirement. Good code _mostly_ documents itself.

**:-1: Bad:**

```javascript
function hashIt(data) {
  // The hash
  let hash = 0;

  // Length of string
  const length = data.length;

  // Loop through every character in data
  for (let i = 0; i < length; i++) {
    // Get character code.
    const char = data.charCodeAt(i);
    // Make the hash
    hash = (hash << 5) - hash + char;
    // Convert to 32-bit integer
    hash &= hash;
  }
}
```

**:+1: Good:**

```javascript
function hashIt(data) {
  let hash = 0;
  const length = data.length;

  for (let i = 0; i < length; i++) {
    const char = data.charCodeAt(i);
    hash = (hash << 5) - hash + char;

    // Convert to 32-bit integer
    hash &= hash;
  }
}
```

**[⬆ back to top](#table-of-contents)**

### Don't leave commented out code in your codebase

Version control exists for a reason. Leave old code in your history.

**:-1: Bad:**

```javascript
doStuff();
// doOtherStuff();
// doSomeMoreStuff();
// doSoMuchStuff();
```

**:+1: Good:**

```javascript
doStuff();
```

**[⬆ back to top](#table-of-contents)**

### Don't have journal comments

Remember, use version control! There's no need for dead code, commented code,
and especially journal comments. Use `git log` to get history!

**:-1: Bad:**

```javascript
/**
 * 2016-12-20: Removed monads, didn't understand them (RM)
 * 2016-10-01: Improved using special monads (JP)
 * 2016-02-03: Removed type-checking (LI)
 * 2015-03-14: Added combine with type-checking (JR)
 */
function combine(a, b) {
  return a + b;
}
```

**:+1: Good:**

```javascript
function combine(a, b) {
  return a + b;
}
```

**[⬆ back to top](#table-of-contents)**

### Avoid positional markers

They usually just add noise. Let the functions and variable names along with the
proper indentation and formatting give the visual structure to your code.

**:-1: Bad:**

```javascript
////////////////////////////////////////////////////////////////////////////////
// Scope Model Instantiation
////////////////////////////////////////////////////////////////////////////////
$scope.model = {
  menu: "foo",
  nav: "bar"
};

////////////////////////////////////////////////////////////////////////////////
// Action setup
////////////////////////////////////////////////////////////////////////////////
const actions = function() {
  // ...
};
```

**:+1: Good:**

```javascript
$scope.model = {
  menu: "foo",
  nav: "bar"
};

const actions = function() {
  // ...
};
```

**[⬆ back to top](#table-of-contents)**

### SOLID

In object-oriented computer programming, `SOLID` is an acronym for five design principles intended to make software designs more understandable, flexible and maintainable.

`S` — Single responsibility principle

`O` — Open closed principle

`L` — Liskov substitution principle

`I` — Interface segregation principle

`D` — Dependency Inversion principle

#### Single responsibility

`A class should have one and only one reason to change, meaning that a class should only have one job.`

Following this principle helps to produce more loosely coupled and modular systems, since many kinds of new behavior can be implemented as new classes, rather than by adding additional responsibility to existing classes. Adding new classes is always safer than changing existing classes, since no code yet depends on the new classes.

When this principle is applied to application architecture and taken to its logical endpoint, you get microservices. A given microservice should have a single responsibility. If you need to extend the behavior of a system, it's usually better to do it by adding additional microservices, rather than by adding responsibility to an existing one.

#### Open closed

`Objects or entities should be open for extension, but closed for modification.`

`Open for extension` means that we should be able to add new features or components to the application without breaking existing code.

`Closed for modification` means that we should not introduce breaking changes to existing functionality, because that would force you to refactor a lot of existing code

#### Liskov substitution

`Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.`

Subclass should override the parent class methods in a way that does not break functionality from a client’s point of view.

#### Interface segregation

`A client should never be forced to implement an interface that it doesn’t use or clients shouldn’t be forced to depend on methods they do not use`

#### Dependency Inversion

`Entities must depend on abstractions not on concretions. It states that the high level module must not depend on the low level module, but they should depend on abstractions`

### Don't repeat yourself (DRY)

The application should avoid specifying behavior related to a particular concept in multiple places as this practice is a frequent source of errors. At some point, a change in requirements will require changing this behavior. It's likely that at least one instance of the behavior will fail to be updated, and the system will behave inconsistently.

Rather than duplicating logic, encapsulate it in a programming construct. Make this construct the single authority over this behavior, and have any other part of the application that requires this behavior use the new construct.

### Keep it Short and Simple (KISS Principle)

Keep it simple, stupid (KISS) is a design principle which states that designs and/or systems should be as simple as possible. Wherever possible, complexity should be avoided in a system—as simplicity guarantees the greatest levels of user acceptance and interaction.
