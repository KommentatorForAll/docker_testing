import { opts } from "./App";

async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
  

export const handleRequest = (path, method, body, onOK, onERROR) => {
    (async () => {
        const url = process.env.REACT_APP_API_URL + path;
        console.log(url);
        const options = {
            ...opts,
            method: method,
        };
        if (method !== "GET") {
            options.body = JSON.stringify(body);
        }
        const t = await postData(url, { answer: 42 })
        .then((data) => {
          console.log(data); // JSON data parsed by `data.json()` call
        });
        try {
            const { audience, scope, ...fetchOptions } = options;
            console.log("doing request");
            const t = await fetch();
            const res = await fetch(url, {
                ...fetchOptions,
                headers: {
                    ...fetchOptions.headers,
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
            });
            if (res.ok) {
                onOK(res);
            } else {
                console.log(res.status)
                onERROR(res);
                console.log("error: " + res.json());
            }
        } catch (error) {
            console.log("!!error: " + error);
        }
    })();
};