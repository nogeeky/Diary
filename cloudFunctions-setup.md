28.03.21

Setting up firebase functions.

## Setting up firebase tools

`npm install -g firebase-tools`

If you think you already have it installed, then do.
`firebase --version`

`firebase login`

## Project setup

cd into directory then init

`firebase init`

Then choose what you need, then choose the project you need and language type.

Apparently No for ESLint and yes for dependencies.

`Functions: Configure and deploy Cloud Functions`

## Emulator Mode

Useful if you're in development mode while creating functions.

`firebase init emulators`

for the Tut seems to be auth, func, store and pub sub, but for the future, not sure.

Enter through all the options regarding ports and Yes for emulator UI then Y for downloading the Emulators now.

`firebase emulators:start`

## NPM

You can use any npm package inside cloud functions.

You have to cd into the Functions folder, not root, but functions. Then you can install npm packages.

## HTTP request

```js
exports.helloWorld = functions.https.onRequest((req, res) => {
  res.send("hello from FB functions");
});
```

## API requests

```js
exports.api = functions.https.onRequest(async (req, res) => {
  switch (req.method) {
    case "GET":
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/users/1"
      );
      res.send(response.data);
      break;
    case "POST":
      const body = req.body;
      res.send(body);
      break;
    case "DELETE":
      res.send("DELETE Request");
      break;
    default:
      res.send("Default request");
  }
});
```

**REST Client** vscode extension to play with the api from the terminal.

## Auth triggers

When a new auth'd user is created or deleted, it can trigger functions.

```js
exports.userAdded = functions.auth.user().onCreate((user) => {
  console.log(`${user.email} is created`);
  return Promise.resolve;
});

exports.userDeleted = functions.auth.user().onDelete((user) => {
  console.log(`${user.email} is deleted`);
  return Promise.resolve();
});
```

## Firestore data triggers

```js
exports.dataAdded = functions.firestore
  .document("/data/{dataid}")
  .onCreate((snapshot, context) => {
    console.log(snapshot.data());
    return Promise.resolve();
  });

exports.dataDeleted = functions.firestore
  .document("/data/{dataid}")
  .onDelete((snapshot, context) => {
    console.log(snapshot.data(), "deleted");
    return Promise.resolve();
  });

exports.dataUpdated = functions.firestore
  .document("/data/{dataid}")
  .onUpdate((snapshot, context) => {
    console.log(snapshot.before.data(), "updated");
    console.log(snapshot.after.data(), "updated");
    return Promise.resolve();
  });
```

## Pub/Sub - Scheduled

You can not yet fire pub sub functions from inside the emulator. So the project has to be deployed before the scheduled ones seem to show up.

```js
exports.scheduledFunction = functions.pubsub
  .schedule("* * * * *")
  .onRun((context) => {
    console.log("running every minute");
    return null;
  });
```

## Deploying functions

cd to root folder.
`firebase deploy` OR

`firebase deploy --only functions`

`firebase deploy --only functions:nameOfFunction`
