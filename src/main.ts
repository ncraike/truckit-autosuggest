// import './style.css'

import { lookup } from "./autosuggest";

const message = await lookup("banana");
console.log(`Looked up 'banana', got: ${message}`);