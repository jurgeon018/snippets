/***************************************
BorisRubin Homework Day 16 - JavaScript
***************************************/


// Проверка введенного значения на его соответствие числу
const isNum = function(n)
{
    return !isNaN(parseFloat(n)) && isFinite(n);
};


// Площадь прямоугольника
const areaCalc = function()
{
    let a, b;

    while(!isNum(a))
    {
       a = parseFloat(prompt("Input side А of th area:"));
    }

    while(!isNum(b))
    {
       b = parseFloat(prompt("Input side B of th area:"));
    }

    return a * b;
};


// Посчитать выражение пользователя
const calc =  function()
{
    let a, b, oprt;

    while(!isNum(a))
    {
        a = Number(prompt("Input first number:"));
    }

    while(!isNum(b))
    {
        b = Number(prompt("Input second number:"));
    }

    while(oprt !== '+' && oprt !== '-')
    {
        oprt = prompt("Input opertion type '-' or '+'");
    }

    if(oprt === '+'){
        return a + b;
    } else {
        return a - b;
    }

};

//Простые числа в диапазоне от 0 до n
const primes = function()
{
    let a;
    let numbers = [];

    while(!isNum(a))
    {
        a = Number(prompt("Input number:"));
    }

    for(let i = 2; i < a + 1; i++)
    {
        let tmp = [];

        for(let j = 2; j <=  i; j++)
        {
            if(i % j === 0)
            {
                tmp.push(j);
            }
        }

        if(tmp.length === 1)
        {
            numbers.push(i);
        }

    }

    return numbers;
};


// Все числа кратные 5 в диапазоне
const multipleOf_5 = function()
{
    let a, b;
    let numbers = [];

    while(!isNum(a))
    {
       a = parseFloat(prompt("Input first number:"));
    }

    while(!isNum(b))
    {
       b = parseFloat(prompt("Input second number:"));
    }

    for(let i = a; i <= b; i++)
    {
        if(i % 5 === 0)
        {
            numbers.push(i);
        }
    }

    return numbers;
};


// сортировка массива
const sortArray = function()
{
    let arr = [1, 12, 44, -12, 20, 99];

    arr = arr.sort();

    return arr;
};


// Создание объекта
const createObj = function()
{
    let obj = {};

    for(let i = 0; i < 5; i++)
    {
        let item = (Math.round(Math.random() * 100));
        obj['item'+item] = item;
    }

    return obj;
};


// Экстремумы массива чисел
const extremum = function()
{
    let arr = [1, -2, 0, 10, 213, 10.4, 883, -1290.102, 3.1415, -1.11111111];
    let max = Math.max(...arr);
    let min = Math.min(...arr);

    return "Max number = " + max + " / Min number = " + min;
};


// Конкатенация значений массива ['Earth', 'Russia', 'Moscow']
const concat = function()
{
    let arr = ['Earth', 'Russia', 'Moscow'];
    let str = lst.join('->');

    return "Result string: " + str;
};


// Распарсить строку в массив '/bin:/usr/bin:/usr/local/bin' по символу ':'
const parseString = function()
{
    let str = '/bin:/usr/bin:/usr/local/bin';
    let arr = str.split(":");

    return "Array: " + arr;
};


// Проверить числа от 1 до 100 на кратность 7
const testMultOf7 = function()
{
    let multiples = [];
    let non_multiples = [];

    for(let i = 0; i <= 100; i++)
    {
        if(i % 7 === 0){
            multiples.push(i);
        } else {
            non_multiples.push(i);
        }
    }

    return {multiples: multiples, non_multiples : non_multiples};
};


// Создать и вывести матрицу 3х4
const matrixPrint = function()
{
    let arr = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]];

    for(let ln = 0; ln < 3; ln++)
    {
        console.log("Line " + (ln + 1) + " [" + arr[ln] + "]");
    }

    for(let cl = 0; cl < 4; cl++)
    {
        let col_str = "";
        for(let ln = 0; ln < 3; ln++)
        {
            col_str = col_str + arr[ln][cl] + (ln === 2 ? "" : " ") ;
        }

        console.log("Column " + (cl + 1) + " [" + col_str + "]");
    }
};


// Вывести элементы массива с индексом
const printArray = function()
{
    let arr = [1, 'some', true, {name:'Boris', age:39}, 222, [1, 2, 3], NaN];
    for(let i in arr)
    {
        console.log("Array item "+ i + " = " + arr[i]);
    }
};


