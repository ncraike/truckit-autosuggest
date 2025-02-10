// import './style.css'

import { lookupCategory } from "./autosuggest";

const MIN_QUERY_LEN = 3;

export function setupAutosuggest(queryField: HTMLInputElement) {
    queryField.addEventListener('input', (_event) => {
        updateAutosuggest(queryField);
    });
}

export async function updateAutosuggest(queryField: HTMLInputElement) {
    const query = queryField.value
    const responseElement = document.querySelector('#response')!;
    if (query && query.length >= MIN_QUERY_LEN) {
        const response = await lookupCategory(query.toString());
        if (response) {
            responseElement.innerHTML = response;
        }
    } else {
        responseElement.innerHTML = '';
    }
}

setupAutosuggest(document.querySelector<HTMLInputElement>('#query')!);
