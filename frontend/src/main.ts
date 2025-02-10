import debounce from 'debounce';

import { lookupCategory } from './autosuggest';

const QUERY_MIN_LENGTH = 3;
const QUERY_DEBOUNCE_MS = 200;


export function setupAutosuggest(queryField: HTMLInputElement) {
    const debouncedUpdate = debounce(
        (_event) => {
            updateAutosuggest(queryField);
        },
        QUERY_DEBOUNCE_MS
    );

    queryField.addEventListener('input', debouncedUpdate);
}

export async function updateAutosuggest(queryField: HTMLInputElement) {
    const query = queryField.value
    const responseElement = document.querySelector('#response')!;
    if (query && query.length >= QUERY_MIN_LENGTH) {
        const response = await lookupCategory(query.toString());
        if (response) {
            responseElement.innerHTML = response;
        }
    } else {
        responseElement.innerHTML = '';
    }
}

setupAutosuggest(document.querySelector<HTMLInputElement>('#query')!);
