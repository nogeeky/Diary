https://www.markdownguide.org/extended-syntax/
List of syntax for MD files.

### List of pages on Git
[Fashion landing page](https://calvin087.github.io/front-end-training-fa1/)
[Front-end / Four Card](https://calvin087.github.io/front-end-training-fc2/)
[JS Slider practice](https://calvin087.github.io/slider/)
[JS counter display practice](https://calvin087.github.io/counter/)
[Last message received](https://calvin087.github.io/last-received/)
["Investment Calculator"](https://calvin087.github.io/investment-calculator/)
[Fight club quotes](https://calvin087.github.io/quote-gen/)
[Random Anime wallpaper changer](https://calvin087.github.io/background-color/)

### 2020-05-13 07:45:05

Just finished the scrimba course on React. Actually made a lot more sense than the Udemy course i downloaded. Maybe because i Did that app academy ruby walkthrough - all of this stuff made mire sense. I could see and understand where data was going and connecting to each other.

I need to try and make something but i want to first do a quick tutorial on building a crud app. Once i'm able to edit delete route pages with ease i should be able to bang out most typical projects, I hope.

### 2020-05-10 15:27:24

Something I want to remember about API calls in React

```js
import React, {Component} from "react"

class App extends Component {
    constructor() {
        super()
        this.state = {
            loading: false,
            character: {}
        }
    }
    
    componentDidMount() {
        this.setState({loading: true})
        fetch("https://swapi.co/api/people/1")
            .then(response => response.json())
            .then(data => {
                this.setState({
                    loading: false,
                    character: data
                })
            })
    }
    
    render() {
        const text = this.state.loading ? "loading..." : this.state.character.name
        return (
            <div>
                <p>{text}</p>
            </div>
        )
    }
}

export default App

```

### 2020-05-09 14:48:57
Started the Scrimba Course on react, it's actually quite interesting and for some Reason It's making more sense than the Udemy course. I have more comfort trying to complete the challenges.

Also instead of believing that I understand the situation, I'm repeating the lessons over and over until I feel like I know why I'm making certain actions.

### 2020-04-02 20:28:39

So just spent the best part of an hour working through a newbie problem. Don't mind so much because with a shitty solution I managed to get it to work. Been a day or two since i've worked on a problem. this is the stage that will really test me. Now is the time to prove that I can work through these problems and get job ready. I'm still months away but this feels like i'm developing mentally faster than with the JS courses that I've tried. I feel this will make me a better JS developer too.

[This particular newb problem](https://github.com/Calvin087/app-academy/blob/master/advanced_methods_exercise/01_coprime.rb)

### 2020-03-31 17:20:58

Keep forgetting to update this journal. AppAcademy IO is really pushing me along the learning curve. Understanding things much better than with JS. Ruby is obviously written in a more english speaking style but may be actual teacher is just better.

### 2020-03-24 19:10:01

Something below was new to me, the ... in Ruby.
2 Dots allows me to go from the chosen character up to and including the final character.

3 Dots goes from char 1 up to but NOT including the chosen character.

```js

def pig_latin_word(word)

  vowels = "aeiou"
  
  if vowels.include?(word[0])
    return word + "yay" 
  end
  
  word.each_char.with_index do |char, i|
  	if vowels.include?(char)
      return word[i..-1] + word[0...i] + "ay"
    end
  end
end

```

### 2020-03-23 18:36:57

Yet again, this stuff is blowing my mind. Currently working on Ruby still with App Academy. Quarantine is still in full force and giving me a little bit of agraphobia. Leaving the house has now become a mental battle.

```js

def combinations(arr)

  hold = []
  // starts the first loop
  arr.each_with_index do |ele1, indx1|
    // starts the second loop inside the first
    arr.each_with_index do |ele2, indx2|
    	if indx2 > indx1 // checks if the second index is larger than the first, if so pair them
          hold << [ele1, ele2] // this returns an array to the array without attaching a ", "
        end
    end
  end
  return hold
end

print combinations(["a", "b", "c"]); # => // [ [ "a", "b" ], [ "a", "c" ], [ "b", "c" ] ]
puts

print combinations([0, 1, 2, 3]); # => // [ [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ] ]
puts

```

### 2020-03-20 19:03:10

Start AppAcademy today. Looking at Ruby is actually kind of interesting. Lots of similar thing, that are a little different. Actually progressing through the intro pretty fast purely because of my exposure to JS in the last few months. Going to try and get as much of this done during quarantine as possible.

### 2020-03-19 19:03:29
Today i realised that i can't download my github stuff because there is a star inside the folder name. So i've just been working offline to continue with my journey. Finally finished the drawing section of the Javascript for Khan academy. CoronaVirus has everyone locked in their house but I have to continue working - making calls to IT managers that are in panic mode for the virus. We'll see what happens.

### 2020-03-10 20:03:01

Well SQL was pretty boring. Doesn't seem too difficult. Probably would need a lot of referrencing in order to get things right, but it's not something that I intend to memorize or master to be honest. Not unless I really see something job wise that requires high knowledge on it.

```sql

CREATE TABLE clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    design TEXT);
    
INSERT INTO clothes (type, design)
    VALUES ("dress", "pink polka dots");
INSERT INTO clothes (type, design)
    VALUES ("pants", "rainbow tie-dye");
INSERT INTO clothes (type, design)
    VALUES ("blazer", "black sequin");
    
ALTER TABLE clothes ADD price INTEGER default "unknown";

SELECT * FROM clothes;

UPDATE clothes SET price = "10" WHERE id = 1;
UPDATE clothes SET price = "20" WHERE id = 2;
UPDATE clothes SET price = "30" WHERE id = 3;

SELECT * FROM clothes;

INSERT INTO clothes (type, design, price) VALUES ("socks", "red", 20);

SELECT * FROM clothes;

```

### 2020-03-08 14:45:37

Today fininshed the HTML & CSS classes suggested for the pre programming prep on Khan academy. No doubt once I get involved with the App Ac io projects i'll be getting my ass handed to me. This one took about a week of lunch time studying and after work studying. Around 6 hours if I take away the distractions.

### 2020-03-06 12:11:18

Khan Academy is messing me up with the basics all over again. but this is good. It's reminding me where my holes are in my knowledge. I thought I understood things while following courses, but obviously not.

```js
var book = [
    {
        title: "The Giver",
        stars: 4,
        author: "Your mum"
    },
    {
        title: "Book Two",
        stars: 3,
        author: "Your mum"
    },
    {
        title: "The Book",
        stars: 5,
        author: "Your mum"
    }
];

// draw shelf
fill(173, 117, 33);
rect(0, 120, width, 10);

// draw one book

for(var i = 0; i < book.length; i++) {
    fill(214, 255, 219);
    rect(10 + i* 120, 20, 90, 100);
    
    fill(0, 0, 0);
    
    text(book[i].title, 20 + i* 120, 29, 70, 100);
    text(book[i].author, 20 + i * 120, 49, 70, 100);
    
    for (var j = 0; j < book[i].stars; j++) {
    image(getImage("cute/Star"), 15 + i * 120 + j *15, 90, 20, 30); // Having to add multiple numbers to a single X position fucked me up in more ways than one. I still don't fully understand the reason why it's happening but now I know where to look for similar problems.
        }
}
```

### 2020-03-03 21:38:31
Drawing pretty pictures with JS. Again, quite surprised that this was even a thing. I guess processJs must be the system behind it. I've left React alone for a while. It's driving me crazy and the course is boring as hell. Still working through P1Xt's stuff so we'll see how far i get when App Academy io has been started. That includes rails etc.

Khan Acaademy is my current course. Will return to react once I've gotten some App IO done. It might help my understanding of data flow etc through programming principles.

### 2020-03-01 14:35:21

Well just started looking into JS drawing and animation. Didn't even know that it was possible to do that. Not so complicated. Reminds me of padding and margins in HTML. Drawing a lot of boring shapes, but accepting that these are the basics suggested by the platform. I imagine things will get complicated very quickly.

### 2020-02-21 20:40:24

Algebra absolutely destroyed me, i'm a week and a half in and I still can't simplify fractions that are divided by other fractions etc. I know the general formula but each new puzzle is worse than the last. At least i've opened up a new wound and found a way to start patching it. Going to move on to the next level and get beaten even worse.

### 2020-02-20 23:12:39

Haven't updated this in almost a month. The react course is kicking the shit out of me but I'm trying to following along. I've also started looking at P1xt's guide to becomming a solid developer. They've included a course on Math and Algebra which is also fucking me over, but it was a weak spot of mine anyway and needed to be addressed. 

### 2020-01-28 20:21:32

Look up #Prototypes and #Classes for #dummies explanation promises + promise chainging - Await + Async Functions

### 2020-01-13 19:24:55

```js
const request = new XMLHttpRequest()

request.addEventListener('readystatechange', () => {
    if(e.target.readyState === 4) {
        const data = JSON.parse(e.target.responseText)
        console.log(data)
    }
})

request.open('GET', 'http://puzzle.mead.io/puzzle')
request.send()
```

### 2020-01-13 05:26:35

Writing a class then overriding it 

```js

class Person {
    constructor(firstName, lastName, age, likes = []) {
        this.firstName = firstName
        this.lastName = lastName
        this.age = age
        this.likes = likes
    }
    getBio() {
        let bio = `${this.firstName} is ${this.age}.`

        this.likes.forEach((like) => {
            bio += ` ${this.firstName} likes ${like}.`
        })
    
        return bio  
    }

    setName(fullName) {
        const names = fullName.split(' ')
        this.firstName = names[0]
        this.lastName = names[1]
    }
}

class Employee extends Person {
    constructor(firstName, lastName, age, position, likes) {
        super(firstName, lastName, age, likes)
        this.position = position
    }
    // ***If you're an employee, use this bio, if you're just a person, use the one above
    getBio() { 
        return `${this.firstName} ${this.lastName} is a ${this.position}.`
    }
    getYearsLeft() {
        return 65 - this.age
    }
}

const me = new Employee('Calvin', 'Torra', 32, 'Teacher', ['teaching', 'biking'])
console.log(me.getBio()) 

```


### 2020-01-12 13:37:14

Look up #Prototypes and #Classes for #dummies explanation

### 2020-01-08 20:34:52

Realised that I had deleted this by accident so I'm missing a few days which is stupid but haven't figured out how to use GIT properly yet.

Learning about making new objects using 
```js
new

const Person = function (firstName, lastName, age, likes = []) {
    this.firstName = firstName
    this.lastName = lastName
    this.age = age
    this.likes = likes

}

Person.prototype.getBio = function () {
    let bio = `${this.firstName} is ${this.age}.`

    this.likes.forEach((like) => {
        bio += ` ${this.firstName} likes ${like}.`
    })

    return bio
}

Person.prototype.setName = function (fullName) {
    const names = fullName.split(' ')
    this.firstName = names[0]
}

const me = new Person('Calvin', 'Torra', 32, ['teaching', 'biking'])
console.log(me.getBio()) 

const person2 = new Person('Clancy' , 'Turner', 51)
console.log(person2.getBio()) 

```

### 2020-01-02 20:32:19

Conditional Operator replacing an IF statement, apparently not the be all and end all of If statements but useful

```js
// const message = myAge >= 18 ? 'You can vote!' : 'You cannot vote'

message = myAge >= 18 ? 'You can vote!' : 'You cannot vote'

// IS EQUAL TO

if (myAge >= 18) {
    message = 'You can vote'
} else {
    message = 'You can not vote '
}

// Another Example

const myAge = 20

const showPage = () => {
    return 'Showing the page'
}

const showErrorPage = () => {
    return 'Showing the error page'
}

const message = myAge >= 21 ? showPage() : showErrorPage()
console.log(message)

const team = ['Tyler', 'Porter', 'Sam', 'Peter']

console.log(team.length <= 4 ? `Team size is ${team.length}` : 'Too many people on your team')
```

### 2019-12-30 12:24:22

Arrow functions

```js
const square = (num) =>  num * num

const people = [{
    name: 'Anderew',
    age: 27
}, {
    name: 'Vikram',
    age: 31
}, {
    name: 'Jess',
    age: 22
}]

// This is the regular function
const under30 = people.filter(function (person){
    return person.age < 30
})

// This is an Arrow Function / short hand
const under30 = people.filter((person) => person.age < 30)

console.log(under30)

// Example with the FIND keyword
const age22 = people.find((person) => person.age === 22)

console.log(age22.name)

```

-----

Christmas is finished and a few days without my laptop gave me a strange feeling. Back to studying things that I don't understand.

Got bought the book, Javascript the good parts which is useful and also started reading eloquent Js which has challenges that I couldn't even begin to tackle..... which is worrying for me.

Something that I want to remember for later is that I don't understand this completely. Sorting things using filters.

```js
// Sort your notes by one of three ways
const sortNotes = function (notes, sortBy) {
    if (sortBy === 'byEdited') {
        return notes.sort(function (a, b) {
            if (a.updatedAt > b.updatedAt) {
                return -1
            } else if (a.updatedAt < b.updatedAt) {
                return 1
            } else {
                return 0
            }
        })
    } else if (sortBy === 'byCreated') {
        return notes.sort (function (a, b) {
            if (a.createdAt > b.createdAt) {
                return -1
            } else if (a.createdAt < b.createdAt) {
                return 1
            } else {
                return 0
            }
        })
    } else if (sortBy === 'alphabetical') {
        return notes.sort(function (a, b) {
            if (a.title.toLowerCase() < b.title.toLowerCase()) {
                return -1
            } else if (a.title.toLowerCase() > b.title.toLowerCase()) {
                return 1
            } else {
                return 0
            }
        })
    } else {
        return notes
    }
}
```


### 2019-12-19 19:58:04

synced up a library called moment.js, gives me the ability to set times and dates then print them in a readable string. Super interesting, now wondering what other kinds of libraries there are and what I can do with them.

```js
moment().valueOf()
```
etc

Still frustrated that I can't figure out the problems once the project starts to grow out of site in various files. I start to get lost with what section is doing what and so on, but we'll get there eventually.

### 2019-12-17 19:04:12

Dom manipulation, creating links using JS. Just need to change the element that is being created and set the attribute. Had no idea how to get this done even with a google search. Still learning what is even possible! Annoying

```js

const textEl = document.createElement('a')

textEl.setAttribute('href', '/edit.html')

```

### 2019-12-16 20:00:04

Tried to get a few hours in today. Organising Xmas has been a bit annoying when it comes to the studying aspect of things, but here we are. Looking into hooking up buttons to javascript listeners and creating buttons to delete specific ID elements.

Added a library in JS using UUIDV4 - gives and element a Unique identifier which saves hours of typing and screwing up doing it from scratch.

### 2019-12-12 19:55:08

Maybe should find a way to organise to do list. Possibly another file or append it to this one.
discovered the JS can add elements like spans and divs, also buttons and check boxes, which is pretty cool.

```javascript
const generateTodoDom = function(todo){
    const todoEl = document.createElement('div')
    const checkbox = document.createElement('input')
    const todoText = document.createElement('span')
    const removeButton = document.createElement('button')


    // set up todo checkbox
    checkbox.setAttribute('type', 'checkbox')
    todoEl.appendChild(checkbox)

    // Set up todo text
    todoText.textContent = todo.text
    todoEl.appendChild(todoText)

    //  Set up the remove button
    removeButton.textContent = 'x'
    todoEl.appendChild(removeButton)
}

    return todoEl
```

### 2019-12-11 20:53:27
Super lost with the refactoring of functions. The reason for it kind of makes sense but deciding how to organise it all is a little confusing. passing functions into functions is confusing.

```javascript

const renderTodos = function (todos, filters) {
    let filteredTodos = todos.filter(function (todo) {

        const searchTextMatch = todo.text.toLowerCase().includes(filters.searchText.toLowerCase())
        const hideCompletedMatch = !filters.hideCompleted || !todo.completed
        
        return searchTextMatch && hideCompletedMatch
    })

    const incompleteTodos = filteredTodos.filter(function (todo) {
        return !todo.completed
    })
    
 // HERE ---------------->   
    document.querySelector('#todos').innerHTML = ''
    document.querySelector('#todos').appendChild(generateSummaryDom(incompleteTodos))
    
    filteredTodos.forEach(function (todo){
        document.querySelector('#todos').appendChild(generateTodoDom(todo))
    })

}

const generateTodoDom = function(todo){
    const p = document.createElement('p')
    p.textContent = todo.text
    return p
}

// HERE ----------------> incomplete todos
const generateSummaryDom = function(incompleteTodos){
    const summary = document.createElement('h2')
    summary.textContent = `You have ${incompleteTodos.length} todos left`
    return summary
}

```

### 2019-12-09 11:56:48

#### Todos

- [ ] Need to look up JSON tutorials, as the concept is something new that I don't quite understand. PARSE etc

- [ ] Local storage is also something that should be looked into. **CRUD**

Learned something cool with Dropdowns and printing the sort method to the console.

```html
        <select id="filter-by">

            <option value="byEdited">Sort by last edited</option>
            <option value="byCreated">Sort by recently created</option>
            <option value="byAlphabetical">Sort by alphabetically</option>

        </select>
```

### 2019-12-08 17:13:42

Started working again after putting up the christmas tree.
Learned how to prevent the browser from refreshing after a form submit

```javascript
    e.preventDefault()

```

Had to look up how to add objects to an object array. Keep forgetting this but instead of taking 40 mins, only took me to mins to find the answer and remember what to do.

```javascript
        array.push({
            text: e.target.elements.text.value, //values of the object being pushed
            completed: false
        })
```

Also learned how to format my code blocks so that if i ever look back at this, i might find something nice.

### 2019-12-06 18:06:34

Managed to hack together a working example by editing the copied js. Couldn't write it from memory as this would take forever. Hopefully with time I'll be able to write it from rote.

### 2019-12-06 17:18:04

Going to attempt to update user input for my todo app using HTML and js listeners.

### 2019-12-05 19:34:39

Figuring out how to commit different types of files here.
Possibly could use this as a todo list of sorts somewhere.

Should learn how to write in markdown again to make this presentable.
