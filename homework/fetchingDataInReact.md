# Fetching Data In React
[Gist](https://gist.github.com/Calvin087/0ec65578583f33168bb2761e039cf38d)
## Fetch API method

This is build into the browser's window object (window.fetch).

We can make HTTP requests using promises.

Calling the method with a URL below

```js

const fetchData = () => {
    return fetch('https:URL/api')
    .then((response) => response.json())
    .then((data) => console.log(data))
}

// Data is the JSONified response.

```

We can then fetch that info everytime {useEffect} runs.

```js

import {useEffect} from 'react'

useeffect(() => {
    fetchData()
}, [])

```

- [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [UseEffect Explained](https://dmitripavlutin.com/react-useeffect-explanation/)

## Axios Library

The difference with Axios is that it returns a JSON object by default, so we don't need to convert it.

Axios includes more features than fetch and has shorter syntax.

```npm install axios```

```js

import axios from 'axios'

const fetchData = () => {
    return axios.get('https:URL/api')
    .then((response) => console.log(response.data))
}

```

- [Axios](https://www.npmjs.com/package/axios)

## Async Await

Using async await removes the need to use a .then(). In this example we're still using axios.

```js

const fetchData = async () => {
    try{
        const result = await axios.get('https:URL/api')
        console.log(result.data)
    } catch (error) {
        console.log(error)
    }
}

```

- [MDN Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)