//Отфильтровать значения to-delete из массива
const filterArray = function()
{
    let arr = ['to-delete', 1, 'some text', 'to-delete', [1,2,3], 'to-delete', NaN, 0];
    let newArr = arr.filter(item => item !== 'to-delete');

    return newArr;
};


const countdown = function(n)
{
    for(let i = n; i > 0; i--)
    {
        console.log(i)
    }
};



/***********************
        All tests
***********************/

confirm("Task1");
alert("Area: " + areaCalc());

confirm("Task 2");
alert("Result: " + calc());

confirm("Task 3");
alert("Primes: " + primes());

confirm("Task 4");
alert("Multiples of 5: " + multipleOf_5());

confirm("Task 5");
alert("Sorted array: " + sortList());

confirm("Task 6");
let some_obj = createObj();
for(let i in some_obj) {
   console.log(i + " = " + some_obj[i]);
}

confirm("Task 7");
alert(extremum());

confirm("Task 8");
alert(concat());

confirm("Task 9");
alert(parseString());

confirm("Task 10");
result = testMultOf7();
alert("Multiples of 7: " + result.multiples);
alert("Non-multiples of 7: " + result.non_multiples);

confirm("Task 11");
matrixPrint();

confirm("Task 12");
printArray();

confirm("Task 13");
alert(filterArray());

confirm("Task 14");
countdown(22);






// ###############################################
function isNumeric(n)
/*Проверка введенного значения на его соответствие числу
:param n: значение, которое нужно проверить
:return: True или False*/
{
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function areaRectangle()
/* Расчет площади прямоугольника по введенным пользователем значениям
:return: вычисленное значение площади прямоугольника*/
{
    var countSide = "";
    while (countSide !== '1' && countSide !== '2')
    {
        countSide = prompt("Сколько сторон прямоугольника будете задавать (1|2)? (введите из указанных)");

    }
    while (!isNumeric(sideA))
    {
       var sideA = parseFloat(prompt("Введите значение стороны прямоугольника"));
    }
    if (countSide === '2')
    {
         while (!isNumeric(sideB))
        {
           var sideB = parseFloat(prompt("Введите значение второй стороны прямоугольника"));
        }
    }
    else
    {
        sideB = sideA;
    }
    return sideA * sideB
}

function twoNumbers()
/* Вычисление выражения, заданного пользователем
:return: значение выражения*/
{
     while (!isNumeric(a))
    {
        var a = Number(prompt("Введите первое число"));
    }
     while (!isNumeric(b))
    {
        var b = Number(prompt("Введите второе число"));
    }
    var sign = "";
    while (sign !== '+' && sign !== '-')
    {
        sign = prompt("Введите значение операции между числами (-|+)");

    }
    switch (sign)
    {
        case "+":
            return a + b;
        case "-":
            return a - b;
    }
}

function primeNumbers()
/* Нахождения всех простых чисел между 0 и заданным пользователем
:return: список простых чисел*/
{
    while (!isNumeric(a))
    {
        var a = Number(prompt("Введите число"));
    }
    var numberList = [];
    for(var k = 2; k < a + 1; k++)
    {
       var elem = [];
       for(var j = 2; j <=  k; j++)
        {
              if(k % j === 0)
              {
                  elem.push(j);
               }
         }
        if(elem.length === 1)
        {
            numberList.push(k);
        }

     }

    return numberList
}

function multipleValue()
/* Нахождения всех числе, кратных 5 между двумя заданными
:return: список чисел*/
{
    while (!isNumeric(first))
    {
       var first = parseFloat(prompt("Введите первое число"));
    }
    while (!isNumeric(second))
    {
       var second = parseFloat(prompt("Введите второе число"));
    }
    var multipleNumbers = [];
    for(var i = first; i <= second; i++)
    {
        if(i % 5 === 0)
        {
            multipleNumbers.push(i);
        }
    }
    return multipleNumbers
}

function newList(n)
/*Создание списка случайных чисел
:return: список*/
{
    var l = []
    for(var i = 0; i < n; i++)
    {
        l.push(Math.round(Math.random() * 100) / 100);
    }
    return l
}

function sortList()
/* Создание сортированного списка
:return: список*/
{
    var l = newList(6);
    l = l.sort();
    return l
}

function printDict()
/* Создание словарь
:return: список*/
{
    var d = {};
    for(var i = 0; i < 5; i++)
    {
        var a = (Math.round(Math.random() * 100) / 100);
        d[a] = a;
    }
    return d
}

function maxMinNumbers()
/* Создание списка из 10 элементов и вывод максимального и минимального чисел
:return: None*/
{
    var l = newList(10);
    maxNum = Math.max.apply({},l);
    minNum = Math.min.apply({},l);
    alert("Максимальное и минимальное числа: " + maxNum + ", " + minNum);
}

function containStr()
/* Создание списка из 3 слов: ['Earth', 'Russia', 'Moscow']
:return: None*/
{
    var l = ['Earth', 'Russia', 'Moscow'];
    var s = l.join('->');
    alert("Строка: " + s);
}

function smashStr()
/* Разбиение строки в список '/bin:/usr/bin:/usr/local/bin'по символу ':'
:return: None*/
{
    var s = '/bin:/usr/bin:/usr/local/bin';
    var l = s.split(":");
    alert("Список: " + l);
}

function multipleNumbers()
/* Нахождения всех чисел, кратных 7  в диапазоне (0, 100)
:return: None*/
{
    var toMult = [];
    var notMult = [];
    for(var i = 0; i <= 100; i++)
    {
        if(i % 7 === 0)
        {
            toMult.push(i);
        }
        else
        {
            notMult.push(i);
        }
    }
    console.log("Делятся на 7: " + toMult);
    console.log("Не делятся на 7: " + notMult);

}

function matrix()
/* Создание матрицы 3х4 и выведение строк и столбцов
:return: None*/
{
    var matr = [];
    var n = 3;
    var m = 4;
    for ( var i = 0; i < n ; i++)
    {
        matr.push(newList(m));
    }
    for(var j =0; j < n; j++)
    {
        console.log("Строка " + (j+1) + ". " + matr[j]);
    }
    for(var k=0; k < m; k++)
    {
        console.log("Столбец " + (k+1));
        for(var f = 0; f < n; f++)
        {
            console.log(matr[f][k]);
        }
    }

}

function anyObjList()
/* Создание списка и выведение в консоль индексов с элементами
:return: None*/
{
    var l = newList(10)
    for(var i = 0; i < l.length; i++)
    {
        console.log(i + ". " + l[i])
    }
}

function toDeleteList()
/* Создание списка с тремя значениями 'to-delete' и нескольми любыми другими, удаление из него всех значений 'to-delete'
:return: None*/
{
    var l = ['to-delete', 'to-stay', 'to-new', 'to-delete', 'to-know', 'to-delete', 556, 78]
    var newArr = l.filter(function(elem) {return elem !== 'to-delete';});
    alert(newArr);
}

function reverseTenToOne()
/* Проход по числам от 10 до 1
:return: None*/
{
    var l = []
    for(var i = 10; i > 0; i--)
    {
        l.push(i)
    }
    alert(l)
}

//Расчет площади прямоугольника
confirm("Задача 1. Вычисление площади прямоугольника");
alert("Площадь прямоугольника равна: " + areaRectangle());
//Операция над двумя числами
confirm("Задача 2. Операция над двумя числами");
alert("Результат операции над числами: " + twoNumbers());
//Нахождение простых чисел между 0 и введенным числом
confirm("Задача 3. Нахождение простых чисел между 0 и введенным числом");
alert("Список простых чисел: " + primeNumbers());
//Нахождение всех кратных 5 чисел между двумя пользовательсикми
confirm("Задача 4. Нахождение всех чисел, кратных 5 между заданными пользователем");
alert("Список чисел, кратных 5: " + multipleValue());
//Список из чисел с сортировкой
confirm("Задача 5. Создается сортированный список");
alert("Сортированный список: " + sortList());
//Словарь из 5 пар
confirm("Задача 6. Создание словаря из 5 пар: int -> str");
d =  printDict();
console.log(d);
//Нахождение максимального и минимального элементов
confirm("Задача 7. Создание списка из 10 дробных чисел и нахождение максимального, минимального элементов");
maxMinNumbers();
//Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
//чтобы получилось: 'Earth -> Russia -> Moscow'
confirm("Задача 8. Создание списка из 3 слов: ['Earth', 'Russia', 'Moscow']");
containStr();
//Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
confirm("Задача 9. Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'");
smashStr();
//Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
confirm("Задача 10. Пройти по числам от 1 до 100 и вывести списки тех, что делятся на 7 и остальных");
multipleNumbers()
//Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
confirm("Задача 11. Создание матрицы и выведение строк и столбцов");
matrix()
//Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
confirm("Задача 12. Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс");
anyObjList()
//Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
confirm("Задача 13. Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'");
toDeleteList()
//Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
confirm("Задача 14. Проход по числам от 10 до 1");
reverseTenToOne()
